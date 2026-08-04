#!/usr/bin/env python3
"""Generate the 7 localized /<lang>/guides/ pages from the EN master."""
import json, os, re
from localize import apply_map, unused_keys
ROOT=os.path.dirname(os.path.abspath(__file__)); PUB=os.path.join(ROOT,'public'); TR=os.path.join(ROOT,'tr')
DOMAIN='https://chichenitzawalk.com'
LANGS=['fr','de','es','it','pt','pl','ru']
CRUMB={'fr':'Guides','de':'Guides','es':'Guías','it':'Guide','pt':'Guias','pl':'Przewodniki','ru':'Гиды'}
POSTFIX=json.load(open(os.path.join(TR,'postfix.json'),encoding='utf-8'))
master=open(os.path.join(PUB,'guides','index.html'),encoding='utf-8').read()
for lang in LANGS:
    tmap=json.load(open(os.path.join(TR,f'trg_{lang}.json'),encoding='utf-8'))
    h=master
    h=h.replace('<html lang="en">',f'<html lang="{lang}">',1)
    h=h.replace(f'<link rel="canonical" href="{DOMAIN}/guides/">',
                f'<link rel="canonical" href="{DOMAIN}/{lang}/guides/">',1)
    # nav switcher
    h=h.replace('<a class="on" href="/guides/">EN</a>','<a href="/guides/">EN</a>',1)
    h=h.replace(f'<a href="/{lang}/guides/">{lang.upper()}</a>',
                f'<a class="on" href="/{lang}/guides/">{lang.upper()}</a>',1)
    # brand + footer links point into the language root
    h=h.replace('<a class="brand" href="/">',f'<a class="brand" href="/{lang}/">',1)
    h=h.replace('<a href="/">Home</a>',f'<a href="/{lang}/">Home</a>',1)
    h=h.replace('<a href="/">Home</a>',f'<a href="/{lang}/">Home</a>')
    h=h.replace('· <a href="/">Home</a>',f'· <a href="/{lang}/">Home</a>')
    missing=unused_keys(h,tmap)
    h=apply_map(h,tmap)
    h=h.replace('&rsaquo; Guides', '&rsaquo; '+CRUMB[lang])
    for k,v in POSTFIX.get(lang,{}).get('guid',{}).items(): h=h.replace(k,v)
    d=os.path.join(PUB,lang,'guides'); os.makedirs(d,exist_ok=True)
    open(os.path.join(d,'index.html'),'w',encoding='utf-8').write(h)
    print(f'{lang}: {len(tmap)} keys, missing {len(missing)}, {len(h)} bytes')
    for m in missing[:5]: print('   !!',repr(m[:70]))
