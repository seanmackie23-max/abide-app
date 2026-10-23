"""Practice: give each of the greats a real page. Adds to keep.json greats.people:
hook (one line), story (their life in three moments), day (a day in their life, as the sources record it),
week (seven days with them: one thing a day), read (books to go further) and sources.
Everything in our own words; short quotations only. Run after greats.py: python3 tools/days/greats_life.py"""
import json, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
K = os.path.join(ROOT, 'content', 'keep.json')
k = json.load(open(K))

L = {
"marcus": dict(
 hook="The most powerful man in the world, writing notes to himself to stay good.",
 story=[
  ["121–138", "A serious boy", "Marcus was born in Rome to a rich family. The emperor Hadrian noticed the boy and arranged for him to be adopted into the imperial line. He had the best teachers in the empire, and in the first book of the Meditations he thanks each of them by name: one for teaching him to bear pain, another, Junius Rusticus, for lending him his own copy of the teachings of Epictetus."],
  ["161–169", "Emperor in a hard time", "He became emperor at forty and at once insisted on sharing power with his adoptive brother. His reign was one disaster after another: a plague brought back by the army from the East that killed millions, floods, famine, and invasions across the Danube. He sold palace treasures at auction rather than raise taxes to pay for the war."],
  ["170–180", "The tent on the Danube", "In his fifties, often ill, he spent years in army camps on the northern frontier. There, at night, he wrote in Greek a notebook to himself. Two of its books end with a note of where he was: 'among the Quadi, on the Gran', and 'at Carnuntum'. He died on campaign in 180. The notebook survived by chance, and we call it the Meditations."]],
 day=[
  ["Before dawn", "When he did not want to get up, he told himself that he was rising to do the work of a human being, for which he was made (Meditations V.1)."],
  ["First thing", "He prepared to meet the meddling, the ungrateful and the arrogant, and reminded himself that they were his kin and could not harm him (II.1)."],
  ["All day", "The work of an emperor: hearing cases and petitions, often far into the night, and commanding an army in the field."],
  ["At night", "Short notes to himself, never meant for anyone else."]],
 week=[
  "Before you look at anything else, write one line to yourself about how you mean to treat people today.",
  "Name one person likely to irritate you today, and decide in advance not to be angry.",
  "When you don't want to get up, say: I am rising to do the work of a human being.",
  "Sort today's worries into two lists: what is in my power, and what is not. Act only on the first.",
  "Do one small good for someone who has wronged you.",
  "Write down one thing you owe to each of three people, as Marcus does in Book I.",
  "Read back your week's lines and keep the one you most need."],
 read=["Marcus Aurelius, Meditations, tr. George Long (1862), free on Project Gutenberg.", "Donald Robertson, How to Think Like a Roman Emperor (2019).", "Frank McLynn, Marcus Aurelius: Warrior, Philosopher, Emperor (2009)."],
 sources=["Marcus Aurelius, Meditations I, II.1, V.1 and the endings of Books I and II.", "Historia Augusta, Life of Marcus 17 (the auction).", "Cassius Dio, Roman History 72."]),

"elizabeth": dict(
 hook="A princess who survived prison by learning, and ruled for forty-five years.",
 story=[
  ["1536–1550", "The schoolroom", "Her mother, Anne Boleyn, was executed when Elizabeth was two. She grew up in the schoolroom. At eleven she translated a French book of devotion into English as a New Year's gift for her stepmother, Catherine Parr. Her tutor Roger Ascham boasted that she read more Greek in a day than some clergy read Latin in a week."],
  ["1554", "The Tower", "After a rebellion against her sister, Queen Mary, Elizabeth was sent to the Tower of London, certain she would die. Nothing was proved against her, and she was moved to house arrest at Woodstock. She learned there what she later lived by: to see everything and say little."],
  ["1588–1593", "Tilbury, and Boethius", "As queen she faced the Spanish Armada and rode out to her army at Tilbury. Five years later, at sixty, grieved by news from France, she translated the whole of Boethius's Consolation of Philosophy from Latin in about a month, the book Christians had read for a thousand years about bearing a fortune that turns."]],
 day=[
  ["Morning (as a girl)", "The Greek New Testament, then Greek orators and Sophocles with Ascham."],
  ["Afternoon (as a girl)", "Latin: Cicero and Livy."],
  ["As queen", "Private prayers in her closet, many of which she wrote herself, in English, Latin, French, Italian and Greek."],
  ["Every day", "Business of state, letters and audiences; and, for pleasure, music at the virginals and translation."]],
 week=[
  "Read ten lines of something hard: a page of Boethius, a psalm, a speech of Shakespeare.",
  "Write a short prayer of your own, as she did in her prayer book.",
  "Learn the three lines she spoke at Tilbury.",
  "Keep one confidence today: see, and say nothing.",
  "Put a hard passage into your own words, as she translated for pleasure.",
  "When you feel outmatched today, say the Tilbury lines to yourself.",
  "Learn Boethius's lines on Fortune's wheel."],
 read=["Elizabeth I: Collected Works, ed. Marcus, Mueller and Rose (2000).", "Helen Castor, Elizabeth I (2018).", "Lisa Hilton, Elizabeth: Renaissance Prince (2014)."],
 sources=["Roger Ascham, The Scholemaster (1570) and his letter to Johann Sturm (1550).", "Boethius translation, 1593, with her secretary's note of the time taken (Public Record Office).", "Elizabeth's prayer book (Precationes privatae, 1563) in Collected Works."]),

"bach": dict(
 hook="He wrote more than a thousand works, and signed them to God.",
 story=[
  ["1694–1700", "The orphan who copied music", "Bach came from a family of musicians. By ten he had lost both parents and went to live with his elder brother. His early biography tells how the boy copied out a book of keyboard music his brother had forbidden him, by moonlight, over six months, only to have it taken away."],
  ["1705", "The walk to Lübeck", "As a young organist he took four weeks' leave and walked some four hundred kilometres north to Lübeck to hear the great Buxtehude play. He stayed nearly four months. His church council reprimanded him. He did not regret it."],
  ["1723–1750", "Leipzig", "As cantor of St Thomas's in Leipzig he ran the music of the city's main churches and taught at the school. In his first years he wrote a new cantata for nearly every Sunday. On Good Friday 1727 the St Matthew Passion was first heard. In his last year, nearly blind, he was still at work."]],
 day=[
  ["Every week", "A cantata to write, copy out, rehearse with the boys of the school and perform on Sunday."],
  ["Weekdays", "Teaching and rehearsing at the Thomasschule, where the family lived."],
  ["At his desk", "Each score begun 'J.J.', Jesu juva, 'Jesus, help', and ended 'S.D.G.', Soli Deo gloria, 'to God alone the glory'."],
  ["At home", "A house full of children, pupils and music; his sons became composers too."]],
 week=[
  "Write 'Jesus, help' at the top of today's first piece of work.",
  "Listen to one Bach chorale all the way through, doing nothing else.",
  "Do one task as well as you possibly can, though no one will notice.",
  "Learn the first verse of 'O sacred Head, now wounded'.",
  "Sing or hum a hymn at home.",
  "Listen to the opening chorus of the St Matthew Passion.",
  "Write 'to God alone the glory' at the end of this week's work."],
 read=["John Eliot Gardiner, Music in the Castle of Heaven (2013).", "Christoph Wolff, Johann Sebastian Bach: The Learned Musician (2000).", "The New Bach Reader, ed. David, Mendel and Wolff (1998)."],
 sources=["The Obituary of Bach by C. P. E. Bach and J. F. Agricola (1754), in The New Bach Reader.", "Arnstadt consistory record, 21 February 1706.", "Bach's annotated Calov Bible (Concordia Seminary, St Louis)."]),

"wilberforce": dict(
 hook="A rich young MP who nearly gave up politics for God, then spent his life ending the slave trade.",
 story=[
  ["1784–1785", "The great change", "Wilberforce was elected to Parliament at twenty-one: rich, witty, a gambler and a famous singer at parties. On a tour of Europe he read the New Testament in Greek with a friend and was converted. He thought he should leave politics. The old clergyman John Newton, once a slave-ship captain, told him God might use him where he was."],
  ["1787", "Two great objects", "Encouraged by his friend William Pitt, he took up the cause of abolition. On 28 October 1787 he wrote in his journal that God had set before him two great objects: the end of the slave trade, and the reform of the nation's manners."],
  ["1807–1833", "The vote", "Year after year his bill failed. In February 1807 the Commons voted to abolish the trade by 283 to 16, and members rose to cheer him while he sat with his head in his hands. The Act to end slavery itself passed in July 1833. He heard of it three days before he died."]],
 day=[
  ["Early morning", "Prayer and Scripture before any business: he wrote in his journal that he must keep this time, and grieved when he lost it."],
  ["Walking to Parliament", "He is said to have recited Psalm 119, the longest psalm, which he knew by heart."],
  ["Day and night", "Parliament, letters, committees and friends, often till late."],
  ["Sunday", "No politics at all: church, family and rest."]],
 week=[
  "Keep the first half hour today for prayer and reading, before any news or messages.",
  "Write down the one wrong in the world you most care about.",
  "Find out one true fact about it, and one group working against it.",
  "Learn Psalm 119:105.",
  "Give something to that work, of money or time.",
  "Keep Sunday free of work.",
  "Write your own 'great object' in one sentence, as he did."],
 read=["William Hague, William Wilberforce (2007).", "Eric Metaxas, Amazing Grace (2007).", "William Wilberforce, A Practical View of Christianity (1797), free online."],
 sources=["R. I. and S. Wilberforce, The Life of William Wilberforce (1838), including the journal for 28 October 1787.", "Hansard, 23 February 1807."]),

"lincoln": dict(
 hook="Less than a year of school, and the English of the King James Bible and Shakespeare.",
 story=[
  ["1809–1830", "The borrowed books", "Lincoln was born in a log cabin in Kentucky. He wrote that his schooling came 'by littles' and did not add up to a year. His stepmother brought books into the house, and he read the Bible, Aesop, The Pilgrim's Progress and a life of Washington until he knew them, walking miles to borrow more."],
  ["1858", "A house divided", "Accepting his party's nomination for the Senate, he took his text from Jesus: 'A house divided against itself cannot stand.' The nation could not stay half slave and half free. He lost the election, but the speech and the debates that followed made him known across the country."],
  ["1865", "With malice toward none", "In March 1865, with the war nearly won, he gave his second inaugural address: a short sermon, quoting the Bible, on a nation under judgement. It ends 'With malice toward none, with charity for all'. Six weeks later he was shot."]],
 day=[
  ["Early", "At his desk before breakfast."],
  ["Morning to afternoon", "Callers, sometimes for hours: anyone could come. He called it his 'public opinion baths'."],
  ["Evening", "To the War Department telegraph office to read the dispatches from the front."],
  ["Late at night", "Reading aloud, often Shakespeare, to whoever was still awake."]],
 week=[
  "Read Psalm 19 aloud.",
  "Read the Gettysburg Address aloud, slowly, twice.",
  "Learn its first sentence.",
  "Read Macbeth's 'To-morrow' speech aloud: he thought nothing equalled Macbeth.",
  "Write the angry letter, and don't send it. He did this.",
  "Learn 'With malice toward none'.",
  "Say the whole Gettysburg Address to someone."],
 read=["Ronald C. White, A. Lincoln (2009).", "Doris Kearns Goodwin, Team of Rivals (2005).", "Douglas L. Wilson, Lincoln's Sword (2006)."],
 sources=["Lincoln, autobiographical sketch for Jesse Fell (1859) and for John Scripps (1860).", "House Divided speech, Springfield, 16 June 1858.", "Lincoln to James Hackett, 17 August 1863 (on Macbeth).", "Unsent letter to General Meade, 14 July 1863.", "John Hay, diaries."]),

"douglass": dict(
 hook="He taught himself to read in secret, and became the greatest speaker in America.",
 story=[
  ["About 1826", "The alphabet", "As an enslaved boy sent to Baltimore, Douglass was taught the alphabet by the woman of the house, until her husband stopped her: learning, he said, would make the boy unfit to be a slave. Douglass wrote that at that moment he understood the pathway from slavery to freedom. He traded bread with white boys in the street for reading lessons."],
  ["1838", "Freedom", "At twenty he escaped, by train and steamboat to New York, dressed as a sailor and carrying a free sailor's papers. Three years later, at an anti-slavery meeting in Nantucket, he stood up and spoke, and was hired at once as a lecturer."],
  ["1845–1852", "The book and the speech", "His Narrative of 1845 made him famous and put him in danger, so he spent two years speaking in Britain and Ireland, where friends bought his legal freedom. Back in Rochester he started his own newspaper, and in 1852 gave the speech 'What to the slave is the Fourth of July?'."]],
 day=[
  ["As a boy", "Reading in secret, and copying letters in chalk on fences and walls, and in the spaces of his young master's copybooks."],
  ["As a young man", "A secret Sunday school for other enslaved men, teaching them to read."],
  ["In Rochester", "Editing his paper, The North Star, every week."],
  ["On tour", "Speaking most evenings, across the North and abroad."]],
 week=[
  "Read one paragraph of a great speech aloud.",
  "Read Psalm 137 and ask what it meant to him.",
  "Learn the opening lines of his Fourth of July speech.",
  "Teach someone something you know, as he did in his Sunday school.",
  "Learn Isaiah 59:1.",
  "Name one place where your country falls short of its own ideals, and write one sentence about it.",
  "Say the lines to someone."],
 read=["Frederick Douglass, Narrative of the Life of Frederick Douglass (1845), free on Project Gutenberg.", "David W. Blight, Frederick Douglass: Prophet of Freedom (2018)."],
 sources=["Narrative (1845), chapters 6, 7 and 10.", "My Bondage and My Freedom (1855), appendix.", "Blight, Frederick Douglass (2018)."]),

"tubman": dict(
 hook="She could not read, knew the Bible by heart, and never lost a passenger.",
 story=[
  ["About 1822–1849", "Araminta", "She was born Araminta Ross, enslaved in Maryland. As a teenager she was struck on the head by a heavy weight thrown by an overseer at someone else. For the rest of her life she had seizures and vivid dreams, which she took to be from God."],
  ["1849", "Escape", "Fearing she would be sold, she escaped alone, walking about ninety miles to Philadelphia. She said later that when she crossed into freedom she looked at her hands to see if she was the same person."],
  ["1850–1863", "Moses", "She went back about thirteen times and led some seventy people to freedom, among them her parents and brothers, and said she never lost a passenger. People called her Moses. In the Civil War she guided a raid on the Combahee River that freed more than seven hundred."]],
 day=[
  ["All day", "Prayer, constantly: she said she talked to God as to a friend, about her work, on the road, at every danger."],
  ["On the road", "Travelling by night; songs and spirituals as signals to those she led."],
  ["In later life", "In Auburn, New York, she took in the old and the poor, and founded a home for the aged."]],
 week=[
  "Talk to God today as to a friend, in your own words, about your work.",
  "Learn the first verse of 'Go down, Moses'.",
  "Do one brave, quiet thing for someone who cannot help themselves.",
  "Listen to a spiritual sung all the way through.",
  "Read Exodus 3:7–10, the story of the Moses she was named after.",
  "When you are afraid today, pray in the moment, not afterwards.",
  "Visit, ring or write to someone old and alone."],
 read=["Sarah H. Bradford, Scenes in the Life of Harriet Tubman (1869), free online.", "Kate Clifford Larson, Bound for the Promised Land (2004)."],
 sources=["Bradford, Scenes in the Life of Harriet Tubman (1869) and Harriet, the Moses of Her People (1886).", "Larson, Bound for the Promised Land (2004)."]),

"nightingale": dict(
 hook="She heard a call at sixteen, defied her family, and made nursing a profession.",
 story=[
  ["1837", "The call", "On 7 February 1837, aged sixteen, she wrote that God spoke to her and called her to his service. Her rich family expected her to marry. It took her sixteen years, and a refusal of a man she loved, before they let her train as a nurse."],
  ["1854–1856", "The lamp", "In the Crimean War she took thirty-eight nurses to the army hospital at Scutari, where soldiers lay in filth. She walked the wards at night with a lamp, and the newspapers made her famous. After the war she used statistics, and a diagram of her own design, to show that most of the dead had died of disease, not wounds."],
  ["1857–1910", "The work from a bed", "Ill for most of the rest of her long life, she worked from her bed: she founded the first school of nursing at St Thomas's in 1860, wrote Notes on Nursing, and pressed ministers for reform for fifty years."]],
 day=[
  ["At Scutari", "Twenty hours on her feet; at night the round of the wards with her lamp."],
  ["Every day", "Private notes and prayers; her copy of Thomas à Kempis's The Imitation of Christ is full of her markings."],
  ["In later life", "Letters, reports and visitors from her room, for hours each day."]],
 week=[
  "Learn the line from Thomas à Kempis she lived by.",
  "Write down what you believe you are called to do.",
  "Do one hidden act of care that no one will thank you for.",
  "Ring or visit someone who is ill.",
  "Count something that matters, and act on what you find.",
  "Pray for nurses and carers, by name if you know them.",
  "Write one step towards your calling, and take it."],
 read=["Florence Nightingale, Notes on Nursing (1859), free on Project Gutenberg.", "Mark Bostridge, Florence Nightingale (2008)."],
 sources=["Nightingale's private note of 7 February 1837, in Bostridge (2008).", "The Times, 8 February 1855 ('ministering angel').", "Nightingale, Notes on Matters Affecting the Health… of the British Army (1858)."]),

"churchill": dict(
 hook="Bottom of the class, prize-winner in poetry, and the voice of a nation alone.",
 story=[
  ["1888", "Harrow", "He was kept in the bottom form at Harrow for three years. But there he was drilled in plain English until, he said, he had the structure of the British sentence in his bones; and he won a prize open to the whole school by reciting twelve hundred lines of Macaulay without a mistake."],
  ["1899", "Escape", "As a young war correspondent in South Africa he was captured by the Boers, escaped from prison in Pretoria, and made his way three hundred miles to freedom. He came home famous and was elected to Parliament the next year."],
  ["1940–1941", "Alone", "He became Prime Minister in May 1940 as France fell. His speeches that summer carried the rhythms of the Bible and the poets he knew by heart. In a broadcast in April 1941 he quoted Clough, 'westward, look, the land is bright'; in August he chose 'O God, our help in ages past' for a service at sea with Roosevelt."]],
 day=[
  ["Morning", "Work in bed with breakfast: papers, letters and dictation."],
  ["Afternoon", "Lunch, then an hour's sleep, which he said doubled his day."],
  ["Evening", "Dinner, then work again, often until two or three in the morning."],
  ["To rest", "Painting and bricklaying at Chartwell: a change of work, not idleness."]],
 week=[
  "Learn the first four lines of Horatius.",
  "Learn the next four.",
  "Read Clough's 'Say not the struggle' aloud.",
  "Write something today, even a single page.",
  "Rest by changing your work: paint, build, play an instrument.",
  "Sing 'O God, our help in ages past'.",
  "Say the Horatius lines aloud to someone."],
 read=["Winston S. Churchill, My Early Life (1930).", "Andrew Roberts, Churchill: Walking with Destiny (2018).", "Winston S. Churchill, Painting as a Pastime (1948)."],
 sources=["My Early Life (1930), chapters 2 and 3.", "Broadcast of 27 April 1941.", "Church service on HMS Prince of Wales, 10 August 1941."]),

"solzhenitsyn": dict(
 hook="He wrote whole books in his head in the camps, and told the world the truth.",
 story=[
  ["1945", "Arrest", "Solzhenitsyn was an artillery captain at the front when he was arrested for criticising Stalin in letters to a friend. He was sentenced to eight years in the labour camps."],
  ["1950–1953", "Lines in his head", "In the camp at Ekibastuz paper was searched and taken. So he composed in his head, a few lines at a time, and repeated everything he had made, counting on a string of beads made from bread. He wrote that he carried some twelve thousand lines this way. In the camps he also came back to the faith of his childhood."],
  ["1962–1974", "One Day", "In 1962 One Day in the Life of Ivan Denisovich was published in Moscow and astonished the world. He won the Nobel Prize in 1970. In 1974, after The Gulag Archipelago appeared in the West, he was expelled from his country. On the day of his arrest his essay 'Live not by lies' was released."]],
 day=[
  ["In the camp", "Labour all day; lines composed in his head while he worked, and repeated in order."],
  ["In exile in Vermont", "At his desk from early morning, every day, for years."],
  ["His rule", "Not to repeat what he knew to be a lie: the one thing anyone can do."]],
 week=[
  "Choose four lines worth keeping, and say them twenty times.",
  "Add four more, after saying yesterday's first.",
  "Refuse to say one thing today that you do not believe.",
  "Learn the Lord's Prayer, if you do not know it yet.",
  "Pray for a prisoner of conscience somewhere in the world.",
  "Add four more lines, and say the whole from the start.",
  "Say everything you have learned, without the page."],
 read=["Aleksandr Solzhenitsyn, One Day in the Life of Ivan Denisovich (1962).", "Aleksandr Solzhenitsyn, The Gulag Archipelago (1973).", "Michael Scammell, Solzhenitsyn: A Biography (1984)."],
 sources=["The Gulag Archipelago, part V, chapter 5 (composing in his head).", "'Live Not by Lies' (12 February 1974).", "Scammell (1984)."]),

"bonhoeffer": dict(
 hook="A theologian who taught a community to pray, and kept praying in a Nazi prison.",
 story=[
  ["1930–1931", "Harlem", "As a young German scholar in New York he found the sermons at his seminary thin. He went instead to the Abyssinian Baptist Church in Harlem, taught Sunday school there and took home recordings of spirituals."],
  ["1935–1937", "Finkenwalde", "Back in Germany he ran a seminary for the Confessing Church, which refused to bow to Hitler. He gave its students a daily rule of Scripture, prayer, silence and work together, and wrote about it in Life Together. The Gestapo closed it in 1937."],
  ["1943–1945", "Prison", "Drawn into the plot against Hitler, he was arrested in April 1943. From his cell in Berlin he wrote letters and prayers, and at the end of 1944 a poem of trust in God's good powers. He was hanged at Flossenbürg on 9 April 1945, weeks before the war ended."]],
 day=[
  ["On waking", "Silence; the first word of the day belongs to God."],
  ["Morning", "Psalms, a hymn, a passage of Scripture and prayer together, before breakfast."],
  ["Then", "Half an hour alone with one short text, the same one all week, and prayer for others by name."],
  ["Evening", "Prayer together, then silence until morning."]],
 week=[
  "Begin the day with Scripture before you speak to anyone.",
  "Choose one short verse and sit with it for ten minutes. Keep the same verse all week.",
  "Pray for three people by name.",
  "Keep an hour of silence in the evening.",
  "Read a psalm aloud with someone.",
  "Do one costly good thing.",
  "Write down what the week's verse taught you."],
 read=["Eberhard Bethge, Dietrich Bonhoeffer: A Biography (1967).", "Charles Marsh, Strange Glory (2014).", "Dietrich Bonhoeffer, Life Together (1939)."],
 sources=["Bonhoeffer, Life Together (1939), chapters 2 and 3.", "Letters and Papers from Prison.", "Bethge (1967)."]),

"king": dict(
 hook="A preacher's son who carried the Hebrew prophets into the streets.",
 story=[
  ["1955–1956", "Montgomery", "At twenty-six, the new pastor of a church in Montgomery, Alabama, he was chosen to lead the boycott of the city's buses after Rosa Parks's arrest. It lasted 381 days, and it won."],
  ["January 1956", "The kitchen table", "One night a phone call threatened to kill him and his family. Unable to sleep, he prayed aloud at the kitchen table, and said he heard an inner voice telling him to stand up for righteousness. Three days later his house was bombed. He stayed calm, and told the angry crowd outside to put away their weapons."],
  ["1963–1968", "Birmingham and Washington", "In April 1963 he wrote his Letter from Birmingham Jail in the margins of a newspaper. In August, before a quarter of a million people, he spoke of his dream, quoting Amos and Isaiah. He was killed in Memphis on 4 April 1968."]],
 day=[
  ["Every day", "Prayer and Scripture; sermons prepared through the week, often in airports and hotel rooms."],
  ["His pledge", "Volunteers in Birmingham signed a card promising, among other things, to meditate daily on the life of Jesus, to pray daily to be used by God, and to walk and talk in the manner of love."],
  ["Sunday", "Preaching, wherever he was."]],
 week=[
  "Read one saying of Jesus this morning, and think about it during the day.",
  "Pray to be used by God today.",
  "Speak gently to someone you disagree with.",
  "Do one thing today for others, not yourself.",
  "Learn Amos 5:24.",
  "When you are afraid, tell God plainly what you fear.",
  "Learn Isaiah 40:4."],
 read=["Martin Luther King Jr., Stride Toward Freedom (1958).", "Martin Luther King Jr., Why We Can't Wait (1964).", "Taylor Branch, Parting the Waters (1988)."],
 sources=["Stride Toward Freedom (1958), chapter 8 (the kitchen).", "Why We Can't Wait (1964), chapter 4 (the commitment card).", "Letter from Birmingham Jail, 16 April 1963."]),

"mandela": dict(
 hook="Twenty-seven years in prison, and he came out without bitterness.",
 story=[
  ["1964", "The dock", "At his trial for sabotage he spoke for three hours, ending that the ideal of a free and democratic society was one for which he was prepared to die. He was sentenced to life imprisonment, aged forty-five."],
  ["1964–1982", "Robben Island", "He broke stones in a lime quarry by day and slept on a mat in a tiny cell. The prisoners shared a copy of Shakespeare; Mandela marked in it the line from Julius Caesar, 'Cowards die many times before their deaths'. He studied law by correspondence and kept 'Invictus' in his head."],
  ["1990–1994", "Freedom", "He was released in February 1990, after twenty-seven years. In 1994 he became South Africa's first president elected by all its people, and invited one of his former jailers to his inauguration."]],
 day=[
  ["Before dawn", "Exercise in his cell: running on the spot, press-ups, sit-ups."],
  ["By day", "Hard labour in the quarry, and talk with the other prisoners, which they called the university."],
  ["At night", "Study for his degree, and letters, which were few and censored."],
  ["Always", "A small garden, which he said gave him a taste of freedom."]],
 week=[
  "Learn the first verse of 'Invictus'.",
  "Learn 'Cowards die many times before their deaths'.",
  "Begin the day with one small act of discipline, before anything else.",
  "Tend one small thing: a plant, a skill or a friendship.",
  "Pray for someone who has wronged you.",
  "Study something for twenty minutes.",
  "Say 'Invictus' to someone."],
 read=["Nelson Mandela, Long Walk to Freedom (1994).", "Nelson Mandela, Conversations with Myself (2010).", "Ashwin Desai, Reading Revolution: Shakespeare on Robben Island (2012)."],
 sources=["Statement from the dock, Rivonia Trial, 20 April 1964.", "Long Walk to Freedom (1994), parts 8–10.", "The 'Robben Island Shakespeare' of Sonny Venkatrathnam, signed by Mandela on 16 December 1977."]),
}

for p in k['greats']['people']:
    if p['id'] in L: p.update(L[p['id']])
missing = [p['id'] for p in k['greats']['people'] if p['id'] not in L]
assert not missing, missing
json.dump(k, open(K, 'w'), ensure_ascii=False, indent=1); open(K, 'a').write('\n')
print('ok', len(L))
