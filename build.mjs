// Abide site builder. No dependencies: run with `node build.mjs`.
//   node build.mjs              -> dist/  (the full website: app + one page per Library entry and Voice)
//   node build.mjs --standalone -> dist/standalone.html (single file, no site links, for previews)
import fs from "node:fs";
import path from "node:path";

const ROOT = path.dirname(new URL(import.meta.url).pathname);
const OUT = path.join(ROOT, "dist");
const standalone = process.argv.includes("--standalone");
import { AGENTS, TOOLS } from "./agents/abide-agents.mjs";
const site = JSON.parse(fs.readFileSync(path.join(ROOT, "site.json"), "utf8"));

/* ---------- Tiny Markdown ---------- */
const esc = s => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
function inline(text) {
  return esc(text)
    .replace(/\[([^\]]+)\]\((https?:\/\/[^)\s]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>')
    .replace(/\*\*([^*]+)\*\*/g, "<b>$1</b>")
    .replace(/\*([^*]+)\*/g, "<i>$1</i>");
}
const paras = body => body.trim().split(/\n\s*\n/).map(p => p.trim().startsWith("- ")
  ? `<ul>${p.trim().split(/\n(?=- )/).map(li => `<li>${inline(li.slice(2).replace(/\n/g, " ").trim())}</li>`).join("")}</ul>`
  : `<p>${inline(p.replace(/\n/g, " ").trim())}</p>`).join("");
const plain = html => html.replace(/<[^>]+>/g, "").replace(/&amp;/g, "&").replace(/&lt;/g, "<").replace(/&gt;/g, ">");

function parseDoc(file) {
  const raw = fs.readFileSync(file, "utf8").replace(/\r\n/g, "\n");
  const m = raw.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!m) throw new Error(`${file}: missing frontmatter`);
  const meta = {};
  for (const line of m[1].split("\n")) {
    const i = line.indexOf(":"); if (i < 0) continue;
    const k = line.slice(0, i).trim(), v = line.slice(i + 1).trim();
    meta[k] = /^\d+$/.test(v) ? Number(v) : v;
  }
  const sections = m[2].split(/^## /m).slice(1).map(chunk => {
    const lines = chunk.split("\n");
    const heading = lines.shift().trim();
    let tag = "";
    if (lines[0] && lines[0].startsWith("tag:")) tag = lines.shift().slice(4).trim();
    return { heading, tag, html: paras(lines.join("\n")) };
  });
  return { id: path.basename(file, ".md"), ...meta, sections };
}
const readDir = dir => fs.readdirSync(path.join(ROOT, dir)).filter(f => f.endsWith(".md")).sort()
  .map(f => parseDoc(path.join(ROOT, dir, f))).sort((a, b) => (a.order ?? 99) - (b.order ?? 99));
const json = f => JSON.parse(fs.readFileSync(path.join(ROOT, "content", f), "utf8"));

/* ---------- Validate ---------- */
const SPECIAL = ["Why it matters for you", "Reading list"];
const library = readDir("content/library").map(d => ({
  id: d.id, title: d.title, summary: d.summary, status: d.status, passage: d.passage || "", series: d.series || "questions",
  why: (d.sections.find(s => s.heading === SPECIAL[0]) || {}).html || "",
  reading: (d.sections.find(s => s.heading === SPECIAL[1]) || {}).html || "",
  live: d.practice ? { title: d.practice_title || "Live it", text: d.practice } : null,
  depths: d.sections.filter(s => !SPECIAL.includes(s.heading)),
  order: Number(d.order) || 99,
}));
/* Peer-reviewed research behind the Science entries (content/research.json) */
const RESEARCH = json("research.json");
for (const t of library) t.research = (RESEARCH.entries[t.id] || []).map(k => Object.assign({ id: k }, RESEARCH.papers[k]));
library.sort((a, b) => a.order - b.order);
const voices = readDir("content/voices").map(d => ({ id: d.id, name: d.name, years: String(d.years), tradition: d.tradition, era: d.era, status: d.status, sections: d.sections }));
const problems = [];
for (const [e, ids] of Object.entries(RESEARCH.entries)) {
  if (!library.some(l => l.id === e)) problems.push(`research: unknown library entry "${e}"`);
  for (const k of ids) { const p = RESEARCH.papers[k];
    if (!p) { problems.push(`research/${e}: unknown paper "${k}"`); continue; }
    for (const f of ["authors", "year", "title", "journal", "design", "found", "limits", "strength"]) if (!p[f]) problems.push(`research/${k}: needs ${f}`);
    if (p.free_url && !/^https:\/\//.test(p.free_url)) problems.push(`research/${k}: free_url must be https`);
    if (p.doi && !/^10\.\d{4,9}\/\S+$/.test(p.doi)) problems.push(`research/${k}: doi looks wrong`);
    if (!["strong", "moderate", "early", "contested", "null"].includes(p.strength)) problems.push(`research/${k}: strength must be strong, moderate, early, contested or null`);
  } }
for (const m of json("memory.json")) if (!m.lines || !m.lines.length || !m.title || !m.tradition) problems.push(`memory/${m.id}: needs title, tradition and lines`);
for (const t of library) if (t.series === "science" && t.research.length < 3) problems.push(`library/${t.id}: Science entries need at least 3 papers in research.json`);
for (const t of library) {
  if (!t.title || !t.summary) problems.push(`library/${t.id}: needs title and summary`);
  if (!t.live) problems.push(`library/${t.id}: needs practice_title and practice (Live it this week)`);
  if (t.depths.length !== 5) problems.push(`library/${t.id}: has ${t.depths.length} depths, expected 5`);
}
for (const v of voices) if (!["early", "modern", "contemporary", "outside"].includes(v.era)) problems.push(`voices/${v.id}: era must be early, modern, contemporary or outside`);
{
  const cal = json("calendar.json"), mids = new Set(json("music.json").map(m => m.id)), lids = new Set(library.map(l => l.id));
  const themes = [...Object.values(cal.variants || {}).flat(), ...cal.weekly, ...cal.lent, ...cal.advent, cal.christmastide, cal.holyweek, cal.easterweek, ...Object.values(cal.movable), ...Object.values(cal.fixed)];
  const seenIds = new Set();
  const artJ = json("art.json"), artUse = {};
  for (const t of themes) {
    if (!artJ.themes[t.id]) problems.push(`calendar/${t.id}: needs its own painting in art.json themes`);
    else if (artUse[artJ.themes[t.id]]) problems.push(`calendar/${t.id}: painting "${artJ.themes[t.id]}" is already used by ${artUse[artJ.themes[t.id]]}; each day needs its own`); else artUse[artJ.themes[t.id]] = t.id;
    if (seenIds.has(t.id)) problems.push(`calendar/${t.id}: duplicate theme id`); seenIds.add(t.id);
    for (const k of ["psalm", "reading", "midday", "evening"]) if (!t[k] || !t[k].text || !t[k].ref) problems.push(`calendar/${t.id}: needs ${k} text and ref`);
    if (!t.idea || !t.ideaLine) problems.push(`calendar/${t.id}: needs an everyday idea and ideaLine`);
    for (const k of ["look", "psalmNote", "prayer"]) if (!t[k]) problems.push(`calendar/${t.id}: needs ${k} (the painting's interpretation, the psalm note and the morning prayer)`);
    for (const m of t.music) if (!mids.has(m)) problems.push(`calendar/${t.id}: unknown music "${m}"`);
    if (!lids.has(t.library)) problems.push(`calendar/${t.id}: unknown library entry "${t.library}"`);
  }
}
for (const c of json("conversations.json")) {
  if (!library.some(l => l.id === c.library)) problems.push(`conversations/${c.id}: unknown library entry "${c.library}"`);
  if (!c.live || !c.live.title || !c.live.text) problems.push(`conversations/${c.id}: needs live.title and live.text`);
  if (!c.url || !c.summary || !c.insight) problems.push(`conversations/${c.id}: needs url, summary and insight`);
}
{
  const mids = new Set(json("music.json").map(m => m.id));
  for (const m of json("music.json")) if (!/^[A-Za-z0-9]{22}$/.test(m.spotify || "")) problems.push(`music/${m.id}: needs a spotify track id (22 characters)`);
  const art = json("art.json"), aw = new Set(art.works.map(w => w.id));
  for (const [k, v] of [...Object.entries(art.themes), ...Object.entries(art.library), ...Object.entries(art.playlists), ...Object.entries(art.weekdayPools || {}).flatMap(([d, l]) => l.map(x => [d, x])), ...Object.entries(art.tradition || {}), ...(art.music || []).map(x => ["music", x]), ...Object.entries(art.stories || {})]) if (!aw.has(v)) problems.push(`art: ${k} uses unknown work "${v}"`);
  for (const p of json("playlists.json")) for (const t of p.tracks) if (!mids.has(t)) problems.push(`playlists/${p.id}: unknown music "${t}"`);
}
{ const aw = new Set(json("art.json").works.map(w => w.id)), mids = new Set(json("music.json").map(m => m.id)), stages = new Set(json("path.json").stages.map(s => s.id));
  for (const [d, x] of Object.entries(json("days.json"))) {
    if (!/^\d{4}-\d{2}-\d{2}$/.test(d)) problems.push(`days/${d}: key must be a date YYYY-MM-DD`);
    for (const k of ["title", "line", "artLink", "see", "meaning", "question", "prayer", "midday", "evening"]) if (!x[k]) problems.push(`days/${d}: needs ${k}`);
    if (!x.story || !x.story.retell || !x.story.verse || !x.story.verseRef) problems.push(`days/${d}: needs story.retell, story.verse and story.verseRef`);
    if (!x.echo || !x.echo.text || !x.echo.link || !x.echo.from) problems.push(`days/${d}: needs echo.from, echo.text and echo.link`);
    if (!aw.has(x.art)) problems.push(`days/${d}: unknown painting "${x.art}"`);
    if (x.family && !json("stories.json").some(s => s.id === x.family)) problems.push(`days/${d}: unknown family story "${x.family}"`);
    if (!x.music || !mids.has(x.music.id) || !x.music.why) problems.push(`days/${d}: needs music.id (in music.json) and music.why`);
    if (!x.passage || !x.passage.ref || !(x.passage.paras || []).length || !x.passage.minutes) problems.push(`days/${d}: needs passage (the whole Bible passage: ref, paras, minutes)`);
    for (const k of ["book", "virtue", "stage"]) if (!x[k]) problems.push(`days/${d}: needs ${k}`);
    if (x.stage && !stages.has(x.stage)) problems.push(`days/${d}: unknown stage "${x.stage}" (add it to path.json)`);
    const r = x.read || {};
    if (!r.why) problems.push(`days/${d}: needs read.why (why this reading, today, on the path)`);
    if (r.paras && !(r.author && r.work && r.ref && r.source && r.who && r.when && r.minutes && r.kind)) problems.push(`days/${d}: a great-book reading needs author, work, ref, kind, who, when, minutes and source`);
  }
}
{ const aw = new Set(json("art.json").works.map(w => w.id)), seen = {};
  for (const st of json("stories.json")) {
    if (!st.title || !st.ref || !st.text || st.text.length < 3 || !st.wonder || st.wonder.length !== 3 || !st.prayer) problems.push(`stories/${st.id}: needs title, ref, text, three wonder questions and a prayer`);
    if (!aw.has(st.art)) problems.push(`stories/${st.id}: unknown painting "${st.art}"`);
    else if (seen[st.art]) problems.push(`stories/${st.id}: painting "${st.art}" is already used by ${seen[st.art]}`); else seen[st.art] = st.id;
  }
  for (const m of json("prayers.json").moments || []) if (!m.moment || !m.words) problems.push(`prayers/moments/${m.id}: needs moment and words`);
}
{ const ids = n => new Set(json(n).map(x => x.id)), mem = ids("memory.json"), mus = ids("music.json"), conv = ids("conversations.json"), deb = ids("debates.json"), aw = new Set(json("art.json").works.map(w => w.id));
  for (const j of json("journeys.json")) {
    const P = `journeys/${j.id}`;
    for (const k of ["title", "question", "line", "why"]) if (!j[k]) problems.push(`${P}: needs ${k}`);
    if (!(j.outcomes || []).length) problems.push(`${P}: needs outcomes`);
    if (!aw.has(j.art)) problems.push(`${P}: unknown painting "${j.art}"`);
    if (!j.closing || !j.closing.prompt || !j.closing.practice || !mus.has(j.closing.music)) problems.push(`${P}: needs closing.prompt, closing.practice and closing.music`);
    (j.sessions || []).forEach((s, i) => { const S = `${P}/session ${i + 1}`;
      for (const k of ["title", "line", "why", "readWhy", "practice", "reflect"]) if (!s[k]) problems.push(`${S}: needs ${k}`);
      const r = s.read || {}; if (!(r.paras || []).length || !r.minutes || (!r.bible && !(r.author && r.work && r.ref && r.source))) problems.push(`${S}: read needs paras and minutes (and author, work, ref, source for a great book)`);
      const lib = library.find(l => l.id === (s.think || {}).library); if (!lib || !(s.think.depth >= 1 && s.think.depth <= lib.depths.length)) problems.push(`${S}: think needs a library id and a depth`);
      if (s.listen && !(conv.has(s.listen.conversation) || deb.has(s.listen.debate))) problems.push(`${S}: unknown conversation or debate`);
      for (const k of (s.evidence || {}).papers || []) if (!RESEARCH.papers[k]) problems.push(`${S}: unknown paper "${k}"`);
      if (s.learn && !mem.has(s.learn.memory)) problems.push(`${S}: unknown memory "${s.learn.memory}"`);
      if (!s.music || !mus.has(s.music.id) || !s.music.why) problems.push(`${S}: needs music.id and music.why`);
      if (s.look && !aw.has(s.look.art)) problems.push(`${S}: unknown painting "${s.look.art}"`);
    });
  }
}
for (const d of json("debates.json")) if (!d.live || !d.live.title) problems.push(`debates/${d.id}: needs live.title and live.text`);
for (const d of json("debates.json")) if (!library.some(l => l.id === d.library)) problems.push(`debates/${d.id}: unknown library entry "${d.library}"`);
if (problems.length) { console.error("Content problems:\n  " + problems.join("\n  ")); process.exit(1); }

const content = { site: !standalone, library, voices, prayers: json("prayers.json"), questions: json("questions.json"), stories: json("stories.json"), days: json("days.json"), path: json("path.json"), journeys: json("journeys.json").map(j => Object.assign({}, j, { sessions: j.sessions.map(s => s.evidence ? Object.assign({}, s, { evidence: Object.assign({}, s.evidence, { items: s.evidence.papers.map(k => Object.assign({ id: k }, RESEARCH.papers[k])) }) }) : s) })), memory: json("memory.json"), music: json("music.json"), playlists: json("playlists.json"), art: Object.assign(json("art.json"), { base: standalone ? site.baseUrl.replace(/\/$/, "") + "/art/" : "art/" }), calendar: json("calendar.json"), debates: json("debates.json"), conversations: json("conversations.json").sort((a, b) => (b.date || "").localeCompare(a.date || "")),
  agents: { endpoint: site.askEndpoint || "", defs: AGENTS, tools: TOOLS },
  business: { plus: site.plus || {}, parishes: site.parishes || {}, contact: site.contactEmail || "" } };

/* ---------- Content for the daily email generator (daily.mjs); not published ---------- */
fs.mkdirSync(path.join(ROOT, ".cache"), { recursive: true });
fs.writeFileSync(path.join(ROOT, ".cache/content.json"), JSON.stringify(content));

/* ---------- App page ---------- */
let app = fs.readFileSync(path.join(ROOT, "src/app.html"), "utf8");
app = app.replace("/*__CHURCHYEAR__*/", () => fs.readFileSync(path.join(ROOT, "src/churchyear.js"), "utf8"));
app = app.replace("/*__CONTENT__*/", "window.ABIDE_CONTENT = " + JSON.stringify(content).replace(/</g, "\\u003c") + ";");
const head = standalone ? "" : `<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<link rel="icon" href="icons/icon-192.png">
<meta name="description" content="${site.description}">
<meta property="og:type" content="website"><meta property="og:site_name" content="${site.name}">
<meta property="og:title" content="${site.name} · A cathedral in your pocket">
<meta property="og:description" content="${site.description}">
<meta property="og:url" content="${site.baseUrl}/">
<meta property="og:image" content="${site.baseUrl}/og-cathedral.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="A cathedral interior by Pieter Saenredam beside the words: Abide, a cathedral in your pocket">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="${site.baseUrl}/og-cathedral.jpg">`;
app = app.replace("<!--__HEAD__-->", head);
const shell = body => `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"></head><body>${body}</body></html>`;

if (!standalone) fs.rmSync(OUT, { recursive: true, force: true });
fs.mkdirSync(OUT, { recursive: true });

if (standalone) {
  fs.writeFileSync(path.join(OUT, "standalone.html"), app);
  console.log(`Built dist/standalone.html: ${library.length} Library entries, ${voices.length} Voices, ${content.music.length} music pieces`);
  process.exit(0);
}
fs.writeFileSync(path.join(OUT, "index.html"), shell(app));

/* ---------- One shareable page per entry ---------- */
const PAGE_CSS = fs.readFileSync(path.join(ROOT, "src/page.css"), "utf8");
const STRENGTH = { strong: "Strong evidence", moderate: "Moderate evidence", early: "Early evidence", contested: "Debated", null: "No effect found" };
const ARTJ = json("art.json"), ARTW = Object.fromEntries(ARTJ.works.map(w => [w.id, w]));
const plateHtml = w => w ? `<figure class="plate"><img src="../../art/${w.id}-1400.jpg" alt="${esc(w.alt || w.title)}" style="object-position:${w.focus}"><figcaption>${esc(w.artist)}, <i>${esc(w.title)}</i>, ${esc(w.date)}. National Gallery of Art, Washington</figcaption></figure>` : "";
function page({ title, description, kicker, sub, sectionsHtml, urlPath, art }) {
  return `<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>${esc(title)} · ${site.name}</title>
<meta name="description" content="${esc(description)}">
<meta property="og:title" content="${esc(title)}"><meta property="og:description" content="${esc(description)}">
<meta property="og:url" content="${site.baseUrl}/${urlPath}"><meta property="og:image" content="${art ? `${site.baseUrl}/art/${art.id}-1400.jpg` : `${site.baseUrl}/og-cathedral.jpg`}"><meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="${site.baseUrl}/${urlPath}">
<link rel="icon" href="../../icons/icon-192.png"><link rel="apple-touch-icon" href="../../icons/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Source+Serif+4:opsz,wght@8..60,400;8..60,500&family=Public+Sans:wght@400;500;600&display=swap">
<style>${PAGE_CSS}</style></head><body>
<header><a class="brand" href="../../">${site.name}</a></header>
<main>${plateHtml(art)}<span class="label">${esc(kicker)}</span><h1>${esc(title)}</h1><p class="sub">${esc(sub)}</p>${sectionsHtml}
<a class="cta" href="../../">Open ${site.name}: pray, learn and explore</a></main>
<footer>${site.name} · ${esc(site.description)}</footer></body></html>`;
}
const urls = [""];
for (const t of library) {
  const dir = path.join(OUT, "library", t.id); fs.mkdirSync(dir, { recursive: true });
  const bg = `https://www.biblegateway.com/passage/?search=${encodeURIComponent(t.passage)}&version=WEB`;
  const sectionsHtml = (t.why ? `<section class="why"><h2>Why it matters for you</h2>${t.why}</section>` : "")
    + t.depths.map((d, i) => `<section><h2><span>${i + 1}</span>${esc(d.heading)}</h2>${d.tag ? `<p class="tag">${esc(d.tag)}</p>` : ""}${d.html}</section>`).join("")
    + (t.passage ? `<section><h2>Read the passage</h2><p><a href="${bg}" target="_blank" rel="noopener">${esc(t.passage)} (World English Bible) →</a></p></section>` : "")
    + (t.reading ? `<section><h2>Reading list</h2>${t.reading}</section>` : "")
    + (t.research.length ? `<section><h2>The research</h2>${t.research.map(r => `<div class="paper"><p class="tag">${esc(STRENGTH[r.strength])}</p><p><b>${esc(r.title)}</b><br><span class="cite">${esc(r.authors)} (${r.year}). <i>${esc(r.journal)}</i>${r.ref ? " " + esc(r.ref) : ""}.</span></p><p><b>What they did.</b> ${esc(r.design)}</p><p><b>What they found.</b> ${esc(r.found)}</p><p><b>Limits.</b> ${esc(r.limits)}</p><p>${r.free_url ? `<a href="${esc(r.free_url)}" rel="noopener">Read the full paper, free (${esc(r.free_kind || "free copy")}) →</a> · ` : ""}${r.doi ? `<a href="https://doi.org/${esc(r.doi)}" rel="noopener">Publisher's page</a>` : ""}</p></div>`).join("")}</section>` : "");
  fs.writeFileSync(path.join(dir, "index.html"), page({ title: t.title, description: t.summary, kicker: t.series === "science" ? `Science and faith · ${t.research.length} peer-reviewed papers` : "The Library · five depths", sub: t.summary, sectionsHtml, urlPath: `library/${t.id}/`, art: ARTW[ARTJ.library[t.id]] }));
  urls.push(`library/${t.id}/`);
}
for (const v of voices) {
  const dir = path.join(OUT, "voices", v.id); fs.mkdirSync(dir, { recursive: true });
  const sectionsHtml = v.sections.map(s => `<section><h2>${esc(s.heading)}</h2>${s.html}</section>`).join("");
  const desc = plain(v.sections[0]?.html || "").slice(0, 155);
  fs.writeFileSync(path.join(dir, "index.html"), page({ title: v.name, description: desc, kicker: `Voices · ${v.years}`, sub: v.tradition, sectionsHtml, urlPath: `voices/${v.id}/` }));
  urls.push(`voices/${v.id}/`);
}

/* ---------- PWA files, icons, sitemap ---------- */
fs.writeFileSync(path.join(OUT, "manifest.webmanifest"), JSON.stringify({
  name: site.name, short_name: site.name, description: site.description, start_url: "./", display: "standalone",
  background_color: "#ECE9E3", theme_color: "#8E2B2B",
  icons: [{ src: "icons/icon-192.png", sizes: "192x192", type: "image/png" }, { src: "icons/icon-512.png", sizes: "512x512", type: "image/png" }],
}, null, 2));
fs.cpSync(path.join(ROOT, "public"), OUT, { recursive: true });
// Abide for Churches: the church portal
{ const P = site.parishes || {}, cfg = { endpoint: site.askEndpoint || "", home: "../", contact: site.contactEmail || "", price: P.price || "", priceYear: P.priceYear || "", linkMonthly: P.link || "", linkYearly: P.linkYearly || "" };
  fs.mkdirSync(path.join(OUT, "church"), { recursive: true });
  fs.writeFileSync(path.join(OUT, "church", "index.html"), fs.readFileSync(path.join(ROOT, "src/church.html"), "utf8").replace("__CONFIG__", JSON.stringify(cfg).replace(/</g, "\\u003c")).replace(/__BASE__/g, site.baseUrl));
  urls.push("church/"); }
// Offline: the app opens without a connection, with today's content and the paintings already seen.
fs.writeFileSync(path.join(OUT, "sw.js"), `// Abide service worker (generated by build.mjs)
const V = "abide-${Date.now()}", SHELL = ["./", "manifest.webmanifest", "icons/icon-192.png", "icons/apple-touch-icon.png"];
self.addEventListener("install", e => { e.waitUntil(caches.open(V).then(c => c.addAll(SHELL)).then(() => self.skipWaiting())); });
self.addEventListener("activate", e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== V && k !== "abide-art").map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener("fetch", e => {
  const r = e.request, u = new URL(r.url);
  if (r.method !== "GET" || u.origin !== location.origin || /\\.(mp4|webm)$/.test(u.pathname)) return;
  if (r.mode === "navigate" || u.pathname.endsWith(".html") || u.pathname.endsWith("/")) {
    e.respondWith(fetch(r).then(res => { const copy = res.clone(); caches.open(V).then(c => c.put(r, copy)); return res; }).catch(() => caches.match(r).then(m => m || caches.match("./"))));
    return;
  }
  if (u.pathname.includes("/art/") || /\\.(jpg|png|webp)$/.test(u.pathname)) {
    e.respondWith(caches.open("abide-art").then(c => c.match(r).then(m => m || fetch(r).then(res => { if (res.ok) c.put(r, res.clone()); return res; }))));
    return;
  }
  e.respondWith(caches.match(r).then(m => { const net = fetch(r).then(res => { if (res.ok) { const cp = res.clone(); caches.open(V).then(c => c.put(r, cp)); } return res; }).catch(() => m); return m || net; }));
});
`);
fs.writeFileSync(path.join(OUT, "sitemap.xml"), `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls.map(u => `  <url><loc>${site.baseUrl}/${u}</loc></url>`).join("\n")}\n</urlset>\n`);
fs.writeFileSync(path.join(OUT, "robots.txt"), `User-agent: *\nAllow: /\nSitemap: ${site.baseUrl}/sitemap.xml\n`);
if (site.customDomain) fs.writeFileSync(path.join(OUT, "CNAME"), site.customDomain + "\n");
fs.writeFileSync(path.join(OUT, ".nojekyll"), "");

console.log(`Built dist/: app + ${library.length} Library pages + ${voices.length} Voice pages, ${content.music.length} music pieces`);
