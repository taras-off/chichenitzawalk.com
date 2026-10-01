#!/usr/bin/env python3
import re,io,sys
def tags(f): return [x.split()[0].lower() for x in re.findall(r'<(/?[a-zA-Z][^>]*)>', io.open(f,encoding='utf-8').read())]
ref=tags('drafts/04-body-EN.html')
print('EN tags', len(ref))
ok=True
for L in (sys.argv[1:] or ['es','fr','de','it','pt','pl','ru']):
    try: t=tags(f'drafts/04-body-{L}.html')
    except FileNotFoundError: print(L,'— нет файла'); ok=False; continue
    if t==ref: print(L,'OK',len(t))
    else:
        ok=False
        print(L,'РАСХОЖДЕНИЕ', len(t),'vs',len(ref))
        for i,(a,b) in enumerate(zip(ref,t)):
            if a!=b: print('  первое на позиции',i,'ожидалось',a,'получено',b); break
sys.exit(0 if ok else 1)
