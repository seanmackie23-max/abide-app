// Run on GitHub Actions: finds Project Gutenberg books with the Gutendex API and downloads their plain text,
// so journeys can quote public-domain texts verbatim. Writes .cache/texts/<id>.txt and search.json.
import fs from "node:fs";
const want = JSON.parse(fs.readFileSync("tools/texts/want.json", "utf8"));
const OUT = ".cache/texts"; fs.mkdirSync(OUT, { recursive: true });
const UA = { "user-agent": "RoseWindowBot/1.0 (https://github.com/seanmackie23-max/abide-app)" };
const results = {};
for (const q of want.search || []) {
  try { const r = await (await fetch("https://gutendex.com/books/?search=" + encodeURIComponent(q), { headers: UA, signal: AbortSignal.timeout(25000) })).json();
    results[q] = (r.results || []).slice(0, 8).map(b => ({ id: b.id, title: b.title, authors: (b.authors || []).map(a => `${a.name} (${a.birth_year}-${a.death_year})`), translators: (b.translators || []).map(a => `${a.name} (${a.birth_year}-${a.death_year})`) })); }
  catch (e) { results[q] = "error " + e.message; } }
fs.writeFileSync(OUT + "/search.json", JSON.stringify(results, null, 1));
for (const id of want.ids || []) {
  for (const u of [`https://www.gutenberg.org/cache/epub/${id}/pg${id}.txt`, `https://www.gutenberg.org/files/${id}/${id}-0.txt`]) {
    try { const r = await fetch(u, { headers: UA, signal: AbortSignal.timeout(40000) }); if (r.ok) { fs.writeFileSync(`${OUT}/${id}.txt`, await r.text()); console.log("got", id); break; } } catch (e) {} } }
console.log("done");
