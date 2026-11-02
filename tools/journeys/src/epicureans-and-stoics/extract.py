"""Extract the set texts for Epicureans and Stoics.

All quotations are copied by this script from the cached files in .cache/texts (never retyped).
Paragraphs are split on blank lines, never on line ends. Footnote markers and editorial insertions
removed here are listed in notes.json. Run: python3 tools/journeys/src/epicureans-and-stoics/extract.py

Sources
- Diogenes Laertius X (Epicurus), tr. R. D. Hicks (Loeb, 1925; Hicks d. 1929): Wikisource page,
  .cache/texts/url/epicureans-and-stoics-epicurus-hicks.txt
- Cicero, Tusculan Disputations III, tr. C. D. Yonge (1853; d. 1891): Gutenberg #14988
- Lucretius, On the Nature of Things I, tr. W. E. Leonard (1916; d. 1944): Gutenberg #785
- Epictetus, Discourses (selection) and Encheiridion, tr. George Long (1877; d. 1879): Gutenberg #10661
- Diogenes Laertius VII (Zeno and the Stoics), tr. C. D. Yonge (1853): Gutenberg #57342
- Augustine, City of God VI.10 (tr. J. J. Smith) and IX.4 (tr. Marcus Dods), Dods edition 1871: Gutenberg #45304
- Augustine, City of God XIV.9, tr. Marcus Dods (1871; d. 1909): New Advent,
  .cache/texts/url/epicureans-and-stoics-city-of-god-14.txt
- Marcus Aurelius, Meditations, tr. George Long (1862): Gutenberg #15877
"""
import re, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
T = os.path.join(ROOT, '.cache', 'texts')
def read(p): return open(os.path.join(T, p), encoding='utf-8', errors='ignore').read().replace('\r', '')
def blocks(t): return [re.sub(r'\s+', ' ', b).strip() for b in re.split(r'\n\s*\n', t) if b.strip()]
def one(bl, start):
    hits = [b for b in bl if b.startswith(start)]
    assert len(hits) == 1, (start, len(hits))
    return hits[0]
def cut(s, a, b=None):
    """The part of paragraph s from the words a up to and including the words b."""
    i = s.index(a); j = (s.index(b, i) + len(b)) if b else len(s)
    return s[i:j]
R = {}

# --- Epicurus (Hicks). Footnote markers like [132] are removed.
H = blocks(read('url/epicureans-and-stoics-epicurus-hicks.txt'))
fn = lambda s: re.sub(r'\[\d+\]', '', s).replace('  ', ' ').strip()
men = [one(H, '“Epicurus to Menoeceus, greeting.'), one(H, '122. “Let no one be slow'), one(H, '123. “Those things which without ceasing'),
       one(H, '“Accustom thyself to believe that death is nothing to us'), one(H, '“We must remember that the future'),
       one(H, '“We must also reflect that of desires'), one(H, '“When we say, then, that pleasure is the end'),
       one(H, '133. “Who, then, is superior'), one(H, '“Exercise thyself in these and kindred precepts')]
R['menoeceus'] = [fn(x) for x in men]
g = one(H, '9. But these people are stark mad.')
R['garden'] = [fn(cut(g, 'Friends indeed came to him from all parts', 'Such was the man who laid down that pleasure was the end of life.')),
               fn(one(H, '“On this blissful day, which is also the last of my life'))]
R['pd'] = [fn(one(H, '1. 139. A blessed and eternal being')), fn(one(H, '2. Death is nothing to us')), fn(one(H, '3. The magnitude of pleasure')),
           fn(one(H, '4. 140. Continuous pain')), fn(one(H, '5. It is impossible to live a pleasant life'))]
R['pd27'] = [fn(one(H, '27. Of all the means which are procured by wisdom'))]

# --- Cicero, Tusculan Disputations III.17-20 (Yonge). Yonge's chapter numerals (XVIII., XX.) are removed.
C = blocks(read('14988.txt'))
c17 = one(C, 'XVII. Should Pythagoras, Socrates, or Plato say to me')
c18 = one(C, 'XVIII. You have here a representation of a happy life')
c18b = one(C, 'Now, should any one, as the same author says, find his spirits sink')
c20 = one(C, 'XX. It may be said, What! do you imagine Epicurus really meant this')
R['cicero'] = [cut(c17, 'But you are for bringing my thoughts over to pleasure.'),
               cut(c18b, 'Why, Epicurus, do we use any evasions', 'with which Epicurus was acquainted.'),
               '…',
               re.sub(r'^XX\. ', '', cut(c20, 'XX. It may be said', 'he has separated the chief good from virtue.')),
               cut(c20, 'Epicurus denies that any one can live pleasantly who does not lead a life of virtue', 'but they are not consistent with pleasure.')]

# --- Lucretius I.62-158 (Leonard). Verse: keep the line breaks inside each verse paragraph.
L = read('785.txt')
def verse(a, b):
    i = L.index(a); j = L.index(b, i) + len(b)
    out = []
    for para in re.split(r'\n\s*\n', L[i:j]):
        ls = [l.strip() for l in para.split('\n') if l.strip()]
        if ls: out.append('\n'.join(ls))
    return out
R['lucretius'] = (verse('Whilst human kind', 'And us his victory now exalts to heaven.')
                  + ['…']
                  + verse('I fear perhaps thou deemest that we fare', 'Dead men whose bones earth bosomed long ago.')
                  + verse('This terror, then, this darkness of the mind,', 'And how accomplished by no tool of Gods.'))

# --- Epictetus (Long). '([Greek: ...])' transliterations of Long's Greek words are removed.
E = read('10661.txt')
gr = lambda s: re.sub(r'\s*\[Greek: [^\]]*\]', '', re.sub(r'\s*\(\[Greek: [^\]]*\]\)', '', s))
D = blocks(E[E.index('A SELECTION FROM THE DISCOURSES OF EPICTETUS.\n\n\nOF THE THINGS'):E.rindex('THE ENCHEIRIDION, OR MANUAL.')])
d1 = one(D, 'OF THE THINGS WHICH ARE IN OUR POWER AND NOT IN OUR POWER.')
d3 = one(D, 'HOW A MAN SHOULD PROCEED FROM THE PRINCIPLE OF GOD BEING THE FATHER')
d6 = one(D, 'OF PROVIDENCE.—From everything')
R['discourses'] = [d1, one(D, 'What then should a man have in readiness in such circumstances?'), one(D, 'What then did Agrippinus say?'),
                   d3, one(D, 'Through this kinship with the flesh'),
                   d6, one(D, 'What, then, are these things done in us only?'), '…',
                   one(D, 'Come, then, do you also having observed these things')]
R['discourses'] = [gr(x) for x in R['discourses']]
EN = blocks(E[E.rindex('THE ENCHEIRIDION, OR MANUAL.'):])
def ench(n):
    i = EN.index(n + '.'); out = []
    for b in EN[i + 1:]:
        if re.fullmatch(r'[IVXL]+\.', b): break
        out.append(gr(b))
    return out
R['ench'] = ench('I') + ench('II') + ench('III') + ench('IV') + ench('V')
R['ench_n'] = [len(ench(x)) for x in ('I', 'II', 'III', 'IV', 'V')]

# --- Diogenes Laertius VII (Yonge). Yonge's section numerals (VI., LIII. ...) and footnote markers are removed.
Y = blocks(read('57342.txt'))
yn = lambda s: re.sub(r'\[\d+\]', '', re.sub(r'^[IVXL]+\. ', '', s))
R['dl7'] = [yn(one(Y, 'VI. And he used to walk up and down in the beautiful colonnade')),
            yn(cut(one(Y, 'VII. Accordingly, for the future, men came thither to hear him'), 'VII. Accordingly', 'but now Zeno’s pupils made the name more notorious.')),
            '…',
            yn(one(Y, 'LIII. On which account Zeno was the first writer')),
            '…',
            yn(cut(one(Y, 'LX. But it seems that all goods are equal'), 'Moreover, they divide all existing things', 'though perhaps a little more near to one species than to the other.')),
            yn(one(Y, 'For, as it is the property of the hot to warm')),
            '…',
            yn(one(Y, 'LXXII. They also say that God is an animal immortal')),
            '…',
            yn(cut(one(Y, 'LXXIV. But Chrysippus, in his treatise on Fate'), 'LXXIV.'))]

# --- Augustine, City of God (Dods edition, 1871; Book VI by J. J. Smith, Book IX by Dods).
A = blocks(read('45304.txt'))
a10 = one(A, 'That liberty, in truth, which this man wanted')
a10b = one(A, 'This liberty Varro did not enjoy.')
R['cog6'] = [fn(cut(a10, 'That liberty, in truth', 'they would be held to be monsters."')),
             '…',
             fn(cut(a10, 'But with what freedom he has written concerning the rites themselves', 'when propitious? But gods who wish to be worshipped in this fashion should be worshipped in none.')),
             '…',
             fn(cut(a10b, 'Whence, with respect to these sacred rites of the civil theology', 'but not as being pleasing to the gods."')),
             '…',
             fn(cut(a10b, 'But this man, whom philosophy had made, as it were, free'))]
a94 = one(A, 'Among the philosophers there are two opinions about these mental emotions')
R['cog9'] = [fn(cut(a94, 'Aulus Gellius, a man of extensive erudition', 'which it ought rationally to desire or avoid.'))]

# New Advent prints Scripture references inline as links ('Romans 8:23', '1 John 1:8'): they are not Dods's words, so they are removed.
N = blocks(read('url/epicureans-and-stoics-city-of-god-14.txt'))
BOOKS = r'(?:[123] )?(?:Genesis|Exodus|Psalm|Psalms|Proverbs|Ecclesiastes|Isaiah|Sirach|Matthew|Mark|Luke|John|Acts|Romans|Corinthians|Galatians|Philippians|Timothy|James|Hebrews)'
nr = lambda s: re.sub(r'\s*\b' + BOOKS + r' \d+:[\dl]+(?:-\d+)?(?=[\s;,.)]|$)', '', s).replace(' ;', ';').replace(' ,', ',')
R['cog14'] = [nr(one(N, 'If these emotions and affections, arising as they do from the love of what is good')),
              nr(one(N, 'But we must further make the admission')),
              '…',
              nr(cut(one(N, 'And since this is so — since we must live a good life'), 'And if some, with a vanity monstrous'))]

# --- Marcus Aurelius, Meditations (Long). Footnote markers [A] and the footnote blocks are removed.
M = read('15877.txt')
mb = [b for b in blocks(M) if not b.startswith('[A]') and not b.startswith('[B]')]
mf = lambda s: re.sub(r'\[[A-D]\]', '', s).replace(' .', '.').strip()
R['marcus'] = [mf(one(mb, 'Begin the morning by saying to thyself')),
               mf(one(mb, '3. Men seek retreats for themselves')), mf(one(mb, 'This then remains: Remember to retire into this little territory')),
               mf(one(mb, '13. When we have meat before us')),
               mf(one(mb, '40. Either the gods have no power or they have power.')),
               mf(one(mb, '33. To look for the fig in winter')), mf(one(mb, '34. When a man kisses his child, said Epictetus'))]

for k, v in R.items():
    if k != 'ench_n': print(k, [len(x.split()) for x in v])
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
