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
- `content/art.json` – the paintings: open-access works from the National Gallery of Art, Washington (`nga` is the image id in the gallery's open data), with a `focus` crop, and which painting goes with each day theme, Library subject and collection. `art.mjs` downloads them so Abide serves them itself; the `art-cache` branch keeps a copy. Never use AI-generated or decorative stand-in images: use real works of art, credited. Every day theme needs its own painting chosen for its idea, and no two themes may share one (the build checks). Round paintings (tondi) get `zoom: 1.42`.
- `content/research.json` – peer-reviewed papers behind the Science entries (`series: science`): authors, year, title, journal, ref, doi, design, found, limits and strength (strong, moderate, early, contested, null), and which entries cite them. Verify every paper against the publisher, Crossref or a repository; take numbers from the abstract; include the strongest critical, null and failed-replication studies; never cite retracted work. Science entries need at least three papers.
- `content/memory.json` – the Learn canon, the words worth carrying from Athens and Jerusalem: id, title, kind, author, work, translator, tradition (athens, rome, jerusalem, church, poets, prayers, hymns), lines, why, source. Every text verbatim from a public-domain translation (translator died before 1955, published before 1929) or the World English Bible, with the source URL.
- Freshness: `calendar.json` `variants` gives each weekday extra ideas that rotate by week, and the app's daily edition rotates the passage, paper, debate or conversation and voice by date. Add to these pools rather than repeating content.
- `content/stories.json` – Family: Bible stories retold for ages 4–10 in our own words, faithful to the World English Bible (id, title, ref, text paragraphs, three 'I wonder' questions, a prayer, a painting id; each painting used once). One a night, by date. Pastoral content (stories, `prayers.json` moments, `questions.json` answers) needs a pastor's review before it is marked reviewed.
- `prayers.json` (graces, night prayers, `moments` blessings with a [Name] placeholder, `table` dinner questions), `questions.json` (children's questions by age, with a `tip` for the parent) – collections
- `public/media/` – the parish welcome film (`parish-welcome.mp4` and its poster), made by `parish-film.mjs` from real NGA paintings with captions in Abide's type; edit the church details and lines there and rerun it (needs Playwright, ffmpeg and the cached art)
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

## Churches near you

Community finds real churches from OpenStreetMap (Overpass API, Nominatim for a typed town), nearest first, in the browser. Location is rounded to about 100 m, used only to search the map and kept on the device. Ranking is by distance only. Christian places of worship are included except groups outside historic Trinitarian Christianity (`NEAR_SKIP` in `src/app.html`); change that list only with the owner's say-so. Service times come from the map's `service_times` tag or, on the live site, from the church's own website through the relay (`agents/churches.mjs`), which extracts only what the page says. Always credit © OpenStreetMap contributors.

## Community

Community is the way from phone to pew: a rhythm alone, one other person, a circle, your church, a first visit, belonging. Circles and "I'm going" run on the relay (`agents/community.mjs`): invite-only, small (up to 12), no likes, follower counts, public profiles or feed, and journal text never leaves the device. "This week near you" puts easy first visits (evensong, concerts, candlelit evenings, cafés, newcomers' courses) before Sunday services. Keep it that way: every social feature should move someone towards real people in a real place.

## Abide Plus

The rhythm and all content stay free; only the AI features are limited, and only on the live site. Never put content behind the paywall, never use countdowns, fake scarcity or guilt, and never let a church pay to rank above another. See `agents/README.md`.

## Rules

- Never mark content `reviewed`. Only a human reviewer does that.
- Never paste copyrighted lyrics or long quotations (see the guide).
- Don't change the app's design or code when asked only for content.
- Keep British spelling and the voice described in the guide.
- One subject per pull request, so review stays easy.
