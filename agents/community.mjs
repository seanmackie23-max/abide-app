// Community on the relay: circles (small, invite-only groups who live the same daily idea) and "I'm going" for church events.
// No accounts. Each device makes a secret id; others only ever see a short public id derived from it.
// A circle is reached only by its secret invite code. Pew stores names, which moments were kept (never journal text),
// prayer requests shared inside the circle, and events people said they're going to. Everything expires when unused.
import { store } from "./store.mjs";

const MAX_MEMBERS = 12, MAX_PRAYERS = 30;
const enc = new TextEncoder();
async function pid(device) { const h = await crypto.subtle.digest("SHA-256", enc.encode("abide:" + device)); return [...new Uint8Array(h)].slice(0, 8).map(b => b.toString(16).padStart(2, "0")).join(""); }
const code = () => { const a = "abcdefghjkmnpqrstuvwxyz23456789", r = crypto.getRandomValues(new Uint8Array(10)); return [...r].map(x => a[x % a.length]).join(""); };
const clean = (s, n) => String(s || "").replace(/[\u0000-\u001f<>]/g, " ").replace(/\s+/g, " ").trim().slice(0, n);
const day = s => /^\d{4}-\d{2}-\d{2}$/.test(s || "") ? s : null;
const MOMENTS = ["morning", "midday", "evening", "compline", "live"];
const ok = json => ({ status: 200, json }), bad = (error, status = 400) => ({ status, json: { error } });

async function view(db, c, k, me) {
  const since = new Date(Date.now() - 8 * 864e5).toISOString().slice(0, 10);
  const members = await Promise.all(Object.entries(c.members).map(async ([id, m]) => {
    const own = (await db.get(`cm:${k}:${id}`)) || { marks: {}, going: [] };
    const marks = Object.fromEntries(Object.entries(own.marks || {}).filter(([d]) => d >= since));
    return { id, name: m.name, me: id === me, joined: m.joined, marks, going: (own.going || []).filter(g => (g.date || "9") >= since.slice(0, 10)) };
  }));
  return { code: k, name: c.name, created: c.created, me, members, prayers: (c.prayers || []).map(p => ({ ...p, mine: p.by === me, iPrayed: (p.prayed || []).includes(me), n: (p.prayed || []).length })) };
}

export async function community(body, env) {
  const db = store(env), a = body.action;
  if (a === "going_count") {
    const ids = (body.ids || []).slice(0, 30).map(x => clean(x, 120));
    const out = {}; for (const id of ids) { const e = await db.get(`ev:${id}`); out[id] = e ? e.n : 0; }
    return ok({ counts: out });
  }
  const device = clean(body.device, 64); if (device.length < 16) return bad("Missing device");
  const me = await pid(device);

  if (a === "circle_new") {
    const name = clean(body.name, 30), title = clean(body.circle, 40) || `${name}'s circle`; if (!name) return bad("Please add your name");
    const k = code(), c = { name: title, created: new Date().toISOString(), members: { [me]: { name, joined: new Date().toISOString() } }, prayers: [] };
    await db.put(`circle:${k}`, c); return ok(await view(db, c, k, me));
  }
  if (a === "going" && !body.code) return ok({ n: await countGoing(db, body.event || {}, me, !!body.on) });
  const k = clean(body.code, 12).toLowerCase(), c = await db.get(`circle:${k}`);
  if (!c) return bad("That circle doesn't exist, or has closed.", 404);
  const member = !!c.members[me];

  if (a === "circle_join") {
    const name = clean(body.name, 30); if (!name) return bad("Please add your name");
    if (!member && Object.keys(c.members).length >= MAX_MEMBERS) return bad("This circle is full. Circles are kept small, up to 12 people.");
    c.members[me] = { name, joined: (c.members[me] || {}).joined || new Date().toISOString() }; await db.put(`circle:${k}`, c);
    return ok(await view(db, c, k, me));
  }
  if (!member) return bad("You're not in this circle.", 403);
  if (a === "circle_get") return ok(await view(db, c, k, me));
  if (a === "circle_mark") {
    const d = day(body.date), m = body.moment; if (!d || !MOMENTS.includes(m)) return bad("Bad mark");
    const own = (await db.get(`cm:${k}:${me}`)) || { marks: {}, going: [] };
    own.marks[d] = [...new Set([...(own.marks[d] || []), m])];
    for (const x of Object.keys(own.marks)) if (x < new Date(Date.now() - 21 * 864e5).toISOString().slice(0, 10)) delete own.marks[x];
    await db.put(`cm:${k}:${me}`, own); return ok({ ok: true });
  }
  if (a === "circle_pray") {
    const text = clean(body.text, 280); if (text.length < 3) return bad("Please write a few words");
    c.prayers = [{ id: code().slice(0, 8), by: me, name: c.members[me].name, text, at: new Date().toISOString(), prayed: [] }, ...(c.prayers || [])].slice(0, MAX_PRAYERS);
    await db.put(`circle:${k}`, c); return ok(await view(db, c, k, me));
  }
  if (a === "circle_prayed") {
    const p = (c.prayers || []).find(x => x.id === body.id); if (!p) return bad("Not found", 404);
    p.prayed = p.prayed.includes(me) ? p.prayed.filter(x => x !== me) : [...p.prayed, me];
    await db.put(`circle:${k}`, c); return ok(await view(db, c, k, me));
  }
  if (a === "circle_unpray") { c.prayers = (c.prayers || []).filter(x => !(x.id === body.id && x.by === me)); await db.put(`circle:${k}`, c); return ok(await view(db, c, k, me)); }
  if (a === "circle_leave") { delete c.members[me]; await db.put(`circle:${k}`, c, Object.keys(c.members).length ? 180 : 1); return ok({ left: true }); }
  if (a === "going") {
    const e = body.event || {}, id = clean(e.id, 120), d = day(e.date); if (!id || !d) return bad("Bad event");
    const own = (await db.get(`cm:${k}:${me}`)) || { marks: {}, going: [] };
    const on = !!body.on; own.going = (own.going || []).filter(g => g.id !== id);
    if (on) own.going.push({ id, title: clean(e.title, 80), church: clean(e.church, 80), date: d, time: clean(e.time, 12), url: /^https?:\/\//.test(e.url || "") ? clean(e.url, 300) : "" });
    await db.put(`cm:${k}:${me}`, own);
    return ok({ n: await countGoing(db, e, me, on), circle: await view(db, c, k, me) });
  }
  return bad("Unknown action");
}
async function countGoing(db, e, me, on) {
  const id = clean(e.id, 120); if (!id) return 0;
  const ev = (await db.get(`ev:${id}`)) || { n: 0, who: [] };
  ev.who = on ? [...new Set([...ev.who, me])] : ev.who.filter(x => x !== me); ev.n = ev.who.length; await db.put(`ev:${id}`, ev, 40);
  return ev.n;
}
export const COMMUNITY_ACTIONS = ["going_count", "circle_new", "circle_join", "circle_get", "circle_mark", "circle_pray", "circle_prayed", "circle_unpray", "circle_leave", "going"];
