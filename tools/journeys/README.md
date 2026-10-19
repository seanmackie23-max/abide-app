# Journey tools

See `JOURNEY_PLAYBOOK.md` first. These scripts build a degree-level learning journey from source files and check it.

- Scripture comes from the World English Bible JSON: `git clone --depth 1 https://github.com/TehShrike/world-english-bible .cache/web`.
- `web.py`: `passage("Genesis 1:1-2:3")` (paragraphs with verse numbers, as the app shows them) and `verse(ref)` (plain text, for checking quotations).
- `texts.py`: extract paragraphs from a Gutenberg text (split on blank lines) and check them verbatim.
- `build.py <id> [--write]`: builds `src/<id>/journey.py` (+ `raw.json`), checks every commentary quote against its text, every required field, check questions, glossary terms and forward references, then writes the journey into `content/` and moves it out of its hall's `later` list.
