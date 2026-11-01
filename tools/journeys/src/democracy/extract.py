"""Extract the set texts for Democracy and its dangers from the fetched texts in .cache/texts.

Paragraphs are split on blank lines, never on line ends. Indented verse keeps its line breaks.
Editorial markers removed (and listed in notes.json): Bekker page numbers such as [1279b] in Ellis's
Politics. No word is changed. Cuts are marked with a paragraph that is just "…".
"""
import re, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(HERE, '..', '..', '..', '..', '.cache', 'texts')

def read(p):
    t = open(os.path.join(T, p), encoding='utf-8', errors='ignore').read().replace('\r', '')
    s = t.find('*** START OF'); e = t.find('*** END OF')
    if s >= 0: t = t[t.index('\n', s) + 1:]
    if e >= 0: t = t[:t.find('*** END OF')]
    return t

def block(b):
    lines = [l for l in b.split('\n') if l.strip()]
    if lines and all(l.startswith('  ') for l in lines):   # indented verse: keep the lines
        return '\n'.join(re.sub(r'\s+', ' ', l).strip() for l in lines)
    return re.sub(r'\s+', ' ', b).strip()

def blocks(t):
    return [block(b) for b in re.split(r'\n\s*\n', t) if b.strip()]

def find(bl, start, after=0):
    for i in range(after, len(bl)):
        if bl[i].startswith(start): return i
    raise ValueError('not found: ' + start)

def run(bl, start, end, after=0):
    """Paragraphs from the one starting `start` to the one starting `end`, inclusive."""
    i = find(bl, start, after); j = find(bl, end, i)
    return bl[i:j + 1]

BEKKER = re.compile(r' ?\[1\d{3}[ab]\]')
R = {}

# Plutarch, Life of Solon (tr. Aubrey Stewart and George Long, 1880), Gutenberg #14033
P = blocks(read('14033.txt'))
s0 = find(P, 'LIFE OF SOLON.')
R['solon-crisis'] = run(P, 'XIII. When the troubles about Kylon', 'The greater part, and those of most spirit', s0)
R['solon-refuses'] = run(P, 'XIV. In this position of affairs', 'XIV. In this position of affairs', s0) + \
    run(P, '"Take thou the helm', 'From which it is clear that he possessed', s0)[:-1]
fm = run(P, 'This was his first measure', 'This was his first measure', s0)[0]
fm = fm[:fm.index('security of the person of the debtor.') + len('security of the person of the debtor.')]
R['solon-burdens'] = run(P, 'Being afterwards asked whether he had composed', 'Being afterwards asked whether he had composed', s0) + [fm, '…']
R['solon-people'] = run(P, 'XVIII. In the next place, Solon', 'Thinking that the weakness of the populace', s0)
R['solon-leaves'] = run(P, 'When Solon had passed all his laws', 'When Solon had passed all his laws', s0)
t0 = find(P, 'LIFE OF THEMISTOKLES.')
R['themistocles-ostracism'] = run(P, 'XXII. As the Athenians, through his unpopularity', 'XXII. As the Athenians, through his unpopularity', t0)
a1 = find(P, 'LIFE OF ALKIBIADES.')
R['hyperbolus'] = run(P, 'There was at Athens one Hyperbolus', '"Full worthy to be punished though he be', a1)

# Aristotle, The Athenian Constitution (tr. F. G. Kenyon, 1891), Gutenberg #26095
A = blocks(read('26095.txt'))
def part(n):
    i = A.index(f'Part {n}'); j = A.index(f'Part {n + 1}')
    return A[i + 1:j]
R['ac-20-21'] = part(20) + part(21)
R['ac-22'] = part(22)
R['ac-42-43'] = part(42) + part(43)[:2]
p12 = part(12)
i = next(k for k, b in enumerate(p12) if b.startswith('Of all the aims'))
R['solon-dark-earth'] = p12[i:i + 2]          # for the memory piece and the notes

# Thucydides (tr. Richard Crawley, 1874), Gutenberg #7142
TH = blocks(read('7142.txt'))
R['pericles-last'] = run(TH, '“I was not unprepared for the indignation', '“I was not unprepared for the indignation')
R['th-2-65'] = run(TH, 'Such were the arguments by which Pericles tried', 'Such were the arguments by which Pericles tried')
R['mytilene-decree'] = run(TH, 'Upon the arrival of the prisoners with Salaethus', 'Upon the arrival of the prisoners with Salaethus')
cl = find(TH, '“I have often before now been convinced that a democracy')
R['cleon'] = TH[cl:cl + 2] + ['…'] + run(TH, '“No hope, therefore, that rhetoric', '“No hope, therefore, that rhetoric', cl)
dd = find(TH, 'Such were the words of Cleon.')
R['diodotus'] = TH[dd:dd + 2] + ['…'] + run(TH, '“However, I have not come forward', '“We must not, therefore, commit ourselves', dd) + \
    run(TH, '“Only consider what a blunder', '“Only consider what a blunder', dd)
R['mytilene-end'] = run(TH, 'Such were the words of Diodotus.', 'The other party whom Paches had sent off')
R['mytilene-end'][-1] = R['mytilene-end'][-1][:R['mytilene-end'][-1].index(' The Athenians also demolished')]

# Plato, Republic (tr. Benjamin Jowett), Gutenberg #1497
RP = blocks(read('1497.txt'))
b8 = find(RP, 'And then democracy comes into being after the poor', find(RP, 'BOOK VIII.'))
R['rep-democracy'] = run(RP, 'And then democracy comes into being after the poor', 'We know her well.', b8 - 1)
dm = find(RP, 'Yes, I said, he lives from day to day indulging', b8)
R['rep-democratic-man'] = RP[dm:dm + 4]
R['rep-freedom'] = run(RP, 'Last of all comes the most beautiful of all', 'As we might expect.', dm)
pr = find(RP, 'The people have always some champion', dm)
R['rep-protector'] = run(RP, 'The people have always some champion', 'No doubt, he said.', pr)
R['rep-smoke'] = run(RP, 'Then he is a parricide', 'True, he said.', pr)
sh = find(RP, 'I perceive, I said, that you are vastly amused')
R['ship'] = run(RP, 'I perceive, I said, that you are vastly amused', 'Precisely so, he said.', sh)

# Aristotle, Politics (tr. William Ellis, 1776), Gutenberg #6762
PO = blocks(read('6762.txt'))
def chap(book, ch):
    b = PO.index(f'BOOK {book}'); i = PO.index(f'CHAPTER {ch}', b)
    j = next(k for k in range(i + 1, len(PO)) if PO[k].startswith('CHAPTER ') or PO[k].startswith('BOOK '))
    return [BEKKER.sub('', x) for x in PO[i + 1:j]]
c311 = chap('III', 'XI'); R['pol-3-11'] = c311[:3] + ['…'] + c311[4:6]
c411 = chap('IV', 'XI'); R['pol-4-11'] = c411[:5]

# Lord Acton, 'The History of Freedom in Antiquity' (1877), in The History of Freedom and Other Essays (1907), Gutenberg #31278
AC = blocks(read('31278.txt'))
a0 = find(AC, 'THE HISTORY OF FREEDOM IN ANTIQUITY[2]')
R['acton-solon'] = run(AC, 'From this universal degradation the world was rescued', 'The only resource against political disorders', a0)
R['acton-athens'] = run(AC, 'It was a momentous step in the progress of nations', 'When the absolute sway of numbers had endured', a0)
R['acton-christ'] = run(AC, 'After the fourth century the declarations against slavery', 'After the fourth century the declarations against slavery', a0)

# The Mayflower Compact (1620), Avalon Project text
MF = blocks(read('url/democracy-mayflower.txt'))
R['mayflower'] = run(MF, 'IN THE NAME OF GOD, AMEN.', 'IN THE NAME OF GOD, AMEN.')
R['mayflower-names'] = len([b for b in MF if re.match(r"^(Mr\.? )?[A-Z][a-z]+ [A-Z][A-Za-z]+,?$", b)])

# Tocqueville (tr. Henry Reeve), Gutenberg #815: one sentence, quoted in the lecture only
TQ = blocks(read('815.txt'))
R['tocqueville'] = [next(b for b in TQ if b.startswith('Religion in America takes no direct part'))]

for k, v in R.items():
    if isinstance(v, list): print(k, len(v), 'paras', sum(len(x.split()) for x in v), 'words')
    else: print(k, v)
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
