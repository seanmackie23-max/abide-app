# Working on Abide (instructions for Claude and other AI agents)

Abide is a website and web app helping people who have never been to church build a daily Christian rhythm and explore the faith in depth. Read `EDITORIAL_GUIDE.md` before writing any content. It is binding.

## Project layout

- `content/library/*.md` – Library subjects, five depths each (frontmatter: title, summary, order, status)
- `content/voices/*.md` – thinker profiles (frontmatter: name, years, tradition, era, order, status)
- `content/music.json`, `memory.json`, `prayers.json`, `questions.json` – collections
- `src/app.html` – the app (one file: styles, markup, script); `src/page.css` – shareable page style
- `build.mjs` – no-dependency build: `node build.mjs` writes `dist/`; `node build.mjs --standalone` writes a single-file preview
- `site.json` – site name, description and public URL

## Adding a Library subject

1. Research first. Use primary sources and reputable references; collect exact references (book, chapter, question number) and dates.
2. Create `content/library/<slug>.md` following the five-depth structure in the guide. Set `status: draft`. Choose the next free `order`.
3. In depth 4, include the strongest objections, stated fairly. Add a `tag:` line.
4. Run `node build.mjs`. It must finish without "Content problems".
5. In your pull request description, list every factual claim with its source so a reviewer can check them quickly. Flag anything you are unsure of.

## Adding a Voice or music

Same process: draft status, sources listed in the pull request, build must pass. For living people, cite where they said what you attribute to them.

## Rules

- Never mark content `reviewed`. Only a human reviewer does that.
- Never paste copyrighted lyrics or long quotations (see the guide).
- Don't change the app's design or code when asked only for content.
- Keep British spelling and the voice described in the guide.
- One subject per pull request, so review stays easy.
