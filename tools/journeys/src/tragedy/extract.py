"""Extract the set texts for Tragedy from the cached files in .cache/texts.

Sources (headers checked; see notes.json):
  8604.txt   Aeschylus, The House of Atreus (Agamemnon, Libation-Bearers, Furies), tr. E. D. A. Morshead
             (1881; Morshead d. 1912). Verse, no line numbers: Greek line numbers matched by content.
  31.txt     Sophocles, Oedipus the King, Oedipus at Colonus, Antigone, tr. F. Storr (Loeb, 1912;
             Storr d. 1919). Used instead of Jebb, whose Perseus files failed to fetch.
  url/tragedy-bacchae.html  Euripides, Bacchae, tr. T. A. Buckley (Bohn, 1850; Buckley d. 1856), in the
             Perseus Digital Library's TEI file (perseus-eng2), which Perseus 'modernized' in language
             (CC BY-SA 4.0). Perseus gives the Greek line numbers. Editorial <note>s are removed; <q> is shown
             as quotation marks. See the flag in notes.json.
  1974.txt   Aristotle, Poetics, tr. S. H. Butcher (1895; Butcher d. 1910).
  16966.txt  A. C. Bradley, Shakespearean Tragedy (1904; Bradley d. 1935), Lecture I.

Paragraphs are split on blank lines, never on line ends. Verse keeps its line breaks. Gutenberg's italic
marks (_..._) and Bradley's footnote numbers ([10]) are removed and listed in notes.json; no word is changed.
Run: python3 tools/journeys/src/tragedy/extract.py
"""
import re, json, os, html
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
T = os.path.join(ROOT, '.cache', 'texts')
REMOVED = []

def read(n):
    t = open(os.path.join(T, f'{n}.txt'), encoding='utf-8').read().replace('\r', '')
    return t[t.index('*** START'):t.index('*** END')]

def verse_blocks(t):
    out = []
    for b in re.split(r'\n\s*\n', t):
        lines = [l.strip() for l in b.split('\n') if l.strip()]
        if lines: out.append('\n'.join(lines).replace('_', ''))
    return out

def prose_blocks(t):
    return [re.sub(r'\s+', ' ', b).strip() for b in re.split(r'\n\s*\n', t) if b.strip()]

def find(bl, start, frm=0):
    for i in range(frm, len(bl)):
        if bl[i].startswith(start): return i
    raise ValueError(start)

def span(bl, start, end, frm=0):
    i = find(bl, start, frm)
    for j in range(i, len(bl)):
        if end in bl[j]: return bl[i:j + 1]
    raise ValueError(end)

def cut(p, a=None, b=None):
    """A verbatim piece of one paragraph, from the words a to the words b (inclusive)."""
    i = p.index(a) if a else 0
    j = p.index(b, i) + len(b) if b else len(p)
    return p[i:j]

R = {}

# ---------- Aeschylus (Morshead) ----------
M = read(8604)
AG = verse_blocks(M[M.index('_A Watchman_'):M.index('THE LIBATION-BEARERS\n\nDRAMATIS')] if 'THE LIBATION-BEARERS\n\nDRAMATIS' in M else M[M.index('_A Watchman_'):])
EU = verse_blocks(M[M.rindex('THE FURIES'):])
# Agamemnon 1-39: the watchman
R['watchman'] = span(AG, 'A Watchman', 'nought remember nor discern.')
# Agamemnon 160-257: the hymn to Zeus and Aulis (the parodos, from 'Zeus-if to The Unknown')
R['hymn'] = span(AG, 'Zeus—if to The Unknown', 'Comes wisdom o’er the unwilling soul')
R['aulis'] = span(AG, 'And then the elder chief', 'Find yet an issue fair!—')
# Agamemnon 1560-1566: the law of the house
lament = AG[find(AG, 'CHORUS\nLo! sin by sin')]
R['law'] = [cut(lament, None, 'The clinging grasp of fate.')]
# Eumenides
R['trial'] = span(EU, 'ATHENA (to the Chorus)', 'that I to these may tell.')
R['court'] = span(EU, 'ATHENA\nO men of Athens', 'Lo, my word is said.')
R['vote'] = span(EU, 'ATHENA\nMine is the right to add the final vote', 'For half the votes condemn him, half set free!')
R['wrath'] = span(EU, 'CHORUS\nWoe on you, younger gods!', 'and by this folk adored.')
R['persuasion'] = span(EU, 'ATHENA\nI will not weary of soft words', 'Lo, I desist from wrath, appeased by thee.')

# ---------- Sophocles (Storr) ----------
S = read(31)
OT = verse_blocks(S[S.index('Suppliants of all ages are seated'):S.index('OEDIPUS AT COLONUS\n\n\nPERSONS') if 'OEDIPUS AT COLONUS\n\n\nPERSONS' in S else S.rindex('OEDIPUS AT COLONUS')])
OC = verse_blocks(S[S.rindex('OEDIPUS AT COLONUS'):S.rindex('ANTIGONE\n')])
AN = verse_blocks(S[S.rindex('ANTIGONE\n'):])

def unfoot(p, where):
    """Storr's Gutenberg text prints footnote numbers glued to a word ('found1'); remove and record them."""
    def f(m):
        REMOVED.append({'where': where, 'marker': m.group(2), 'after': m.group(1)}); return m.group(1)
    return re.sub(r'([a-z])(\d{1,2})(?=\s|$)', f, p)

R['ot-prologue'] = [unfoot(p, 'Oedipus the King, prologue') for p in span(OT, 'OEDIPUS.\nMy children, latest born', 'rid us of this pest.')]
R['ot-discovery'] = span(OT, 'OEDIPUS.\nAh me! ah me! all brought to pass', 'And now through thee I feel a second death.')
R['ot-apollo'] = span(OT, 'OEDIPUS.\n(Str. 2)\nApollo, friend, Apollo', 'Brought no delight?')
wd = OT[find(OT, 'OEDIPUS.\nWhat’s done was well done.')]
R['ot-welldone'] = [cut(wd, None, 'How had I dared to look you in the face?')]
od = OC[find(OC, 'OEDIPUS.\nO shameless railer')]
R['oc-defence'] = [cut(od, None, 'shall I be held to blame.')]
R['ode-to-man'] = span(AN, 'CHORUS.\n(Str. 1)\nMany wonders there be', 'or share the thoughts of his heart.')
R['creon-edict'] = [AN[find(AN, 'CREON.\nElders, the gods have righted')]]
R['antigone-creon'] = span(AN, 'CREON.\nSpeak, girl, with head bent low', 'No woman shall be the master while I live.')

# ---------- Euripides (Buckley, in Perseus) ----------
X = open(os.path.join(T, 'url', 'tragedy-bacchae.html'), encoding='utf-8').read()
body = X[X.index('<div type="textpart"'):]
SP = []
for m in re.finditer(r'<sp\b[^>]*>(.*?)</sp>', body, re.S):
    s = m.group(1)
    spk = re.sub(r'<[^>]+>', '', re.search(r'<speaker>(.*?)</speaker>', s, re.S).group(1)).strip()
    ls = re.findall(r'<l\b([^>]*)>(.*?)</l>', s, re.S)
    n = next((int(re.search(r'n="(\d+)"', a).group(1)) for a, _ in ls if re.search(r'n="(\d+)"', a)), None)
    txt = ' '.join(x for _, x in ls)
    for nt in re.findall(r'<note.*?</note>', txt, re.S):
        REMOVED.append({'where': f'Bacchae {n}', 'marker': 'Perseus editorial note', 'after': re.sub(r'<[^>]+>', '', nt)[:80]})
    txt = re.sub(r'<note.*?</note>', '', txt, flags=re.S)
    txt = re.sub(r'</q>\s*<q[^>]*rend="merge"[^>]*>', ' ', txt)
    txt = re.sub(r'<q\b[^>]*>', '“', txt).replace('</q>', '”')
    txt = re.sub(r'<gap[^>]*/>', '', txt)
    txt = re.sub(r'<[^>]+>', '', txt)
    txt = re.sub(r'\s+', ' ', html.unescape(txt)).strip()
    SP.append((n, spk, txt))

def bac(a, b):
    return [f'{spk}\n{txt}' for n, spk, txt in SP if n is not None and a <= n <= b and txt]

R['bac-prologue'] = bac(1, 63)
mess = next(f'{spk}\n{txt}' for n, spk, txt in SP if n == 1043)
R['bac-death'] = [cut(mess, 'Pentheus fell crashing', 'and he did not persuade her.')]
R['bac-recognition'] = bac(1259, 1300)
R['bac-kadmos'] = bac(1301, 1328)
R['bac-end'] = bac(1344, 1351)

# ---------- Aristotle, Poetics (Butcher) ----------
P = read(1974)
P = P[P.index("ARISTOTLE'S POETICS"):]
def chapter(roman, nxt):
    a = P.index(f'\n{roman}\n'); b = P.index(f'\n{nxt}\n', a)
    return prose_blocks(P[a + len(roman) + 2:b])
P4, P6, P13, P14 = chapter('IV', 'V'), chapter('VI', 'VII'), chapter('XIII', 'XIV'), chapter('XIV', 'XV')
R['poetics4'] = [P4[0], '…', P4[4], P4[5]]
R['poetics6'] = [P6[1], '…', P6[4], P6[5], '…', P6[9]]
R['poetics13'] = [P13[1], P13[2]]
R['poetics14'] = [P14[0], '…', P14[2], P14[3]]
assert R['poetics6'][0].startswith('Tragedy, then, is an imitation') and R['poetics13'][0].startswith('A perfect tragedy')

# ---------- Bradley, Shakespearean Tragedy, Lecture I ----------
B = read(16966)
B = B[B.index('LECTURE I\n\nTHE SUBSTANCE'):]
BB = prose_blocks(B[:B.index('FOOTNOTES:')])
def unbrad(p, where):
    def f(m):
        REMOVED.append({'where': where, 'marker': m.group(0), 'after': p[max(0, m.start() - 30):m.start()]}); return ''
    return re.sub(r'\[\d+\]', f, p).replace('_', '')
w = BB[find(BB, 'The tragic hero with Shakespeare, then, need not be')]
R['bradley'] = [unbrad(cut(w, 'Hence, in the first place, a Shakespearean tragedy is never'), 'Bradley I.3'), '…',
                unbrad(BB[find(BB, 'It will be agreed, however, first, that this question must not be')], 'Bradley I.4'), '…',
                unbrad(BB[find(BB, 'Thus we are left at last with an idea showing two sides')], 'Bradley I.6')]

for k, v in R.items():
    print(f'{k:16}', len(v), 'paras', sum(len(x.split()) for x in v), 'words |', v[0][:60].replace('\n', ' / '))
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
json.dump(REMOVED, open(os.path.join(HERE, 'removed.json'), 'w'), ensure_ascii=False, indent=1)
print('removed markers:', len(REMOVED))
