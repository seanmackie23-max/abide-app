# How Abide works as a business

Abide is free for everyone. It earns money in two ways: people who want more of the AI guide pay for **Abide Plus**, and churches that want more than a free listing pay to be **Abide Partners**. Faith itself is never behind a paywall, and no church can pay to rank above another.

## What's free, for everyone, always

- The daily rhythm: today's idea, the four moments, Live it, the calendar
- Every idea, debate, conversation, voice and paper in Ideas
- Music, Learn, Family (stories, bedtime, the table, the questions, the blessings)
- Community: churches near you, circles, "I'm going", going together, prayer in your circle
- A taste of the AI guide: 3 questions to Ask Abide a day, one personal path, Shape my week once a week

## Abide Plus, for individuals

| | Free | Plus |
|---|---|---|
| Ask Abide | 3 a day | Unlimited |
| Your path (a personal four-week path) | One | As many as you like, reshaped any time |
| Shape my week (a weekly practice coach) | Once a week | Every week |
| Everything else | Yes | Yes |

**€6.99 a month or €49 a year.** Also: a **gift** year (€49), and **Founding Patron** (€120 a year) for people who want to carry Abide. Anyone who can't afford it can write in and get Plus free.

Why it's fair: every AI answer costs Abide real money (roughly a cent on the current model), so heavy use is paid for by the people who use it most. Everything else costs almost nothing to serve.

## Abide for Churches

The free tier is how Abide gets people into churches, so it is generous. Partner is how churches that want to do more pay for it.

| | Free, for every church | Partner |
|---|---|---|
| Claim your church on Abide | Yes | Yes |
| Keep service times and events up to date | Yes | Yes |
| Name a welcomer who meets newcomers at the door | Yes | Yes |
| An email when someone says "I'm coming" | Yes | Yes |
| "Kept up to date by the church" mark | Yes | Yes |
| **Abide Plus for your members** (a church code, up to 100 people) | | Yes |
| **Your own welcome film**, made from your details | | Yes |
| **Newcomer insights**: how many found you, said they'd come, and came | | Yes |
| **Advent and Lent groups** with sign-ups (coming next) | | Yes |

**€19 a month or €190 a year per church.** Free during the pilot. Partner never changes where a church appears: churches are always listed nearest first.

## The numbers that matter

Abide's purpose is people in church, so its main number is **first church visits** ("I went" after "I'm going"). Then second visits, people in a circle, and churches claimed. Revenue follows: Plus members, Partner churches.

## What's built, and what's left

Built:
- the free app;
- Plus (Stripe Payment Links, signed membership keys, free limits);
- church claiming and the church portal (`/church/`);
- newcomer alerts;
- member codes for Partner churches;
- circles and "I'm going".

Before launch:
- [ ] Deploy the server (`agents/README.md`) with ANTHROPIC_API_KEY, TOKEN_SECRET, STRIPE_SECRET_KEY, RESEND_API_KEY, EMAIL_FROM, ADMIN_EMAIL and a KV store
- [ ] Create the Stripe Payment Links (Plus monthly, yearly, patron, gift; Partner monthly, yearly) and paste them into `site.json`
- [ ] Your domain, Impressum and privacy policy
- [ ] Register as a sole trader (Gewerbe) before taking money; check your employer's outside-activities policy

Next to build: the welcome film generator for Partner churches, Advent and Lent groups, and newcomer insights.
