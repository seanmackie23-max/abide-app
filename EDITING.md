# Changing Rose Window without touching the live site

Rose Window has two copies, built from two branches of the same repository:

| Branch | Address | Who sees it |
|---|---|---|
| `main` | `https://yourdomain/` | everyone: the live site |
| `staging` | `https://yourdomain/staging/` | you: hidden from search, a red "Staging" banner, no analytics, and its own storage on your device, so testing never mixes with your real days |

Every push to either branch rebuilds both, in about three minutes (watch it under the repository's **Actions** tab).

## The everyday loop

1. **Change things on `staging`.**
   - Asking Claude: say "make this change on staging". Claude commits to `staging` and never to `main`.
   - On GitHub yourself: open the file, switch the branch picker (top left) to `staging`, press the pencil, edit, and **Commit changes**.
2. **Check it** at `/staging/` once the Actions run is green. On your phone, pull down to refresh; if it looks unchanged, close and reopen the tab (the app keeps an offline copy).
3. **Publish it.** On GitHub: **Pull requests → New pull request**, base `main` ← compare `staging` → **Create pull request** → **Merge**. The live site updates about three minutes later.

## Undoing a change on the live site

Open the merged pull request and press **Revert**. GitHub makes a new pull request that undoes it; merge that. The live site is back as it was in about three minutes. Then fix things on `staging` at your own pace.

## Keeping the two in step

After you publish, `staging` and `main` are the same. If something lands on `main` some other way (a content pull request merged straight into `main`, say), bring `staging` up to date with a pull request the other way round: base `staging` ← compare `main`, then merge.

Content pull requests from the scheduled agents can be previewed the same way: change the pull request's base to `staging` (the **Edit** button next to its title), merge it, check `/staging/`, then publish `staging` as usual.

## Protect the live site (once, 2 minutes)

GitHub → Settings → Branches → **Add branch ruleset** (or "Add rule") for `main`: tick **Require a pull request before merging**. Then nothing reaches the live site except through a pull request you merged.

## Good to know

- **The daily email always comes from `main`.** Staging never sends it.
- **Signing up on staging is real.** The sign-up form on `/staging/` uses the real list (use your own address when testing), and the confirmation link brings you to the live site.
- **Staging also runs Ask Rose Window and the other switches** exactly as `site.json` on the `staging` branch says, so you can try a switch on staging before turning it on live.
- **A quick look without any branch:** `node build.mjs --standalone` makes one file you can open in a browser; Claude publishes the same as the preview page.
