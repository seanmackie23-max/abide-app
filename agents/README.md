# Abide's agents

Abide has two small Claude-powered agents:

- **Ask Abide** answers questions about meaning, faith, the West and how to live. It searches and reads Abide's own entries (tools `search_ideas`, `read_entry`), gives each side its strongest case, cites the entries it used and ends with one "Live it" practice. It routes crisis and pastoral matters to people and helplines.
- **Shape my week** (the practice coach) reads the person's recent rhythm (`get_my_rhythm`: no journal text) and suggests one practice for the week, which they can take on with one tap.

Both are defined once in `abide-agents.mjs` (prompts and tool schemas). The tools always run in the browser, over Abide's content and the person's own device data.

## Where they run

| Where | How Claude is reached | Who pays |
|---|---|---|
| Inside Claude (the artifact preview) | The viewer's own Claude, via the `sample` capability | The viewer |
| The live site | `relay.mjs`, a tiny server that holds the API key | Abide |
| Neither available | The Ask and Shape buttons are hidden | — |

The browser never holds the API key and never chooses the prompt: it sends only `{agent, messages}`, and the relay adds the system prompt and tools.

## Turning it on for the live site

You need an Anthropic API key from https://console.anthropic.com (set a monthly spend limit there).

### Option A: Cloudflare Worker (simplest, free tier)

```
cd agents
npx wrangler login
npx wrangler deploy
npx wrangler secret put ANTHROPIC_API_KEY
```

Wrangler prints a URL like `https://abide-relay.<you>.workers.dev`. Put it in `site.json` as `"askEndpoint"` and push. Add a Cloudflare rate-limiting rule for real traffic.

### Option B: AWS Lambda in Frankfurt (eu-central-1)

1. Zip `aws-lambda.mjs`, `relay.mjs` and `abide-agents.mjs` together.
2. Create a Node.js 22 function with handler `aws-lambda.handler`, 256 MB and a 60 s timeout.
3. Set the environment variables `ANTHROPIC_API_KEY` (better: read it from Secrets Manager), `ALLOWED_ORIGINS`, `MODEL` and `RATE_PER_10_MIN`.
4. Add a Function URL (auth NONE) with CORS allowing your site's origin and the POST method.
5. Set reserved concurrency, for example 20, to cap spend.
6. Put the URL in `site.json` as `"askEndpoint"`.

## Settings

- `MODEL`: defaults to `claude-haiku-4-5-20251001`, which is fast and cheap. `claude-sonnet-5-5` gives richer answers.
- `ALLOWED_ORIGINS`: a comma-separated list of the sites allowed to call the relay.
- `RATE_PER_10_MIN`: requests per IP per 10 minutes. This is a best-effort limit per instance.

## Changing the agents

Edit the prompts in `abide-agents.mjs`, run `node build.mjs`, push, and redeploy the relay so both copies match. Keep the safety paragraph. Never let an agent mark content `reviewed`, store journal text or claim to be a minister.
