# Working on Pew (instructions for Claude and other AI agents)

Pew is a website and web app helping people who have never been to church build a daily Christian rhythm and explore the faith in depth. Read `EDITORIAL_GUIDE.md` before writing any content. It is binding.

## Project layout

- `content/library/*.md` – Ideas subjects, five depths each (frontmatter: title, summary, series, order, passage, status). `series: west` puts an entry in Foundations of the West; no series means Big questions.
- `content/debates.json` – the Great Debates: who, when, where, the question, each side's best case in our own words, where they agree, what to listen for, a YouTube search string and a related Library id
- `content/conversations.json` – Conversations: podcast episodes summarised in our own words (show, episode, guests, date, official url, summary, insight, question, optional practice, library id, status)
- `content/voices/*.md` – thinker profiles (frontmatter: name, years, tradition, era, order, status)
- `content/calendar.json` – the daily themes: the weekly cycle, Advent, Christmastide, Lent, Holy Week, Easter week, movable feasts (keyed by days from Easter in the app) and fixed feasts (keyed MM-DD). Each theme has an everyday `idea` and `ideaLine` (the headline seekers see; plain language, no church words), the traditional title (shown quietly as "On the old calendar"), a psalm, reading, midday and evening texts, an intention, two music ids and one Library id; the build checks the ids exist.
- `content/music.json` – each piece has a verified Spotify track id (`spotify`, 22 characters; check with https://open.spotify.com/oembed?url=https://open.spotify.com/track/ID) and internal `recording` notes. Music plays through Spotify's own embed; no YouTube.
- `content/playlists.json` – Music collections (title, line, optional `season`, track ids). Each collection's painting is set in `art.json`.
- `content/art.json` – the paintings: open-access works from the National Gallery of Art, Washington (`nga` is the image id in the gallery's open data), with a `focus` crop, and which painting goes with each day theme, Library subject and collection. `art.mjs` downloads them so Pew serves them itself; the `art-cache` branch keeps a copy. Never use AI-generated or decorative stand-in images: use real works of art, credited. Every day theme needs its own painting chosen for its idea, and no two themes may share one (the build checks). Round paintings (tondi) get `zoom: 1.42`.
- `content/research.json` – peer-reviewed papers behind the Science entries (`series: science`): authors, year, title, journal, ref, doi, design, found, limits and strength (strong, moderate, early, contested, null), and which entries cite them. Verify every paper against the publisher, Crossref or a repository; take numbers from the abstract; include the strongest critical, null and failed-replication studies; never cite retracted work. Science entries need at least three papers.
- `content/memory.json` – the Learn canon, the words worth carrying from Athens and Jerusalem: id, title, kind, author, work, translator, tradition (athens, rome, jerusalem, church, poets, prayers, hymns), lines, why, source. Every text verbatim from a public-domain translation (translator died before 1955, published before 1929) or the World English Bible, with the source URL.
- Freshness: `calendar.json` `variants` gives each weekday extra ideas that rotate by week, and the app's daily edition rotates the passage, paper, debate or conversation and voice by date. Add to these pools rather than repeating content.
- `content/path.json` – the reading path's stages (see below)
- `content/journeys.json` – Explore's learning journeys, and `content/halls.json` – the eight halls they sit in (see below)
- `content/stories.json` – Family: Bible stories retold for ages 4–10 in our own words, faithful to the World English Bible (id, title, ref, text paragraphs, three 'I wonder' questions, a prayer, a painting id; each painting used once). One a night, by date. Pastoral content (stories, `prayers.json` moments, `questions.json` answers) needs a pastor's review before it is marked reviewed.
- `prayers.json` (graces, night prayers, `moments` blessings with a [Name] placeholder, `table` dinner questions), `questions.json` (children's questions by age, with a `tip` for the parent) – collections
- `public/media/` – the parish welcome film (`parish-welcome.mp4` and its poster), made by `parish-film.mjs` from real NGA paintings with captions in Pew's type; edit the church details and lines there and rerun it (needs Playwright, ffmpeg and the cached art)
- `src/app.html` – the app (one file: styles, markup, script); `src/page.css` – shareable page style
- `daily.mjs` + `daily/` – the daily idea: picture, share page and email, sent each morning by GitHub Actions through Resend (see `daily/README.md`). `src/churchyear.js` decides the day's theme for both the app and the email.
- `build.mjs` – no-dependency build: `node build.mjs` writes `dist/`; `node build.mjs --standalone` writes a single-file preview
- `agents/` – Ask Pew, the practice coach and Your path: prompts and tools in `abide-agents.mjs`, the server relay in `relay.mjs` (see `agents/README.md`)
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

Use the show's official episode page or listing for the title, guests, date and link. Write the summary, insight and question in our own words: at most one short quotation (under 25 words) per entry, and never paste or store transcripts. Only summarise what is publicly available; don't summarise subscriber-only content beyond its public description. Choose episodes that bear on Pew's questions (meaning, faith, morality, the West, death, beauty, consciousness, living well). Represent living people fairly and never imply they endorse Pew.

## What guides the content

Pew draws on everything that shaped the West: the Christian faith at the centre, alongside the Greek and Roman classics, the great poets and the art and music of Christendom. Don't say this in the app; let it show. Pair the day's Scripture with wisdom from Athens and Rome where it fits (the midday companion does this daily), and keep Learn, Ideas and the daily edition drawing on both.

## The day's story (content/bank.json and content/schedule.json)

Stories live once in the story bank, `content/bank.json`, keyed by a story id. `content/schedule.json` says which story is told on which date (`"2026-11-01": "all-saints-great-multitude"`). The build joins them into the dated days. To fill a date, add a story to the bank and schedule it; a story can be scheduled again in a later year without copying it, and no painting may be used by two stories in the bank (the build checks). Reviewer notes for each batch of stories are in `content/review/stories-notes.json`.

A day is one thread, and everything that day follows it: the story (`story.retell`, a World English Bible `verse`), the painting of that exact moment (`art`, `artLink`, `see`), what it means (`meaning`), an echo from the classics or the Bible with the connection spelled out (`echo.link`), the day's `question`, a `prayer` that answers the story, `midday` and `evening` lines, `music` with a `why`, and an optional children's `family` story. The morning, midday and evening, Today, the entrance, the two-minute read and the daily email all use it. Choose the story first, and only if the gallery has a painting of that very moment; never write text to justify a painting. Name the church calendar only on real feasts and seasons. Days without an entry fall back to `calendar.json`; keep writing days ahead (in batches, reviewed) so that fallback is rare.

## Loading in pieces

The app page carries only what the first screen needs: days near the build date (today and tomorrow whole), a light index of the other days for the reading path, and an index of each learning journey. Long readings, whole days (`data/days/<date>.json`) and whole journeys (`data/journeys/<id>.json`) are fetched on demand with `fetchData()` and kept offline by the service worker. The site rebuilds daily, so today is always inline. The standalone preview inlines everything. When a feature needs a field that the light index leaves out, fetch it rather than inlining more.

## Today

Today is one card: the day's painting, its idea, and one button, Begin, which opens the next moment (the morning first). "Just read the story" is the quiet alternative. Midday, evening and night appear afterwards as quiet optional chips, never as a checklist. Reading, music, lines to learn, a journey in progress and the children's story sit under "Go further today". Don't add cards to Today; put new things under Go further, in Explore or in Your story.

## Your story

The logo opens Your story (`openJourney`): the reading path, the Bible, the great voices, paintings, your words, learning journeys in progress and Your year. It is the one place for progress; don't add another.

## Analytics

Off unless `site.json` `analytics.plausible` is set (a cookie-free, Plausible-compatible host). It counts three things only: "Morning kept", "Returned after a week" and "First church visit". Never send anything personal or any text the person wrote. Don't add events without the owner's say-so.

## The reading path and your journey (content/path.json)

Each dated day also carries a full reading and a place on the reading path:
- `passage`: the whole Bible passage of the story, verbatim World English Bible, with verse numbers.
- `book`, `virtue` and `classic`: these feed the journey.
- `stage`: an id from `content/path.json`. Stages run a few days to a few weeks (Setting out, Seeing others…); each has a `title`, `line` and `why`, and each must build on the one before.
- `read.why`: why this reading, today, at this point on the path.

The day's long read is the Bible passage, or a chapter from a great book when one fits better: a theologian, philosopher, poet or psychologist. A great-book `read` has `author`, `work`, `ref`, `kind` (church, philosophy, psychology, poetry), `who`, `when` (place, year), `minutes`, `translator`, `source` and `paras`. The text must be verbatim from a public-domain edition (the same rule as Learn: translator died before 1955; original English published before 1929). Take it from the Project Gutenberg text, for example the GITenberg mirrors on GitHub, and link the Gutenberg page. Mark any cut with a paragraph that is just "…". Never paste copyrighted modern writers (C. S. Lewis, Frankl, Jung, Bonhoeffer in translation); point to them in our own words in Ideas instead.

Your journey (`openJourney`) and Your year (`openYear`) are worked out on the device from `store.days` (kept, `read`, `intention`, `art`, `listened`), the day entries, `store.learned` and `store.visits`. They are free, and the person's words never leave the device. No streak guilt: show what was lived, never what was missed.

## Learning journeys (content/journeys.json)

Explore leads with learning journeys: a deep course on one great question, in six sessions and a closing. The daily rhythm is the ritual; the journeys are the deeper learning, and they tie everything else together. Each session has:
- `why`: how it builds on the session before. The sessions must make an arc.
- `read`: a whole Bible passage (verbatim WEB, with verse numbers in `paras`), or a great-book chapter (verbatim public domain, with the same fields as the daily read), plus `readWhy`.
- `think`: a Library entry and the depth that fits.
- `listen`: an optional conversation or debate.
- `evidence`: papers from research.json, described honestly.
- `learn`: a memory id.
- `music`: with a `why`.
- `look`: a painting; describe only what is in it.
- `practice`: Live it.
- `reflect`: a question.

Journeys live in eight halls (`content/halls.json`), drawn as a cathedral floor plan on Explore with the cross at the crossing: I The Great Story (west door), II The Great Questions and III Know Thyself (the nave), VI Athens, Rome and Jerusalem and VII The City (the transepts), IV The Noble Life and VIII Beauty (the choir), V The Inner Life (the apse). A hall's first journey is its 'Start here'; `later` lists the journeys still to be written; the app does not show them, only finished journeys. Every journey must be in a hall (the build checks). When you write one, move it from `later` into `journeys`.

Every journey has one session that states the strongest objection at full strength. The closing asks for the person's own answer. The first session of each journey is free; the rest is Plus. Progress, notes and answers live in `store.courses` on the device. The reviewer's notes for each journey (every claim and its source) are in `content/review/journeys-notes.json`. The build checks every id.

## The four moments

The moments (`OFFICES` in `src/app.html`) are built around the day: each opens with today's idea, its place on the church's calendar (`title`, `line`, the season) and why this moment exists. The morning: pray the psalm verse with its `psalmNote`, look at today's painting and then read its interpretation (`look`), the weekday question, today's action (`intention`), and today's own morning prayer (`prayer`), then a pointer to today's music, lines, question and story. Every theme needs `look`, `psalmNote` and `prayer` (the build checks). Interpretations must only describe what is really in the painting. Intentions are kind, concrete actions, not wellness habits (no going outside, daylight, phones or breathing). The question to carry rotates by weekday (`CARRY`; Friday keeps "take up your cross"); the evening reviews today's idea; the night looks ahead to tomorrow's idea. Keep them varied: don't add fixed prompts that repeat every day.

## Live it

Every Ideas entry, debate and conversation needs a 'Live it this week' practice (see the guide). The build fails without one.

## Changing the agents

Prompts live only in `agents/abide-agents.mjs`. Keep the safety paragraph, the citation rule and the 'Live it' ending. The agents may read content and the person's rhythm, never journal text. Never put an API key in the app or the repository.

## Churches near you

Community finds real churches from OpenStreetMap (Overpass API, Nominatim for a typed town), nearest first, in the browser. Location is rounded to about 100 m, used only to search the map and kept on the device. Ranking is by distance only. Christian places of worship are included except groups outside historic Trinitarian Christianity (`NEAR_SKIP` in `src/app.html`); change that list only with the owner's say-so. Service times come from the map's `service_times` tag or, on the live site, from the church's own website through the relay (`agents/churches.mjs`), which extracts only what the page says. Always credit © OpenStreetMap contributors.

## Sunday (the third tab)

One purpose, said at the top: **go to church once, knowing exactly what to expect.** It must work anywhere on day one with no church signed up, so it depends only on OpenStreetMap and content in the app. It has three steps, then a question.
1. **Choose a church near you.** Nearest first from the map, with a link to check Sunday's time on the church's website, and directions.
2. **Read the three-minute guide** (`content/sunday.json`). The service step by step in the church's tradition (Anglican, choral evensong, Catholic, Protestant, free church, Orthodox): what happens, when to stand, sit or kneel, what to say, and why. It has a quiet mode for use in church. The tradition comes from the person's choice, the church's own portal setting, or its map denomination (`map`). Responses are short traditional or ecumenical texts only. It stays draft until a minister of each tradition has read it.
3. **Say you're going.** On Saturday Today shows "Tomorrow, in two minutes"; on Sunday it opens the guide, then "I went".

Afterwards it asks "Would you go back?", and the tab becomes "Your church".

The only social element is "Going alone is fine. Most first-timers do. Or bring someone": a share message. Don't add groups, feeds or strangers meeting up: people don't do it. What a church adds by signing up through the portal (welcomer, weekly note, a journey run as a course) appears quietly when it exists; nothing depends on it. Circles show only on the live site for people already in one.

## Community

Community is the way from phone to pew: a rhythm alone, one other person, a circle, your church, a first visit, belonging. Circles and "I'm going" run on the relay (`agents/community.mjs`): invite-only, small (up to 12), no likes, follower counts, public profiles or feed, and journal text never leaves the device. "This week near you" puts easy first visits (evensong, concerts, candlelit evenings, cafés, newcomers' courses) before Sunday services. Keep it that way: every social feature should move someone towards real people in a real place.

## Pew for Churches

`src/church.html` (built to `/church/`) is the church portal, backed by `agents/parish.mjs`. Free for every church: claim, set its tradition (so newcomers get the right Sunday guide), keep times and events up to date, a named welcomer, "someone's coming" emails. Partner adds running Pew's learning journeys as the church's newcomers' course (`course`: journey, start, day, time, place), members' Plus, a welcome film and newcomer numbers. See `BUSINESS.md` for the whole model; keep it, the app's Plus page and the portal saying the same thing.

## Pew Plus

The app has three places: Today (free), Explore (Plus) and Sunday (free). Free: the daily rhythm, today's music, the first two depths of every idea, churches near you, "I'm going" and joining a circle. Plus (€4.99 a month, €39 a year, 30-day free trial): the rest of Explore (all depths, papers, debates, conversations, voices, the music library, Learn, Family), starting circles, the full AI guide and the calendar. Gate Plus features with `needPlus()` at the start of the function that opens them. Keep it simple: before adding a feature, decide which of the three places it belongs in, and prefer improving what exists. Never use countdowns, fake scarcity or guilt, and never let a church pay to rank above another. See `BUSINESS.md` and `agents/README.md`.

## Rules

- Never mark content `reviewed`. Only a human reviewer does that.
- Never paste copyrighted lyrics or long quotations (see the guide).
- Don't change the app's design or code when asked only for content.
- Keep British spelling and the voice described in the guide.
- One subject per pull request, so review stays easy.
