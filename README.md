# Pew

An ancient Christian rhythm for a busy life: prayer at fixed hours, help for families, prayers and poems to learn by heart, a Library of the great questions in five depths, sacred music, and a front door to your local church.

## Put it on the web (about 15 minutes, free)

1. Create a free account at github.com, if you don't have one.
2. Click **New repository**, name it `abide`, make it **Public**, and create it.
3. On the new repository's page, click **uploading an existing file**, drag in **everything inside this folder** (including the hidden `.github` folder; on a Mac press Cmd+Shift+. in Finder to show hidden files), and click **Commit changes**.
4. Go to **Settings → Pages**, and under "Build and deployment" choose **Source: GitHub Actions**.
5. Open the **Actions** tab and wait for "Deploy Pew" to turn green (a minute or two).
6. Your site is live at `https://YOUR-GITHUB-NAME.github.io/abide/`. Put that address into `site.json` as `baseUrl`.

**Your own domain:** buy one (for example from a domain registrar or Amazon Route 53), set `customDomain` in `site.json`, and follow GitHub's "Configuring a custom domain" guide.

## Adding content with Claude

Connect this repository to Claude (Claude Code on the web, or the GitHub connector). Then ask, for example:

> Add a Library entry on "What is prayer?" following CLAUDE.md and the editorial guide. Open a pull request with the sources listed.

Claude drafts the entry, checks that the build passes and opens a pull request. You (and your reviewers) read it, check the sources, and merge it. The site updates itself within minutes.

## Build it yourself (optional)

With Node.js 18 or newer: `node build.mjs`, then open `dist/index.html`.

## Content status

All current content is **draft**: written with AI assistance and awaiting a fact check and theological review. See `EDITORIAL_GUIDE.md`.
