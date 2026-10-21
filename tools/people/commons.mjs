// Run on GitHub Actions (the museums and Wikimedia are not reachable from the editing sandbox).
// 1. Reports candidate portraits from Wikimedia Commons categories, with licence, author and date.
// 2. Downloads the chosen files in content/art.json (works with a `commons` field) as <id>-600.jpg and <id>-1400.jpg.
import fs from "node:fs";
const UA = { "user-agent": "RoseWindowBot/1.0 (https://github.com/seanmackie23-max/abide-app)" };
const api = async q => (await fetch("https://commons.wikimedia.org/w/api.php?format=json&origin=*&" + new URLSearchParams(q), { headers: UA })).json();
const OUT = ".cache/people"; fs.mkdirSync(OUT, { recursive: true });
const info = async titles => { const r = await api({ action: "query", prop: "imageinfo", iiprop: "url|extmetadata|size", iiurlwidth: 1400, titles: titles.join("|") });
  return Object.values(r.query?.pages || {}).map(p => { const ii = (p.imageinfo || [])[0] || {}, m = ii.extmetadata || {}; const v = k => (m[k]?.value || "").replace(/<[^>]+>/g, "").trim().slice(0, 200);
    return { title: p.title, missing: !!p.missing, w: ii.width, h: ii.height, thumb: ii.thumburl, licence: v("LicenseShortName"), artist: v("Artist"), date: v("DateTimeOriginal"), desc: v("ImageDescription"), credit: v("Credit") }; }); };
const cats = JSON.parse(fs.readFileSync("tools/people/categories.json", "utf8"));
const report = {};
for (const [who, list] of Object.entries(cats)) { report[who] = [];
  for (const c of list) { const r = await api({ action: "query", list: "categorymembers", cmtitle: c, cmtype: "file", cmlimit: 60 });
    const titles = (r.query?.categorymembers || []).map(x => x.title);
    for (let i = 0; i < titles.length; i += 40) report[who].push(...(await info(titles.slice(i, i + 40)))); } }
fs.writeFileSync(OUT + "/report.json", JSON.stringify(report, null, 1));
// download the chosen ones, plus small previews of good candidates
const art = JSON.parse(fs.readFileSync("content/art.json", "utf8"));
for (const w of art.works.filter(w => w.commons)) {
  const [i] = await info(["File:" + w.commons]); if (!i || i.missing) { console.log("MISSING", w.id, w.commons); continue; }
  for (const px of [600, 1400]) { const r = await api({ action: "query", prop: "imageinfo", iiprop: "url", iiurlwidth: px, titles: "File:" + w.commons });
    const u = Object.values(r.query.pages)[0].imageinfo[0].thumburl; const b = await fetch(u, { headers: UA }); if (b.ok) fs.writeFileSync(`${OUT}/${w.id}-${px}.jpg`, Buffer.from(await b.arrayBuffer())); }
  fs.writeFileSync(`${OUT}/${w.id}.json`, JSON.stringify(i, null, 1)); console.log("got", w.id, i.licence, i.artist);
}
const prev = JSON.parse(fs.readFileSync("tools/people/preview.json", "utf8"));
let n = 0; for (const [who, list] of Object.entries(report)) for (const x of list.filter(x => /public domain|PD|CC0|CC BY/i.test(x.licence) && x.thumb && (prev[who] || 0) > 0).slice(0, prev[who] || 0)) {
  const r = await api({ action: "query", prop: "imageinfo", iiprop: "url", iiurlwidth: 300, titles: x.title }); const u = Object.values(r.query.pages)[0].imageinfo?.[0]?.thumburl; if (!u) continue;
  const b = await fetch(u, { headers: UA }); if (b.ok) { fs.writeFileSync(`${OUT}/prev-${who}-${++n}.jpg`, Buffer.from(await b.arrayBuffer())); x.preview = `prev-${who}-${n}.jpg`; } }
fs.writeFileSync(OUT + "/report.json", JSON.stringify(report, null, 1));
console.log("done");
