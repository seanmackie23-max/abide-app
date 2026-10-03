# How Abide works as a business

Abide's daily rhythm and its way into a church are free for everyone. It earns money in two ways: people who want the deep end pay for **Abide Plus**, and churches that want more than a free listing pay to be **Abide Partners**. No church can pay to rank above another.

## The app: three places

**Today** (free): one idea, four short moments to live it, one thing to do, your church. **Explore** (Plus): the deep end, behind four doors: Ideas, Music, Learn, Family. **Church** (free): churches near you, this week, your circle, your first visit.

## What's free, for everyone, always

- Today: the idea, the four moments, Live it, today's music
- The first two depths of every idea
- Churches near you, this week near you, "I'm going", joining a friend's circle
- A taste of the AI guide

## Abide Plus, for individuals

| | Free | Plus |
|---|---|---|
| Today, the four moments, Live it, today's music | ✓ | ✓ |
| Churches near you, "I'm going" | ✓ | ✓ |
| Ideas: every depth, the papers, debates, conversations, voices | 2 depths | ✓ |
| The whole music library | | ✓ |
| Learn: words worth carrying | | ✓ |
| Family: a story and bedtime ritual every night, the big questions, blessings | | ✓ |
| Start a circle (anyone you invite joins free) | | ✓ |
| Ask Abide, Your path, Shape my week | A little | ✓ |
| The four moments in your calendar | | ✓ |

**€4.99 a month or €39 a year**, with a **30-day free trial** (no card; it simply ends). Also a gift year (€39) and Founding Patron. Anyone who can't afford it can write in and get Plus free.

Why this split: the daily rhythm and the way into a church are the mission, so they stay free. The deep end is where people who love Abide spend hours, and it's fair for them to pay for it.

Note: until payments are live, Plus is unlocked on the device (the trial, keys and codes are checked in the browser). That is fine for a pilot; before Plus earns real money, serve the Plus content from the server so it can't be unlocked by editing the page.

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
