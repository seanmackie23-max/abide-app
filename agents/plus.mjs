// Pew Plus on the relay: Stripe checks and signed membership keys. No database.
// A "Plus key" is a small signed token: base64url(JSON {p: plan, s: Stripe id, e: expiry seconds}) + "." + HMAC-SHA256.
// The browser keeps it; the relay checks the signature on every agent call. Needs env TOKEN_SECRET and STRIPE_SECRET_KEY.

const enc = new TextEncoder();
const b64u = buf => btoa(String.fromCharCode(...new Uint8Array(buf))).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
const unb64u = s => Uint8Array.from(atob(s.replace(/-/g, "+").replace(/_/g, "/")), c => c.charCodeAt(0));
async function hmac(secret, data) {
  const key = await crypto.subtle.importKey("raw", enc.encode(secret), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  return b64u(await crypto.subtle.sign("HMAC", key, enc.encode(data)));
}
export async function makeKey(payload, env) {
  const body = b64u(enc.encode(JSON.stringify(payload)));
  return body + "." + await hmac(env.TOKEN_SECRET, body);
}
// Returns the payload if the key is genuine and unexpired, else null
export async function readKey(key, env) {
  if (!key || typeof key !== "string" || !env.TOKEN_SECRET || key.length > 600) return null;
  const [body, sig] = key.trim().split(".");
  if (!body || !sig || await hmac(env.TOKEN_SECRET, body) !== sig) return null;
  try { const p = JSON.parse(new TextDecoder().decode(unb64u(body))); return p.e * 1000 > Date.now() ? p : null; } catch (e) { return null; }
}

export async function stripe(path, env) {
  const r = await fetch("https://api.stripe.com/v1/" + path, { headers: { Authorization: "Bearer " + env.STRIPE_SECRET_KEY } });
  return r.ok ? r.json() : null;
}
const DAY = 86400, now = () => Math.floor(Date.now() / 1000);
export const periodEnd = sub => sub.current_period_end || sub.items?.data?.[0]?.current_period_end || now() + 35 * DAY;
const LIVE = ["active", "trialing", "past_due"];

// After Stripe Checkout: turn a paid session into a key. A subscription gives Plus; a one-off payment gives a year's gift key.
async function fromSession(id, env) {
  if (!/^cs_[A-Za-z0-9_]+$/.test(id || "")) return null;
  const s = await stripe(`checkout/sessions/${id}?expand[]=subscription`, env);
  if (!s || s.status !== "complete" || !["paid", "no_payment_required"].includes(s.payment_status)) return null;
  if (s.mode === "subscription" && s.subscription && LIVE.includes(s.subscription.status))
    return { p: (s.metadata && s.metadata.plan) || "plus", s: s.subscription.id, e: periodEnd(s.subscription) + 3 * DAY };
  if (s.mode === "payment") return { p: "gift", s: s.id, e: (s.created || now()) + 365 * DAY };
  return null;
}
// Before a key runs out: renew it if the subscription is still live
async function renew(key, env) {
  const p = await readKey(key, env); if (!p || !String(p.s).startsWith("sub_")) return p;
  const sub = await stripe(`subscriptions/${p.s}`, env);
  return sub && LIVE.includes(sub.status) ? { p: p.p, s: p.s, e: periodEnd(sub) + 3 * DAY } : null;
}

// Handles {action: "verify", session_id} | {action: "refresh", key} | {action: "check", key}
export async function plusAction(body, env) {
  if (!env.TOKEN_SECRET || !env.STRIPE_SECRET_KEY) return { status: 501, json: { error: "Pew Plus is not set up yet." } };
  let payload = null;
  if (body.action === "verify") payload = await fromSession(body.session_id, env);
  else if (body.action === "refresh") payload = await renew(body.key, env);
  else if (body.action === "check") payload = await readKey(body.key, env);
  else return { status: 400, json: { error: "Unknown action" } };
  if (!payload) return { status: 404, json: { error: "We couldn't find an active membership for that." } };
  return { status: 200, json: { key: body.action === "check" ? body.key : await makeKey(payload, env), plan: payload.p, exp: payload.e } };
}
