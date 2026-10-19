"""Helpers for set texts from Project Gutenberg (GITenberg mirrors on GitHub).

Clone a book:   git clone --depth 1 https://github.com/GITenberg/<Title-With-Dashes>_<ebook number> .cache/books/<name>
Then:           paras(path, start_text, count)  -> list of paragraphs, split on blank lines (never on line ends)
"""
import glob, re, os

def book_text(folder):
    fs = [f for f in glob.glob(os.path.join(folder, '*.txt')) if not f.endswith('-0.txt') or True]
    return open(sorted(fs, key=len)[0], encoding='utf-8', errors='ignore').read()

def paras(text_or_folder, start, count=1, until=None):
    t = book_text(text_or_folder) if os.path.isdir(text_or_folder) else text_or_folder
    i = t.index(start)
    i = t.rfind('\n\n', 0, i) + 2 if t.rfind('\n\n', 0, i) >= 0 else i
    blocks = [re.sub(r'\s+', ' ', b).strip() for b in re.split(r'\n\s*\n', t[i:])]
    blocks = [b for b in blocks if b]
    if until:
        out = []
        for b in blocks:
            out.append(b)
            if until in b: break
        return out
    return blocks[:count]

def norm(t):
    return re.sub(r'\s+', ' ', t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"'))

def check_verbatim(paras_, folder, allowed=()):
    """Every paragraph must appear in the source (after removing the listed editorial strings)."""
    big = norm(book_text(folder))
    for a in allowed: big = big.replace(norm(a), '')
    big = re.sub(r'\s+', ' ', big)
    bad = [p[:60] for p in paras_ if p != '…' and norm(p) not in big]
    return bad
