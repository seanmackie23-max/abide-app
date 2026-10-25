"""Extract the set texts for In the beginning (rewrite, October 2026).

Sources: the Gutenberg files in .cache/books (Milton, Hesiod, Gilgamesh, Huxley, Darwin, as in the first version, kept in _old/)
and .cache/texts/3296.txt (Augustine, Confessions, tr. E. B. Pusey). Paragraphs are split on blank lines, never on line ends.
Run: python3 tools/journeys/src/in-the-beginning/extract.py
"""
import re, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
B = os.path.join(ROOT, '.cache', 'books'); T = os.path.join(ROOT, '.cache', 'texts')
def read(p, enc='utf-8'): return open(p, encoding=enc, errors='ignore').read()
def lines_between(t, start, end):
    i = t.index(start); j = t.index(end, i) + len(end); return t[i:j]
def blocks(t): return [re.sub(r'\s+', ' ', b.strip()) for b in re.split(r'\n\s*\n', t) if b.strip()]
R = {}

# Augustine, Confessions, tr. E. B. Pusey (1838), Gutenberg #3296. Pusey's text has no chapter numbers;
# the chapters are identified by their opening words against the standard division (see notes.json).
A = read(os.path.join(T, '3296.txt'))
b11 = blocks(A[A.index('\nBOOK XI\n'):A.index('\nBOOK XII\n')])
b12 = blocks(A[A.index('\nBOOK XII\n'):A.index('\nBOOK XIII\n')])
def ap(bl, start):
    hits = [b for b in bl if b.startswith(start)]
    assert len(hits) == 1, start
    return hits[0]
R['aug12'] = [ap(b12, 'The lowliness of my tongue confesseth'),          # XII.2
              ap(b12, 'And now this earth was invisible and without form'),  # XII.3
              ap(b12, 'How then should it be called'),                     # XII.4
              ap(b12, 'So that when thought seeketh'),                     # XII.5
              '…',                                                         # XII.6 left out (Augustine's long account of failing to imagine formless matter)
              ap(b12, 'But whence had it this degree of being'),           # XII.7
              ap(b12, 'But that heaven of heavens was for Thyself')]       # XII.8
R['aug11'] = [ap(b11, 'But how didst Thou speak?'),                        # XI.6
              '…',                                                         # XI.7 left out
              ap(b11, 'Why, I beseech Thee, O Lord my God?'),              # XI.8
              ap(b11, 'In this Beginning, O God, hast Thou made heaven and earth')]  # XI.9

# Milton, Paradise Lost, Gutenberg #20 (the 1667 text in ten books: the 1674 Book IX is its Book VIII).
# Line numbers follow the standard twelve-book numbering; counted by script (see notes.json).
M = read(os.path.join(B, 'milton', '20.txt'))
def ml(a, b): return '\n'.join(l.strip() for l in lines_between(M, a, b).split('\n') if l.strip())
R['milton'] = [ml('Of Mans First Disobedience, and the Fruit', 'And justifie the wayes of God to men.'),
               ml('So saying, her rash hand in evil hour', 'And knew not eating Death: Satiate at length,'),
               ml('Soon as the force of that fallacious Fruit,', 'At length gave utterance to these words constraind.'),
               ml('O EVE, in evil hour thou didst give care', 'There sit not, and reproach us as unclean.')]

# Hesiod, Works and Days, tr. Evelyn-White (1914), Gutenberg #348 (kept from the first version)
H = read(os.path.join(B, 'hesiod', '348.txt'))
def hp(a, b): return re.sub(r'\s+', ' ', re.sub(r'\s*\[\d+\]', '', lines_between(H, a, b))).strip()
R['hesiod'] = [hp('(ll. 109-120) First of all', 'loved by the blessed gods.'), '…',
               hp('(ll. 140-155) But when earth had covered this generation also', 'left the bright light of the sun.'), '…',
               hp('(ll. 170-201) Thereafter, would that I were not', 'there will be no help against evil.')]

# Gilgamesh XI, Budge (1920), Gutenberg #7096; the file is Latin-1 (kept from the first version)
G = read(os.path.join(B, 'deluge', '7096-8.txt'), 'latin-1')
def gl(a, b):
    blk = lines_between(G, a, b)
    blk = re.sub(r'\n\[[^\]]+\]\n', '\n', blk)        # editorial headings
    blk = re.sub(r' \[\d+\]', '', blk)                 # footnote numbers
    ls = []
    for raw in blk.split('\n'):
        s = raw.strip()
        if not s: continue
        if re.match(r'^\d+[O\d]*\.\s', s): ls.append(s)
        elif ls: ls[-1] += ' ' + s
    return '\n'.join(ls)
R['gil'] = [gl('8. Uta-Napishtim said unto him, to Gilgamish:', '31. ... the ocean, provide it with a roof."'),
            gl('97. As soon as the gleam of dawn shone in the sky', '124. That they might fill the sea like little fishes?"'),
            gl('125. The gods of the Anunnaki wailed with her.', '162. The gods gathered together like flies over him that sacrificed.')]

# Huxley, 'The Interpreters of Genesis and the Interpreters of Nature' (1885), Gutenberg #2630 (kept)
xb = blocks(read(os.path.join(B, 'huxley1', '2630.txt')))
def xp(start): b = next(b for b in xb if b.startswith(start)); return re.sub(r'\s+', ' ', re.sub(r' \[\d+\]', '', b))
R['huxley'] = [xp('For I can meet the statement'), xp('Now what I want to make clear is this'), xp('Either the geological record'),
               xp('The water-population of vertebrated animals'), '…',
               xp('The antagonism between science and religion'), '…',
               xp('"And what doth the Lord require'), xp('If any so-called religion'), xp('But what extent of knowledge'), '…',
               xp('The antagonism of science is not to religion')]

# Darwin, The Origin of Species, 6th edition (1872), Gutenberg #2009 (kept)
db = blocks(read(os.path.join(B, 'origin6', '2009.txt')))
def dp(start): return re.sub(r'\s+', ' ', next(b for b in db if b.startswith(start)))
R['darwin'] = [dp('I see no good reasons why the views given in this volume'), '…', dp('Authors of the highest eminence'), dp('It is interesting to contemplate a tangled bank')]

for k, v in R.items(): print(k, [len(x.split()) for x in v])
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
