"""Keep: Live like the greats. What the people who built the West knew by heart, did every day and understood,
and what you can do. Writes content/keep.json `greats` and adds the memory entries they need.
Run: python3 tools/days/greats.py"""
import json, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
K = os.path.join(ROOT, 'content', 'keep.json'); M = os.path.join(ROOT, 'content', 'memory.json')
k = json.load(open(K)); m = json.load(open(M)); have = {x['id'] for x in m}

def web(id, title, ref, author, lines, why, src):
    return {"id": id, "title": title, "kind": "Scripture", "src": f"{ref} · World English Bible", "author": author, "work": ref, "translator": "World English Bible", "tradition": "jerusalem", "lines": lines, "why": why, "source": f"https://ebible.org/eng-web/{src}.htm"}

NEW = [
 web("psalm-22-1", "My God, my God", "Psalm 22:1", "Psalms", ["My God, my God, why have you forsaken me?", "Why are you so far from helping me, and from the words of my groaning?"], "The psalm Jesus prayed from the cross (Mark 15:34).", "PSA022"),
 web("psalm-31-5", "Into your hand", "Psalm 31:5", "Psalms", ["Into your hand I commend my spirit.", "You redeem me, Yahweh, God of truth."], "Jesus's last words on the cross in Luke (23:46), and the night prayer of Jews and Christians ever since.", "PSA031"),
 {"id": "macaulay-horatius", "title": "Horatius at the bridge", "kind": "Poem", "src": "Thomas Babington Macaulay, Lays of Ancient Rome (1842), 'Horatius', stanza XXVII", "author": "Thomas Babington Macaulay", "work": "Lays of Ancient Rome", "translator": "", "tradition": "poets",
  "lines": ["Then out spake brave Horatius,", "The Captain of the Gate:", "\"To every man upon this earth", "Death cometh soon or late.", "And how can man die better", "Than facing fearful odds,", "For the ashes of his fathers,", "And the temples of his gods,"],
  "why": "Part of the poem Churchill recited at school, twelve hundred lines without a mistake: a Roman soldier holding a bridge alone against an army.", "source": "https://www.gutenberg.org/ebooks/847"},
 {"id": "shakespeare-tomorrow", "title": "To-morrow, and to-morrow", "kind": "Poem", "src": "William Shakespeare, Macbeth, Act V, Scene 5", "author": "William Shakespeare", "work": "Macbeth", "translator": "", "tradition": "poets",
  "lines": ["To-morrow, and to-morrow, and to-morrow,", "Creeps in this petty pace from day to day,", "To the last syllable of recorded time;", "And all our yesterdays have lighted fools", "The way to dusty death. Out, out, brief candle!", "Life's but a walking shadow; a poor player,", "That struts and frets his hour upon the stage,", "And then is heard no more: it is a tale", "Told by an idiot, full of sound and fury,", "Signifying nothing."],
  "why": "Macbeth's despair, from the play Lincoln said nothing equalled. Learn it to know what a life without hope sounds like.", "source": "https://www.gutenberg.org/ebooks/1533"},
 {"id": "lincoln-gettysburg", "title": "The Gettysburg Address", "kind": "Speech", "src": "Abraham Lincoln, Gettysburg, 19 November 1863 (the Bliss copy)", "author": "Abraham Lincoln", "work": "The Gettysburg Address", "translator": "", "tradition": "poets",
  "lines": ["Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.",
   "Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.",
   "But, in a larger sense, we can not dedicate—we can not consecrate—we can not hallow—this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here.",
   "It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us—that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion—that we here highly resolve that these dead shall not have died in vain—that this nation, under God, shall have a new birth of freedom—and that government of the people, by the people, for the people, shall not perish from the earth."],
  "why": "Two minutes, 272 words, written by a man steeped in the King James Bible. Generations of American schoolchildren learned it by heart.", "source": "https://www.loc.gov/exhibits/gettysburg-address/"},
 {"id": "henley-invictus", "title": "Invictus", "kind": "Poem", "src": "William Ernest Henley, 'Invictus' (1875, published 1888)", "author": "William Ernest Henley", "work": "Invictus", "translator": "", "tradition": "poets",
  "lines": ["Out of the night that covers me,", "Black as the pit from pole to pole,", "I thank whatever gods may be", "For my unconquerable soul.", "In the fell clutch of circumstance", "I have not winced nor cried aloud.", "Under the bludgeonings of chance", "My head is bloody, but unbowed.", "Beyond this place of wrath and tears", "Looms but the Horror of the shade,", "And yet the menace of the years", "Finds, and shall find, me unafraid.", "It matters not how strait the gate,", "How charged with punishments the scroll,", "I am the master of my fate:", "I am the captain of my soul."],
  "why": "Written by a young man in hospital after losing a leg, and kept in the heads of Mandela and his fellow prisoners on Robben Island. It is a poem of courage, not of faith: a Christian would say the captain of the soul is God.", "source": "https://www.gutenberg.org/ebooks/author/1102"},
 {"id": "o-sacred-head", "title": "O sacred Head, now wounded", "kind": "Hymn", "src": "Paul Gerhardt (1656), from a medieval Latin hymn; translated by James Waddell Alexander (1830)", "author": "Paul Gerhardt", "work": "O Haupt voll Blut und Wunden", "translator": "James Waddell Alexander (1830)", "tradition": "hymns",
  "lines": ["O sacred Head, now wounded,", "With grief and shame weighed down,", "Now scornfully surrounded", "With thorns, thine only crown;", "How pale thou art with anguish,", "With sore abuse and scorn!", "How does that visage languish", "Which once was bright as morn!"],
  "why": "Bach set this hymn five times in the St Matthew Passion; Bonhoeffer knew Gerhardt's hymns by heart in his prison cell.", "source": "https://hymnary.org/text/o_sacred_head_now_wounded_with_grief_and"},
]
for e in NEW:
    if e['id'] not in have: m.append(e); have.add(e['id'])

k['greats'] = {
 "title": "Live like the greats",
 "line": "The people who built our world carried great words in their heads, kept small habits every day, and understood a few things deeply. Here is what they knew, what they did and what they understood, and how you can do the same.",
 "people": [
  {"id": "jesus", "name": "Jesus of Nazareth", "years": "about 4 BC – AD 30", "who": "A carpenter's son from a village in Galilee, who knew the Scriptures of Israel by heart.",
   "knew": [["deuteronomy-6-4", "The Shema, which every Jewish boy learned to say morning and evening."], ["psalm-22-1", "The psalm he prayed from the cross."], ["psalm-31-5", "His last words, in Luke: a psalm he had known since childhood."]],
   "did": "He went to the synagogue every Sabbath, 'as was his custom' (Luke 4:16), and rose before dawn to pray alone: 'Early in the morning, while it was still dark, he rose up and went out, and departed into a deserted place, and prayed there' (Mark 1:35).",
   "you": "Before the day starts, go somewhere quiet for five minutes and pray, alone.",
   "understood": "That the whole law hangs on two commandments: love God with everything, and love your neighbour as yourself. And that in the worst hour, the words that hold you up are the ones you learned long before you needed them."},
  {"id": "benedict", "name": "Benedict of Nursia", "years": "about 480 – 547", "who": "Wrote the Rule that shaped Western monasteries, and through them Europe's schools, farms and libraries.",
   "knew": [["ps23", "His monks sang all 150 psalms every week; many knew the whole psalter by heart."], ["psalm-121", "One of the 'songs of ascents', sung at the short hours of the day."], ["lords", "Said aloud at the end of morning and evening prayer, by the Rule's own instruction."]],
   "did": "Under his Rule the monks stopped work at set hours of the day and night to sing the psalms, worked with their hands, and gave hours each day to slow reading of Scripture. He wrote that idleness is the enemy of the soul (Rule, chapter 48).",
   "you": "Choose one fixed time each day, the same every day, to stop whatever you are doing and say one psalm.",
   "understood": "That a life is shaped by small things done at the same hour every day: prayer, work and reading, kept in balance. Freedom grows inside a good rhythm, not outside it."},
  {"id": "marcus", "name": "Marcus Aurelius", "years": "121 – 180", "who": "Roman emperor and Stoic philosopher, who spent years of his reign at war on the Danube.",
   "knew": [["within-our-power", "From Epictetus, whose teaching he was given as a young man and never forgot (Meditations I.7)."], ["begin-the-morning", "His own morning note to himself."], ["ten-thousand-years", "His reminder that life is short."]],
   "did": "Each day he wrote short notes to himself in Greek, never meant for anyone else; we call them the Meditations. He began his mornings by preparing to meet difficult people without anger.",
   "you": "Each morning, write one line to yourself about how you mean to treat people today.",
   "understood": "That we cannot control what happens to us, only how we respond; and that the people who wrong us are our own kin. Christians later found in him a pagan who came close to the Sermon on the Mount."},
  {"id": "augustine", "name": "Augustine of Hippo", "years": "354 – 430", "who": "A brilliant, restless teacher of rhetoric who became the most influential thinker of the Western Church.",
   "knew": [["smooth-the-descent", "He learned Virgil by heart as a schoolboy, and wept over Dido (Confessions I.13)."], ["psalm-51", "He had the penitential psalms written on the wall by his bed as he was dying (Possidius, Life of Augustine 31)."], ["augustine-our-heart-is-restless", "His own first words in the Confessions."]],
   "did": "As bishop, he had a verse written on his dining table forbidding anyone to speak ill of people who were not there, and he enforced it (Possidius, Life of Augustine 22).",
   "you": "Keep your table free of gossip: no one is spoken ill of who is not there to answer.",
   "understood": "That the heart is restless until it rests in God: every longing, even the wrong ones, is in the end a longing for him."},
  {"id": "bach", "name": "Johann Sebastian Bach", "years": "1685 – 1750", "who": "Organist and cantor in Leipzig, thought by many the greatest composer who ever lived.",
   "knew": [["o-sacred-head", "Paul Gerhardt's hymn, which he set again and again in the St Matthew Passion."], ["lords", "In Luther's Small Catechism, which he learned as a schoolboy in Eisenach."]],
   "did": "He headed his scores 'J.J.', Jesu juva, 'Jesus, help', and ended them 'S.D.G.', Soli Deo gloria, 'to God alone the glory'. In his first years at Leipzig he wrote a new cantata for nearly every Sunday.",
   "you": "Begin your work today with 'Jesus, help', and end it with 'to God alone the glory'.",
   "understood": "That all work, done well, can be offered to God. In the margin of his Bible he wrote that where there is devotional music, God is always present with his grace."},
  {"id": "lincoln", "name": "Abraham Lincoln", "years": "1809 – 1865", "who": "With barely a year of schooling, he became the President who held the United States together through civil war and set it on the road to ending slavery.",
   "knew": [["shakespeare-tomorrow", "He said that nothing equalled Macbeth, and knew long passages by heart."], ["lincoln-gettysburg", "What he wrote, in the rhythm of the King James Bible he had read all his life."], ["lincoln-with-malice", "The close of his Second Inaugural, six weeks before his death."]],
   "did": "He read the few great books he owned over and over, often aloud. In the war years he read the Bible, writing to his friend Joshua Speed in 1864, 'I am profitably engaged in reading the Bible.'",
   "you": "Read one great passage aloud every day this week, until you know its rhythm by heart.",
   "understood": "That a nation can be judged by a justice higher than its own. His Second Inaugural reads the war through the Psalms and the Gospels, and ends with 'malice toward none'."},
  {"id": "churchill", "name": "Winston Churchill", "years": "1874 – 1965", "who": "The Prime Minister who led Britain through the Second World War, and won the Nobel Prize for Literature.",
   "knew": [["macaulay-horatius", "He won a prize at Harrow for reciting twelve hundred lines of Macaulay's Lays of Ancient Rome without a mistake (My Early Life)."], ["shakespeare-what-a-piece-of-work", "He could quote Shakespeare at length all his life."]],
   "did": "He wrote nearly every day of his life. From the age of forty he painted, to rest a mind worn by war and politics; he argued that a change of occupation, not idleness, is what truly refreshes (Painting as a Pastime).",
   "you": "Learn eight lines of poetry this week, and say them aloud when you need courage.",
   "understood": "That great words steady people in dark times. In 1940 he gave a frightened nation words it could stand on, drawn from the Bible, Shakespeare and the poems he had learned as a boy."},
  {"id": "bonhoeffer", "name": "Dietrich Bonhoeffer", "years": "1906 – 1945", "who": "German pastor and theologian who opposed Hitler, and was executed weeks before the end of the war.",
   "knew": [["o-sacred-head", "He knew Paul Gerhardt's hymns by heart, and wrote from prison how they held him up."], ["psalm-121", "He prayed the psalms daily, in his seminary and in his cell."]],
   "did": "He taught his students to begin each day with Scripture and prayer before speaking to anyone else, to meditate on one short passage for half an hour, and to pray for others by name. He kept it up in prison.",
   "you": "Read one verse slowly each morning, and pray for three people by name.",
   "understood": "That grace is free but never cheap: following Christ costs something, and is worth everything. He paid with his life."},
  {"id": "mandela", "name": "Nelson Mandela", "years": "1918 – 2013", "who": "Leader of the struggle against apartheid, imprisoned for twenty-seven years, then the first President of a free South Africa.",
   "knew": [["henley-invictus", "Kept in the heads of the prisoners on Robben Island; he recited it to the men around him."]],
   "did": "In prison he exercised every morning in his cell, studied for a law degree by correspondence, and tended a small garden, which he said gave him a taste of freedom.",
   "you": "Tend one small thing every day, a plant, a skill or a friendship, however hard the day.",
   "understood": "That no one can take your inner freedom, and that forgiving his jailers freed him as much as them. Educated in Methodist schools, he never lost the language of the Bible."}
 ]}
json.dump(k, open(K, 'w'), ensure_ascii=False, indent=1); open(K, 'a').write('\n')
json.dump(m, open(M, 'w'), ensure_ascii=False, indent=1); open(M, 'a').write('\n')
for p in k['greats']['people']:
    for mid, _ in p['knew']: assert mid in have, (p['id'], mid)
print('ok', len(k['greats']['people']))
