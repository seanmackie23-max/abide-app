// AWS Lambda entry for the Abide relay (Node.js 20+, behind a Lambda Function URL). See agents/README.md.
// Configure CORS on the Function URL itself (allowed origin = your site), not here.
import { handle, cors } from "./relay.mjs";
import { confirm } from "./subscribe.mjs";

export const handler = async (event) => {
  const env = process.env, origin = event.headers?.origin || event.headers?.Origin || "";
  const selfUrl = `https://${event.requestContext?.domainName || event.headers?.host}${event.rawPath || "/"}`;
  if ((event.requestContext?.http?.method) === "GET" && event.queryStringParameters?.confirm) return { statusCode: 302, headers: { Location: await confirm(event.queryStringParameters.confirm, env) }, body: "" };
  if (!cors(origin, env).ok) return { statusCode: 403, body: JSON.stringify({ error: "Origin not allowed" }) };
  if ((event.requestContext?.http?.method || "POST") !== "POST") return { statusCode: 405, body: "Abide relay" };
  let body; try { body = JSON.parse(event.isBase64Encoded ? Buffer.from(event.body, "base64").toString() : event.body || ""); } catch (e) { return { statusCode: 400, body: JSON.stringify({ error: "Bad JSON" }) }; }
  const { status, json } = await handle(body, { ip: event.requestContext?.http?.sourceIp || "?", env, selfUrl });
  return { statusCode: status, headers: { "content-type": "application/json" }, body: JSON.stringify(json) };
};
