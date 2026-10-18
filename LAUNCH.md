# Launching Rose Window

Everything in the code is ready. These are the accounts and settings only the owner can create. Do them in this order; each step says how long it takes and how to check it worked. Total: about two hours, plus waiting for DNS.

Where things are set:
- **`site.json`** in the repository (edit it on GitHub, or ask Claude).
- **GitHub secrets and variables**: the repository → Settings → Secrets and variables → Actions. *Secrets* are hidden (keys, passwords); *Variables* are visible settings.

---

## 1. A domain (30 minutes, then up to a day for DNS)

Search engines, email delivery and trust all need a proper address. Buy it before anything else, because people's data on their device is tied to the address, and the email needs it.

1. Check the name first: search the EUIPO and UK IPO trademark databases for "Rose Window" in software and education (classes 9, 41 and 42).
2. Buy the domain. Cloudflare Registrar is simplest, because the relay and DNS will live there too.
3. In your DNS (Cloudflare → the domain → DNS), add:
   - four `A` records for the bare domain (`@`): `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`, with the proxy **off** (grey cloud);
   - four `AAAA` records for `@` (IPv6): `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`, proxy off;
   - a `CNAME` record `www` → `seanmackie23-max.github.io`, proxy off.
   A `.app` address only ever opens over HTTPS, so between saving the domain on GitHub and GitHub issuing its certificate (usually 15–60 minutes) the address shows a security error. That's expected.
4. `site.json` already says `"customDomain": "rosewindow.app"` on staging; it goes live when staging is published.
5. On GitHub: Settings → Pages → Custom domain: enter it, save, and tick **Enforce HTTPS** once it allows you.

**Check:** `https://rosewindow.app/` opens Rose Window, and `https://rosewindow.app/staging/` opens the staging copy.

## 2. Imprint and privacy (10 minutes)

A website run from Germany needs an Imprint (Impressum) with a name and a postal address where you can be reached, and a privacy page.

1. In `site.json`, fill in `legal`: `name`, `address` (one line, commas between parts), `email`.
2. Read `/privacy/` and `/imprint/` on staging. The privacy page describes exactly what Rose Window does today. Have it looked over by someone who knows German data-protection law before you advertise.

## 3. Email: Resend (30 minutes, plus DNS)

1. Sign up at resend.com.
2. **Domains → Add domain**: use a subdomain such as `mail.rosewindow.app`. Add the DNS records Resend shows (in Cloudflare DNS), then press Verify.
3. **Segments** (or Audiences) → create one called "Daily story". Copy its ID.
4. **API keys** → create a key with full access. Copy it.
5. Leave open and click tracking **off** in Resend: clicks are already counted without tracking anyone, through the links in the email.
6. On GitHub, add:
   - Secret `RESEND_API_KEY` = the key
   - Secret `TOKEN_SECRET` = a long random password (60 characters from a password manager). It signs the confirmation links. Never change it once people are signing up.
   - Variable `EMAIL_FROM` = `Rose Window <daily@mail.rosewindow.app>`
   - Variable `RESEND_SEGMENT_ID` = the segment ID
   - Remove the old `EMAIL_TO` secret once you are in the segment yourself.

## 4. The relay: Cloudflare Worker (15 minutes)

The relay is the small server that receives sign-ups and sends the confirmation email. It is free at this size.

1. In Cloudflare: **My Profile → API Tokens → Create Token → "Edit Cloudflare Workers"** template → Create. Copy the token.
2. Copy your **Account ID** (Cloudflare dashboard, right-hand column of any domain, or Workers & Pages overview).
3. On GitHub, add secrets `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`.
4. GitHub → **Actions → Deploy the relay → Run workflow**. When it finishes, its log shows the address, like `https://rose-window-relay.<you>.workers.dev`.
5. Put that address in `site.json` as `"askEndpoint"` and commit. Leave everything in `features` false.

**Check, end to end:** on `/staging/join/`, sign up with your own address. You should get a confirmation email within a minute; tapping its link should bring you to Rose Window with "You're in", and your address should appear in the Resend segment. Then Actions → Deploy Rose Window → Run workflow with "Also send today's email" ticked: the daily email should arrive, with an Unsubscribe link at the bottom.

If the confirmation never arrives, look in Cloudflare → Workers → rose-window-relay → Logs: a Resend error there usually means the domain isn't verified yet or `EMAIL_FROM` doesn't use it.

## 5. Analytics: Plausible (10 minutes)

1. Sign up at plausible.io (EU-hosted, no cookies, so no cookie banner is needed). Add your site with your domain.
2. In `site.json`, set `analytics.plausible` to that domain. From the next deploy, the live site is counted; staging never is.
3. In Plausible → Site settings → **Goals**, add each event below as a "custom event" goal (exact names). Under **Custom properties**, add `moment`, `journey`, `session` and `from`.
4. If your plan has funnels, add two:
   - **Becoming a regular:** Story read → Moment begun → Morning kept → Returned after a week
   - **The way to church:** Sunday guide opened → Going on Sunday → First church visit

### What is counted

Plausible counts page visits and where they came from (search, Instagram, your Substack, the email: email links carry `utm_source=email`). On top of that, Rose Window sends these events. They carry no personal data and nothing anyone writes.

| Event | When | Property |
|---|---|---|
| Story read | the day's story is opened | |
| Reading opened | the long reading is opened | |
| Moment begun | Begin, or any moment, is started | `moment` |
| Moment kept | a moment is finished | `moment` |
| Morning kept | the morning is finished | |
| Returned after a week | someone keeps a moment 7+ days after their first (once per device) | |
| Returned after a month | the same at 30+ days (once) | |
| Added to home screen | Rose Window is opened as an installed app (once) | |
| Shared | the share button is used | |
| Your story opened | the progress page is opened | |
| Journey opened / Journey session opened | a learning journey or one of its sessions | `journey`, `session` |
| Plus viewed / Trial started | the Plus page, the 30-day trial | |
| Sunday guide opened | the three-minute guide | |
| Going on Sunday | "I'm going" | |
| First church visit | "I went", the first time (once) | |
| Signup started | the email form is sent | `from` (join, advent, app, daily page) |
| Signup confirmed | someone arrives from the confirmation link | |
| Candle lit | a candle is lit (what it is for never leaves the device) | |
| Sat in silence | a time of silence ends | |

### The numbers to look at each Monday

1. **New people** (unique visitors) and **where they came from** (Top sources).
2. **Signup confirmed** this week, and the total in the Resend segment.
3. **Morning kept**, divided by unique visitors: how many who come actually pray.
4. **Returned after a week**: the most important number. Compare it with the new people of the week before.
5. **The way to church**: Sunday guide opened → Going on Sunday → First church visit.
6. **Email clicks**: visits with source `email`.

## 6. Before you tell anyone (15 minutes)

- [ ] Open the live site on your phone: Today, Begin, Explore, Sunday, Your story.
- [ ] Add it to your home screen; open it with flight mode on: today's story should still be there.
- [ ] Sign up on `/join/` with a second address; confirm; unsubscribe from the next email.
- [ ] Check Plausible shows your visit and a "Morning kept".
- [ ] Look at `/advent/` and `/join/` as a stranger would, then share one of them in your Substack.
- [ ] Make sure the next two weeks of stories have been reviewed (`REVIEW.md`).

## Later, when you are ready

- **Ask Rose Window, Plus payments, church portal, circles**: each needs more setup on the relay (`agents/README.md`), then its switch in `site.json` `features`.
- **An iPhone app** wrapping the site, once day-7 return looks healthy.
