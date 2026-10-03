# Working on Abide (instructions for Claude and other AI agents)

Abide is a website and web app helping people who have never been to church build a daily Christian rhythm and explore the faith in depth. Read `EDITORIAL_GUIDE.md` before writing any content. It is binding.

## Project layout

- `content/library/*.md` – Ideas subjects, five depths each (frontmatter: title, summary, series, order, passage, status). `series: west` puts an entry in Foundations of the West; no series means Big questions.
- `content/debates.json` – the Great Debates: who, when, where, the question, each side's best case in our own words, where they agree, what to listen for, a YouTube search string and a related Library id
- `content/conversations.json` – Conversations: podcast episodes summarised in our own words (show, episode, guests, date, official url, summary, insight, question, optional practice, library id, status)
- `content/voices/*.md` – thinker profiles (frontmatter: name, years, tradition, era, order, status)
- `content/calendar.json` – the daily themes: the weekly cycle, Advent, Christmastide, Lent, Holy Week, Easter week, movable feasts (keyed by days from Easter in the app) and fixed feasts (keyed MM-DD). Each theme has an everyday `idea` and `ideaLine` (the headline seekers see; plain language, no church words), the traditional title (shown quietly as "On the old calendar"), a psalm, reading, midday and evening texts, an intention, two music ids and one Library id; the build checks the ids exist.
- `content/music.json` – each piece has a verified Spotify track id (`spotify`, 22 characters; check with https://open.spotify.com/oembed?url=https://open.spotify.com/track/ID) and internal `recording` notes. Music plays through Spotify's own embed; no YouTube.
- `content/playlists.json` – Music collections (title, line, optional `season`, track ids). Each collection's painting is set in `art.json`.
- `content/art.json` – the paintings: open-access works from the National Gallery of Art, Washington (`nga` is the image id in the gallery's open data), with a `focus` crop, and which painting goes with each day theme, Library subject and collection. `art.mjs` downloads them so Abide serves them itself; the `art-cache` branch keeps a copy. Never use AI-generated or decorative stand-in images: use real works of art, credited.
- `memory.json`, `prayers.json`, `questions.json` – collections
- `public/media/` – images and video (the parish film is an illustration; `src/parish-film-scene.html` is its source)
- `src/app.html` – the app (one file: styles, markup, script); `src/page.css` – shareable page style
- `daily.mjs` + `daily/` – the daily idea: picture, share page and email, sent each morning by GitHub Actions through Resend (see `daily/README.md`). `src/churchyear.js` decides the day's theme for both the app and the email.
- `build.mjs` – no-dependency build: `node build.mjs` writes `dist/`; `node build.mjs --standalone` writes a single-file preview
- `agents/` – Ask Abide, the practice coach and Your path: prompts and tools in `abide-agents.mjs`, the server relay in `relay.mjs` (see `agents/README.md`)
- `site.json` – site name, description, public URL, `askEndpoint` (the relay URL; empty hides the agents on the live site), `plus` (prices, Stripe Payment Links, portal, free limits), `parishes` and `contactEmail`

## Adding a Library subject

1. Research first. Use primary sources and reputable references; collect exact references (book, chapter, question number) and dates.
2. Create `content/library/<slug>.md` following the five-depth structure in the guide. Set `status: draft`. Choose the next free `order`.
3. In depth 4, include the strongest objections, stated fairly. Add a `tag:` line.
4. Run `node build.mjs`. It must finish without "Content problems".
5. In your pull request description, list every factual claim with its source so a reviewer can check them quickly. Flag anything you are unsure of.

## Adding a feast day or theme

Add it to `content/calendar.json` with every field filled, Scripture from the World English Bible, music that exists in `music.json`, and a Library id. Keep feasts ecumenical, and say in the line which tradition keeps a feast when it is not shared by all.

## Adding a Voice or music

Same process: draft status, sources listed in the pull request, build must pass. For living people, cite where they said what you attribute to them.

## Adding a Conversation

Use the show's official episode page or listing for the title, guests, date and link. Write the summary, insight and question in our own words: at most one short quotation (under 25 words) per entry, and never paste or store transcripts. Only summarise what is publicly available; don't summarise subscriber-only content beyond its public description. Choose episodes that bear on Abide's questions (meaning, faith, morality, the West, death, beauty, consciousness, living well). Represent living people fairly and never imply they endorse Abide.

## Live it

Every Ideas entry, debate and conversation needs a 'Live it this week' practice (see the guide). The build fails without one.

## Changing the agents

Prompts live only in `agents/abide-agents.mjs`. Keep the safety paragraph, the citation rule and the 'Live it' ending. The agents may read content and the person's rhythm, never journal text. Never put an API key in the app or the repository.

## Abide Plus

The rhythm and all content stay free; only the AI features are limited, and only on the live site. Never put content behind the paywall, never use countdowns, fake scarcity or guilt, and never let a church pay to rank above another. See `agents/README.md`.

## Rules

- Never mark content `reviewed`. Only a human reviewer does that.
- Never paste copyrighted lyrics or long quotations (see the guide).
- Don't change the app's design or code when asked only for content.
- Keep British spelling and the voice described in the guide.
- One subject per pull request, so review stays easy.
