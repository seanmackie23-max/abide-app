// Pew for Churches, on the relay.
// A church leader claims their church (found on OpenStreetMap) with their email. The link we email them opens the church portal.
// If their email is on the church website's own domain, the claim is verified at once; otherwise Pew's admin approves it by email.
// Verified churches keep their times, events and welcomer up to date, and get an email when someone says they're coming.
// Partner churches (paid through Stripe) also get a member code that gives their people Pew Plus, and newcomer numbers.
// Env: TOKEN_SECRET, RESEND_API_KEY, EMAIL_FROM, SITE_URL, ADMIN_EMAIL; STRIPE_SECRET_KEY for Partner; a store (see store.mjs).
import { store } from "./store.mjs";
import { makeKey, readKey, stripe, periodEnd } from "./plus.mjs";

const DAY = 86400, now = () => Math.floor(Date.now() / 1000), SEATS = 100;
const EMAIL = /^[^\s@<>"]{1,64}@[^\s@<>"]{1,190}\.[a-z]{2,}$/i;
const clean = (s, n) => String(s || "").replace(/[\u0000-\u001f<>]/g, " ").replace(/\s+/g, " ").trim().slice(0, n);
const ok = json => ({ status: 200, json }), bad = (error, status = 400) => ({ status, json: { error } });
const site = env => (env.SITE_URL || "").replace(/\/$/, "");
const month = () => new Date().toISOString().slice(0, 7);
const host = u => { try { return new URL(/^https?:/.test(u) ? u : "https://" + u).hostname.replace(/^www\./, "").toLowerCase(); } catch { return ""; } };
const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const code = () => { const a = "ABCDEFGHJKMNPQRSTUVWXYZ23456789", r = crypto.getRandomValues(new Uint8Array(8)); return [...r].map(x => a[x % a.length]).join(""); };

async function mail(env, to, subject, html, text) {
  if (!env.RESEND_API_KEY || !env.EMAIL_FROM) { console.log("[mail not configured]", to, subject); return false; }
  const r = await fetch("https://api.resend.com/emails", { method: "POST", headers: { Authorization: "Bearer " + env.RESEND_API_KEY, "Content-Type": "application/json" },
    body: JSON.stringify({ from: env.EMAIL_FROM, to: [to], subject, html: `<div style="font:17px/1.6 Georgia,serif;color:#1D1B18;max-width:540px;margin:0 auto;padding:24px"><p style="font:600 14px Arial,sans-serif;letter-spacing:.3em">PEW</p>${html}</div>`, text }) });
  if (!r.ok) console.error("Resend failed", r.status, await r.text().catch(() => ""));
  return r.ok;
}
const button = (href, label) => `<p><a href="${href}" style="display:inline-block;padding:14px 24px;background:#1D1B18;color:#F7F5F1;text-decoration:none;font:600 13px Arial,sans-serif;letter-spacing:.14em;text-transform:uppercase">${label}</a></p>`;

// What anyone can see about a church. Never emails or private notes.
const fresh = (d, days) => d && (Date.now() - new Date(d + "T12:00").getTime()) < days * 864e5;
const publicView = c => ({ id: c.id, name: c.name, welcome: c.welcome || "", welcomer: c.welcomer && c.welcomer.name ? c.welcomer : null,
  note: c.note && fresh(c.note.date, 10) ? c.note : null, reading: c.reading && c.reading.date >= new Date().toISOString().slice(0, 10) ? c.reading : null,
  tradition: c.tradition || "", course: c.course && isPartner(c) ? c.course : null,
  services: c.services || [], events: (c.events || []).filter(e => e.date >= new Date().toISOString().slice(0, 10)), updated: c.updated || "", partner: isPartner(c), takesNotes: !!c.alertEmail });
const isPartner = c => !!(c.partner && c.partner.until > now());
const ownerView = c => ({ ...publicView(c), website: c.website || "", status: c.status, email: c.email, alertEmail: c.alertEmail || "", partner: c.partner ? { until: c.partner.until, code: isPartner(c) ? c.partner.code : "", members: c.partner.members || 0, seats: SEATS } : null, stats: c.stats || {} });

function sanitize(d) {
  const day = s => /^(Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday)$/i.test(s || "") ? s[0].toUpperCase() + s.slice(1).toLowerCase() : "";
  return {
    welcome: clean(d.welcome, 240),
    alertEmail: EMAIL.test(d.alertEmail || "") ? clean(d.alertEmail, 200).toLowerCase() : "",
    welcomer: d.welcomer && clean(d.welcomer.name, 40) ? { name: clean(d.welcomer.name, 40), note: clean(d.welcomer.note, 160) } : null,
    services: (d.services || []).slice(0, 10).map(s => ({ day: day(s.day), time: clean(s.time, 12), title: clean(s.title, 80) })).filter(s => s.day && s.time),
    note: clean(d.note && d.note.text, 700) ? { text: clean(d.note.text, 700), by: clean(d.note.by, 60), date: new Date().toISOString().slice(0, 10) } : null,
    reading: d.reading && clean(d.reading.ref, 80) && /^\d{4}-\d{2}-\d{2}$/.test(d.reading.date || "") ? { ref: clean(d.reading.ref, 80), date: d.reading.date, title: clean(d.reading.title, 80) } : null,
    tradition: /^(anglican|evensong|catholic|protestant|free|orthodox)$/.test(d.tradition || "") ? d.tradition : "",
    course: d.course && /^[a-z0-9-]{2,40}$/.test(d.course.journey || "") && /^\d{4}-\d{2}-\d{2}$/.test(d.course.start || "") ? { journey: d.course.journey, start: d.course.start, day: day(d.course.day) || "", time: clean(d.course.time, 12), where: clean(d.course.where, 80) } : null,
    events: (d.events || []).slice(0, 20).map(e => ({ date: /^\d{4}-\d{2}-\d{2}$/.test(e.date || "") ? e.date : "", time: clean(e.time, 12), title: clean(e.title, 80), kind: clean(e.kind, 12), why: clean(e.why, 160) })).filter(e => e.date && e.title),
  };
}
async function session(token, env) { const p = await readKey(token, env); return p && p.p === "church" ? p : null; }

export const PARISH_ACTIONS = ["church_claim", "church_open", "church_get", "church_save", "church_public", "church_coming", "church_went", "church_partner", "church_redeem"];

export async function parish(body, env, selfUrl = "") {
  if (!env.TOKEN_SECRET) return bad("Pew for Churches is not set up yet.", 501);
  const db = store(env), a = body.action;

  if (a === "church_public") {
    const ids = (body.ids || []).slice(0, 30).map(x => clean(x, 24)), out = {};
    for (const id of ids) { const c = await db.get(`church:${id}`); if (c && c.status === "verified") out[id] = publicView(c); }
    return ok({ churches: out });
  }

  if (a === "church_claim") {
    const id = clean(body.id, 24), email = clean(body.email, 200).toLowerCase();
    if (!/^[nwr]\d+$/.test(id) || !EMAIL.test(email)) return bad("Please choose your church and give your email address.");
    const c = await db.get(`church:${id}`);
    if (c && c.status === "verified" && c.email !== email) return bad("Someone has already claimed this church. If that's a mistake, write to us and we'll sort it out.", 409);
    const t = await makeKey({ p: "chclaim", s: id, m: email, n: clean(body.name, 120), w: clean(body.website, 300), r: clean(body.role, 60), e: now() + 3 * DAY }, env);
    const link = `${site(env)}/church/?t=${encodeURIComponent(t)}`;
    await mail(env, email, `Confirm: ${clean(body.name, 120)} on Pew`, `<p>Please confirm you look after <b>${esc(clean(body.name, 120))}</b> and would like to keep its page on Pew up to date.</p>${button(link, "Open my church on Pew")}<p style="font-size:14px;color:#6E675D">The link works for three days. If you didn't ask for this, ignore this email.</p>`, `Open your church on Pew: ${link}`);
    return ok({ sent: true, devLink: env.ABIDE_DEV ? link : undefined });
  }

  if (a === "church_open") { // from the emailed link
    const p = await readKey(body.t, env); if (!p || p.p !== "chclaim") return bad("This link has expired. Please ask for a new one.", 410);
    let c = await db.get(`church:${p.s}`);
    if (c && c.status === "verified" && c.email !== p.m) return bad("Someone else has already claimed this church.", 409);
    const verified = host(p.w) && p.m.endsWith("@" + host(p.w)) || p.m.endsWith("." + host(p.w));
    c = Object.assign(c || { id: p.s, created: new Date().toISOString(), stats: {} }, { name: p.n, website: p.w, email: p.m, role: p.r, alertEmail: (c && c.alertEmail) || p.m, status: verified || (c && c.status === "verified") ? "verified" : "pending" });
    await db.put(`church:${c.id}`, c, 730);
    if (c.status === "pending" && env.ADMIN_EMAIL) {
      const at = await makeKey({ p: "chapprove", s: c.id, e: now() + 14 * DAY }, env);
      await mail(env, env.ADMIN_EMAIL, `Approve a church claim: ${c.name}`, `<p><b>${esc(c.email)}</b> (${esc(c.role || "no role given")}) has claimed <b>${esc(c.name)}</b>.</p><p>Website: ${esc(c.website || "none")}. Their email isn't on the church's own domain, so it needs a quick check.</p>${button(`${selfUrl}?approve=${encodeURIComponent(at)}`, "Approve this claim")}`, `Approve: ${selfUrl}?approve=${at}`);
    }
    return ok({ session: await makeKey({ p: "church", s: c.id, m: c.email, e: now() + 90 * DAY }, env), church: ownerView(c) });
  }

  if (a === "church_coming" || a === "church_went") {
    const id = clean(body.id, 24), c = await db.get(`church:${id}`); if (!c || c.status !== "verified") return ok({ ok: false });
    const dev = clean(body.device, 64), k = `chnote:${id}:${dev}:${new Date().toISOString().slice(0, 10)}:${a}`;
    if (dev && await db.get(k)) return ok({ ok: true, again: true });
    if (dev) await db.put(k, 1, 2);
    c.stats = c.stats || {}; const m = c.stats[month()] = c.stats[month()] || { coming: 0, went: 0 };
    m[a === "church_coming" ? "coming" : "went"]++;
    await db.put(`church:${id}`, c, 730);
    if (a === "church_coming" && c.alertEmail) {
      const who = clean(body.name, 40) || "Someone", when = clean(body.when, 60), what = clean(body.title, 80), note = clean(body.note, 280);
      await mail(env, c.alertEmail, `${who} is planning to come${when ? ": " + when : ""}`, `<p><b>${esc(who)}</b> found ${esc(c.name)} on Pew and is planning to come${what ? ` to <b>${esc(what)}</b>` : ""}${when ? `, <b>${esc(when)}</b>` : ""}.</p>${note ? `<p style="border-left:2px solid #8E2B2B;padding-left:12px">${esc(note)}</p>` : ""}<p>Many people on Pew have never been to church. A warm hello at the door, and someone to sit with, makes all the difference.${c.welcomer ? ` We've told them ${esc(c.welcomer.name)} will look out for them.` : ""}</p><p style="font-size:14px;color:#6E675D">We don't share their contact details. Manage these emails in your church page on Pew.</p>`, `${who} is planning to come to ${c.name}${when ? ", " + when : ""}.`);
    }
    return ok({ ok: true, welcomer: c.welcomer || null });
  }

  if (a === "church_redeem") { // a Partner church's member code becomes a year of Plus
    const cd = clean(body.code, 12).toUpperCase(), id = await db.get(`chcode:${cd}`); const c = id && await db.get(`church:${id}`);
    if (!c || !isPartner(c) || c.partner.code !== cd) return bad("That church code isn't active.", 404);
    const dev = clean(body.device, 64); c.partner.devs = c.partner.devs || [];
    if (!c.partner.devs.includes(dev)) { if (c.partner.devs.length >= SEATS) return bad("Your church's member places are all taken. Ask your church about it."); c.partner.devs.push(dev); c.partner.members = c.partner.devs.length; await db.put(`church:${c.id}`, c, 730); }
    const exp = Math.min(c.partner.until, now() + 365 * DAY);
    return ok({ key: await makeKey({ p: "church", s: c.id, e: exp }, env), plan: "church", exp, church: c.name });
  }

  // Everything below needs the church's own session
  const s = await session(body.session, env); if (!s) return bad("Please open your church from the link in your email again.", 401);
  let c = await db.get(`church:${s.s}`); if (!c || c.email !== s.m) return bad("We couldn't find your church.", 404);

  if (a === "church_get") {
    if (c.partner && c.partner.sub && c.partner.until < now() + 5 * DAY && env.STRIPE_SECRET_KEY) { // keep Partner in step with Stripe
      const sub = await stripe(`subscriptions/${c.partner.sub}`, env);
      if (sub && ["active", "trialing", "past_due"].includes(sub.status)) { c.partner.until = periodEnd(sub) + 3 * DAY; await db.put(`church:${c.id}`, c, 730); }
    }
    return ok({ church: ownerView(c) });
  }
  if (a === "church_save") {
    if (c.status !== "verified") return bad("Your claim is waiting for a quick check by Pew. You'll get an email when it's done; you can save your details now and they'll appear then.", 202);
    const next = sanitize(body.data || {}); if (next.note && c.note && c.note.text === next.note.text && c.note.by === next.note.by) next.note.date = c.note.date;
    Object.assign(c, next, { updated: new Date().toISOString().slice(0, 10) }); await db.put(`church:${c.id}`, c, 730);
    return ok({ church: ownerView(c) });
  }
  if (a === "church_partner") { // back from Stripe Checkout for the Partner plan
    if (!env.STRIPE_SECRET_KEY) return bad("Payments aren't set up yet.", 501);
    const sid = clean(body.session_id, 200); if (!/^cs_[A-Za-z0-9_]+$/.test(sid)) return bad("Bad payment reference");
    const ss = await stripe(`checkout/sessions/${sid}?expand[]=subscription`, env);
    if (!ss || ss.status !== "complete" || ss.client_reference_id !== c.id) return bad("We couldn't match that payment to your church.", 404);
    const until = ss.mode === "subscription" && ss.subscription ? periodEnd(ss.subscription) + 3 * DAY : now() + 365 * DAY;
    if (!c.partner || !c.partner.code) { let cd; do cd = code(); while (await db.get(`chcode:${cd}`)); c.partner = { code: cd, devs: [], members: 0 }; await db.put(`chcode:${cd}`, c.id, 800); }
    Object.assign(c.partner, { until, sub: ss.subscription ? ss.subscription.id : "" }); await db.put(`church:${c.id}`, c, 730);
    return ok({ church: ownerView(c) });
  }
  return bad("Unknown action");
}

// GET ?approve=… from the admin email. Returns where to send the browser.
export async function approve(token, env) {
  const p = await readKey(token, env), db = store(env);
  if (!p || p.p !== "chapprove") return `${site(env)}/church/?approved=expired`;
  const c = await db.get(`church:${p.s}`); if (!c) return `${site(env)}/church/?approved=missing`;
  c.status = "verified"; await db.put(`church:${c.id}`, c, 730);
  await mail(env, c.email, `${c.name} is live on Pew`, `<p>Thank you for waiting. <b>${esc(c.name)}</b> is now verified on Pew, and your details show to people nearby.</p>${button(`${site(env)}/church/`, "Open my church")}`, `${c.name} is verified on Pew.`);
  return `${site(env)}/church/?approved=1`;
}
