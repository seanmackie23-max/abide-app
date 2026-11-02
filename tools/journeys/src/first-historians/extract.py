"""Extract the set texts for The first historians from the cached Gutenberg and New Advent files (.cache/texts).

Herodotus: G. C. Macaulay (1890; d. 1915), Gutenberg #2707 (vol. I, from the 1890 edition) and #2456 (vol. II, from the 1914 third edition).
Thucydides: Richard Crawley (1874; d. 1893), Gutenberg #7142.
Eusebius, Church History VII.22: A. C. McGiffert (NPNF II.1, 1890; d. 1933), New Advent 250107.
Augustine, City of God IV.4: Marcus Dods (NPNF I.2, 1887; d. 1909), New Advent 120104.

Paragraphs are split on blank lines, never on line ends. Macaulay's footnote numbers (bare numbers after a word,
e.g. 'to the end that 1 neither') are removed and listed by this script; New Advent's section numbers ('7. ') are
removed from the start of Eusebius's paragraphs. No word is changed.
"""
import re, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(HERE, '..', '..', '..', '..', '.cache', 'texts')
def read(p): return open(os.path.join(T, p), encoding='utf-8', errors='ignore').read().replace('\r', '')
def blocks(t): return [re.sub(r'\s+', ' ', b).strip() for b in re.split(r'\n\s*\n', t) if b.strip()]
def run(bl, start, end):
    i = next(k for k, b in enumerate(bl) if b.startswith(start))
    j = next(k for k in range(i, len(bl)) if end in bl[k])
    return bl[i:j + 1]
REMOVED = []
FN = re.compile(r'(?<=[A-Za-z,;:.!?"\'\)—-]) (\d{1,3})(?=[\s,;:.!?"\']|$)')
def nofn(p, where):
    for m in FN.finditer(p): REMOVED.append(f'{where}: footnote {m.group(1)} after "...{p[max(0, m.start() - 25):m.start()]}"')
    return FN.sub('', p)
def clean(ps, where): return [nofn(p, where) for p in ps]

R = {}
H1 = blocks(read('2707.txt')); H2 = blocks(read('2456.txt')); TH = blocks(read('7142.txt'))

# Herodotus I, proem and 1-5 (the causes of the war)
R['hdt-proem'] = clean(run(H1, 'This is the Showing forth of the Inquiry', 'may be remembered for which these waged war'), 'Hdt I.0')
R['hdt-1-5'] = clean(run(H1, '1. Those of the Persians who have knowledge of history', 'I shall make mention of both indifferently'), 'Hdt I.1-5')
# Herodotus I.28-33 (Solon and Croesus) and I.86-88 (the pyre)
R['hdt-solon'] = clean(run(H1, '28. As time went on, when nearly all those dwelling', 'bade men look to the end of every matter'), 'Hdt I.28-33')
R['hdt-pyre'] = clean(run(H1, '86. The Persians then had obtained possession of Sardis', 'it is thy wealth that they are carrying and driving away'), 'Hdt I.86-88')
# Herodotus II.123 (I write what is told me)
R['hdt-2-123'] = [nofn(run(H1, '123. Now as to the tales told by the Egyptians', 'which is reported by the people in each place')[0].split(' The Egyptians say that Demeter')[0], 'Hdt II.123')]
# Herodotus VII.44-52 (Xerxes weeps at Abydos), 101-104 (Xerxes and Demaratos), 152 (bound to report), 223-228 (Thermopylae)
R['hdt-abydos'] = clean(run(H2, '44. When Xerxes had come into the midst of Abydos', 'is discovered in this matter to be full of jealousy'), 'Hdt VII.44-46')
R['hdt-demaratos'] = clean(run(H2, '101. Now when he had sailed through these', 'May it come to pass however according to thy mind, O king'), 'Hdt VII.101-104')
p152 = next(b for b in H2 if 'I however am bound to report' in b)
i = p152.index('I however am bound to report'); j = p152.index('every narrative in the history:') + len('every narrative in the history')
R['hdt-7-152'] = [nofn(p152[i:j], 'Hdt VII.152')]
R['hdt-thermopylae'] = clean(run(H2, '223. Xerxes meanwhile, having made libations at sunrise', 'on account of guest-friendship'), 'Hdt VII.223-228')

# Thucydides I.20-23 (method), II.47-54 (plague), V.84-116 (Melos), VII.84-87 (the end in Sicily)
R['thuc-method'] = run(TH, 'Having now given the result of my inquiries into early times', 'dissolution of the treaty and the breaking out of the war')
R['thuc-plague'] = run(TH, 'Such was the funeral that took place during this winter', 'Such was the history of the plague.')
R['thuc-melos'] = run(TH, 'The next summer Alcibiades sailed with twenty ships to Argos', 'inhabited the place themselves')
R['thuc-sicily'] = run(TH, 'As soon as it was day Nicias put his army in motion', 'Such were the events in Sicily.')

# Eusebius VII.22.2-10 (Dionysius of Alexandria on the plague)
EU = blocks(read('url/first-historians-eusebius-7.txt'))
eu = run(EU, '2. To other men the present might not seem', '3. For as it was written of the firstborn') + run(EU, '6. But after both we and they', '10. But with the heathen everything')
eu = [b for b in eu if not b.startswith('7. Farther on he adds')]
R['eusebius'] = [re.sub(r'^\d+\. ', '', b).replace(" Exodus 12:30 ", ' ') for b in eu]  # New Advent's inserted reference removed
R['eusebius'].insert(2, '…')

# Augustine, City of God IV.4
CG = blocks(read('url/first-historians-city-of-god-4.txt'))
R['augustine'] = [next(b for b in CG if b.startswith('Justice being taken away, then, what are kingdoms but great robberies?'))]

for k, v in R.items(): print(k, len(v), 'paras', sum(len(x.split()) for x in v), 'words')
print('\n'.join(REMOVED))
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
