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
}));
const voices = readDir("content/voices").map(d => ({ id: d.id, name: d.name, years: String(d.years), tradition: d.tradition, era: d.era, status: d.status, sections: d.sections }));
const problems = [];
for (const t of library) {
  if (!t.title || !t.summary) problems.push(`library/${t.id}: needs title and summary`);
  if (!t.live) problems.push(`library/${t.id}: needs practice_title and practice (Live it this week)`);
  if (t.depths.length !== 5) problems.push(`library/${t.id}: has ${t.depths.length} depths, expected 5`);
}
for (const v of voices) if (!["early", "modern", "contemporary", "outside"].includes(v.era)) problems.push(`voices/${v.id}: era must be early, modern, contemporary or outside`);
{
  const cal = json("calendar.json"), mids = new Set(json("music.json").map(m => m.id)), lids = new Set(library.map(l => l.id));
  const themes = [...cal.weekly, ...cal.lent, ...cal.advent, cal.christmastide, cal.holyweek, cal.easterweek, ...Object.values(cal.movable), ...Object.values(cal.fixed)];
  for (const t of themes) {
    if (!t.idea || !t.ideaLine) problems.push(`calendar/${t.id}: needs an everyday idea and ideaLine`);
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
  for (const [k, v] of [...Object.entries(art.themes), ...Object.entries(art.library), ...Object.entries(art.playlists)]) if (!aw.has(v)) problems.push(`art: ${k} uses unknown work "${v}"`);
  for (const p of json("playlists.json")) for (const t of p.tracks) if (!mids.has(t)) problems.push(`playlists/${p.id}: unknown music "${t}"`);
}
for (const d of json("debates.json")) if (!d.live || !d.live.title) problems.push(`debates/${d.id}: needs live.title and live.text`);
for (const d of json("debates.json")) if (!library.some(l => l.id === d.library)) problems.push(`debates/${d.id}: unknown library entry "${d.library}"`);
if (problems.length) { console.error("Content problems:\n  " + problems.join("\n  ")); process.exit(1); }

const content = { site: !standalone, library, voices, prayers: json("prayers.json"), questions: json("questions.json"), memory: json("memory.json"), music: json("music.json"), playlists: json("playlists.json"), art: Object.assign(json("art.json"), { base: standalone ? site.baseUrl.replace(/\/$/, "") + "/art/" : "art/" }), calendar: json("calendar.json"), debates: json("debates.json"), conversations: json("conversations.json").sort((a, b) => (b.date || "").localeCompare(a.date || "")),
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
<meta property="og:title" content="${site.name}">
<meta property="og:description" content="${site.description}">
<meta property="og:image" content="${site.baseUrl}/icons/icon-512.png">`;
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
function page({ title, description, kicker, sub, sectionsHtml, urlPath }) {
  return `<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>${esc(title)} · ${site.name}</title>
<meta name="description" content="${esc(description)}">
<meta property="og:title" content="${esc(title)}"><meta property="og:description" content="${esc(description)}">
<meta property="og:url" content="${site.baseUrl}/${urlPath}"><meta property="og:image" content="${site.baseUrl}/icons/icon-512.png">
<link rel="canonical" href="${site.baseUrl}/${urlPath}">
<link rel="icon" href="../../icons/icon-192.png"><link rel="apple-touch-icon" href="../../icons/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Source+Serif+4:opsz,wght@8..60,400;8..60,500&family=Public+Sans:wght@400;500;600&display=swap">
<style>${PAGE_CSS}</style></head><body>
<header><a class="brand" href="../../">${site.name}</a></header>
<main><span class="label">${esc(kicker)}</span><h1>${esc(title)}</h1><p class="sub">${esc(sub)}</p>${sectionsHtml}
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
    + (t.reading ? `<section><h2>Reading list</h2>${t.reading}</section>` : "");
  fs.writeFileSync(path.join(dir, "index.html"), page({ title: t.title, description: t.summary, kicker: "The Library · five depths", sub: t.summary, sectionsHtml, urlPath: `library/${t.id}/` }));
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
fs.writeFileSync(path.join(OUT, "sitemap.xml"), `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls.map(u => `  <url><loc>${site.baseUrl}/${u}</loc></url>`).join("\n")}\n</urlset>\n`);
fs.writeFileSync(path.join(OUT, "robots.txt"), `User-agent: *\nAllow: /\nSitemap: ${site.baseUrl}/sitemap.xml\n`);
if (site.customDomain) fs.writeFileSync(path.join(OUT, "CNAME"), site.customDomain + "\n");
fs.writeFileSync(path.join(OUT, ".nojekyll"), "");

console.log(`Built dist/: app + ${library.length} Library pages + ${voices.length} Voice pages, ${content.music.length} music pieces`);
