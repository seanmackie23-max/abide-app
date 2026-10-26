"""Extract the set texts for Homer and the heroes.

Sources (all in .cache/texts, headers checked):
  2199.txt  Homer, The Iliad, tr. Samuel Butler (1898; Butler d. 1902)
  1727.txt  Homer, The Odyssey, tr. Samuel Butler (1900; 2nd ed. 1922 from his notes)
  1497.txt  Plato, The Republic, tr. Benjamin Jowett (1871; 3rd ed. 1888; Jowett d. 1893)
  3296.txt  Augustine, Confessions, tr. E. B. Pusey (1838; Pusey d. 1882)
Butler's prose has no line numbers: the Greek line ranges in the refs were matched to his paragraphs by
their content (see notes.json). Paragraphs are split on blank lines, never on line ends. Butler's Odyssey
prints footnote numbers glued to the word before ('land.112'); they are removed here and listed in notes.json.
Run: python3 tools/journeys/src/homer/extract.py
"""
import re, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
T = os.path.join(ROOT, '.cache', 'texts')

def read(n):
    t = open(os.path.join(T, f'{n}.txt'), encoding='utf-8').read()
    return t[t.index('*** START'):t.index('*** END')]

def blocks(t): return [re.sub(r'\s+', ' ', b.strip()) for b in re.split(r'\n\s*\n', t) if b.strip()]

def books(t):
    ms = list(re.finditer(r'^BOOK ([IVXL]+)\.?\s*$', t, re.M))
    return {m.group(1): blocks(t[m.end():(ms[k + 1].start() if k + 1 < len(ms) else len(t))]) for k, m in enumerate(ms)}

FOOT = []
def unfoot(p, where):
    """Remove Butler's footnote numbers, which are glued to the preceding word or punctuation."""
    out = re.sub(r'(?<=[A-Za-z\.,;:!?’”—])(\d{1,3})(?=[\s\.,;:!?’”—]|$)', lambda m: FOOT.append((where, m.group(1), p[max(0, m.start() - 25):m.start()])) or '', p)
    # one marker in Odyssey V stands alone between spaces ('flowed. 51 Even')
    out = re.sub(r'(?<=[\.;:]) (\d{1,3}) (?=[A-Z])', lambda m: FOOT.append((where, m.group(1), out[max(0, m.start() - 25):m.start()])) or ' ', out)
    return out

def pick(bl, idxs, where, starts):
    out = []
    for i in idxs:
        if i == '…': out.append('…'); continue
        out.append(unfoot(bl[i], where))
    # guard: each picked paragraph must begin as expected, so a changed file cannot shift the text silently
    got = [p[:len(s)] for p, s in zip([x for x in out if x != '…'], starts)]
    assert got == starts, (where, got, starts)
    return out

IL = books(read(2199)); OD = books(read(1727))
R = {}

# Iliad I.1–52 (the proem, Chryses, the plague) and I.101–244 (the quarrel, to Achilles' oath)
R['il1'] = pick(IL['I'], [1, 2, 3, 4, 5, 6, '…', 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], 'Iliad I',
    ['Sing, O goddess', 'And which of the gods', '“Sons of Atreus,”', 'On this the rest', 'The old man feared', 'Thus did he pray',
     'With these words he sat down, and Agamemnon', 'And Achilles answered, “Most noble', 'Then Agamemnon said', 'Achilles scowled',
     'And Agamemnon answered, “Fly', 'The son of Peleus was furious', 'And Minerva said', '“Goddess,” answered', 'He stayed his hand',
     'But the son of Peleus again'])
# Odyssey I.1–10 (the proem)
R['od1'] = pick(OD['I'], [1], 'Odyssey I', ['Tell me, O Muse'])
# Iliad IX.307–429 (Achilles answers Ulysses)
R['il9'] = pick(IL['IX'], [18, 19, 20, 21], 'Iliad IX', ['Achilles answered, “Ulysses', '“Nevertheless he did', '“As for me, hound', '“My mother Thetis'])
# Iliad VI.390–502 (Hector and Andromache)
R['il6'] = pick(IL['VI'], [29, 30, 31, 32, 33], 'Iliad VI', ['Hector hurried from the house', 'And Hector answered, “Wife', 'He stretched his arms', 'With this he laid the child', 'He took his plumed helmet'])
# Iliad XXII.247–366 (the duel and the death of Hector) and XXII.395–404 (the body dragged)
R['il22'] = pick(IL['XXII'], [17, 18, 19, 20, 21, 22, 23, 24, 25, '…', 28], 'Iliad XXII',
    ['Thus did Minerva inveigle', 'Achilles glared at him and answered, “Fool', 'He poised his spear as he spoke and hurled it. Hector', 'He poised his spear as he spoke and hurled it. His aim',
     'As he spoke he drew the keen blade', 'Then Hector said, as the life', 'Achilles glared at him and answered, “Dog', 'Hector with his dying breath', 'When he had thus said the shrouds', 'On this he treated the body'])
# Iliad XXIV.468–676 (Priam in the tent of Achilles)
R['il24'] = pick(IL['XXIV'], list(range(36, 48)), 'Iliad XXIV',
    ['With these words Mercury went back', 'As when some cruel spite', 'Thus spoke Priam, and the heart', 'And Priam answered, “O king', 'Achilles looked at him sternly',
     'The old man feared him', 'Achilles then went back', 'With this Achilles sprang', 'As he spoke Achilles told', 'And Priam answered, “Since', 'And Achilles answered, “All', 'As he spoke he laid his hand'])
# Odyssey V.1–227 (Calypso)
R['od5'] = pick(OD['V'], list(range(1, 20)), 'Odyssey V',
    ['And now, as Dawn rose', '“Father Jove,”', '“What, my dear', 'When he had thus spoken', 'Thus he spoke, and Mercury', 'He found her at home', 'Calypso knew him at once', 'As she spoke she drew',
     '“We are speaking god', 'Calypso trembled with rage', '“Then send him away,”', 'On this he took his leave', '“My poor fellow', 'Ulysses shuddered', 'Calypso smiled at this', 'When she had thus spoken',
     '“Ulysses, noble son', '“Goddess,” replied Ulysses', 'Presently the sun set'])
# Odyssey XXIII.153–240 (the bed)
R['od23'] = pick(OD['XXIII'], [16, 17, 18, 19, 20], 'Odyssey XXIII', ['This was what they said', '“My dear,” answered Penelope', 'She said this to try him', 'When she heard the sure proofs', 'Then Ulysses in his turn'])
# Odyssey XI.465–540 (Achilles among the dead)
R['od11'] = pick(OD['XI'], [40, 41, 42, 43, 44], 'Odyssey XI', ['“As we two sat weeping', '“And I said, ‘Achilles', '“‘Say not a word,’', '“‘I have heard nothing,’', '“When I had told him this'])
# Odyssey XIII.187–360 (Ulysses wakes on Ithaca; Minerva)
R['od13'] = pick(OD['XIII'], list(range(20, 30)), 'Odyssey XIII',
    ['“Alas,” he exclaimed', 'He counted his goodly', '“My friend,” said he', 'Minerva answered, “Stranger', 'Ulysses was glad', '“I heard of Ithaca,”', 'Such was his story', 'And Ulysses answered, “A man', '“You are always taking', 'As she spoke the goddess dispersed'])

# Plato, Republic, tr. Jowett: the dialogue text (after the translator's long introduction)
P = read(1497); P2 = blocks(P[P.index('\n BOOK II.\n', P.index('PERSONS OF THE DIALOGUE.', 5000)):P.index('\n BOOK III.\n', P.index('PERSONS OF THE DIALOGUE.', 5000))])
P3s = P.index('\n BOOK III.\n', P.index('PERSONS OF THE DIALOGUE.', 5000)); P3 = blocks(P[P3s:P.index('\n BOOK IV.\n', P3s)])
def find(bl, start):
    hits = [k for k, b in enumerate(bl) if b.startswith(start)]; assert len(hits) == 1, (start, hits); return hits[0]
a = find(P2, 'Those, I said, which are narrated by Homer'); b = find(P2, 'There you are right, he replied; but if any one asks')
c = find(P2, 'Then God, if he be good, is not the author of all things'); d = find(P2, 'I agree with you, he replied, and am ready')
R['rep2'] = P2[a:b] + ['…'] + P2[c:d + 1]                      # Republic II.377d–378e; '…'; 379c–380c
e = find(P3, 'Such then, I said, are our principles of theology'); f = find(P3, 'And we must beg Homer and the other poets')
g = find(P3, 'Then we will once more entreat Homer'); h = find(P3, 'It ought not to be.')
R['rep3'] = P3[e:f + 1] + ['…'] + P3[g:h + 1]                  # Republic III.386a–387b; '…'; 388a–388e

# Augustine, Confessions I.13, I.14, I.16 (Pusey's Gutenberg text has no chapter numbers: chapters by opening words)
A = read(3296); AB = blocks(A[A.index('\nBOOK I\n'):A.index('\nBOOK II\n')])
R['conf'] = [AB[find(AB, 'But why did I so much hate the Greek')], AB[find(AB, 'For what more miserable than a miserable being')], '…',
             AB[find(AB, 'Why then did I hate the Greek classics')], '…', AB[find(AB, 'But woe is thee, thou torrent of human custom')]]

for k, v in R.items(): print(k, len(' '.join(v).split()), 'words', [len(x.split()) for x in v])
for w, n, ctx in FOOT: print('footnote removed:', w, n, 'after', repr(ctx))
left = [(k, m.group(0)) for k, v in R.items() for p in v for m in re.finditer(r'\S*\d\S*', p)]
print('digits left:', left)
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
json.dump([{'where': w, 'number': n, 'after': ctx} for w, n, ctx in FOOT], open(os.path.join(HERE, 'footnotes.json'), 'w'), ensure_ascii=False, indent=1)
