# Abide's agents

Abide has two small Claude-powered agents:

- **Ask Abide** answers questions about meaning, faith, the West and how to live. It searches and reads Abide's own entries (tools `search_ideas`, `read_entry`), gives each side its strongest case, cites the entries it used and ends with one "Live it" practice. It routes crisis and pastoral matters to people and helplines.
- **Shape my week** (the practice coach) reads the person's recent rhythm (`get_my_rhythm`: no journal text) and suggests one practice for the week, which they can take on with one tap.

- **Your path** plans a personal four-week route. The person answers four quick questions (where they're starting from, what draws them, time each day, anything in their own words). The agent reads the whole catalogue (`list_catalogue`) and plans weekly themes, three to five steps a week and one practice to live each week. The app drops any step whose ref doesn't exist, and any duplicate. The path is kept on the device, works without Claude once planned, and can be adjusted or started again.

All three are defined once in `abide-agents.mjs` (prompts and tool schemas). The tools always run in the browser, over Abide's content and the person's own device data.

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

## Church service times

The same relay reads a church's website for its service times (`agents/churches.mjs`, called with `{action: "church_times", url, name}`), so "Churches near you" can show times for churches that don't list them on OpenStreetMap. It fetches the home page and one likely services page, sends the text to Claude to extract only the times it states, and caches each answer for a day. Until the relay is live, the button opens the church's website instead.

## Settings

- `MODEL`: defaults to `claude-haiku-4-5-20251001`, which is fast and cheap. `claude-sonnet-5-5` gives richer answers.
- `ALLOWED_ORIGINS`: a comma-separated list of the sites allowed to call the relay.
- `RATE_PER_10_MIN`: requests per IP per 10 minutes. This is a best-effort limit per instance.

## Changing the agents

Edit the prompts in `abide-agents.mjs`, run `node build.mjs`, push, and redeploy the relay so both copies match. Keep the safety paragraph. Never let an agent mark content `reviewed`, store journal text or claim to be a minister.

## Abide Plus (how Abide pays its way)

**Free forever:** the daily rhythm, every idea, debate and conversation, music, Learn, Family and a first path.

**Free on the website, with limits:** 3 Ask Abide questions a day and Shape my week once a week. The relay also enforces a per-IP daily cap (`FREE_ASK_PER_DAY`, `FREE_PATH_PER_DAY`, `FREE_COACH_PER_DAY`).

**Plus:** the AI features without limits, reshaping your path, and a new path whenever you like. Also on offer: Founding Patron (Plus at a higher price, for supporters), Gift a year, and Abide for parishes.

**The preview inside Claude is never limited**, because the viewer's own Claude pays there.

There's no database and no accounts yet. Payment uses Stripe Payment Links. When someone returns from checkout, the relay checks the session with Stripe and issues a signed **Plus key** (`plus.mjs`), which the browser keeps. Every agent call carries the key, and the relay checks its signature. Members can copy their key to use Plus on another device. Gift buyers receive a key to send on. Keys for subscriptions renew themselves while the subscription is active.

### Setting it up (do it in Stripe's test mode first)

1. In Stripe, create the products:
   - Abide Plus, recurring at €6.99 a month and €49 a year
   - Founding Patron, recurring at €120 a year
   - Gift a year of Plus, a one-off €49
2. Create a Payment Link for each one. Under "After payment", choose to redirect to your site:
   - Subscriptions: `https://seanmackie23-max.github.io/abide-app/?plus=success&session_id={CHECKOUT_SESSION_ID}`
   - The gift: `https://seanmackie23-max.github.io/abide-app/?gift=success&session_id={CHECKOUT_SESSION_ID}`
3. Turn on Stripe's customer portal and copy its login link. This is how members manage or cancel.
4. Add two secrets to the relay:
   - `STRIPE_SECRET_KEY`: a restricted key that can read Checkout Sessions and Subscriptions
   - `TOKEN_SECRET`: a long random string, for example from `openssl rand -hex 32`
   With Cloudflare, add them with `npx wrangler secret put STRIPE_SECRET_KEY` and `npx wrangler secret put TOKEN_SECRET`.
5. Put the Payment Links and the portal link in `site.json` under `plus`. Add `parishes.link` (or `contactEmail`) for the parishes offer, then push.
   Any plan without a link shows as "Opening soon".

Prices, the free limits and the copy all live in `site.json` and `src/app.html`. Changing the free limits means updating both `site.json` and the relay's variables.

Before taking real money in Germany, also check:
- the legal pages: Impressum, privacy policy, terms and the 14-day withdrawal notice;
- the online cancellation button that German law (§312k BGB) requires for subscriptions;
- VAT (Stripe Tax can handle it).
