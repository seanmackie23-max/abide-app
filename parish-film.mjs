// The parish welcome film: a one-minute invitation from a local church, told through real paintings
// from the National Gallery of Art in Abide's own type and colours. No stock footage, no AI imagery.
//   node art.mjs (or fetch the art-cache branch into .cache/art), then: node parish-film.mjs
// Writes public/media/parish-welcome.mp4 and parish-welcome.jpg (the poster). Needs Playwright and ffmpeg.
// A church using Abide can change CHURCH and the lines below to make its own.
import fs from "node:fs";
import path from "node:path";
import { spawn } from "node:child_process";

const ROOT = path.dirname(new URL(import.meta.url).pathname);
const { chromium } = await import(process.env.PLAYWRIGHT || "playwright").catch(() => import("/home/claude/.npm-global/lib/node_modules/playwright/index.mjs"));
const art = JSON.parse(fs.readFileSync(path.join(ROOT, "content/art.json"), "utf8"));
const W = Object.fromEntries(art.works.map(w => [w.id, w]));

const CHURCH = { name: "St Andrew's Parish Church", when: "Sundays at 10:30 · about an hour", extras: "Children welcome · step-free · tea and coffee afterwards" };
// [painting, small heading, the line, slow move: [from x%, from y%, to x%, to y%, from zoom, to zoom]]
const SCENES = [
  ["saenredam-cathedral", "Welcome", "Whoever you are, you are welcome here.", [50, 60, 50, 35, 1.0, 1.12]],
  ["rembrandt-philosopher", "Come as you are", "Curious, doubting or believing: bring your questions. We have them too.", [50, 40, 50, 30, 1.0, 1.1]],
  ["gentileschi-cecilia", "Sunday at half past ten", "We sing, we listen to the Bible, we pray, and there's a short talk. About an hour.", [40, 40, 60, 40, 1.05, 1.15]],
  ["ricci-last-supper", "Bread for the journey", "We share bread and wine, as Christians have for two thousand years.", [55, 60, 45, 55, 1.1, 1.0]],
  ["mieris-saying-grace", "Children welcome", "Children are welcome, noise and all. Nobody minds.", [55, 60, 60, 50, 1.0, 1.12]],
  ["brooke-pastoral-visit", "Why come?", "An app can bring you the cathedral. Only a church can bring you people, who learn your name and turn up when life is hard.", [45, 55, 50, 45, 1.0, 1.1]],
  ["american-emmaus", "Not alone", "Faith was never meant to be walked alone. Walk a little way with us.", [50, 50, 50, 40, 1.12, 1.0]],
  ["constable-salisbury", "Come and see", "Tell us you're coming, and someone will meet you at the door.", [40, 55, 55, 50, 1.0, 1.1]],
];
const FPS = 30, SCENE = 7, FADE = 1, END = 6, DUR = SCENES.length * SCENE + END, WIDTH = 1280, HEIGHT = 720;

const b64 = f => fs.readFileSync(path.join(ROOT, f)).toString("base64");
const imgs = SCENES.map(([id]) => {
  const f = path.join(ROOT, ".cache/art", `${id}-1400.jpg`);
  if (!fs.existsSync(f)) throw new Error(`Missing ${f}: run node art.mjs or fetch the art-cache branch first`);
  return "data:image/jpeg;base64," + fs.readFileSync(f).toString("base64");
});
const credits = SCENES.map(([id]) => { const w = W[id]; return `${w.artist}, ${w.title}, ${w.date}. National Gallery of Art, Washington`; });

const html = `<!doctype html><html><head><meta charset="utf-8"><style>
@font-face { font-family: Corm; src: url(data:font/ttf;base64,${b64("daily/fonts/CormorantGaramond.ttf")}); }
@font-face { font-family: CormI; src: url(data:font/ttf;base64,${b64("daily/fonts/CormorantGaramond-Italic.ttf")}); }
@font-face { font-family: CormSC; src: url(data:font/ttf;base64,${b64("daily/fonts/CormorantSC-SemiBold.ttf")}); }
@font-face { font-family: Src; src: url(data:font/ttf;base64,${b64("daily/fonts/SourceSerif4.ttf")}); }
html,body{margin:0;background:#000} canvas{display:block}</style></head><body><canvas id="c" width="${WIDTH}" height="${HEIGHT}"></canvas>
<script>
const SC = ${JSON.stringify(SCENES)}, SRC = ${JSON.stringify(imgs)}, CR = ${JSON.stringify(credits)}, CH = ${JSON.stringify(CHURCH)};
const SCENE = ${SCENE}, FADE = ${FADE}, DUR = ${DUR}, Wd = ${WIDTH}, Ht = ${HEIGHT};
const cv = document.getElementById("c"), g = cv.getContext("2d");
const ease = x => x <= 0 ? 0 : x >= 1 ? 1 : x * x * (3 - 2 * x), mix = (a, b, t) => a + (b - a) * t;
const IM = SRC.map(s => { const i = new Image(); i.src = s; return i; });
window.ready = Promise.all([...IM.map(i => i.decode()), document.fonts.load("40px Corm"), document.fonts.load("40px CormI"), document.fonts.load("20px CormSC"), document.fonts.load("16px Src")]);
function wrap(text, font, max) { g.font = font; const words = text.split(" "), lines = []; let l = "";
  for (const w of words) { const t = l ? l + " " + w : w; if (g.measureText(t).width > max && l) { lines.push(l); l = w; } else l = t; } if (l) lines.push(l); return lines; }
function painting(i, t) { // t: 0..1 through the scene
  const im = IM[i], m = SC[i][3], z = mix(m[4], m[5], t), fx = mix(m[0], m[2], t) / 100, fy = mix(m[1], m[3], t) / 100;
  const s = Math.max(Wd / im.width, Ht / im.height) * z, w = im.width * s, h = im.height * s;
  g.drawImage(im, (Wd - w) * fx, (Ht - h) * fy, w, h);
}
function caption(i, a) {
  const grd = g.createLinearGradient(0, Ht * .42, 0, Ht); grd.addColorStop(0, "rgba(8,7,6,0)"); grd.addColorStop(1, "rgba(8,7,6,.86)");
  g.fillStyle = grd; g.fillRect(0, 0, Wd, Ht);
  g.globalAlpha = a;
  const lines = wrap(SC[i][2], "500 46px Corm", 960), top = Ht - 92 - lines.length * 54, dy = (1 - a) * 10;
  g.fillStyle = "#EBD196"; g.font = "600 19px CormSC"; g.letterSpacing = "4px"; g.fillText(SC[i][1].toUpperCase(), 80, top + 6 + dy); g.letterSpacing = "0px";
  g.fillStyle = "#F6F1E7"; g.font = "500 46px Corm";
  lines.forEach((l, k) => g.fillText(l, 80, top + 54 + k * 54 + dy));
  g.fillStyle = "rgba(246,241,231,.62)"; g.font = "13px Src"; g.fillText(CR[i], 80, Ht - 40);
  g.globalAlpha = 1;
}
function mark(x, y, s, color) { g.strokeStyle = color; g.lineWidth = 1.6; g.beginPath();
  g.moveTo(x, y + 30 * s); g.lineTo(x, y + 10 * s); g.quadraticCurveTo(x, y, x + 10 * s, y - 6 * s); g.quadraticCurveTo(x + 20 * s, y, x + 20 * s, y + 10 * s); g.lineTo(x + 20 * s, y + 30 * s);
  g.moveTo(x + 10 * s, y - 6 * s); g.lineTo(x + 10 * s, y + 30 * s); g.stroke(); }
function endCard(a) {
  g.globalAlpha = a; g.fillStyle = "#F3EEE5"; g.fillRect(0, 0, Wd, Ht);
  const cx = Wd / 2; g.textAlign = "center";
  mark(cx - 14, 150, 1.4, "#A9823A");
  g.fillStyle = "#1D1B18"; g.font = "600 20px CormSC"; g.letterSpacing = "8px"; g.fillText("ABIDE", cx + 4, 238); g.letterSpacing = "0px";
  g.font = "500 64px Corm"; g.fillText(CH.name, cx, 340);
  g.font = "italic 34px CormI"; g.fillStyle = "#4A443B"; g.fillText(CH.when, cx, 396);
  g.fillStyle = "#6E665A"; g.font = "17px Src"; g.fillText(CH.extras, cx, 446);
  g.strokeStyle = "rgba(169,130,58,.5)"; g.lineWidth = 1; g.beginPath(); g.moveTo(cx - 60, 490); g.lineTo(cx + 60, 490); g.stroke();
  g.fillStyle = "#1D1B18"; g.font = "500 30px Corm"; g.fillText("Come and see.", cx, 548);
  g.fillStyle = "#8A8174"; g.font = "15px Src"; g.fillText("In Abide, tap “Let them know I'm coming”, and someone will meet you at the door.", cx, 600);
  g.textAlign = "left"; g.globalAlpha = 1;
}
window.draw = T => {
  g.fillStyle = "#000"; g.fillRect(0, 0, Wd, Ht);
  const n = SC.length, i = Math.min(n - 1, Math.floor(T / SCENE)), local = T - i * SCENE;
  painting(i, (T - i * SCENE) / (SCENE + FADE));
  if (local < FADE && i > 0) { g.globalAlpha = 1 - ease(local / FADE); painting(i - 1, (T - (i - 1) * SCENE) / (SCENE + FADE)); g.globalAlpha = 1; }
  const a = ease((local - .4) / .9) * (1 - ease((local - (SCENE - .7)) / .6));
  caption(i, i === n - 1 ? ease((local - .4) / .9) : a);
  if (T < 1.2) { g.fillStyle = "rgba(0,0,0," + (1 - ease(T / 1.2)) + ")"; g.fillRect(0, 0, Wd, Ht); }
  if (T > n * SCENE - 0.8) endCard(ease((T - (n * SCENE - .8)) / 1.2));
};
</script></body></html>`;

const out = path.join(ROOT, "public/media");
fs.mkdirSync(out, { recursive: true });
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: WIDTH, height: HEIGHT } });
await page.setContent(html);
await page.evaluate(() => window.ready);
if (process.env.PREVIEW) { // stills only: PREVIEW=4,25,59
  for (const t of process.env.PREVIEW.split(",").map(Number)) { const url = await page.evaluate(t => { draw(t); return document.getElementById("c").toDataURL("image/jpeg", 0.9); }, t); fs.writeFileSync(path.join(process.env.TMPDIR || "/tmp", `film-${t}.jpg`), Buffer.from(url.split(",")[1], "base64")); }
  await browser.close(); process.exit(0);
}
const ff = spawn("ffmpeg", ["-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", String(FPS), "-c:v", "mjpeg", "-i", "-",
  "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "24", "-preset", "slow", "-movflags", "+faststart", path.join(out, "parish-welcome.mp4")], { stdio: ["pipe", "inherit", "inherit"] });
const total = Math.round(DUR * FPS);
for (let f = 0; f < total; f++) {
  const url = await page.evaluate(t => { draw(t); return document.getElementById("c").toDataURL("image/jpeg", 0.92); }, f / FPS);
  const buf = Buffer.from(url.split(",")[1], "base64");
  if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once("drain", r));
  if (f === Math.round(3.2 * FPS)) fs.writeFileSync(path.join(out, "parish-welcome.jpg"), buf);
}
ff.stdin.end();
await new Promise(r => ff.on("close", r));
await browser.close();
console.log(`Parish film: ${DUR}s, ${total} frames → public/media/parish-welcome.mp4`);
