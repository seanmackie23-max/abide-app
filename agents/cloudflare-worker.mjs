// Cloudflare Worker entry for the Abide relay. Deploy with: npx wrangler deploy (see agents/README.md)
import { handle, cors } from "./relay.mjs";
import { confirm } from "./subscribe.mjs";

export default {
  async fetch(request, env) {
    const h = cors(request.headers.get("Origin") || "", env), { ok, ...headers } = h;
    if (request.method === "OPTIONS") return new Response(null, { status: 204, headers });
    const url = new URL(request.url);
    if (request.method === "GET" && url.searchParams.get("confirm")) return Response.redirect(await confirm(url.searchParams.get("confirm"), env), 302);
    if (request.method !== "POST") return new Response("Abide relay", { status: 405, headers });
    if (!ok) return Response.json({ error: "Origin not allowed" }, { status: 403, headers });
    let body; try { body = await request.json(); } catch (e) { return Response.json({ error: "Bad JSON" }, { status: 400, headers }); }
    const { status, json } = await handle(body, { ip: request.headers.get("CF-Connecting-IP") || "?", env, selfUrl: url.origin + url.pathname });
    return Response.json(json, { status, headers });
  },
};
