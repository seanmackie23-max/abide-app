// The Abide relay: a tiny server-side pass-through to the Claude API, so the API key never reaches the browser.
// The browser sends {agent, messages}. The relay adds the system prompt and tool list itself, caps sizes,
// calls Claude once and returns {content, stop_reason}. The browser runs the tools over Abide's content and calls again.
// Runtime-agnostic: used by cloudflare-worker.mjs and aws-lambda.mjs.
import { AGENTS, TOOLS } from "./abide-agents.mjs";
import { plusAction, readKey } from "./plus.mjs";
import { subscribe } from "./subscribe.mjs";

const MAX_MESSAGES = 24, MAX_CHARS = 80000, MAX_TOKENS = 1000;
const hits = new Map(); // best-effort per-instance rate limit; add your platform's rate limiting for real traffic

export function cors(origin, env) {
  const allowed = (env.ALLOWED_ORIGINS || "").split(",").map(s => s.trim()).filter(Boolean);
  const ok = allowed.length === 0 || allowed.includes(origin);
  return { "Access-Control-Allow-Origin": ok ? origin || "*" : allowed[0], "Access-Control-Allow-Methods": "POST, OPTIONS", "Access-Control-Allow-Headers": "content-type", "Vary": "Origin", ok };
}

function limited(ip, env) {
  const per = Number(env.RATE_PER_10_MIN || 30), now = Date.now(), win = 10 * 60 * 1000;
  const list = (hits.get(ip) || []).filter(t => now - t < win);
  list.push(now); hits.set(ip, list);
  if (hits.size > 5000) hits.clear();
  return list.length > per;
}

// Free tier: new questions (not tool rounds) per IP per day, per agent. Plus members are not limited here.
const FREE = { ask: "FREE_ASK_PER_DAY", path: "FREE_PATH_PER_DAY", coach: "FREE_COACH_PER_DAY" }, DEFAULT_FREE = { ask: 5, path: 3, coach: 3 };
const daily = new Map();
function overFree(ip, agent, env) {
  const k = new Date().toISOString().slice(0, 10) + "|" + ip + "|" + agent, n = (daily.get(k) || 0) + 1;
  daily.set(k, n); if (daily.size > 20000) daily.clear();
  return n > Number(env[FREE[agent]] || DEFAULT_FREE[agent] || 5);
}

function validate(body) {
  if (!body || typeof body !== "object") return "Bad request";
  const agent = AGENTS[body.agent]; if (!agent) return "Unknown agent";
  const m = body.messages;
  if (!Array.isArray(m) || !m.length || m.length > MAX_MESSAGES) return "Bad messages";
  if (JSON.stringify(m).length > MAX_CHARS) return "Conversation too long";
  for (const x of m) if (!["user", "assistant"].includes(x.role)) return "Bad role";
  if (m[m.length - 1].role !== "user") return "Last message must be from the user";
  return null;
}

// Returns {status, json}
export async function handle(body, { ip = "?", env, selfUrl = "" }) {
  if (body && body.action === "subscribe") { if (limited(ip, env)) return { status: 429, json: { error: "Too many requests. Please wait a few minutes." } }; return subscribe(body, env, selfUrl); }
  if (body && body.action) { if (limited(ip, env)) return { status: 429, json: { error: "Too many requests. Please wait a few minutes." } }; return plusAction(body, env); }
  if (!env.ANTHROPIC_API_KEY) return { status: 500, json: { error: "Relay not configured" } };
  if (limited(ip, env)) return { status: 429, json: { error: "Too many questions. Please wait a few minutes." } };
  const bad = validate(body); if (bad) return { status: 400, json: { error: bad } };
  const agent = AGENTS[body.agent];
  const fresh = typeof body.messages[body.messages.length - 1].content === "string"; // a new question, not a tool round
  if (fresh && !(await readKey(body.plus, env)) && overFree(ip, body.agent, env))
    return { status: 402, json: { error: "You've used today's free questions.", upgrade: true } };
  const r = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: { "content-type": "application/json", "x-api-key": env.ANTHROPIC_API_KEY, "anthropic-version": "2023-06-01" },
    body: JSON.stringify({
      model: env.MODEL || "claude-haiku-4-5-20251001",
      max_tokens: agent.max_tokens || MAX_TOKENS,
      system: agent.system,
      tools: agent.tools.map(n => TOOLS[n]),
      messages: body.messages,
    }),
  });
  const data = await r.json().catch(() => ({}));
  if (!r.ok) { console.error("Claude API error", r.status, JSON.stringify(data).slice(0, 500)); return { status: 502, json: { error: "Abide could not reach Claude just now." } }; }
  return { status: 200, json: { content: data.content, stop_reason: data.stop_reason } };
}
