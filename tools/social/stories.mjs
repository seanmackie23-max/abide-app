// Instagram story images (1080x1920) from real NGA paintings in the Rose Window arch. node tools/social/stories.mjs  (needs Playwright and the cached art; writes story-*.png here)
import { chromium } from "/home/claude/.npm-global/lib/node_modules/playwright/index.mjs";
import fs from "node:fs";
const R = "/home/claude/abide-app", F = R + "/public/fonts", A = R + "/.cache/art";
const art = JSON.parse(fs.readFileSync(R + "/content/art.json", "utf8")).works;
const W = id => art.find(w => w.id === id);
const img = id => "data:image/jpeg;base64," + fs.readFileSync(`${A}/${id}-1400.jpg`).toString("base64");
const rose = fs.readFileSync(R + "/public/icons/rose-medallion.svg", "utf8").replace(/^<svg /, '<svg class="rose" ');
const S = [
 { id: "ai", art: "pannini-st-peters", pos: "44% 50%", kicker: "In the age of AI", h: "AI will give you back hours.<br>What will you do with them?", p: "Speed was never the question. What is it all for?", cta: "Start free" },
 { id: "podcasts", art: "fragonard-reading", pos: "50% 40%", kicker: "For the podcast listener", h: "300 hours of podcasts.<br>What do you actually know?", p: "Turn the big questions into a path: read, weigh both sides, answer, live it.", cta: "Begin a journey" },
 { id: "start", art: "bellini-jerome", pos: "50% 50%", kicker: "Never read the Bible?", h: "Start with the<br>hardest question.", p: "Can a thinking person trust it? The evidence, the sceptics, then you decide.", cta: "First session free" },
 { id: "byheart", art: "chardin-bubbles", pos: "50% 45%", kicker: "Words to carry", h: "Name one thing<br>you know by heart.", p: "Psalm 23. The Lord's Prayer. A line of Shakespeare. Learn one a week.", cta: "Learn the first" },
];
const fnt = f => "data:font/woff;base64," + fs.readFileSync(`${F}/${f}`).toString("base64");
const css = `
@font-face{font-family:C;src:url(${fnt("cormorant.woff")})} @font-face{font-family:CSC;src:url(${fnt("cormorant-sc-600.woff")});font-weight:600}
@font-face{font-family:SS;src:url(${fnt("source-serif-italic.woff")});font-style:italic} @font-face{font-family:PS;src:url(${fnt("public-sans.woff")})}
*{margin:0;box-sizing:border-box} body{width:1080px;height:1920px;overflow:hidden;background:radial-gradient(120% 70% at 50% 34%,#2a2230 0%,#120f15 55%,#0a090d 100%);color:#F3E9D6;font-family:C;position:relative}
.top{position:absolute;top:150px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:18px}
.rose{width:62px;height:62px} .brand{font:600 30px/1 CSC;letter-spacing:.3em;padding-left:.3em}
.arch{position:absolute;top:262px;left:150px;width:780px;height:975px;-webkit-mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 125' preserveAspectRatio='none'%3E%3Cpath d='M0 125V45C0 20 28 3 50 0C72 3 100 20 100 45V125Z'/%3E%3C/svg%3E") center/100% 100%;mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 125' preserveAspectRatio='none'%3E%3Cpath d='M0 125V45C0 20 28 3 50 0C72 3 100 20 100 45V125Z'/%3E%3C/svg%3E") center/100% 100%}
.arch img{width:100%;height:100%;object-fit:cover;display:block}
.line{position:absolute;top:262px;left:150px;width:780px;height:975px;fill:none;stroke:rgba(242,226,190,.8);stroke-width:2.2px}
.glow{position:absolute;top:240px;left:110px;width:860px;height:1010px;border-radius:430px 430px 20px 20px;box-shadow:0 0 140px 30px rgba(255,190,110,.10)}
.k{position:absolute;top:1318px;left:0;right:0;text-align:center;font:600 27px/1 CSC;letter-spacing:.24em;color:#D9B35E}
h1{position:absolute;top:1366px;left:80px;right:80px;text-align:center;font:500 80px/1.02 C;letter-spacing:-.005em}
p{position:absolute;top:1560px;left:120px;right:120px;text-align:center;font:italic 34px/1.35 SS;color:#D8CCB6}
.cta{position:absolute;top:1680px;left:50%;transform:translateX(-50%);display:flex;align-items:center;gap:16px;background:linear-gradient(#EED08A,#C99A3E);color:#16120C;border-radius:999px;padding:24px 44px;font:600 28px/1 CSC;letter-spacing:.14em;white-space:nowrap}
.cta b{font:600 28px/1 PS;letter-spacing:.02em;text-transform:none;opacity:.85}
.credit{position:absolute;top:1252px;left:0;right:0;text-align:center;font:18px/1 PS;color:#8f8579}`;
const b = await chromium.launch();
for (const s of S) {
  const w = W(s.art);
  const html = `<html><head><style>${css}</style></head><body><div class="top">${rose}<span class="brand">ROSE WINDOW</span></div>
  <div class="arch"><img src="${img(s.art)}" style="object-position:${s.pos}"></div>
  <svg class="line" viewBox="0 0 100 125" preserveAspectRatio="none"><path d="M3 125V46C3 22 30 6 50 3C70 6 97 22 97 46V125" vector-effect="non-scaling-stroke"/></svg>
  <div class="credit">${w.artist.split(" and ")[0]}, ${w.title}</div>
  <div class="k">${s.kicker.toUpperCase()}</div><h1>${s.h}</h1><p>${s.p}</p>
  <div class="cta">${s.cta.toUpperCase()} · <b>rosewindow.app</b></div></body></html>`;
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.setContent(html); await p.waitForTimeout(900); await p.screenshot({ path: `story-${s.id}.png` }); await p.close();
}
await b.close();
