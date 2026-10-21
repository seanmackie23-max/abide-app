"""Keep, reframed as living it: adds to content/keep.json
- byheart.people: people who carried great words by heart
- words: the sentences of the West worth remembering (memory ids + one line each)
- home.start and home.greats: where a family starts, and how great households did it
- great: music to hear, art to see, places to go
- rule.rhythm: fitting Today and Explore into an ordinary day
and new memory entries (luke-6-31, lincoln-with-malice, teresa-let-nothing-disturb-thee).
Run: python3 tools/days/keep_more.py"""
import json, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
K = os.path.join(ROOT, 'content', 'keep.json'); M = os.path.join(ROOT, 'content', 'memory.json')
k = json.load(open(K)); m = json.load(open(M)); ids = {x['id'] for x in m}

NEW_MEM = [
 {"id": "luke-6-31", "title": "The golden rule", "kind": "Scripture", "src": "Luke 6:31 · World English Bible", "author": "Luke", "work": "Luke 6:31", "translator": "World English Bible", "tradition": "jerusalem",
  "lines": ["“As you would like people to do to you, do exactly so to them."], "why": "Jesus's rule for every relationship, the sentence the West came to call golden.", "source": "https://ebible.org/eng-web/LUK06.htm"},
 {"id": "lincoln-with-malice", "title": "With malice toward none", "kind": "Speech", "src": "Abraham Lincoln, Second Inaugural Address, 4 March 1865", "author": "Abraham Lincoln", "work": "Second Inaugural Address", "translator": "", "tradition": "poets",
  "lines": ["With malice toward none, with charity for all,", "with firmness in the right as God gives us to see the right,", "let us strive on to finish the work we are in,", "to bind up the nation's wounds,", "to care for him who shall have borne the battle and for his widow and his orphan,", "to do all which may achieve and cherish a just and lasting peace among ourselves and with all nations."],
  "why": "Spoken a month before the end of the American Civil War and six weeks before Lincoln was killed: mercy to the defeated, in the language of the Bible he knew by heart.", "source": "https://avalon.law.yale.edu/19th_century/lincoln2.asp"},
 {"id": "teresa-let-nothing-disturb-thee", "title": "Let nothing disturb thee", "kind": "Poem", "src": "Teresa of Ávila, translated by Henry Wadsworth Longfellow as 'Santa Teresa's Book-Mark'", "author": "Teresa of Ávila", "work": "Santa Teresa's Book-Mark", "translator": "Henry Wadsworth Longfellow", "tradition": "church",
  "lines": ["Let nothing disturb thee,", "Nothing affright thee;", "All things are passing;", "God never changeth;", "Patient endurance", "Attaineth to all things;", "Who God possesseth", "In nothing is wanting;", "Alone God sufficeth."],
  "why": "Found in Teresa's breviary after her death in 1582: nine short lines that have steadied people ever since.", "source": "https://www.gutenberg.org/ebooks/1365"},
]
for e in NEW_MEM:
    if e['id'] not in ids: m.append(e)

k['words'] = {
 "title": "Words of the great",
 "line": "Fifteen sentences that made the West, from Moses to Lincoln. Each is short enough to carry. Start with the first, and add one a week.",
 "items": [
  {"mem": "deuteronomy-6-4", "who": "Moses", "when": "Deuteronomy, the law of Israel", "line": "Hear, Israel: Yahweh is our God. Yahweh is one.", "why": "The Shema, said by Jews morning and evening for nearly three thousand years: the first words of Western faith."},
  {"mem": "micah-what-does-the-lord-require", "who": "Micah", "when": "a prophet of Judah, about 700 BC", "line": "to act justly, to love mercy, and to walk humbly with your God?", "why": "The whole of religion in one sentence."},
  {"mem": "unexamined-life", "who": "Socrates", "when": "at his trial in Athens, 399 BC", "line": "the unexamined life is not worth living", "why": "Said by a man on trial for his life, who would not stop asking questions."},
  {"mem": "by-doing-just-actions", "who": "Aristotle", "when": "Athens, about 330 BC", "line": "by doing just actions we come to be just", "why": "Character is built by practice: the idea behind every habit in this app."},
  {"mem": "luke-6-31", "who": "Jesus", "when": "the Sermon on the Plain, about AD 30", "line": "As you would like people to do to you, do exactly so to them.", "why": "The golden rule. If you remember only one sentence, remember this.", "start": True},
  {"mem": "corinthians-love-is-patient", "who": "Paul", "when": "a letter to Corinth, about AD 55", "line": "Love is patient and is kind.", "why": "Read at more weddings than any other passage."},
  {"mem": "ten-thousand-years", "who": "Marcus Aurelius", "when": "Roman emperor, on campaign, about AD 170", "line": "Do not act as if thou wert going to live ten thousand years.", "why": "The most powerful man in the world, writing notes to himself about death and goodness."},
  {"mem": "augustine-our-heart-is-restless", "who": "Augustine", "when": "North Africa, about AD 397", "line": "Thou madest us for Thyself, and our heart is restless, until it repose in Thee.", "why": "The first sentence of the first autobiography, and the best description of human longing."},
  {"mem": "julian-all-shall-be-well", "who": "Julian of Norwich", "when": "an anchoress in Norwich, 1373", "line": "all shall be well, and all shall be well, and all manner of thing shall be well.", "why": "Written in a plague century by a woman who had nearly died: hope that is not naive."},
  {"mem": "dante-midway-upon-the-journey", "who": "Dante", "when": "Italy, about 1308", "line": "Midway upon the journey of our life I found myself within a forest dark", "why": "The opening of the greatest Christian poem: everyone gets lost, and the way out begins there."},
  {"mem": "shakespeare-what-a-piece-of-work", "who": "Shakespeare", "when": "Hamlet, about 1600", "line": "What a piece of work is man", "why": "Human greatness and human dust in one speech."},
  {"mem": "donne-no-man-is-an-island", "who": "John Donne", "when": "Dean of St Paul's, London, 1624", "line": "No man is an island, entire of itself", "why": "Written on what he thought was his deathbed, hearing a funeral bell."},
  {"mem": "milton-on-his-blindness", "who": "John Milton", "when": "London, about 1655, after going blind", "line": "They also serve who only stand and wait.", "why": "For anyone who cannot do what they once could."},
  {"mem": "teresa-let-nothing-disturb-thee", "who": "Teresa of Ávila", "when": "Spain, before 1582", "line": "Let nothing disturb thee", "why": "Kept in her prayer book: a pocket prayer for anxious days."},
  {"mem": "lincoln-with-malice", "who": "Abraham Lincoln", "when": "Washington, 4 March 1865", "line": "With malice toward none, with charity for all", "why": "How to end a war: Lincoln, who knew the Bible by heart, speaking as it taught him."},
 ]}

k['byheart']['people'] = {
 "title": "They knew it by heart",
 "line": "For most of history, educated people carried great words in their heads. It was not a party trick. It was what they had to think with, and what held them up when everything else was taken away.",
 "items": [
  {"name": "Jesus", "what": "answered every temptation in the desert with words of Scripture he knew by heart, and died praying a psalm (Matthew 4; Psalm 22; Mark 15:34)."},
  {"name": "The monks of St Benedict", "what": "sang all 150 psalms every week under Benedict's Rule (about 530). Many knew the whole psalter by heart."},
  {"name": "Augustine", "what": "learned Virgil by heart as a schoolboy, and admits he wept over Dido before he ever wept over his own soul (Confessions I.13)."},
  {"name": "Abraham Lincoln", "what": "had only a year or so of schooling, but knew long passages of the King James Bible and Shakespeare by heart. His great speeches are full of both."},
  {"name": "Frederick Douglass", "what": "taught himself to read as a slave and learned the speeches in The Columbian Orator by heart. He became the greatest orator of his age."},
  {"name": "Winston Churchill", "what": "won a prize at Harrow for reciting twelve hundred lines of Macaulay's Lays of Ancient Rome without a mistake (My Early Life, 1930), and could recite poetry for hours all his life."},
  {"name": "Dietrich Bonhoeffer", "what": "prayed the psalms and the hymns of Paul Gerhardt that he knew by heart in a Nazi prison cell, before his execution in 1945."},
  {"name": "Aleksandr Solzhenitsyn", "what": "composed thousands of lines of verse in the Soviet labour camps and kept them in his memory, counting them on a rosary made of bread (The Gulag Archipelago)."},
  {"name": "Nelson Mandela", "what": "and his fellow prisoners on Robben Island kept Henley's poem 'Invictus' in their heads; he recited it to the men around him."}
 ]}

k['home']['start'] = {
 "title": "Where to start, with children or without",
 "line": "You do not need to know much. Begin with three small things, in this order, and add the next only when the last has stuck.",
 "steps": [
  {"title": "Say grace at one meal a day", "how": "Use the short one in By heart: 'Come, Lord Jesus, be our guest'. Children can say it within a week.", "go": "byheart"},
  {"title": "A Bible story at bedtime", "how": "Tonight's story, then the three 'I wonder' questions and a one-line prayer. Ten minutes.", "go": "story"},
  {"title": "One line by heart each week", "how": "This week's words, read at breakfast every day. By Sunday, see who can say it. Children usually win.", "go": "week"}
 ],
 "couple": "With a husband or wife: read today's story together at breakfast, and end the day with the night prayer in By heart. Two minutes each, side by side."}
k['home']['greats'] = {
 "title": "How great households did it",
 "items": [
  {"name": "Martin Luther", "what": "wrote his Small Catechism (1529) for the head of each household to teach the family at home: the commandments, the creed, the Lord's Prayer, and short prayers for morning, evening and meals."},
  {"name": "Thomas More", "what": "had Scripture read aloud at meals in his house at Chelsea, and talked it over with his children, whom he educated as seriously as any scholar's sons, daughters included."},
  {"name": "Susanna Wesley", "what": "mother of John and Charles Wesley and of many other children, set aside time alone with each child every week to talk about their soul and their life."},
  {"name": "Johann Sebastian Bach", "what": "made music at home with his large family; the household songbooks he kept for his wife Anna Magdalena include hymns and prayers alongside dances."}
 ]}

k['great'] = {
 "title": "The great works",
 "line": "The music, art and places that people have travelled to for centuries, because they make the faith visible and audible. Hear one, see one, go to one. Each is worth a journey once in your life; several are free.",
 "hear": [
  {"title": "Choral Evensong", "who": "The Church of England", "where": "Any cathedral or college chapel in England, most days, around 5 pm; free", "why": "Sung prayer at dusk, unchanged in shape since 1549. You can sit at the back and say nothing.", "start": True},
  {"title": "A Festival of Nine Lessons and Carols", "who": "King's College, Cambridge", "where": "Christmas Eve, on the radio worldwide since 1928, or queue for a seat", "why": "Nine Bible readings from the fall to the birth of Christ, with carols between."},
  {"title": "St Matthew Passion", "who": "Johann Sebastian Bach, 1727", "where": "Performed across Europe in Holy Week; at its home, the Thomaskirche in Leipzig, most years", "why": "The story of Jesus's death in three hours of music; many think it the greatest work ever written."},
  {"title": "Messiah", "who": "George Frideric Handel, 1741", "where": "Advent and Christmas, everywhere; look for a 'scratch' performance where the audience sings", "why": "The whole Christian story in Scripture's own words. Audiences still stand for the Hallelujah chorus."},
  {"title": "Mass in B minor", "who": "Johann Sebastian Bach, finished 1749", "where": "Concert halls and churches, any season", "why": "Bach's summary of everything he knew, set to the ancient words of the Mass."},
  {"title": "Gregorian chant at a monastery", "who": "Benedictine monks", "where": "Vespers in the evening at an abbey such as Solesmes in France or Maria Laach in Germany; visitors welcome", "why": "The oldest music of the West, still sung where it was born: in monasteries, every day."}
 ],
 "see": [
  {"title": "The Baptism of Christ", "who": "Piero della Francesca, 1440s", "where": "National Gallery, London; free", "why": "Stillness and light: one of the calmest paintings in the world, and an easy first visit.", "start": True},
  {"title": "The Sistine Chapel", "who": "Michelangelo, 1508–12 and 1536–41", "where": "Vatican Museums, Rome; book ahead, go early", "why": "Creation on the ceiling, the Last Judgement on the wall: the Bible painted for the whole of Europe."},
  {"title": "The Calling of Saint Matthew", "who": "Caravaggio, 1600", "where": "San Luigi dei Francesi, Rome; free, in a working church", "why": "A beam of light, a pointing hand, and a tax collector who cannot believe he is chosen."},
  {"title": "The Ghent Altarpiece", "who": "Hubert and Jan van Eyck, 1432", "where": "St Bavo's Cathedral, Ghent", "why": "The Adoration of the Lamb: heaven as a meadow, painted with every leaf."},
  {"title": "The Isenheim Altarpiece", "who": "Matthias Grünewald, 1512–16", "where": "Unterlinden Museum, Colmar", "why": "Painted for a hospital: the most harrowing crucifixion in art, and a blazing resurrection."},
  {"title": "The Last Supper", "who": "Leonardo da Vinci, 1495–98", "where": "Santa Maria delle Grazie, Milan; book weeks ahead, fifteen minutes inside", "why": "The moment Jesus says one of you will betray me, and twelve men react."},
  {"title": "The Scrovegni Chapel", "who": "Giotto, about 1305", "where": "Padua; book ahead", "why": "The life of Christ round the walls of one small chapel, where Western painting learned to show feeling."}
 ],
 "go": [
  {"title": "Your nearest cathedral", "where": "Wherever you live", "why": "Go on an ordinary weekday. Walk slowly from the west door to the altar, as Explore's halls do, and sit for ten minutes.", "start": True},
  {"title": "Chartres Cathedral", "where": "an hour from Paris", "why": "The most complete medieval cathedral, with its 13th-century glass and the labyrinth on the floor."},
  {"title": "Sainte-Chapelle", "where": "Paris", "why": "Built in the 1240s as a reliquary: walls made almost entirely of stained glass."},
  {"title": "Hagia Sophia", "where": "Istanbul", "why": "Justinian's church of Holy Wisdom (537), the greatest building of the ancient world."},
  {"title": "Assisi", "where": "Umbria, Italy", "why": "The hill town of Francis and Clare, with Giotto's frescoes in the basilica."},
  {"title": "Canterbury Cathedral", "where": "Kent, England", "why": "Where Thomas Becket was killed in 1170, and the goal of Chaucer's pilgrims."},
  {"title": "Cologne Cathedral", "where": "Germany", "why": "Begun in 1248 and finished in 1880; the shrine of the Three Kings."},
  {"title": "The Camino de Santiago", "where": "northern Spain, to Santiago de Compostela", "why": "The great pilgrim road of the Middle Ages, walked again by hundreds of thousands each year."}
 ]}

k['rule']['rhythm'] = {
 "title": "Your rhythm",
 "line": "A rule starts with a rhythm. Here is the one Rose Window is built around; keep what helps.",
 "items": [
  {"when": "Every morning · 7 minutes", "what": "Today's story", "how": "Before your phone, or with your first coffee. Read, look, take one question into the day.", "go": "today"},
  {"when": "Three times a week · 30 minutes", "what": "A journey session", "how": "At lunch, on the train, or after the children are in bed. Walk the halls of Explore in order.", "go": "explore"},
  {"when": "Every week", "what": "One line by heart", "how": "Read it each morning; say it from memory by Sunday.", "go": "byheart"},
  {"when": "Every night · 2 minutes", "what": "A night prayer", "how": "Alone or with your family: the Lord's Prayer, or the short prayers in By heart.", "go": "byheart"},
  {"when": "Once a season", "what": "Hear, see or go", "how": "One of the great works: Evensong, a painting, a cathedral.", "go": "great"}
 ]}

json.dump(k, open(K, 'w'), ensure_ascii=False, indent=1); open(K, 'a').write('\n')
json.dump(m, open(M, 'w'), ensure_ascii=False, indent=1); open(M, 'a').write('\n')
mm = {x['id']: x for x in m}
for w in k['words']['items']:
    x = mm.get(w['mem']); assert x, w['mem']
    joined = ' '.join(x['lines']).replace('\xa0', ' ')
    assert w['line'] in joined, (w['mem'], w['line'])
print('ok')
