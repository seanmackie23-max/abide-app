// A tiny key-value store for Community (circles, "I'm going" counts).
//   Cloudflare: bind a KV namespace as ABIDE_KV in wrangler.toml.
//   AWS Lambda: create a DynamoDB table (partition key "k", string; TTL attribute "ttl") and set ABIDE_TABLE.
//   Neither: an in-memory store, fine for local testing only (it forgets on restart).
const mem = new Map();
let ddb = null;

export function store(env) {
  if (env.ABIDE_KV) return {
    get: async k => { const v = await env.ABIDE_KV.get(k); return v ? JSON.parse(v) : null; },
    put: (k, v, days = 180) => env.ABIDE_KV.put(k, JSON.stringify(v), { expirationTtl: days * 86400 }),
    kind: "kv",
  };
  if (env.ABIDE_TABLE) return {
    async get(k) { const c = await client(); const r = await c.send(new c.GetItemCommand({ TableName: env.ABIDE_TABLE, Key: { k: { S: k } } })); return r.Item ? JSON.parse(r.Item.v.S) : null; },
    async put(k, v, days = 180) { const c = await client(); await c.send(new c.PutItemCommand({ TableName: env.ABIDE_TABLE, Item: { k: { S: k }, v: { S: JSON.stringify(v) }, ttl: { N: String(Math.floor(Date.now() / 1000) + days * 86400) } } })); },
    kind: "dynamodb",
  };
  return {
    get: async k => { const x = mem.get(k); return x && x.exp > Date.now() ? structuredClone(x.v) : null; },
    put: async (k, v, days = 180) => { mem.set(k, { v: structuredClone(v), exp: Date.now() + days * 864e5 }); },
    kind: "memory",
  };
}
async function client() {
  if (ddb) return ddb;
  const m = await import("@aws-sdk/client-dynamodb"); // included in the Lambda Node.js runtime
  const c = new m.DynamoDBClient({});
  ddb = { send: x => c.send(x), GetItemCommand: m.GetItemCommand, PutItemCommand: m.PutItemCommand };
  return ddb;
}
