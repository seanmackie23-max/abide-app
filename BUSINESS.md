# How Abide works as a business

Abide's daily rhythm and its way into a church are free for everyone. It earns money in two ways: people who want the deep end pay for **Abide Plus**, and churches that want more than a free listing pay to be **Abide Partners**. No church can pay to rank above another.

## The app: three places

**Today** (free): one idea, four short moments to live it, one thing to do, your church. **Explore** (Plus): learning journeys, deep courses on one great question each, tying together the readings, ideas, evidence, podcasts and debates, poetry, music and art; then the collections behind them: Ideas, Music, Learn, Family. **Sunday** (free): the week builds to Sunday. A step-by-step guide to the service in your church's tradition, your church's week, a group journey with friends, and your circle.

## What's free, for everyone, always

- Today: the idea, the four moments, Live it, today's music, the day's full reading, your journey and your year
- The first session of every learning journey
- The first two depths of every idea
- Churches near you, this week near you, "I'm going", joining a friend's circle
- A taste of the AI guide

## Abide Plus, for individuals

| | Free | Plus |
|---|---|---|
| Today, the four moments, Live it, today's music | ✓ | ✓ |
| Sunday: the service guide, churches near you, "I'm going", a group journey | ✓ | ✓ |
| Learning journeys: six sessions and a closing each | Session 1 of each | ✓ |
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

Why a church would bother: Google can find a church; it can't get a nervous person through the door, and it does nothing for a congregation from Monday to Saturday. Abide does both. For the congregation, it is a daily companion: a few minutes of prayer and thought each day, with **the minister's weekly note and this Sunday's reading in every member's Today**. For newcomers, Abide suggests **one easy first visit** (an evensong, a concert, a candlelit evening before a Sunday morning), helps them **go prepared** (Sunday's reading, the week's idea), tells the church they're coming and tells them **who will meet them at the door**.

| | Free, for every church | Partner |
|---|---|---|
| A weekly note in your members' Today, all week | Yes | Yes |
| This Sunday's reading, so people come prepared | Yes | Yes |
| Claim your church; keep times and events up to date | Yes | Yes |
| Newcomers sent to an easy first visit, with a named welcomer | Yes | Yes |
| An email when someone says "I'm coming" | Yes | Yes |
| **Run Abide's learning journeys as your newcomers' course** (six weeks, everything ready) | | Yes |
| **The whole of Abide for your members** (Plus, up to 100 people) | | Yes |
| **Your own welcome film** | | Yes |
| **Newcomer numbers**: found you, said they'd come, came | | Yes |

**€19 a month or €190 a year per church.** Free during the pilot. Partner never changes where a church appears: churches are always listed nearest first.

Why a church pays: churches already pay for newcomers' courses. Abide's journeys are that course, built on the Bible and the great books, with the music, the art and the evidence, and nothing to prepare.

How it spreads: a minister mentions Abide from the front ("my note's in there every week"); members use it daily; they invite friends to a circle; those friends' first church is the one their friend goes to, where the welcomer is already on Abide.

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
