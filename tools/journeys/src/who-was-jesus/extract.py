"""Extract the set texts for 'Who was Jesus?' into raw.json. Run: python3 tools/journeys/src/who-was-jesus/extract.py

Sources (all in .cache/texts):
- Psalms of Solomon 17, tr. H. E. Ryle (d. 1925) and M. R. James (d. 1936), Cambridge 1891:
  url/who-was-jesus-psalms-of-solomon.txt (archive.org OCR of the 1891 edition, Greek and English on facing pages).
  The English verses are taken by line number from the OCR, lines joined with spaces. The OCR misreads Ryle and James's
  italic words and leaves marginal-note letters in the lines; each repair is listed in FIX below and in notes.json.
- Philostratus, Life of Apollonius IV.44-45, tr. F. C. Conybeare (d. 1924), Loeb 1912: url/who-was-jesus-philostratus-4-41-45.txt (Livius).
- 1 Enoch 46:1-3 and 48:2-6, tr. R. H. Charles (d. 1931), SPCK 1917: 77935.txt (Gutenberg #77935). Verse lines are kept;
  the '=...=' marks (Charles's emphasis, printed as bold) are removed.
- Thomas Paine, The Age of Reason, Part I (1794), chapters III and IV: 3743.txt (Gutenberg #3743, Conway's edition).
  Conway's bracketed editorial notes '[NOTE: ...—Editor.]' are removed.
- D. F. Strauss, The Life of Jesus Critically Examined, section 15, tr. George Eliot (d. 1880), 1846: 64037.txt (Gutenberg #64037).
- The Koran, Sura IV.171-172 and V.116-118, tr. J. M. Rodwell (d. 1900), 1861: 2800.txt (Gutenberg #2800).
  Rodwell's footnote numbers glued to words ('religion;31', 'Spirit32', '. .\n.44') are removed.
Paragraphs are split on blank lines, never on line ends. No word is changed except the OCR repairs listed.
"""
import re, json, os
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(HERE, '..', '..', '..', '..', '.cache', 'texts')
def read(p): return open(os.path.join(T, p), encoding='utf-8', errors='ignore').read().replace('\r', '')
def blocks(t): return [re.sub(r'\s+', ' ', b).strip() for b in re.split(r'\n\s*\n', t) if b.strip()]
def para(bl, start): return next(b for b in bl if b.startswith(start))
R = {}

# ---- Psalms of Solomon 17 (Ryle and James 1891), by line numbers in the OCR file ----
L = read('url/who-was-jesus-psalms-of-solomon.txt').split('\n')
def lines(a, b): return re.sub(r'\s+', ' ', ' '.join(L[a - 1:b])).strip()
assert L[23428].startswith('1 O LorpD, thou art our King')
assert L[24927].startswith('23 Behold, O LORD') and L[25141].startswith('25 Purge Jerusalem')
assert L[25422].startswith('32 And he shall possess') and L[25740].startswith('37 For he shall not')
assert L[26039].startswith('41 He himself also')
FIX = [  # (OCR reading, the printed text) -- italics misread, marginal letters, note markers
    ('O LorpD,', 'O LORD,'),
    ('for ever- more', 'for evermore'),
    ('servant ;', 'servant;'),
    ('azd with', 'and with'),
    ('He shall” thrust', 'He shall thrust'),
    ('inheritance, *\' ©": ie utterly', 'inheritance, utterly'),
    ('avd as potter’s os vessels', 'and as potter’s vessels'),
    ('all their accents, substance”. “ἐν', 'all their substance.'),
    ('his tiene mouth', 'his mouth'),
    ('before him,’ and', 'before him, and'),
    ('earth ;', 'earth;'),
    ('elorified', 'glorified'),
    ('God zs he', 'God is he'),
    ('shall be” no', 'shall be no'),
    ('Lord Messiah™.', 'Lord Messiah.'),
]
def fix(s):
    for a, b in FIX: s = s.replace(a, b)
    return s
v1 = fix(lines(23429, 23430))
v23_24 = fix(lines(24928, 24941))
v25_27 = fix(lines(25142, 25156))
v25_27 = v25_27[:v25_27.index(' 28 And he shall gather')]
v32_36 = fix(' '.join([lines(25423, 25427), lines(25436, 25457)]))
v37 = fix(lines(25741, 25743))
v41 = fix(lines(26040, 26044))
R['pssol'] = [v1, '…', v23_24, v25_27, '…', v32_36, v37, '…', v41]
for s in R['pssol']:
    assert not re.search(r'[α-ωΑ-Ω™”“*©]', s), s

# ---- Philostratus IV.44-45 (Conybeare 1912, from Livius) ----
P = blocks(read('url/who-was-jesus-philostratus-4-41-45.txt'))
R['apollonius'] = [para(P, 'But when Tigellinus unrolled the scroll'),
                   '…',
                   para(P, '"And about the demons," said Tigellinus'),
                   para(P, '"In the same way," he answered'),
                   para(P, '[4.45] Here too is a miracle')[len('[4.45] '):],
                   para(P, 'And withal he asked what was her name'),
                   para(P, 'Now whether he detected some spark of life')]

# ---- 1 Enoch 46:1-3; 48:2-6 (Charles 1917): keep the verse lines ----
E = read('77935.txt')
def en(a, b):
    i = E.index(a); j = E.index(b, i) + len(b); blk = E[i:j]
    out = []
    for raw in blk.split('\n'):
        s = raw.strip()
        if not s: continue
        prose = not raw.startswith(' ')
        if raw.startswith('       ') and out and not re.match(r'^\d+\.', s): out[-1] += ' ' + s  # a wrapped verse line
        elif prose and out and out[-1].endswith('\x00'): out[-1] = out[-1][:-1] + ' ' + s + '\x00'  # prose lines run on
        elif prose: out.append(s + '\x00')
        else: out.append(s)
    return '\n'.join(x.rstrip('\x00') for x in out).replace('=angel=', 'angel')
R['enoch'] = [en('XLVI. 1. And there I saw One', 'uprightness for ever.')[len('XLVI. '):],
              '…',
              en('2. And at that hour that Son of Man was named', 'Before the creation of the world and for evermore.')]

# ---- Paine, The Age of Reason, Part I, chapters III-IV (1794) ----
PA = blocks(read('3743.txt'))
note = lambda s: re.sub(r'\s*\[NOTE: .*?—Editor\.(?: \(Conway\))?\]', '', s)
R['paine'] = [para(PA, 'Nothing that is here said can apply, even with the most distant'),
              para(PA, 'Jesus Christ wrote no account of himself'),
              '…',
              note(para(PA, 'That such a person as Jesus Christ existed')),
              note(para(PA, 'It is upon this plain narrative of facts')),
              '…',
              note(para(PA, 'Having thus made an insurrection and a battle in heaven'))]
assert 'NOTE' not in ' '.join(R['paine'])

# ---- Strauss, The Life of Jesus Critically Examined, section 15 (tr. George Eliot, 1846) ----
S = blocks(read('64037.txt'))
fn = lambda s: re.sub(r'\s*\[\d+\]', '', s)
i = S.index(para(S, 'We distinguish by the name evangelical mythus'))
R['strauss'] = [fn(x) for x in S[i:i + 4]] + ['…', fn(para(S, 'It is to the various forms of the unhistorical in the Gospels'))]

# ---- The Koran, Rodwell (1861): Sura IV.171-172 and V.116-118 ----
Q = blocks(read('2800.txt'))
q1 = para(Q, 'O ye people of the Book! overstep not bounds in your religion;31')
q1 = q1.replace('religion;31', 'religion;').replace('a Spirit32 proceeding', 'a Spirit proceeding')
q2 = para(Q, 'The Messiah disdaineth not to be a servant of God')
q3 = para(Q, 'And when God shall say-"O Jesus, Son of Mary: hast thou said unto mankind')
q4 = para(Q, '"I spake not to them aught but that which thou didst bid me')
q5 = para(Q, '"If Thou punish them, they are Thy servants').replace('. . .44 Thou', '. . . Thou')
R['quran'] = [q1, q2, q3, q4, q5]
assert not re.search(r'[a-z;.]\d', ' '.join(R['quran']))

for k, v in R.items(): print(k, [len(x.split()) for x in v])
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
