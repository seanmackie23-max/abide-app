"""Extract the set texts for Abraham and the promise from the Gutenberg files in .cache/books."""
import re, json, os
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', '.cache', 'books')
def read(p, enc='utf-8'): return open(os.path.join(B, p), encoding=enc, errors='ignore').read()
def blocks(t): return [re.sub(r'\s+', ' ', b).strip() for b in re.split(r'\n\s*\n', t) if b.strip()]
def para(bl, start): return next(b for b in bl if b.startswith(start))
def lines(t, a, b):
    i = t.index(a); j = t.index(b, i) + len(b); return t[i:j]
R = {}
# Ginzberg, Legends of the Jews I (tr. Henrietta Szold, 1909)
L = blocks(read('legends1/1493.txt'))
R['legends'] = [re.sub(r'\[\d+\]', '', para(L, 'When Abraham attained the age of twenty years')), '…',
                re.sub(r'\[\d+\]', '', para(L, 'Alone with the idols')), re.sub(r'\[\d+\]', '', para(L, 'The feast ended, the king returned'))]
# The Koran, tr. J. M. Rodwell (1861): Sura XXI (The Prophets) and XXXVII (The Ranks); one line per verse
K = read('koran/2800.txt')
def kl(a, b):
    blk = re.sub(r'(\D)\d{1,2}(?=[\s,.;:!?"])', r'\1', lines(K, a, b))  # footnote numbers attached to words
    return '\n'.join(re.sub(r'\s+', ' ', x).strip() for x in re.split(r'\n\s*\n', blk) if x.strip())
R['quran21'] = [kl('Of old we gave unto Abraham his direction', 'We said, "O fire! be thou cold, and to Abraham a safety!"')]
R['quran37'] = [kl('And he said, "Verily, I repair to my Lord who will guide me:', 'And we announced Isaac to him-a righteous Prophet-')]
R['quran14'] = [kl('ABRAHAM said, "O Lord make this land secure', 'My Lord is the hearer of prayer.')]
R['quran2'] = [kl('And when Abraham, with Ismael, raised the foundations', 'for thou art He who\nturneth, the Merciful.')]
# Ovid, Metamorphoses VIII, tr. H. T. Riley (1851): Baucis and Philemon
O = blocks(read('ovid/26073-0.txt'))
clean = lambda s: re.sub(r'\[\d+\]', '', s)
R['ovid'] = [clean(para(O, '“And that thou mayst the less doubt')), '…', clean(para(O, '“There is {now} a short pause')), clean(para(O, '“They both obeyed'))]
# Ingersoll, Lectures I
I = read('ingersoll/8140.txt'); IB = blocks(I)
R['ingersoll'] = [para(IB, 'Abraham was commanded to offer his son Isaac'), '…',
                  re.sub(r'^.*?(And the next we find Him talking to Abraham)', r'\1', para(IB, 'Nothing. And so He let them go on')).split(' Finally, these people')[0], '…',
                  para(IB, 'I want him to answer'), para(IB, 'Robert Collyer says that we should read')]
for k, v in R.items(): print(k, [len(x.split()) for x in v])
json.dump(R, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'raw.json'), 'w'), ensure_ascii=False, indent=1)
