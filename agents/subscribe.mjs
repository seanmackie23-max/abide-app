// Daily email sign-up with double opt-in (the norm in Germany and the EU).
// 1. The site posts {action: "subscribe", email}. The relay emails a signed confirmation link (valid 3 days).
// 2. The link comes back here (GET ?confirm=...). The relay adds the address to the Resend segment and sends them to the site.
// Env: RESEND_API_KEY, RESEND_SEGMENT_ID, TOKEN_SECRET, EMAIL_FROM (a verified domain), SITE_URL.
import { makeKey, readKey } from "./plus.mjs";

const EMAIL = /^[^\s@<>"]{1,64}@[^\s@<>"]{1,190}\.[a-z]{2,}$/i;
async function resend(path, body, env, method = "POST") {
  const r = await fetch("https://api.resend.com" + path, { method, headers: { Authorization: "Bearer " + env.RESEND_API_KEY, "Content-Type": "application/json" }, body: body ? JSON.stringify(body) : undefined });
  return { ok: r.ok, status: r.status, json: await r.json().catch(() => ({})) };
}

export async function subscribe(body, env, selfUrl) {
  if (!env.RESEND_API_KEY || !env.RESEND_SEGMENT_ID || !env.TOKEN_SECRET || !env.EMAIL_FROM) return { status: 501, json: { error: "Sign-up is not open yet." } };
  const email = String(body.email || "").trim().toLowerCase();
  if (!EMAIL.test(email)) return { status: 400, json: { error: "Please check your email address." } };
  const token = await makeKey({ p: "sub", s: email, e: Math.floor(Date.now() / 1000) + 3 * 86400 }, env);
  const link = `${selfUrl}?confirm=${encodeURIComponent(token)}`;
  const html = `<div style="font:17px/1.6 Georgia,serif;color:#1D1B18;max-width:520px;margin:0 auto;padding:24px">
<p style="font:600 14px Arial,sans-serif;letter-spacing:.3em">ABIDE</p>
<p>Please confirm you'd like Abide's idea of the day by email: one short email each morning, which you can stop at any time.</p>
<p><a href="${link}" style="display:inline-block;padding:14px 24px;background:#1D1B18;color:#F7F5F1;text-decoration:none;font:600 13px Arial,sans-serif;letter-spacing:.14em;text-transform:uppercase">Yes, send me the daily idea</a></p>
<p style="font-size:14px;color:#6E675D">If you didn't ask for this, ignore this email and nothing will happen.</p></div>`;
  const r = await resend("/emails", { from: env.EMAIL_FROM, to: [email], subject: "Confirm your daily idea from Abide", html, text: `Confirm you'd like Abide's daily idea by email:\n${link}\n\nIf you didn't ask for this, ignore this email.` }, env);
  if (!r.ok) { console.error("Resend confirm email failed", r.status, JSON.stringify(r.json)); return { status: 502, json: { error: "We couldn't send the confirmation just now. Please try again later." } }; }
  return { status: 200, json: { ok: true } };
}

// Returns the URL to send the person to afterwards
export async function confirm(token, env) {
  const site = (env.SITE_URL || "").replace(/\/$/, "");
  const p = await readKey(token, env);
  if (!p || p.p !== "sub") return `${site}/?subscribed=expired`;
  const c = await resend("/contacts", { email: p.s, unsubscribed: false }, env);
  if (!c.ok && c.status !== 409 && c.status !== 422) { console.error("Resend contact failed", c.status, JSON.stringify(c.json)); return `${site}/?subscribed=error`; }
  const s = await resend(`/contacts/${encodeURIComponent(p.s)}/segments/${env.RESEND_SEGMENT_ID}`, null, env);
  if (!s.ok && s.status !== 409) { console.error("Resend segment failed", s.status, JSON.stringify(s.json)); return `${site}/?subscribed=error`; }
  return `${site}/?subscribed=1`;
}
