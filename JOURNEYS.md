# Writing a degree-level learning journey

The first one written this way is `light-stone-glass` (Light, stone and glass), in the Beauty hall: use it as the model.

A learning journey is a course on one great question, at the depth of a good first-year university paper in theology, history of art, philosophy or classics, written so that someone who has never studied can follow every step. Read `EDITORIAL_GUIDE.md` and the "Learning journeys" section of `CLAUDE.md` first; this file adds the degree-level parts.

A journey is about **6 to 10 hours** of study: six sessions of about an hour each and a closing of about an hour, plus whatever the person chooses to listen to and read next. Every session divides into sittings of 10 to 15 minutes, and the app remembers where the person stopped.

The older journeys use the short session (read, think, listen, evidence, learn, music, look, live it, reflect). A degree-level journey keeps all of that and adds the parts below. The build checks them whenever a journey has `"level"` set.

## Before writing: the course pack

Gather everything first, then write. Never write text to justify a source you have not found.

- **The paper it follows** (`follows`, internal, never shown): the university paper whose depth it aims at, e.g. "a first-year history of art paper on Gothic architecture". Use it to judge depth; never name a university in the app.
- **Set texts**: every primary source, from a public-domain edition (translator died before 1955 and published before 1929, or original English published before 1929) or the World English Bible. Take the text from the Project Gutenberg file (the GITenberg mirrors on GitHub), never retype it.
- **People** (`people`): the figures and the modern scholars who matter, one line each.
- **Timeline** (`timeline`): 10 to 20 dates.
- **Places** (`places`): the real buildings or sites, where they are and why they matter.
- **Paintings**: open-access works from the National Gallery of Art, chosen before writing, described only from what is in them.
- **Music**: pieces in `music.json` (or new ones with a verified Spotify id).
- **Glossary** (`glossary`): 20 to 40 terms with plain definitions.
- **Reading list** (`reading`): the modern books, in three tiers: `start` (anyone), `deeper` (a keen reader), `scholars` (what a student would be set). Titles and one line each; modern books are summarised, never quoted at length.

## The journey

| Field | What it is |
|---|---|
| `id`, `title`, `question`, `line`, `why`, `art`, `status` | as for every journey (`status: draft`) |
| `level` | `foundation`, `intermediate` or `advanced`, like the years of a degree |
| `follows` | internal: the paper it aims at (see above) |
| `before` | optional: ids of journeys worth taking first |
| `outcomes` | four to six, as concrete as an exam: "explain why…", "read a window pane by pane" |
| `people`, `timeline`, `places`, `glossary`, `reading` | the course pack, shown on the journey's front page |
| `sessions` | six, each building on the last; one of them has `"objection": true` |
| `closing` | see below |

## How a session is shown

A degree-level session is a click-through, never one long page. Each screen is short and says where the person is and why: a row of stages at the top (Start, Read, Compare, Lecture, Debate, Look, Listen, Check, Write, Finish), the stage's purpose on its first screen, and a Next button that names the next stage. The reading is split into pages of about 200 words with their notes; the lecture is one section per screen, each ending with its key point; the debate is one view per screen, then 'which convinces you?'; each check question is its own screen. Contents lets people jump, and the app reopens a session where they stopped. Write with this in mind: short sections, one idea each.

## Each session (about an hour)

Everything the short session has, plus:

| Field | What it is | Time |
|---|---|---|
| `plain` | **In plain words**: three sentences, what this is about and why it matters, for someone who has never studied it | 1 min |
| `before` | **Before you read**: two or three questions to read with | 1 min |
| `read.notes` | **Margin notes** on the set text: `[{ "p": paragraph index, "text": "…" }]`, explaining a hard line, a name or an allusion | (in the reading) |
| `read` | the set text, 800 to 6,000 words for a great book (dense texts can be shorter) (a whole Bible passage for Scripture). Mark cuts with a paragraph that is just "…" | 20–30 min |
| `compare` | **Compare**: a second, short primary text that agrees or disagrees, in the same shape as `read`, plus `why` | 5 min |
| `lecture` | **The lecture**: `{ "sections": [{ "h": "…", "paras": ["…"], "key": "…" }], "refs": ["…"] }`; each section is one screen, so keep it to 120–250 words, and `key` is its point in one sentence, 1,000 to 2,500 words in our own words, one idea per section, with references a reviewer can check | 15 min |
| `debate` | **The scholars' debate**: `{ "question": "…", "positions": [{ "name", "who", "view", "evidence" }], "agree": "…" }`, two or three positions stated fairly | 8 min |
| `look.points` | **What to look for**: three to six things that are really in the painting | 5 min |
| `terms` | glossary terms this session uses | |
| `check` | **Check your understanding**: four or five `{ "q", "options": [4], "answer": index, "why" }`. For the person, not a score: no marks, no badges | 5 min |
| `tutorial` | **The tutorial question**: `{ "question", "approach", "strong": ["…"] }`. The person writes 200 to 500 words, kept on the device; `strong` (what a good answer would cover) is shown after they write | 15 min |
| `reading` | **Read next**: three to five books from the journey's list, `[{ "author", "title", "year", "level", "why" }]` | |
| `takeaways` | three sentences: what the person has learned, shown at the end | |
| `minutes` | the session's total time, for the front page | |

The session with `"objection": true` states the strongest case against the journey's answer at full strength, in its best advocates' terms, before any reply.

## The closing (about 60 minutes)

`closing` keeps `title`, `prompt`, `practice` and `music`, and adds:
- `synthesis`: about 1,000 words pulling the six sessions together, as paragraphs.
- `exam`: six to eight essay questions of the kind a student might be set.
- `next`: `{ "place": "…", "book": "…", "journey": optional id }`, where to go from here.

The person's big answer (`prompt`) is written beside their earlier tutorial answers, so they can see how their thinking moved.

## Make the case

The last journey in each hall closes with a short essay: the person defends one idea from the hall in about 300 words and answers the strongest objection to it. Over nine halls this trains them to argue for what they have learned.

## Reusing passages

Outside the Bible hall, don't reuse a reading another journey already uses. The Bible hall may read any passage, because it is its home; if another hall later needs the same passage, that hall chooses a different one.

## Checking

1. Every factual claim, with its source, goes in `content/review/journeys-notes.json` under the journey's id. Flag anything uncertain.
2. Every set text is checked against its source file by script, not by eye.
3. `node build.mjs` must finish without "Content problems".
4. A reviewer with a degree in the subject reads it before anyone marks it `reviewed`.
