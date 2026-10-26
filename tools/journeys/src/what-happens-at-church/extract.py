"""Extract the set texts for What happens at church from the fetched files in .cache/texts.

Run: python3 tools/journeys/src/what-happens-at-church/extract.py

Sources and what is done to them (no word is changed; every removal is listed here and in notes.json):
- Justin Martyr, First Apology 61, 65-67, tr. Marcus Dods and George Reith, ANF I (1885), via New Advent
  (url/what-happens-at-church-justin-1apol.txt). New Advent's inserted Scripture references
  ('John 3:5', 'Luke 22:19') are removed. ANF's own bracketed glosses ('[illuminated]', '[the Eucharist]') are kept.
- Didache 7 and 14, tr. J. B. Lightfoot, ed. J. R. Harmer (1891), via earlychristianwritings.com
  (url/didache-lightfoot.txt): the site's verse numbers and the curly braces it puts round Scripture quotations
  are removed, exactly as first-christians does.
- Cyril of Jerusalem, Mystagogical Lectures 1-2 (Catechetical Lectures 19-20), tr. E. H. Gifford, NPNF II.7 (1894),
  via New Advent: inserted Scripture references removed; the stray space New Advent leaves before punctuation where a
  link was is closed up.
- Ambrose, On the Mysteries 8-9, tr. H. de Romestin, E. de Romestin and H. T. F. Duckworth, NPNF II.10 (1896),
  via New Advent: inserted Scripture references removed.
- Robert Barclay, An Apology for the True Christian Divinity (English 1678), Proposition XI, Gutenberg #56487
  (the 'eighth edition in English'): the printer's sidenotes '[Sidenote: ...]', footnote markers '[97]' and the
  underscores marking italics are removed.
- Martin Luther, A Treatise on Good Works (1520), tr. J. M. Reu, Gutenberg #418.
- The Book of Common Prayer (1662), Morning Prayer, from url/guilt-bcp-morning.txt (an Andrews University
  transcription of a twentieth-century printing). The page drops the large initial letter of some prayers
  ('LMIGHTY', 'HE grace'); it is restored ('ALMIGHTY', 'THE grace'). The reference line '2 Corinthians xiii.' is
  removed from the Grace.
"""
import re, json, os, html
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(HERE, '..', '..', '..', '..', '.cache', 'texts')
def read(p): return open(os.path.join(T, p), encoding='utf-8', errors='replace').read().replace('\r', '')
def blocks(t): return [re.sub(r'\s+', ' ', html.unescape(b)).strip() for b in re.split(r'\n\s*\n', t) if b.strip()]
def one(bl, start):
    hits = [b for b in bl if b.startswith(start)]
    assert len(hits) == 1, (start, len(hits))
    return hits[0]
def drop(p, *refs):
    """Remove New Advent's inserted Scripture references, each of which must be present exactly once."""
    for r in refs:
        assert p.count(r) == 1, (r, p[:60])
        p = p.replace(r, '')
    return re.sub(r'\s+([,.;:?!])', r'\1', re.sub(r'\s+', ' ', p)).strip()
def cut(p, a=None, b=None):
    """A verbatim stretch of one paragraph, from the words a to the end of the words b."""
    i = p.index(a) if a else 0
    j = p.index(b, i) + len(b) if b else len(p)
    return p[i:j]
R = {}

# Justin Martyr, First Apology (about AD 155)
J = blocks(read('url/what-happens-at-church-justin-1apol.txt'))
j61a = one(J, 'I will also relate the manner in which we dedicated ourselves')
j61b = one(J, 'And for this [rite] we have learned from the apostles this reason.')
R['justin61'] = [drop(cut(j61a, None, 'you shall not enter into the kingdom of heaven. John 3:5'), ' John 3:5'), '…', j61b]
R['justin65'] = [one(J, 'But we, after we have thus washed him who has been convinced')]
R['justin66'] = [drop(one(J, 'And this food is called among us'), ' Luke 22:19')]
R['justin67'] = [one(J, 'And we afterwards continually remind each other of these things.')]

# The Didache (late first or early second century), tr. Lightfoot
D = blocks(read('url/didache-lightfoot.txt'))
def did(n):
    b = next(x for x in D if x.startswith(f'{n}:1 '))
    b = re.sub(r'(^|\s)\d+:\d+\s', r'\1', b)
    b = b.replace('{', '').replace('}', '')
    return re.sub(r'\s+', ' ', b).strip()
R['didache7'] = [did(7)]
R['didache14'] = [did(14)]

# Cyril of Jerusalem, Mystagogical Lectures (about 350; some scholars credit his successor John)
C1 = blocks(read('url/what-happens-at-church-cyril-myst-1.txt'))
C2 = blocks(read('url/what-happens-at-church-cyril-myst-2.txt'))
R['cyril1'] = [drop(one(C1, '4. But nevertheless you are bidden to say'), ' Hebrews 2:14-15'),
               '…',
               drop(one(C1, '9. When therefore you renounce Satan'), ' Isaiah 28:15')]
R['cyril2'] = [drop(one(C2, '2. As soon, then, as you entered'), ' Colossians 3:9', ' Ephesians 4:22', ' Song of Songs 5:3'),
               drop(one(C2, '3. Then, when you were stripped')),
               drop(one(C2, '4. After these things, you were led'), ' Ecclesiastes 3:2'),
               drop(one(C2, '5. O strange and inconceivable thing!'))]

# Ambrose, On the Mysteries (about 390)
A = blocks(read('url/what-happens-at-church-ambrose-mysteries.txt'))
R['ambrose'] = [drop(one(A, '47. We have proved the sacraments')),
                drop(one(A, '48. Now consider whether the bread of angels')),
                '…',
                drop(one(A, '50. Perhaps you will say')),
                '…',
                drop(one(A, '52. We observe, then, that grace has more power')),
                drop(one(A, '53. But why make use of arguments?')),
                drop(one(A, '54. The Lord Jesus Himself proclaims'), ' Matthew 26:26')]

# Robert Barclay, Apology, Proposition XI (1678)
BT = read('56487.txt')
BT = BT[BT.index('\nPROPOSITION XI.\n'):BT.index('\nPROPOSITION XII.\n')]
def bclean(s):
    s = re.sub(r'\[Sidenote:[^\]]*\]', ' ', s)
    s = re.sub(r'\[\d+\]', '', s)
    s = s.replace('_', '')
    return re.sub(r'\s+([,.;:?!])', r'\1', re.sub(r'\s+', ' ', s)).strip()
BB = [bclean(b) for b in re.split(r'\n\s*\n', BT) if b.strip()]
b3 = one(BB, '§. III. Secondly, Albeit I say')
b3b = one(BB, 'But the Limitation we condemn is')
b7 = next(b for b in BB if 'when I came into the silent Assemblies' in b)
b27 = one(BB, '§. XXVII. But Lastly')
R['barclay'] = [b3, b3b, '…', cut(b7, 'I myself, in Part, am a true Witness', 'they could add nothing to us.'), '…', b27]

# Luther, A Treatise on Good Works (1520), tr. Reu
L = blocks(read('418.txt'))
R['luther_formal'] = [one(L, 'The first works of this Commandment are plain and outward')]
R['luther_mass'] = [one(L, 'II. In the mass it is necessary that we attend with our a hearts also'),
                    one(L, 'Here there is need that a man practise the first works')]

# The Book of Common Prayer (1662), Morning Prayer
M = blocks(read('url/guilt-bcp-morning.txt'))
mp = lambda s: one(M, s)
R['bcp_open'] = [mp('Then likewise he shall say, O Lord, open thou our lips.'), mp('Answer. And our mouth shall show forth thy praise.'),
                 mp('Priest. O God, make speed to save us.'), mp('Answer. O Lord, make haste to help us.'),
                 mp('Here all standing up, the Priest shall say, Glory be to the Father'), mp('Answer. As it was in the beginning, is now, and ever shall be, world without end. Amen.'),
                 mp('Priest. Praise ye the Lord.'), mp("Answer. The Lord's Name be praised."),
                 cut(mp('Then shall be said or sung this Psalm following'), None, 'and the sheep of his hand.')]
R['bcp_lessons'] = [mp('Then shall be read distinctly with an audible voice the First Lesson'),
                    mp('Note, That before every Lesson the Minister shall say'),
                    mp("Then shall be sung or said the Apostle's Creed")]
R['bcp_end'] = [mp('A Prayer of St. Chrysostom. LMIGHTY God').replace('LMIGHTY God', 'ALMIGHTY God', 1),
                mp('2 Corinthians xiii. HE grace').replace('2 Corinthians xiii. HE grace', 'THE grace', 1)]

for k, v in R.items(): print(k, [len(x.split()) for x in v])
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
