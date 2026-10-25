You are drafting one learning journey for Rose Window. The repository is /home/claude/abide-app, on the `staging` branch. Other agents are drafting other journeys in the same repository at the same time.

Your journey id: {ID}

## Before you start

Read these first:
- `specs/AGENTS.md`, the Stage B section, which is your exact task.
- `specs/DECISIONS.md`, which is binding and overrides the spec and plan where they differ.
- Your spec: `specs/journeys/{ID}.md`.
- Your Stage A plan: `tools/journeys/src/{ID}/plan.json`.
- `CLAUDE.md`, the Learning journeys section and Rules.
- `EDITORIAL_GUIDE.md`, `JOURNEY_PLAYBOOK.md` and `JOURNEYS.md`.
- The models in `tools/journeys/src/in-the-beginning/` and `tools/journeys/src/kings/`: their `journey.py` and session files, `extract.py` and `raw.json`.

## The texts

Fetched texts are in `.cache/texts/`:
- `<gutenberg-id>.txt`
- `url/<key>.txt` (`index.json` lists what was fetched, and errors)

Check that each file really is the edition and translator the plan says: read its header. If a text you need is missing or fails the rule, choose another qualifying text you have, or teach that part in our own words. Note which in `notes.json` under `missing`. Never quote from memory: every quotation must be copied by script from a file.

## Rules

- **Write only inside `tools/journeys/src/{ID}/`.**
  - Never edit `content/`, `specs/`, other journeys' folders, or anything else.
  - Never run `build.py --write`, `assemble.py`, `git commit` or `git push`.
- **New paintings:** claim each one with `python3 tools/journeys/nga.py claim {ID} <uuid> <art-id>` before you use it. If it is already claimed by another journey, choose another or go without.
- **Work at degree level, in the house voice.** Use British spelling, short sentences and plain words. Be fair to every side, and give the objection at full strength.
- **Make it complete.** Every session needs every field the playbook asks for, with no placeholders and no "TBD".
- **Check it.** Run `python3 tools/journeys/build.py {ID}`. It must print "No problems." Then do the playbook's critique pass, twice, and fix what you find.

## Finishing

Write `notes.json` with every factual claim and its source, flags and missing items.

End with a short report:
- sessions written and total words;
- the texts quoted, with translator and dates;
- what is in our own words, and why;
- the paintings used;
- anything a reviewer must check.
