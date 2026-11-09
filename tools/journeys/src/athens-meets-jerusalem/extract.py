"""Extract the set texts for When Athens met Jerusalem.

Sources (fetched into .cache/texts/url/ by the texts workflow; HTML already turned into paragraphs separated by blank lines):
  amj-justin-1apol.txt, amj-justin-2apol.txt   Justin Martyr, First and Second Apology, tr. Marcus Dods and George Reith (ANF I, 1885), New Advent
  amj-tertullian-prescription.txt               Tertullian, Prescription against Heretics, tr. Peter Holmes (ANF III, 1885), New Advent
  amj-clement-stromata1.txt                     Clement of Alexandria, Stromata I, tr. William Wilson (ANF II, 1885), New Advent
  amj-origen-gregory.txt                        Origen, Letter to Gregory, tr. Frederick Crombie (ANF IV, 1885), New Advent
  amj-origen-celsus1.txt, amj-origen-celsus3.txt Origen, Against Celsus I and III, tr. Frederick Crombie (ANF IV, 1885), New Advent
  amj-basil-young-men.txt                       Basil, Address to Young Men, tr. F. M. Padelford (Yale Studies in English 15, 1902), tertullian.org
  amj-jerome-22.txt                             Jerome, Letter 22, tr. W. H. Fremantle and others (NPNF II.6, 1893), New Advent
  amj-julian-rescript.txt                       Julian, Letter 36 (Rescript on Christian Teachers), tr. Wilmer Cave Wright (Loeb, 1923), earlychurchtexts.com
  amj-philo-creation.txt                        Philo, On the Creation, tr. C. D. Yonge (1854-55), earlychristianwritings.com
and .cache/texts/45304.txt                      Augustine, The City of God VIII, tr. Marcus Dods (1871), Gutenberg #45304

Editorial changes, all recorded in notes.json: HTML entities decoded (&AElig; -> Æ, &aelig; -> æ); New Advent's inserted
Scripture references (e.g. '1 Timothy 4:1') removed; Padelford's footnote numbers and page markers ('|102') removed;
Yonge's editor's footnote '{1}{...}' removed; Dods's footnote numbers '[297]' and italic underscores removed.
No word of any translation is changed. Paragraphs are split on blank lines, never on line ends.
Run: python3 tools/journeys/src/athens-meets-jerusalem/extract.py
"""
import re, json, os, html
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
T = os.path.join(ROOT, '.cache', 'texts')
def read(p): return html.unescape(open(os.path.join(T, p), encoding='utf-8', errors='ignore').read().replace('\r', ''))
def blocks(t): return [re.sub(r'\s+', ' ', b).strip() for b in re.split(r'\n\s*\n', t) if b.strip()]
def para(bl, start):
    hits = [b for b in bl if b.startswith(start)]
    assert len(hits) == 1, (start, len(hits))
    return hits[0]
def cut(p, a=None, b=None):
    """The part of paragraph p from the words a (inclusive) to the words b (inclusive)."""
    i = p.index(a) if a else 0
    j = p.index(b, i) + len(b) if b else len(p)
    return p[i:j].strip()
def drop(p, *refs):
    """Remove New Advent's inserted Scripture references (each must be present)."""
    for r in refs:
        assert r in p, r
        p = p.replace(' ' + r + ' ', ' ').replace(' ' + r, '')
    return re.sub(r'\s+', ' ', p).strip()
R = {}

# Justin, First Apology 46; Second Apology 12 and 13 (Dods and Reith, ANF I)
J1 = blocks(read('url/amj-justin-1apol.txt')); J2 = blocks(read('url/amj-justin-2apol.txt'))
p12 = para(J2, 'For I myself, too, when I was delighting in the doctrines of Plato')
R['justin'] = [para(J1, 'But lest some should, without reason, and for the perversion of what we teach'),
               cut(p12, None, 'perceived that it was impossible that they could be living in wickedness and pleasure.'), '…',
               para(J2, 'For I myself, when I discovered the wicked disguise')]

# Tertullian, Prescription against Heretics 7, 9 (part) and 14 (part) (Holmes, ANF III)
TP = blocks(read('url/amj-tertullian-prescription.txt'))
t7 = drop(para(TP, 'These are the doctrines of men and of demons'), '1 Timothy 4:1', '1 Timothy 1:4', 'Titus 3:9', '2 Timothy 2:17', 'Wisdom 1:1')
t9 = para(TP, 'I now purposely relinquish this ground of argument.')
t14 = drop(para(TP, 'So long, however, as its form exists in its proper order'), 'Luke 18:42', 'Matthew 15:14')
R['tertullian'] = [cut(t7, None, 'and really treating of nothing!'), cut(t7, 'Whence spring those fables'),
                   '…', cut(t9, 'But at the outset I lay down', 'that nothing else is to be believed, and therefore nothing else is to be sought, after you have found and believed what has been taught by Him who charges you to seek no other thing than that which He has taught.'),
                   '…', cut(t14, None, 'To know nothing in opposition to the rule (of faith), is to know all things.')]

# Clement, Stromata I.5 (Wilson, ANF II)
CS = blocks(read('url/amj-clement-stromata1.txt'))
c1 = drop(para(CS, 'Accordingly, before the advent of the Lord, philosophy was necessary'), 'Proverbs 3:23', 'Galatians 3:24')
c2 = drop(para(CS, 'Now, says Solomon, defend wisdom'), 'Proverbs 4:8-9', 'Proverbs 4:18')
c3 = para(CS, 'Jerusalem, Jerusalem, how often would I have gathered')
c4 = drop(para(CS, 'You may have also another image of what has been said, in Thamar'), 'Genesis 16:6', 'Proverbs 3:11-12; Hebrews 12:5-6', 'John 14:6')
R['clement'] = [c1, cut(c2, None, 'streams flow from all sides.'), '…',
                cut(c3, 'For what was bestowed on each generation advantageously', 'if cultivated for the honour and knowledge of God.'), '…',
                cut(c4, 'Wherefore also, when Sarah was jealous at Hagar', 'but your knowledge I honour and reverence as true wife.'),
                cut(c4, 'We merely therefore assert here')]

# Origen, Letter to Gregory 1-3 (Crombie, ANF IV): the whole letter
OG = blocks(read('url/amj-origen-gregory.txt'))
R['gregory'] = [para(OG, '1. Greeting in God'), para(OG, '2. Perhaps something of this kind'), para(OG, '3. Do you then, my son')]

# Basil, Address to Young Men I-IV and V (part) (Padelford 1902). Footnote numbers and page markers removed.
B = read('url/amj-basil-young-men.txt')
B = B[B.index('ADDRESS TO YOUNG MEN ON THE RIGHT USE OF GREEK LITERATURE\n\nI.'):]
def basil(p):
    p = re.sub(r'\s*\|\d+\s*', ' ', p)                       # page markers |102
    p = re.sub(r"(?<=[A-Za-z,.;:?'’—])(\d+)(?=[\s,.;:]|$)", '', p)  # footnote numbers glued to a word or stop
    p = re.sub(r"(?<=['’.,;:]) (\d+)(?=\s|$)", '', p)        # footnote numbers after a closing quote
    p = re.sub(r' (\d+)(?= )', '', p)                        # footnote numbers after a name ('Solon 19 had')
    return re.sub(r'\s+', ' ', p).strip()
BB = [basil(b) for b in blocks(B)]
R['basil'] = [para(BB, 'I. Many considerations, young men'), para(BB, 'Do not be surprised if to you'),
              para(BB, 'II. We Christians, young men'), '…',
              para(BB, 'Into the life eternal the Holy Scriptures lead us'),
              para(BB, 'III. If, then, there is any affinity'),
              para(BB, 'IV. Perhaps it is sufficiently demonstrated'), '…',
              cut(para(BB, 'X. To be sure, we shall become more intimately acquainted'), None, 'to gain accessions on every hand.')]

# Jerome, Letter 22.30 (NPNF II.6)
JE = blocks(read('url/amj-jerome-22.txt'))
R['jerome'] = [drop(para(JE, '30. Many years ago'), 'Matthew 6:21')]

# Origen, Against Celsus I.9-10 and III.44, III.55 (Crombie, ANF IV)
C1 = blocks(read('url/amj-origen-celsus1.txt')); C3 = blocks(read('url/amj-origen-celsus3.txt'))
o19 = para(C1, 'He next proceeds to recommend, that in adopting opinions')
R['celsus'] = [o19, cut(para(C1, 'In the next place, since our opponents keep repeating'), None, 'or an Epicurean, or a follower of some other school, and is thus borne, although they will not admit it, by a kind of irrational impulse to the practice, say of Stoicism, to the disregard of the others;'),
               '…', cut(para(C1, 'Since, then, as reason teaches, we must repose faith'), None, 'to believe God rather than them?'),
               para(C3, 'After these points Celsus quotes some objections'),
               para(C3, 'But as Celsus delights to heap up calumnies against us')]

# Julian, Letter 36, Rescript on Christian Teachers (Wright, Loeb 1923). The site prints a stray 'available at Amazoncoming soon...' before it.
JU = blocks(read('url/amj-julian-rescript.txt'))
j1 = next(b for b in JU if 'I hold that a proper education results' in b)
j1 = j1[j1.index('I hold that a proper education results'):]
R['julian'] = [j1, para(JU, 'For religious and secular teachers let there be a general ordinance')]

# Philo, On the Creation I-II and IV-VI (Yonge). Section numbers in brackets are kept as printed on the page.
P = read('url/amj-philo-creation.txt')
P = re.sub(r'\s*\{1\}\{this is in accordance with the description of him in the Bible, where he is represented as being learned in all the wisdom of the Egyptians\.\}', '', P)
PB = blocks(P)
ph2 = para(PB, 'II. (7) For some men, admiring the world itself')
R['philo'] = [para(PB, 'I. (1) Of other lawgivers'), cut(ph2, None, 'by whom everything must be managed and governed.'), '…',
              para(PB, 'IV. We must mention as much as we can'), para(PB, 'V. (20) As therefore the city'), para(PB, 'VI. (23) And God, not being urged on')]

# Augustine, The City of God VIII.9-11 (Dods 1871), Gutenberg #45304
A = read('45304.txt')
a8 = A[A.index('BOOK EIGHTH.'):]
a8 = a8[a8.index('9. _Concerning that philosophy which has come nearest'):a8.index('12. _That even the Platonists')]
a8 = re.sub(r'\[\d+\]', '', a8).replace('_', '')
AB = blocks(a8)
a10 = para(AB, 'For although a Christian man instructed only in ecclesiastical')
R['augustine'] = [para(AB, 'Whatever philosophers, therefore, thought concerning the supreme God'),
                  cut(a10, None, 'He knows well, too, to be on his guard against even these philosophers in their errors.'),
                  '…', cut(a10, 'With respect, however, to that wherein they agree with us', 'whether Platonists or others, agree with us.'),
                  cut(para(AB, 'Certain partakers with us in the grace of Christ'), None, 'by means of conversation.')]

for k, v in R.items(): print(k, [len(x.split()) for x in v])
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
