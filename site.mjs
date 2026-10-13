// Reads site.json once for build.mjs and daily.mjs, and applies the staging settings.
// PEW_STAGING=1 builds the staging copy: served under <baseUrl>/staging/, hidden from search,
// marked with a banner, analytics off, and its own storage on the device so testing never touches your real data.
import fs from "node:fs";
import path from "node:path";
const ROOT = path.dirname(new URL(import.meta.url).pathname);
export const site = JSON.parse(fs.readFileSync(path.join(ROOT, "site.json"), "utf8"));
export const staging = !!process.env.PEW_STAGING;
if (site.customDomain && !process.env.PEW_KEEP_BASE) site.baseUrl = "https://" + site.customDomain;
site.baseUrl = site.baseUrl.replace(/\/$/, "") + (staging ? "/staging" : "");
site.features = Object.assign({ agents: false, community: false, plus: false, churchTimes: false }, site.features || {});
const A = site.analytics || {};
export const analytics = staging ? { plausible: "", src: "" } : { plausible: A.plausible || "", src: A.src || "https://plausible.io/js/script.js" };
// The tag for static pages (Library, Voices, the daily share pages, Join, the church portal). Cookie-free, nothing personal.
export const analyticsTag = () => analytics.plausible
  ? `<script defer data-domain="${analytics.plausible}" src="${analytics.src}"></script><script>window.plausible=window.plausible||function(){(window.plausible.q=window.plausible.q||[]).push(arguments)}</script>`
  : "";
export const stagingHead = () => staging ? `<meta name="robots" content="noindex,nofollow">` : "";
export const stagingBanner = () => staging ? `<div style="position:fixed;z-index:9999;top:0;left:50%;transform:translateX(-50%);background:#8E2B2B;color:#fff;font:600 11px/1 system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase;padding:5px 10px;border-radius:0 0 6px 6px;pointer-events:none">Staging · not the live site</div>` : "";
