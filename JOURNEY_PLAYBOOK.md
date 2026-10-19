# Journey playbook: how to write a learning journey that works

Read this before writing any learning journey, together with `JOURNEYS.md` (the fields and build checks) and `CURRICULUM.md` (where it sits). It records what the owner's reviews of `can-i-trust-the-bible` taught us, so the next journey starts where that one finished. That journey is the model; read it in the app before you begin.

## The one rule

**Explain it so a bright ten-year-old who has never opened a Bible could follow every step, and a university tutor would find nothing wrong.** Both halves matter. Most failures were the first half: jumping in without context, assuming the reader knew the story, the dates, the names or why a passage mattered.

## What went wrong before, and the fix

| What the owner found | The fix, now required |
|---|---|
| Margin notes that didn't point at anything the reader could see; no idea which passage was being read | Passages in **parts**: each with its reference, a title, a **context** box (where, who, when, why), the text, then a **commentary** that quotes the exact words it explains. The build script checks every quote is in the text |
| "Jumps straight in with little context" | A **Background** stage before every reading: the story so far, a **timeline**, who the writer was, and **why we read these passages now** |
| "Why does it jump to Ezra?" | Every reading must say, in the background and the read intro, **what question it answers and why this text answers it**. If you can't say that in two sentences, choose another text |
| Quizzes "easy and obvious" | Five or six **reasoning** questions (why, what follows, which is the best reply) with wrong answers a half-attentive reader might pick: true facts that don't answer the question, the opposite tradition's view, a common misreading. Never a joke option. `build.py` shuffles the options, so write the right answer anywhere |
| "Make clear how Catholic, Orthodox, Protestant differ" | Where the traditions differ, a **side-by-side table** (shown as cards), and Jewish views where relevant |
| "Needs more evidence than what the people in the Bible said" | Bring in **outside evidence**: archaeology, other ancient texts, hostile witnesses, science. Say plainly **where it is silent or against** |
| "Not coherent, a little chaotic" | **One frame** a child can hold for the whole journey; sessions as **steps of one argument**, each needing only the ones before; **no forward references**; a **finding** per session, shown as "The case so far" |
| Old English (Spinoza, Pusey, Whiston) too hard cold | **In plain words** (two to four simple sentences) before every old or difficult text |
| Torah / Old Testament / Tanakh confusion | Define every name and term the **first time it appears**, simply; when two groups use different names for one thing, explain why |
| Painting descriptions that were guessed | Write `look` only from the NGA's own description (`assistivetext`); never assume what is in a picture |
| The verdict buried at the end | The last session opens with a plain **verdict**; the closing gives **short answers** to the journey's questions, in order |

## Step by step

1. **Find the real questions.** Write down the eight to twelve questions an ordinary person actually asks about the subject (what they would type into a search box), in their words. The journey must answer every one, plainly, by the end.
2. **Choose the frame.** One simple picture that orders the questions: for the Bible's reliability, "test it like an old family story"; for Genesis, "the questions a child asks". Write it in two sentences. Every session is one step of it.
3. **Order the steps.** Each session needs only what came before. Put the strongest objection near the end, after the reader has the tools to weigh it, and the verdict last. Draft each session's `finding` now, in one plain sentence: if the findings don't read as an argument, reorder.
4. **Choose texts that answer the step.** For each session: a main reading and a comparison that answer its question directly. Prefer passages that make a claim, tell a story or can be tested. Out-of-copyright only (translator died before 1955 and published before 1929, or original English before 1929); WEB for Scripture.
5. **Gather before writing.** Extract the texts by script (see `tools/journeys/`), the painting descriptions from NGA data, the music ids, the outside evidence with dates and sources. Never write to justify a source you haven't found.
6. **Write each session in this order:** `plain`, `why`, `answers`, `finding`; Background (story so far, timeline if dates matter, who the writer was, why these passages); the reading parts (context, `plain` for old texts, commentary walking through the passage); the comparison; the lecture (one idea per screen, a `key` each, tables for comparisons); the debate (two or three real positions, fairly); look; check; tutorial; takeaways.
7. **Write the commentary like a good teacher talking.** Walk through the passage in order. Quote the words, then say what they meant then, what is surprising, how it connects to the question, and why it matters now. Short paragraphs. No jargon without a definition.
8. **Run the critique pass before shipping.** Read the whole journey as a beginner, session by session, and answer honestly:
   - Could someone who knows nothing follow each screen? Is every name, date and term explained where it first appears?
   - Does every reading say why it is here?
   - Does each session answer its `answers`, and does each `finding` follow from the evidence shown?
   - Is there any forward reference, repetition or jump?
   - Are the traditions' differences shown side by side where they matter?
   - Is the outside evidence there, with its gaps?
   - Is the objection at full strength, in its best advocates' terms?
   - Are the check questions hard enough?
   Fix everything you find, then do it again.
9. **Check by machine.** `python3 tools/journeys/build.py <id>` validates quotes, Scripture, set texts and ids; `node build.mjs` must pass; click through every session at phone width (Playwright) and look at the screenshots.
10. **Reviewer notes.** Every claim and its source in `content/review/journeys-notes.json`, with anything uncertain flagged "PLEASE CHECK".

## Voice

British spelling. Short sentences. Concrete before abstract: a story, a date, a place, then the idea. Fair to every side; never sneer at sceptics or at believers. Say "most scholars think" only when that is true, and name who disagrees. Never pretend evidence proves more than it does; say what it shows and what it doesn't.

## Source traps we have hit

- **Gutenberg paragraphs:** split on blank lines, never on line ends (lines wrap mid-sentence; we once cut paragraphs short). `tools/journeys/texts.py` does this.
- **Footnote and endnote markers** (Whiston's "9", Elwes's "[Endnote 9]") must be removed and noted in the reviewer notes; never silently change words.
- **The WEB's wording** differs from older Bibles ("At that time, Canaanites were in the land", not "the Canaanite was then"); quote the WEB, and say when a writer used another translation.
- **Tacitus** (Church and Brodribb) is in the Perseus TEI files on GitHub (PerseusDL/canonical-latinLit).
- **Rodwell's Qur'an** (Gutenberg #2800) prints a footnote number glued to words ('costly12') and sometimes breaks a verse mid-sentence; strip the numbers, keep the breaks, and give standard verse numbers in the `ref`.
- **Mixed comparisons** (two authors in one compare): put the author in each part's `ref`, because the reader sees the part's ref, not the reading's author.
- **NGA images** can't be downloaded from here; the staging build fetches them. Describe them only from the NGA description.
