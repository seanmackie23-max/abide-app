# Journey specs: write the plan first, then the journeys

Every learning journey still to be written has a spec here, one file per journey in `specs/journeys/<id>.md`. A spec is the agreed plan: the question, the frame, the seven steps of the argument and their findings, the set texts, the objection, and what the journey must not repeat. The owner reviews the specs, not the drafts, so that changing direction costs nothing.

## How the work runs

1. **Specs** (this folder). Drafted together, checked together (`python3 tools/journeys/specs_check.py` finds texts read twice and journeys out of order), reviewed by the owner hall by hall. A spec moves from `status: draft` to `status: agreed` only when the owner says so.
2. **Fetch.** Every set text listed under *Sources to fetch* is downloaded once (the texts workflow, or locally), extracted to `tools/journeys/src/<id>/raw.json`, and checked for footnote markers. NGA painting candidates are found in the gallery's open data and described only from its own text. Nothing is written until its sources are in hand.
3. **Draft.** One agent per agreed spec, working only in `tools/journeys/src/<id>/` and its own reviewer notes, following `JOURNEY_PLAYBOOK.md`, `JOURNEYS.md` and the two models (`can-i-trust-the-bible`, `in-the-beginning`). It must pass `python3 tools/journeys/build.py <id>`.
4. **Verify.** A second agent that did not write it checks every quotation against the source, every date and reference, the playbook's critique list, and that the objection is at full strength. The drafter fixes what it finds.
5. **Assemble.** One pass merges the journeys into `content/journeys.json` and `content/halls.json` in hall order, runs `node build.mjs`, and checks across journeys for repeated paintings, memory pieces and readings.
6. **Review.** The owner reads session 1 (the free one) and the objection session of each, with the reviewer notes.

The first wave is three journeys only, to calibrate: whatever the owner corrects goes into `JOURNEY_PLAYBOOK.md` before the next wave.

## Rules every spec follows

- **One argument.** Seven sessions are seven steps; each `finding` follows from the evidence of that session and needs only the ones before. Read the findings in order: they must read as a case.
- **Read once.** A text read in an earlier journey is pointed back to, not read again (see *Read elsewhere*). The specs' check script enforces this.
- **Public domain or our own words.** Set texts: translator died before 1955 and published before 1929, original English before 1929, or the World English Bible. Everyone else is a *voice*, in our own words, cited to where they said it. When a spec lists a translation, the fetch stage confirms the edition and its Gutenberg or archive source; anything unconfirmed is flagged in *Flags*.
- **The objection at full strength,** in one session, after the reader has the tools to weigh it, before the verdict.
- **The traditions side by side** where Catholic, Orthodox, Protestant (and Jewish) views differ.
- **Outside evidence** where the question can be tested, with what it does not show.
- **Paintings and music are wanted, not chosen.** A spec names the subject wanted; the drafter finds an NGA work of that very subject, or says there is none.
