import json,re
import os
W=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','.cache','web','json')+'/'
def bookfile(b):
    b=b.strip(); m={'psalm':'psalms','song of songs':'songofsolomon'}
    return W+m.get(b.lower(), b.lower().replace(' ',''))+'.json'
def parse(ref):
    m=re.match(r'^(.+?)\s+(\d+)(?::(\d+))?(?:\s*[-–]\s*(\d+)(?::(\d+))?)?$',ref.strip())
    book,c1,v1,x,y=m.groups(); c1=int(c1)
    if v1 is None: # whole chapter(s)
        c2=int(x) if x else c1; return book,(c1,1),(c2,999)
    v1=int(v1)
    if y: return book,(c1,v1),(int(x),int(y))
    if x: return book,(c1,v1),(c1,int(x))
    return book,(c1,v1),(c1,v1)
def passage(ref):
    book,a,b=parse(ref); d=json.load(open(bookfile(book)))
    paras=[];cur=[];poetry=False;started=False;startc=a[0]
    def flush():
        nonlocal cur
        if cur: paras.append(cur); cur=[]
    for x in d:
        t=x['type']
        if t in('paragraph start','stanza start'): flush(); continue
        if t in ('paragraph end','stanza end'): continue
        if t=='line break':
            if cur and not cur[-1][1].endswith('\n'): cur[-1][1]+='\n'
            continue
        if 'verseNumber' not in x: continue
        cv=(x['chapterNumber'],x['verseNumber'])
        if not(a<=cv<=b): continue
        val=x['value']
        lab=cv[1] if cv[0]==startc else f"{cv[0]}:{cv[1]}"
        if cur and cur[-1][0]==lab: cur[-1][1]+=( '' if cur[-1][1].endswith('\n') else '')+val
        else:
            if cur and cur[-1][1].endswith('\n') and t=='paragraph text': pass
            cur.append([lab,val])
        if t=='line text' and not val.endswith('\n'): cur[-1][1]=cur[-1][1].rstrip()+'\n'
    flush()
    out=[]
    for p in paras:
        q=[[v,re.sub(r'[ \t]+',' ',re.sub(r' *\n *','\n',t)).strip()] for v,t in p]
        out.append(q)
    words=sum(len(t.split()) for p in out for v,t in p)
    verses=set((v) for p in out for v,t in p)
    return {'ref':ref.replace('-','–'),'paras':out,'minutes':max(1,round(words/200)),'verses':len(verses)}
if __name__=='__main__':
    import sys; r=passage(sys.argv[1]); print(r['verses'],r['minutes']); print(json.dumps(r['paras'][:2],ensure_ascii=False)[:600])

def verse(ref):
    """The plain text of a reference, for checking quotations."""
    book,a,b=parse(ref); d=json.load(open(bookfile(book)))
    out=[x['value'].strip() for x in d if 'verseNumber' in x and a<=(x['chapterNumber'],x['verseNumber'])<=b]
    return ' '.join(' '.join(out).split())
