#!/usr/bin/env python3
"""Generate one article page (any language) from a body fragment + meta json."""
import re, os, json, html, sys
import build_article as B

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = B.BASE

def strip_tags(s):
    s = re.sub(r'<[^>]+>', '', s)
    return html.unescape(s).strip()

def extract_faq(body):
    block = re.search(r'<div class="faq">(.*?)</div>', body, re.S)
    if not block:
        return []
    out = []
    for m in re.finditer(r'<details><summary>(.*?)</summary>(.*?)</details>', block.group(1), re.S):
        q = strip_tags(m.group(1))
        a = strip_tags(m.group(2))
        out.append((q, a))
    return out

def extract_h1(body):
    return strip_tags(re.search(r'<h1>(.*?)</h1>', body, re.S).group(1))

def jsonld(meta, body, lang, crumbs):
    url  = BASE + B.path_for(lang, meta['slug'])
    root = BASE + ('/' if lang == 'en' else f'/{lang}/')
    faq  = extract_faq(body)
    g = [
        {"@type": "Article",
         "@id": url + "#article",
         "headline": extract_h1(body),
         "description": html.unescape(meta['desc']),
         "inLanguage": lang,
         "datePublished": "2026-09-13",
         "dateModified": "2026-09-13",
         "mainEntityOfPage": {"@id": url},
         "image": BASE + "/img/hero-1536.webp",
         "author": {"@type": "Person", "@id": BASE + "/#author", "name": "Eugene"},
         "publisher": {"@type": "Organization", "@id": BASE + "/#org", "name": "TouringBee",
                       "url": "https://touringbee.com/"},
         "about": {"@type": "TouristAttraction", "name": crumbs['attraction']}},
        {"@type": "FAQPage",
         "@id": url + "#faq",
         "inLanguage": lang,
         "mainEntity": [{"@type": "Question", "name": q,
                         "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]},
        {"@type": "BreadcrumbList",
         "@id": url + "#crumbs",
         "itemListElement": [
             {"@type": "ListItem", "position": 1, "name": crumbs['home'],   "item": root},
             {"@type": "ListItem", "position": 2, "name": crumbs['guides'], "item": root + "guides/"},
             {"@type": "ListItem", "position": 3, "name": crumbs['self']}]},
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": g},
                      ensure_ascii=False, indent=None, separators=(',', ':'))

def generate(lang, meta_path, body_path, outdir=None):
    meta = json.load(open(meta_path, encoding='utf-8'))
    body = open(body_path, encoding='utf-8').read()
    meta['jsonld'] = jsonld(meta, body, lang, meta['crumbs'])
    page = B.build(meta, body, lang=lang, labels=meta['labels'])
    out = outdir or os.path.join(ROOT, 'public' + B.path_for(lang, meta['slug']))
    os.makedirs(out, exist_ok=True)
    p = os.path.join(out, 'index.html')
    open(p, 'w', encoding='utf-8').write(page)
    return p, len(page), len(extract_faq(body))

if __name__ == '__main__':
    lang = sys.argv[1]
    print(generate(lang, sys.argv[2], sys.argv[3]))
