# Reviewing Pew

Everything in Pew is written as a draft. Nothing is marked `reviewed` except by a human reviewer, who changes `status: draft` to `status: reviewed` in the file after checking it. This page says what to review first, who should review it, and how.

## The order

Review in order of how many people will see it.

| # | What | Where | Who | Roughly |
|---|---|---|---|---|
| 1 | **The next two weeks of daily stories.** Everyone sees these. | `content/bank.json` (find each date's story id in `content/schedule.json`); the notes for each story are in `content/review/stories-notes.json` | A pastor or minister, plus one person who knows the classics for the echoes | 15 minutes a day |
| 2 | **The Sunday guide.** People will read it in the pew. | `content/sunday.json` | A minister of each tradition: Anglican (and a choir person for evensong), Catholic, Protestant, free church, Orthodox | 30 minutes each |
| 3 | **Pastoral words.** Blessings, children's stories and answers to children's questions. | `content/prayers.json` (`moments`), `content/stories.json`, `content/questions.json` | A pastor, and a parent | an evening |
| 4 | **The first session of each learning journey.** These are free, so most people meet a journey here. | `content/journeys.json`; every claim and its source is in `content/review/journeys-notes.json` | A theologian or well-read minister | 20 minutes each |
| 5 | **Science entries and their papers.** | `content/library/*` with `series: science`, `content/research.json` | Someone who reads research papers for a living | an hour each |
| 6 | **The first two depths of each Library entry** (free), then the rest. | `content/library/*.md` | A theologian; a philosopher for the classical entries | 30 minutes each |
| 7 | Everything else: Voices, debates, conversations, the rest of the journeys. | the matching file in `content/` | as above | as it comes |

Keep two weeks of stories reviewed ahead of today. That is the one deadline that matters.

## What to check

For every piece:

1. **Is it true?** Every fact (dates, places, who said what, which book and chapter) against the source in the notes. Anything the writer was unsure of is flagged in the notes.
2. **Is Scripture exact?** Bible text must be the World English Bible, word for word.
3. **Is the painting described honestly?** `see` and `look` describe only what is really in the painting. Open the gallery's page from the `nga` id in `content/art.json` and compare.
4. **Is it fair?** Other traditions, other religions, unbelievers and living people are described as they would describe themselves. The strongest objection is stated at full strength.
5. **Is it kind and plain?** British English, short sentences, no jargon, no guilt, no pressure. Intentions are concrete kindnesses, never wellness habits.
6. **Is it public domain?** Long quotations only from translations whose translator died before 1955 and that were published before 1929. Modern writers are summarised, never quoted at length.

## How to review

- **Easiest:** open the app on the date in question and read it as a newcomer would. Note anything wrong with the date and the exact words.
- **Send changes** as comments on the pull request, an issue on GitHub, or an email to the owner. Small fixes can be made straight in the file.
- **When a piece is right,** change its `status` to `reviewed` and commit with your name in the message. If you changed anything of substance, say what.
- **When a piece is wrong and can't be fixed quickly,** leave it as `draft` and say why. If it is a daily story, the owner can remove it from `content/schedule.json`; that date then falls back to the calendar theme in `content/calendar.json`.

Run `node build.mjs` after any change. It must finish without "Content problems".

## Already flagged

- The Sunday guide stays `draft` until a minister of each tradition has read it.
- The story for 8 December names the Catholic and Orthodox feasts of Mary's conception: check that the line says who keeps them.
- The story of Mary of Egypt uses a painting in which she is partly unclothed. Decide whether it suits a general audience.
- Verses are quoted from the World English Bible as written (checked by script against the WEB text), so some say "Yahweh" where others say "the Lord". Decide whether that is acceptable or whether to choose different verses. Tobit 5 (7 October) is not in the WEB text used here: check it against the WEB deuterocanon.
- Some daily passages are only one or two minutes long. That is fine, but check they are whole stories.
