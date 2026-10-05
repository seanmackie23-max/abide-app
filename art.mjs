// Downloads the paintings in content/art.json from the National Gallery of Art's IIIF service (open access, CC0)
// into .cache/art/<id>-<size>.jpg, and copies them to dist/art/ so Pew serves them itself.
//   node art.mjs            (after node build.mjs)
import fs from "node:fs";
import path from "node:path";
const ROOT = path.dirname(new URL(import.meta.url).pathname);
const art = JSON.parse(fs.readFileSync(path.join(ROOT, "content/art.json"), "utf8"));
const CACHE = path.join(ROOT, ".cache/art"), OUT = path.join(ROOT, "dist/art");
const SIZES = [600, 1400];
fs.mkdirSync(CACHE, { recursive: true });
let got = 0, failed = [];
for (const w of art.works) for (const px of SIZES) {
  const file = path.join(CACHE, `${w.id}-${px}.jpg`);
  if (fs.existsSync(file) && fs.statSync(file).size > 1000) continue;
  const url = `https://api.nga.gov/iiif/${w.nga}/full/!${px},${px}/0/default.jpg`;
  let ok = false;
  for (let tries = 0; tries < 3 && !ok; tries++) {
    try { const r = await fetch(url); if (r.ok) { fs.writeFileSync(file, Buffer.from(await r.arrayBuffer())); ok = true; got++; } else await new Promise(r => setTimeout(r, 1500)); }
    catch (e) { await new Promise(r => setTimeout(r, 1500)); }
  }
  if (!ok) failed.push(`${w.id}-${px}`);
}
if (fs.existsSync(path.join(ROOT, "dist"))) { fs.mkdirSync(OUT, { recursive: true }); for (const f of fs.readdirSync(CACHE)) fs.copyFileSync(path.join(CACHE, f), path.join(OUT, f)); }
console.log(`Art: ${got} downloaded, ${art.works.length * SIZES.length - failed.length} available${failed.length ? ", failed: " + failed.join(", ") : ""}`);
if (failed.length) process.exitCode = 1;
