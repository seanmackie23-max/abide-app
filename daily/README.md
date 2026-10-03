# The daily idea: email, picture and share page

Every morning at about 06:15 Berlin time (05:15 in winter), GitHub Actions:

1. rebuilds the site, so the day is current;
2. runs `daily.mjs`, which makes the day's **picture** (`card.jpg`, 1080×1350, for Instagram and WhatsApp; `og.jpg`, 1200×630, for link previews), the **share page** (`/daily/<date>/`) and the **email**;
3. publishes the site;
4. runs `daily/send.mjs`, which sends the email through [Resend](https://resend.com).

The day's theme comes from `src/churchyear.js`, the same code the app runs, so the email and the app always agree. Pictures are drawn by a headless browser using the fonts in `daily/fonts` (Open Font License).

Try it locally: `node build.mjs && node daily.mjs --back 0 --ahead 0`, then open `dist/daily/<today>/`.

## Stage 1: the email to you (about 5 minutes)

1. Sign up at resend.com **with the address that should receive the email**. Until you verify a domain, Resend's test sender (`onboarding@resend.dev`) only delivers to your own account address.
2. In Resend, go to API Keys and create a key with "Sending access".
3. In GitHub, open the repository, then Settings → Secrets and variables → Actions → New repository secret, and add:
   - `RESEND_API_KEY`: the key
   - `EMAIL_TO`: the address (more than one: separate with commas)
4. To send one now, go to Actions → Deploy Abide → Run workflow and tick "Also send today's email". From then on, it arrives every morning.

## Stage 2: subscribers

1. In Resend, add and verify a domain (for example `abide.app`). This needs a few DNS records at your domain registrar.
2. In Resend, create a segment, for example "Daily idea", and copy its ID.
3. In GitHub, under Settings → Secrets and variables → Actions → Variables, add:
   - `EMAIL_FROM` = `Abide <daily@yourdomain>`
   - `RESEND_SEGMENT_ID` = the segment ID
   The email then goes as a broadcast to everyone in the segment, with an unsubscribe link. Add yourself to the segment too.
4. On the relay (see `agents/README.md`), set `RESEND_API_KEY`, `RESEND_SEGMENT_ID`, `EMAIL_FROM` and `SITE_URL` (your site's address). `TOKEN_SECRET` is already set for Plus.

The sign-up forms on Today, in the idea page and on every share page then work. New subscribers get a confirmation email first (double opt-in, which is expected in Germany and the EU), and are added only after they tap the link.

## Notes

- **Timing:** GitHub sometimes starts scheduled runs late on busy mornings. The schedule is in `.github/workflows/deploy.yml`.
- **No double sends:** a direct send uses one idempotency key per day, so a re-run on the same day doesn't send twice.
- **Keep the schedule alive:** GitHub pauses scheduled workflows in repositories with no activity for 60 days. Any commit, such as a content pull request, resets the clock.
