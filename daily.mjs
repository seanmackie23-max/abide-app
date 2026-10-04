// Abide's daily idea: the picture, the share page and the email, for each day.
//   node build.mjs && node daily.mjs                 -> dist/daily/ for the last 30 days, today and tomorrow
//   node daily.mjs --date 2026-10-03 --back 0        -> one day
//   node daily.mjs --no-images                       -> skip the pictures (no browser needed)
// Writes, per day: dist/daily/<date>/index.html (share page), card.jpg (1080x1350), og.jpg (1200x630), email.html, email.json
// Pictures are rendered with Playwright and the fonts in daily/fonts (Open Font License).
import fs from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";

const ROOT = path.dirname(new URL(import.meta.url).pathname);
const args = process.argv.slice(2), arg = (k, d) => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : d; };
const site = JSON.parse(fs.readFileSync(path.join(ROOT, "site.json"), "utf8"));
const content = JSON.parse(fs.readFileSync(path.join(ROOT, ".cache/content.json"), "utf8"));
const OUT = path.join(ROOT, "dist/daily");
const BASE = site.baseUrl.replace(/\/$/, "");

// The same church-year code the app runs
const cy = new Function("CAL", fs.readFileSync(path.join(ROOT, "src/churchyear.js"), "utf8") + "\nreturn { addDays, season, themeFor, weekNumber };")(content.calendar);

const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const plain = h => String(h || "").replace(/<[^>]+>/g, " ").replace(/&amp;/g, "&").replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/\s+/g, " ").trim();
const ymd = d => d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0");
const q = encodeURIComponent;

export function dayData(date) {
  const DAYX = (content.days || {})[ymd(date)];
  const theme = DAYX ? Object.assign({}, cy.themeFor(date), { idea: DAYX.title, ideaLine: DAYX.line, intention: DAYX.question, story: DAYX, music: [DAYX.music.id] }) : cy.themeFor(date), season = cy.season(date);
  const lib = content.library.find(l => l.id === theme.library) || content.library[0];
  const music = content.music.find(m => m.id === theme.music[0]);
  const key = ymd(date);
  return {
    key, theme, season, lib, music, date,
    dateLong: date.toLocaleDateString("en-GB", { weekday: "long", day: "numeric", month: "long", year: "numeric" }),
    dateShort: date.toLocaleDateString("en-GB", { weekday: "long", day: "numeric", month: "long" }),
    short: lib.depths[0] ? lib.depths[0].html : `<p>${esc(lib.summary)}</p>`,
    url: `${BASE}/daily/${key}/`, card: `${BASE}/daily/${key}/card.jpg`, og: `${BASE}/daily/${key}/og.jpg`,
    app: `${BASE}/`, libUrl: `${BASE}/library/${lib.id}/`,
    accent: theme.color || season.color || "#C9A227",
  };
}

/* ---------- The picture ---------- */
const fontCache = {};
const FONT = f => fontCache[f] ||= "data:font/ttf;base64," + fs.readFileSync(path.join(ROOT, "daily/fonts", f)).toString("base64");
const MARK = (stroke = "#CFA857") => `<svg viewBox="0 0 60 76" fill="none" stroke="${stroke}" stroke-width="3" stroke-linecap="round"><path d="M6 74C6 40 20 14 30 2M54 74C54 40 40 14 30 2"/><path d="M9.3 46H50.7M30 2V74" stroke-width="2"/></svg>`;
const ART = content.art || { works: [], themes: {}, fallback: [] };
const ARTW = Object.fromEntries(ART.works.map(w => [w.id, w]));
const artFor = d => { if (d.theme.story && ARTW[d.theme.story.art]) return ARTW[d.theme.story.art]; if (ART.themes[d.theme.id]) return ARTW[ART.themes[d.theme.id]];
  const pool = (ART.weekdayPools || {})[d.date.getDay()] || ART.fallback; return ARTW[pool[cy.weekNumber(d.date) % pool.length]]; };
const artData = w => { const f = path.join(ROOT, ".cache/art", `${w.id}-1400.jpg`); return fs.existsSync(f) ? "data:image/jpeg;base64," + fs.readFileSync(f).toString("base64") : ""; };
function pictureHTML(d, w, h) {
  const wide = w > h, a = artFor(d), img = a ? artData(a) : "";
  const title = d.theme.idea, line = d.theme.ideaLine;
  const credit = a ? `${esc(a.artist)}, <i>${esc(a.title)}</i>, ${esc(a.date)}` : "";
  const tSize = wide ? (title.length > 22 ? 64 : 76) : (title.length > 22 ? 84 : 100);
  return `<!doctype html><html><head><meta charset="utf-8"><style>
@font-face { font-family: Cormorant; src: url("${FONT("CormorantGaramond.ttf")}"); font-weight: 300 700; }
@font-face { font-family: Cormorant; src: url("${FONT("CormorantGaramond-Italic.ttf")}"); font-style: italic; font-weight: 300 700; }
@font-face { font-family: CormorantSC; src: url("${FONT("CormorantSC-SemiBold.ttf")}"); }
@font-face { font-family: SourceSerif; src: url("${FONT("SourceSerif4.ttf")}"); font-weight: 200 900; }
html, body { margin: 0; width: ${w}px; height: ${h}px; overflow: hidden; }
body { background: #F4F0E8; color: #1D1B18; font-family: Cormorant, Georgia, serif; display: grid; ${wide ? "grid-template-columns: 520px 1fr;" : "grid-template-rows: 800px 1fr;"} }
.art { background: #2A241C ${img ? `url("${img}")` : ""} ${a ? a.focus : "50% 50%"} / ${a && a.zoom ? `${Math.round(a.zoom * 100)}% auto` : "cover"} no-repeat; }
.t { padding: ${wide ? "56px 60px 44px 56px" : "54px 76px 46px"}; display: flex; flex-direction: column; gap: ${wide ? 14 : 16}px; }
.k { font-family: CormorantSC, serif; letter-spacing: .2em; font-size: ${wide ? 20 : 24}px; color: #8C6A2B; }
h1 { margin: 0; font-weight: 500; font-size: ${tSize}px; line-height: 1.02; letter-spacing: -.01em; text-wrap: balance; }
.l { font-style: italic; font-size: ${wide ? 30 : 36}px; line-height: 1.3; color: #34302B; text-wrap: balance; }
.w { margin-top: 10px; font-family: SourceSerif, Georgia, serif; font-size: 23px; line-height: 1.5; color: #34302B; max-width: 860px; } .w span { display: block; margin-top: 6px; font-family: CormorantSC, serif; letter-spacing: .16em; font-size: 18px; color: #8C6A2B; text-transform: uppercase; }
.foot { margin-top: auto; display: flex; justify-content: space-between; align-items: flex-end; gap: 30px; border-top: 1px solid rgba(29,27,24,.18); padding-top: ${wide ? 14 : 18}px; }
.c { font-family: SourceSerif, Georgia, serif; font-size: ${wide ? 15 : 17}px; line-height: 1.4; color: #6E675D; max-width: ${wide ? 380 : 640}px; }
.b { display: flex; align-items: center; gap: 12px; flex: none; }
.b svg { width: 24px; height: 31px; } .b span { font-family: CormorantSC, serif; letter-spacing: .32em; font-size: ${wide ? 22 : 26}px; font-weight: 600; }
</style></head><body><div class="art"></div>
<div class="t"><div class="k">TODAY'S IDEA · ${esc(d.dateShort.toUpperCase())}</div><h1>${esc(title)}</h1><div class="l">${esc(line)}</div>
${wide ? "" : `<div class="w">“${esc(d.theme.reading.text)}”<span>${esc(d.theme.reading.ref)}</span></div>`}
<div class="foot"><div class="c">${credit}${credit ? ". National Gallery of Art, Washington" : ""}</div><div class="b">${MARK("#8C6A2B")}<span>ABIDE</span></div></div></div>
</body></html>`;
}

/* ---------- The share page ---------- */
const PAGE_CSS = fs.readFileSync(path.join(ROOT, "src/page.css"), "utf8");
function sharePage(d, endpoint) {
  const t = d.theme, desc = `${t.ideaLine} A two-minute idea for today, from Abide.`;
  return `<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>${esc(t.idea)} · Today's idea · ${esc(site.name)}</title>
<meta name="description" content="${esc(desc)}">
<meta property="og:type" content="article"><meta property="og:title" content="${esc(t.idea)}"><meta property="og:description" content="${esc(t.ideaLine)}">
<meta property="og:url" content="${d.url}"><meta property="og:image" content="${d.og}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><link rel="canonical" href="${d.url}">
<link rel="icon" href="../../icons/icon-192.png"><link rel="apple-touch-icon" href="../../icons/apple-touch-icon.png">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Source+Serif+4:opsz,wght@8..60,400;8..60,500&family=Public+Sans:wght@400;500;600&display=swap">
<style>${PAGE_CSS}
.card { width: 100%; height: auto; display: block; border-radius: 4px; }
.quote { font-style: italic; font-size: 21px; }
.signup { border: 1px solid var(--line); padding: 18px; border-radius: 6px; display: grid; gap: 10px; }
.signup form { display: flex; gap: 8px; flex-wrap: wrap; } .signup input { flex: 1; min-width: 200px; padding: 12px; font: inherit; border: 1px solid var(--line); border-radius: 4px; }
.signup button { padding: 12px 18px; border: 0; border-radius: 999px; background: var(--lapis); color: var(--bg); font-weight: 600; cursor: pointer; }
.small { font-size: 14px; color: var(--muted); }</style></head><body>
<header><a class="brand" href="../../">${esc(site.name)}</a></header>
<main><span class="label">Today's idea · ${esc(d.dateLong)}</span><h1>${esc(t.idea)}</h1><p class="sub">${esc(t.ideaLine)}</p>
<img class="card" src="card.jpg" alt="${esc(t.idea)}: ${esc(t.ideaLine)}" width="1080" height="1350">
<section><h2>An ancient word</h2><p class="quote">“${esc(t.reading.text)}”</p><p class="small">${esc(t.reading.ref)} (World English Bible)</p></section>
<section><h2>To think about: ${esc(d.lib.title)}</h2>${d.short}<p><a href="../../library/${d.lib.id}/">Go deeper →</a></p></section>
<section><h2>A question for today</h2><p class="quote">${esc(t.intention)}</p></section>
${d.lib.live ? `<section><h2>Live it this week</h2><p><b>${esc(d.lib.live.title)}.</b> ${esc(d.lib.live.text)}</p></section>` : ""}
${endpoint ? `<section class="signup" id="signup"><h2>Get the day's idea every morning</h2><p class="small">One short email a day. Unsubscribe any time.</p>
<form onsubmit="event.preventDefault();var f=this,m=document.getElementById('su-msg');m.textContent='Sending…';fetch('${esc(endpoint)}',{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify({action:'subscribe',email:f.email.value})}).then(function(r){return r.json().then(function(j){m.textContent=r.ok?'Nearly there: check your inbox to confirm.':(j.error||'Something went wrong.');});}).catch(function(){m.textContent='Something went wrong. Please try again.';});">
<input name="email" type="email" required placeholder="you@example.com" autocomplete="email"><button>Sign up</button></form><p class="small" id="su-msg"></p></section>` : ""}
<a class="cta" href="../../">Open ${esc(site.name)}: today's idea, practice and music</a></main>
<footer>${esc(site.name)} · think, then live</footer></body></html>`;
}

/* ---------- The email (table layout, inline styles, Georgia fallback for mail apps) ---------- */
function emailHTML(d) {
  const t = d.theme, serif = "'Cormorant Garamond', Georgia, 'Times New Roman', serif", body = "Georgia, 'Times New Roman', serif", sans = "-apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif";
  const label = s => `<p style="margin:0 0 8px;font:600 12px/1.2 ${sans};letter-spacing:.14em;text-transform:uppercase;color:#8C6A2B">${s}</p>`;
  const para = h => plain(h);
  const shortParas = d.short.split(/<\/p>/).map(p => plain(p)).filter(Boolean).map(p => `<p style="margin:0 0 12px;font:17px/1.6 ${body};color:#34302B">${esc(p)}</p>`).join("");
  const block = (inner, extra = "") => `<tr><td style="padding:22px 32px;border-top:1px solid #E2DDD3;${extra}">${inner}</td></tr>`;
  const m = d.music;
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light only"><title>${esc(t.idea)}</title></head>
<body style="margin:0;padding:0;background:#ECE9E3">
<div style="display:none;max-height:0;overflow:hidden;opacity:0">${esc(t.ideaLine)}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#ECE9E3"><tr><td align="center" style="padding:24px 12px">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#F7F5F1;border:1px solid #E2DDD3">
<tr><td style="padding:22px 32px 12px"><span style="font:600 15px/1 ${sans};letter-spacing:.32em;color:#1D1B18">ABIDE</span><span style="float:right;font:13px/1.4 ${sans};color:#6E675D">${esc(d.dateShort)}</span></td></tr>
<tr><td style="padding:0 32px"><a href="${d.url}"><img src="${d.card}" width="536" alt="${esc(t.idea)}: ${esc(t.ideaLine)}" style="display:block;width:100%;max-width:536px;height:auto;border:0;border-radius:2px"></a></td></tr>
<tr><td style="padding:24px 32px 18px">${label("Today's idea")}<h1 style="margin:0 0 10px;font:500 36px/1.1 ${serif};color:#1D1B18">${esc(t.idea)}</h1><p style="margin:0;font:italic 21px/1.45 ${serif};color:#34302B">${esc(t.ideaLine)}</p></td></tr>
${block(label("An ancient word") + `<p style="margin:0 0 6px;font:italic 19px/1.5 ${body};color:#1D1B18">“${esc(t.reading.text)}”</p><p style="margin:0;font:13px ${sans};color:#6E675D">${esc(t.reading.ref)}</p>`)}
${block(label("To think about · " + esc(d.lib.title)) + shortParas + `<a href="${d.libUrl}" style="font:600 14px ${sans};color:#8E2B2B;text-decoration:none">Go deeper →</a>`)}
${block(label("A question for today") + `<p style="margin:0;font:italic 20px/1.45 ${serif};color:#1D1B18">${esc(t.intention)}</p>`, "border-left:3px solid #8E2B2B;")}
${d.lib.live ? block(label("Live it this week") + `<p style="margin:0 0 6px;font:500 20px/1.3 ${serif};color:#1D1B18">${esc(d.lib.live.title)}</p><p style="margin:0;font:16px/1.55 ${body};color:#34302B">${esc(d.lib.live.text)}</p>`) : ""}
${m ? block(label("Listen") + `<p style="margin:0 0 4px;font:500 19px/1.3 ${serif};color:#1D1B18">${esc(m.title)}</p><p style="margin:0 0 8px;font:14px ${sans};color:#6E675D">${esc(m.by)}</p><a href="https://www.youtube.com/results?search_query=${q(m.search)}" style="font:600 14px ${sans};color:#8E2B2B;text-decoration:none">YouTube</a> &nbsp;·&nbsp; <a href="https://open.spotify.com/search/${q(m.search)}" style="font:600 14px ${sans};color:#8E2B2B;text-decoration:none">Spotify</a> &nbsp;·&nbsp; <a href="https://music.apple.com/search?term=${q(m.search)}" style="font:600 14px ${sans};color:#8E2B2B;text-decoration:none">Apple Music</a>`) : ""}
<tr><td style="padding:26px 32px 30px;border-top:1px solid #E2DDD3" align="center"><a href="${d.app}" style="display:inline-block;padding:15px 28px;background:#1D1B18;color:#F7F5F1;font:600 13px/1 ${sans};letter-spacing:.16em;text-transform:uppercase;text-decoration:none;border-radius:2px">Open today in Abide</a>
<p style="margin:16px 0 0;font:14px/1.5 ${sans};color:#6E675D">Know someone asking the big questions? <a href="${d.url}" style="color:#8E2B2B">Send them today's idea</a>.</p></td></tr>
</table>
<p style="max-width:560px;margin:18px auto 0;font:12px/1.6 ${sans};color:#6E675D;text-align:center">You're receiving this because you asked for Abide's daily idea. %%UNSUBSCRIBE%%<br><a href="${d.url}" style="color:#6E675D">View in your browser</a></p>
</td></tr></table></body></html>`;
}
function emailText(d) {
  const t = d.theme;
  return [`ABIDE · ${d.dateShort}`, "", `TODAY'S IDEA: ${t.idea}`, t.ideaLine, "", `An ancient word: "${t.reading.text}" (${t.reading.ref})`, "",
    `To think about: ${d.lib.title}`, plain(d.short), `Go deeper: ${d.libUrl}`, "", `A question for today: ${t.intention}`, "",
    d.lib.live ? `Live it this week: ${d.lib.live.title}. ${d.lib.live.text}\n` : "",
    `Open today in Abide: ${d.app}`, `Share today's idea: ${d.url}`, "", "%%UNSUBSCRIBE%%"].join("\n");
}

/* ---------- Run ---------- */
async function main() {
  const start = arg("--date") ? new Date(arg("--date") + "T12:00:00") : new Date();
  const back = Number(arg("--back", 30)), ahead = Number(arg("--ahead", 1)), images = !args.includes("--no-images");
  const days = []; for (let i = -back; i <= ahead; i++) days.push(cy.addDays(new Date(start.getFullYear(), start.getMonth(), start.getDate(), 12), i));
  let browser = null;
  if (images) {
    const pw = await import(process.env.PLAYWRIGHT_MODULE || "playwright");
    browser = await (pw.chromium || pw.default.chromium).launch();
  }
  for (const date of days) {
    const d = dayData(date), dir = path.join(OUT, d.key); fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(path.join(dir, "index.html"), sharePage(d, site.askEndpoint));
    fs.writeFileSync(path.join(dir, "email.html"), emailHTML(d));
    fs.writeFileSync(path.join(dir, "email.json"), JSON.stringify({ date: d.key, subject: `Today's idea: ${d.theme.idea}`, text: emailText(d), url: d.url }));
    if (browser) for (const [name, w, h] of [["card.jpg", 1080, 1350], ["og.jpg", 1200, 630]]) {
      const page = await browser.newPage({ viewport: { width: w, height: h } });
      await page.setContent(pictureHTML(d, w, h), { waitUntil: "load" }); await page.evaluate(() => document.fonts.ready);
      await page.screenshot({ path: path.join(dir, name), type: "jpeg", quality: 90 }); await page.close();
    }
  }
  if (browser) { // the site's own link preview
    const w = ARTW["saenredam-cathedral"], img = w ? artData(w) : "";
    const page = await browser.newPage({ viewport: { width: 1200, height: 630 } });
    await page.setContent(`<!doctype html><html><head><meta charset="utf-8"><style>
@font-face { font-family: Cormorant; src: url("${FONT("CormorantGaramond.ttf")}"); font-weight: 300 700; }
@font-face { font-family: Cormorant; src: url("${FONT("CormorantGaramond-Italic.ttf")}"); font-style: italic; font-weight: 300 700; }
@font-face { font-family: CormorantSC; src: url("${FONT("CormorantSC-SemiBold.ttf")}"); }
@font-face { font-family: SourceSerif; src: url("${FONT("SourceSerif4.ttf")}"); font-weight: 200 900; }
html, body { margin: 0; width: 1200px; height: 630px; overflow: hidden; }
body { display: grid; grid-template-columns: 470px 1fr; background: #F4F0E8; color: #1D1B18; font-family: Cormorant, Georgia, serif; }
.art { background: #2A241C ${img ? `url("${img}")` : ""} ${w ? w.focus : "50% 50%"} / cover no-repeat; }
.t { padding: 58px 64px 44px 60px; display: flex; flex-direction: column; gap: 18px; }
.b { display: flex; align-items: center; gap: 14px; } .b svg { width: 30px; height: 38px; } .b span { font-family: CormorantSC, serif; letter-spacing: .34em; font-size: 28px; font-weight: 600; }
h1 { margin: 26px 0 0; font-weight: 500; font-size: 78px; line-height: 1.0; letter-spacing: -.01em; }
p { margin: 0; font-family: SourceSerif, Georgia, serif; font-size: 23px; line-height: 1.45; color: #34302B; max-width: 600px; }
.c { margin-top: auto; font-family: SourceSerif, Georgia, serif; font-size: 14px; color: #6E675D; border-top: 1px solid rgba(29,27,24,.18); padding-top: 14px; }
</style></head><body><div class="art"></div><div class="t"><div class="b">${MARK("#8C6A2B")}<span>ABIDE</span></div>
<h1>A cathedral<br>in your pocket</h1><p>The great ideas, prayers, music, art and poetry of the Christian tradition, and a church near you, in a few minutes a day.</p>
<div class="c">${w ? `${esc(w.artist)}, <i>${esc(w.title)}</i>, ${esc(w.date)}. National Gallery of Art, Washington` : ""}</div></div></body></html>`, { waitUntil: "load" });
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: path.join(ROOT, "dist/og-cathedral.jpg"), type: "jpeg", quality: 90 }); await page.close();
    await browser.close();
  }
  const todayKey = ymd(start);
  fs.writeFileSync(path.join(OUT, "today.json"), JSON.stringify({ date: todayKey, url: `${BASE}/daily/${todayKey}/` }));
  console.log(`Daily: ${days.length} days written to dist/daily (${images ? "with" : "without"} pictures), today is ${todayKey}`);
}
if (import.meta.url === pathToFileURL(process.argv[1]).href) main().catch(e => { console.error(e); process.exit(1); });
