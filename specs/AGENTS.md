# Drafting the journeys in parallel: instructions for each agent

The owner asked on 24 October 2026 for every planned journey to be drafted now, in parallel, without waiting for spec review. Each journey stays `status: draft` until a person reviews it. Work only in the files named for your stage; other agents are working beside you in the same repository at the same time.

Read first, every time: `CLAUDE.md` (the Learning journeys section and Rules), `EDITORIAL_GUIDE.md`, `JOURNEY_PLAYBOOK.md`, `JOURNEYS.md`, `specs/README.md`, and your journey's spec in `specs/journeys/<id>.md`. The models are `tools/journeys/src/in-the-beginning/` and `tools/journeys/src/kings/` (source) and the same journeys in `content/journeys.json` (built).

## Stage A: sources, paintings and music (one agent per hall)

For every spec in your hall, write `tools/journeys/src/<id>/plan.json` and `tools/texts/want/<id>.json`. Nothing else.

1. **Set texts.** For each non-Bible text in the spec (`reads`, and any compare text named in the sessions), find a public-domain source that meets the rule: translator died before 1955 and published before 1929, or original English published before 1929. Prefer, in order:
   - Project Gutenberg (find the ebook number with WebSearch, e.g. `site:gutenberg.org Bacon Advancement of Learning`): add the number to `ids`.
   - New Advent's Fathers (`https://www.newadvent.org/fathers/NNNN.htm`, the ANF/NPNF translations) and Summa (`https://www.newadvent.org/summa/NNNN.htm`).
   - CCEL (`https://ccel.org/ccel/...html`), Wikisource, Perseus (`https://www.perseus.tufts.edu/hopper/...`), Lacus Curtius (`https://penelope.uchicago.edu/Thayer/E/Roman/Texts/...`), the Internet Sacred Text Archive, Fordham's sourcebooks.
   - archive.org plain text: `https://archive.org/download/<identifier>/<identifier>_djvu.txt` (find the identifier with WebSearch).
   Put each non-Gutenberg page in `urls` as `{ "key": "<id>-<short>", "url": "..." }`. One page per key; for a work split over pages, list each page you need. Check with WebSearch that the URL exists; you cannot fetch it yourself (the shell can't reach these sites; a GitHub Actions workflow fetches every `want` file).
   If no qualifying text exists, say so in `plan.json` and plan that part in our own words (one short quotation at most, under 25 words).
2. **Paintings.** For each session's `look`, find a National Gallery of Art painting of the very subject: `python3 tools/journeys/nga.py search "kw1, kw2"` (add `--all` to search the gallery's descriptions too), then `show <uuid>` to read the description. Reserve it with `python3 tools/journeys/nga.py claim <journey-id> <uuid> <new-art-id>` so no other journey takes it. Prefer works not already used in `content/art.json`; reuse an existing art id only if it is exactly right and say so. If nothing fits, write `null` and the reason.
3. **Music.** Pick ids that exist in `content/music.json`, with a one-line why. If none fits, `null`.
4. **Memory pieces.** For each session's `learn`: an existing id in `content/memory.json`, or a new piece with its exact source (WEB reference, or a public-domain text and URL).

`plan.json` shape:
```json
{"id": "...", "sources": [{"key": "...", "what": "Justin, First Apology 65-67", "translator": "Marcus Dods (d. 1909), ANF 1885", "url": "...", "gutenberg": null, "ok": true, "note": ""}],
 "art": [{"session": 1, "art": "new-art-id or existing id", "nga": "uuid or null", "title": "...", "artist": "...", "why": "..."}],
 "music": [{"session": 1, "id": "...", "why": "..."}],
 "memory": [{"session": 1, "id": "existing-or-new-id", "new": true, "title": "...", "ref": "...", "source": "..."}],
 "flags": ["..."]}
```
`tools/texts/want/<id>.json` shape: `{"ids": [1497, 3296], "urls": [{"key": "...", "url": "..."}]}`.

## Stage B: draft the journey (one agent per journey)

You own `tools/journeys/src/<id>/` and nothing else. Do not edit `content/*.json`, `halls.json`, other journeys' folders, or the spec.

1. **Texts.** The fetched texts are in `.cache/texts/` (`<gutenberg-id>.txt`, and `url/<key>.txt` for other pages: HTML already turned into paragraphs separated by blank lines). Extract the passages you need with a script (`tools/journeys/src/<id>/extract.py`, as in the models; `tools/journeys/texts.py` helps) into `tools/journeys/src/<id>/raw.json`. Split on blank lines, never on line ends. Remove footnote markers and note them in your reviewer notes; never change a word. Mark cuts with a paragraph that is just "…". Scripture comes from `web.py` (WEB), never retyped. If a text you need is missing from `.cache/texts`, say so in your notes and either use another qualifying text you have, or teach that part in our own words.
2. **Write.** Follow the spec's frame, the seven sessions and their findings, and the playbook exactly: every session has `plain`, `why`, `answers`, `finding`, `background` (2–4 sections), `before`, `read` parts with `context`, `plain` for old texts and `commentary` quoting the exact words, `compare`, `lecture` (sections of 120–250 words, each with a `key`), `debate`, `look` (described only from the gallery's description), `music`, `think`, `check` (five or six reasoning questions, four options), `tutorial`, `reading`, `practice`, `reflect`, `takeaways`, `terms`. One session has `"objection": True`. The closing has `synthesis`, `exam`, `next`, `prompt`, `practice`, `music`. Course pack: `people`, `timeline`, `places`, `glossary`, `reading` (three tiers). Use the shape of `src/in-the-beginning/journey.py` and its session files. Set `HALL` and `AFTER` (the journey before it in the hall's walk, from the spec's `order`).
3. **Paintings.** Use `plan.json`. For each new painting, add an entry to `tools/journeys/src/<id>/art_new.json` (a list in the same shape as works in `content/art.json`: id, title, artist, date, museum "National Gallery of Art, Washington", nga uuid, w, h, focus, alt from the gallery's description). The `look` text and points must describe only what the gallery's description says is there.
4. **Memory pieces.** New ones go in `tools/journeys/src/<id>/memory_new.json` (a list in the shape of `content/memory.json` entries), verbatim from WEB or the public-domain source.
5. **Check.** `python3 tools/journeys/build.py <id>` (without `--write`) must print "No problems." Fix everything it reports. Then do the playbook's critique pass (step 8) honestly, twice, and fix what you find.
6. **Reviewer notes.** `tools/journeys/src/<id>/notes.json`: `{"claims": [{"claim": "...", "source": "..."}], "flags": ["PLEASE CHECK ..."], "missing": ["..."]}`: every factual claim with its source; anything uncertain flagged.
7. **Report.** End with a short summary: sessions written, words, any missing sources, anything a reviewer must know.

Voice: British spelling, short sentences, plain words, fair to every side. Never quote in-copyright modern writers beyond one short quotation; never paste lyrics; never mark anything `reviewed`.

## Stage C: verify (one fresh agent per journey)

Read the spec, the built journey (`python3 tools/journeys/build.py <id>`), `notes.json` and the raw texts. Check: every quotation is verbatim from its source; dates, names and references are right; each finding follows from its session; the objection is at full strength; no session repeats another or another journey's readings (`specs_check.py`); the paintings' `look` text matches the gallery's description. Fix what you can in `tools/journeys/src/<id>/`, list the rest in `notes.json` under `flags`, rerun the build, and report.

## Assembly (the lead agent only)

Merges each journey with `build.py <id> --write`, merges `art_new.json` into `content/art.json` and `memory_new.json` into `content/memory.json`, merges `notes.json` into `content/review/journeys-notes.json`, runs `node build.mjs` and the cross-journey checks, and commits to `staging`.
