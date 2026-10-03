// Sends today's email through Resend. Run after `node build.mjs && node daily.mjs` (GitHub Actions does this each morning).
// Environment:
//   RESEND_API_KEY     required (a GitHub secret)
//   EMAIL_FROM         default "Abide <onboarding@resend.dev>" (Resend's test sender delivers only to your own Resend account address)
//   EMAIL_TO           comma-separated addresses for a direct send (a GitHub secret), used while there is no subscriber list
//   RESEND_SEGMENT_ID  when set, sends a broadcast to everyone in this Resend segment instead (needs a verified domain in EMAIL_FROM)
//   DRY_RUN=1          print what would be sent
import fs from "node:fs";
import path from "node:path";

const ROOT = path.join(path.dirname(new URL(import.meta.url).pathname), "..");
const env = process.env;
const today = JSON.parse(fs.readFileSync(path.join(ROOT, "dist/daily/today.json"), "utf8"));
const dir = path.join(ROOT, "dist/daily", today.date);
const meta = JSON.parse(fs.readFileSync(path.join(dir, "email.json"), "utf8"));
let html = fs.readFileSync(path.join(dir, "email.html"), "utf8");
const from = env.EMAIL_FROM || "Abide <onboarding@resend.dev>";
const broadcast = !!env.RESEND_SEGMENT_ID;

const unsubHtml = broadcast ? `<a href="{{{RESEND_UNSUBSCRIBE_URL}}}" style="color:#6E675D">Unsubscribe</a>.` : "";
const unsubText = broadcast ? "Unsubscribe: {{{RESEND_UNSUBSCRIBE_URL}}}" : "";
html = html.replace("%%UNSUBSCRIBE%%", unsubHtml);
const text = meta.text.replace("%%UNSUBSCRIBE%%", unsubText);

if (!env.RESEND_API_KEY) { console.log("::notice::RESEND_API_KEY is not set, so no email was sent. See daily/README.md."); process.exit(0); }
if (!broadcast && !env.EMAIL_TO) { console.log("::notice::Set EMAIL_TO (or RESEND_SEGMENT_ID) to choose who receives the email."); process.exit(0); }

// Make sure the picture is live on the site before sending (the deploy can take a minute to propagate)
const img = (html.match(/<img src="([^"]+)"/) || [])[1];
for (let i = 0; img && !env.DRY_RUN && i < 20; i++) {
  try { const r = await fetch(img, { method: "HEAD" }); if (r.ok) break; } catch (e) {}
  console.log("Waiting for the picture to go live…"); await new Promise(r => setTimeout(r, 15000));
}

async function resend(pathname, body, extraHeaders = {}) {
  if (env.DRY_RUN) { console.log("DRY RUN", pathname, JSON.stringify({ ...body, html: `[${body.html.length} chars]`, text: `[${body.text.length} chars]` })); return {}; }
  const r = await fetch("https://api.resend.com" + pathname, {
    method: "POST", headers: { Authorization: "Bearer " + env.RESEND_API_KEY, "Content-Type": "application/json", ...extraHeaders }, body: JSON.stringify(body),
  });
  const j = await r.json().catch(() => ({}));
  if (!r.ok) { console.error(`Resend ${pathname} failed (${r.status}):`, JSON.stringify(j)); process.exit(1); }
  return j;
}

if (broadcast) {
  const j = await resend("/broadcasts", { segment_id: env.RESEND_SEGMENT_ID, from, subject: meta.subject, html, text, name: `Daily idea ${today.date}`, send: true });
  console.log(`Broadcast sent for ${today.date}: ${j.id || ""}`);
} else {
  const to = env.EMAIL_TO.split(",").map(s => s.trim()).filter(Boolean);
  const j = await resend("/emails", { from, to, subject: meta.subject, html, text }, { "Idempotency-Key": `abide-daily-${today.date}` });
  console.log(`Email sent for ${today.date} to ${to.length} address${to.length === 1 ? "" : "es"}: ${j.id || ""}`);
}
