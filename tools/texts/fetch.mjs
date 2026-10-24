// Run on GitHub Actions: downloads public-domain texts the journeys quote verbatim, so drafting can work offline.
// Reads tools/texts/want.json and every tools/texts/want/*.json:
//   { "search": ["gutendex query"], "ids": [gutenberg ids], "urls": [{ "key": "justin-apology-1", "url": "https://..." }] }
// Writes .cache/texts/<id>.txt (Gutenberg), .cache/texts/url/<key>.html|.txt (raw) and <key>.txt (HTML turned into
// plain paragraphs separated by blank lines), search.json and index.json. Files already on the texts-cache branch are kept.
import fs from "node:fs";
import path from "node:path";
const OUT = ".cache/texts"; fs.mkdirSync(OUT + "/url", { recursive: true });
const UA = { "user-agent": "RoseWindowBot/1.0 (+https://github.com/seanmackie23-max/abide-app; public-domain texts for study)" };
const wants = [];
for (const f of ["tools/texts/want.json", ...(fs.existsSync("tools/texts/want") ? fs.readdirSync("tools/texts/want").filter(x => x.endsWith(".json")).map(x => "tools/texts/want/" + x) : [])]) {
  try { wants.push(JSON.parse(fs.readFileSync(f, "utf8"))); } catch (e) { console.log("bad", f, e.message); } }
const index = fs.existsSync(OUT + "/index.json") ? JSON.parse(fs.readFileSync(OUT + "/index.json", "utf8")) : {};
const dec = s => s.replace(/&nbsp;/g, " ").replace(/&amp;/g, "&").replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&quot;/g, '"').replace(/&#39;|&apos;|&rsquo;/g, "’").replace(/&lsquo;/g, "‘").replace(/&ldquo;/g, "“").replace(/&rdquo;/g, "”").replace(/&mdash;/g, "—").replace(/&ndash;/g, "–").replace(/&hellip;/g, "…").replace(/&#(\d+);/g, (_, n) => String.fromCodePoint(+n)).replace(/&#x([0-9a-f]+);/gi, (_, n) => String.fromCodePoint(parseInt(n, 16)));
const html2text = h => dec(h.replace(/<script[\s\S]*?<\/script>|<style[\s\S]*?<\/style>|<!--[\s\S]*?-->/gi, "")
  .replace(/<\/(p|div|h[1-6]|li|blockquote|tr|dd|dt)>/gi, "\n\n").replace(/<br\s*\/?>/gi, "\n").replace(/<[^>]+>/g, ""))
  .split(/\n\s*\n/).map(p => p.replace(/[ \t]*\n[ \t]*/g, " ").replace(/\s+/g, " ").trim()).filter(Boolean).join("\n\n");
const get = async (u, tries = 3) => { for (let i = 0; i < tries; i++) { try { const r = await fetch(u, { headers: UA, signal: AbortSignal.timeout(60000), redirect: "follow" }); if (r.ok) return r; console.log("status", r.status, u); if (r.status === 404) return null; } catch (e) { console.log("err", e.message, u); } await new Promise(r => setTimeout(r, 3000 * (i + 1))); } return null; };
const results = fs.existsSync(OUT + "/search.json") ? JSON.parse(fs.readFileSync(OUT + "/search.json", "utf8")) : {};
for (const w of wants) {
  for (const q of w.search || []) {
    if (results[q] && typeof results[q] !== "string") continue;
    const r = await get("https://gutendex.com/books/?search=" + encodeURIComponent(q));
    try { const j = await r.json(); results[q] = (j.results || []).slice(0, 8).map(b => ({ id: b.id, title: b.title, authors: (b.authors || []).map(a => `${a.name} (${a.birth_year}-${a.death_year})`), translators: (b.translators || []).map(a => `${a.name} (${a.birth_year}-${a.death_year})`) })); }
    catch (e) { results[q] = "error"; } }
  for (const id of w.ids || []) {
    if (fs.existsSync(`${OUT}/${id}.txt`)) continue;
    for (const u of [`https://www.gutenberg.org/cache/epub/${id}/pg${id}.txt`, `https://www.gutenberg.org/files/${id}/${id}-0.txt`, `https://www.gutenberg.org/files/${id}/${id}.txt`]) {
      const r = await get(u, 2); if (r) { fs.writeFileSync(`${OUT}/${id}.txt`, await r.text()); index["g" + id] = { url: u, at: new Date().toISOString() }; console.log("got", id); break; } } }
  for (const { key, url } of w.urls || []) {
    if (!key || !url || fs.existsSync(`${OUT}/url/${key}.txt`) && index[key]?.url === url) continue;
    const r = await get(url); if (!r) { index[key] = { url, error: true }; continue; }
    const type = r.headers.get("content-type") || ""; const body = await r.text();
    if (/html/i.test(type) || /^\s*</.test(body)) { fs.writeFileSync(`${OUT}/url/${key}.html`, body); fs.writeFileSync(`${OUT}/url/${key}.txt`, html2text(body)); }
    else fs.writeFileSync(`${OUT}/url/${key}.txt`, body);
    index[key] = { url, type, at: new Date().toISOString() }; console.log("got", key);
    await new Promise(r => setTimeout(r, 800)); } }
fs.writeFileSync(OUT + "/search.json", JSON.stringify(results, null, 1));
fs.writeFileSync(OUT + "/index.json", JSON.stringify(index, null, 1));
console.log("done");
