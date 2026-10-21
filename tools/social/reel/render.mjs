import { chromium } from "/home/claude/.npm-global/lib/node_modules/playwright/index.mjs";
import fs from "node:fs";
fs.mkdirSync("frames", { recursive: true });
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
await p.goto("file://" + process.cwd() + "/film.html"); await p.waitForTimeout(1500);
const N = 21 * 30;
for (let i = 0; i < N; i++) { await p.evaluate(t => render(t), i / 30); await p.screenshot({ path: `frames/f${String(i).padStart(4, "0")}.jpg`, type: "jpeg", quality: 90 }); }
await b.close();
