"""Extract the set texts for In the beginning from the Gutenberg files in .cache/books (see tools/journeys/README.md)."""
import re, json, os
B = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '.cache', 'books')
def read(p, enc='utf-8'): return open(os.path.join(B, p), encoding=enc, errors='strict' if enc != 'utf-8' else 'ignore').read()
def lines_between(t, start, end):
    i = t.index(start); j = t.index(end, i) + len(end); return t[i:j]
def verse_lines(block):
    """Numbered verse lines (Budge's translations): drop footnotes and illustrations, join wrapped lines."""
    block = re.sub(r'\[(Footnote|Illustration)[^\]]*\]\]?', '', block, flags=re.S)
    out = []
    for raw in block.split('\n'):
        s = raw.strip()
        if not s: continue
        if re.match(r'^\d+[O\d]*\.\s', s) or re.match(r'^\[.*\]$', s): out.append(s)
        elif out: out[-1] += ' ' + s
    return [re.sub(r'\[\d\]', '', x) for x in out if not re.match(r'^\[.*\]$', x)]
def blocks(t): return [re.sub(r'[ \t]+', ' ', b.strip()) for b in re.split(r'\n\s*\n', t) if b.strip()]
R = {}
# Enuma Elish, Budge (British Museum, 1921)
E = read('creation/9914.txt')
tab1 = E[E.index('FIRST TABLET.[1]'):]
R['ee1'] = ['\n'.join(verse_lines(lines_between(tab1, '1. When the heavens above', '9. The gods came into being in the midst of them.')))]
tab4 = E[E.index('FOURTH TABLET.'):]
R['ee4'] = ['\n'.join(verse_lines(lines_between(tab4, '128. He turned back to Tiamat', '140. He ordered them not to let her water escape.')))]
tab6 = E[E.index('SIXTH TABLET.'):]
R['ee6'] = ['\n'.join(verse_lines(lines_between(tab6, '1. On hearing the words of the gods', '6. "The service of the gods shall be established, and I will set them\n(i.e., the gods) free.'))),
            '\n'.join(verse_lines(lines_between(tab6, '23. "[It was] Kingu who created the strife,', '27. After Ea had fashioned man he ... laid service upon him.')))]
# Gilgamesh XI, Budge (1920); file is Latin-1
G = read('deluge/7096-8.txt', 'latin-1')
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
# Milton, Paradise Lost (1667/1674), Gutenberg #20
M = read('milton/20.txt')
def ml(a, b): return '\n'.join(l.strip() for l in lines_between(M, a, b).split('\n'))
R['milton'] = [ml('Of Mans First Disobedience, and the Fruit', 'And justifie the wayes of God to men.'),
               ml('So saying, her rash hand in evil hour', 'And knew not eating Death: Satiate at length,'),
               ml('O fairest of Creation, last and best', "Mine never shall be parted, bliss or woe.")]
# Hesiod, Works and Days, tr. Evelyn-White (1914)
H = read('hesiod/348.txt')
def hp(a, b): return re.sub(r'\s+', ' ', re.sub(r'\s*\[\d+\]', '', lines_between(H, a, b))).strip()
R['hesiod'] = [hp('(ll. 109-120) First of all', 'loved by the blessed gods.'), '…',
               hp('(ll. 140-155) But when earth had covered this generation also', 'left the bright light of the sun.'), '…',
               hp('(ll. 170-201) Thereafter, would that I were not', 'there will be no help against evil.')]
# Huxley, The Interpreters of Genesis and the Interpreters of Nature (1885)
X = read('huxley1/2630.txt')
xb = blocks(X)
def xp(start): b = next(b for b in xb if b.startswith(start)); return re.sub(r'\s+', ' ', re.sub(r' \[\d+\]', '', b))
R['huxley'] = [xp('For I can meet the statement'), xp('Now what I want to make clear is this'), xp('Either the geological record'),
               xp('The water-population of vertebrated animals'), '…',
               xp('The antagonism between science and religion'), '…',
               xp('"And what doth the Lord require'), xp('If any so-called religion'), xp('But what extent of knowledge'), '…',
               xp('The antagonism of science is not to religion')]
# Darwin, The Origin of Species, 6th edition (1872)
D = read('origin6/2009.txt'); db = blocks(D)
def dp(start): return re.sub(r'\s+', ' ', next(b for b in db if b.startswith(start)))
R['darwin'] = [dp('I see no good reasons why the views given in this volume'), '…', dp('Authors of the highest eminence'), dp('It is interesting to contemplate a tangled bank')]
for k, v in R.items(): print(k, [len(x.split()) for x in v])
json.dump(R, open(os.path.join(os.path.dirname(__file__), 'raw.json'), 'w'), ensure_ascii=False, indent=1)
