#!/usr/bin/env python3
"""Wire article #2 into the site: header dropdown on every page + live /guides/ card."""
import re, os, json, glob

ROOT  = os.path.dirname(os.path.abspath(__file__))
LANGS = ['en','es','fr','de','it','pt','pl','ru']
SLUG  = 'chichen-itza-tour'

READ = {'en':'Read the guide','es':'Leer la guía','fr':'Lire le guide','de':'Guide lesen',
        'it':'Leggi la guida','pt':'Ler o guia','pl':'Czytaj przewodnik','ru':'Читать'}

def meta(l):
    return json.load(open(os.path.join(ROOT,'meta',f'02_{l}.json'), encoding='utf-8'))

def pages(l):
    """All pages of one language that carry the shared header."""
    p = 'public/' if l == 'en' else f'public/{l}/'
    return [os.path.join(ROOT, p+'index.html'), os.path.join(ROOT, p+'guides/index.html')]

# ---------------------------------------------------------------- 1. dropdown
def add_to_menu(html, l):
    apath = f'/{SLUG}/' if l == 'en' else f'/{l}/{SLUG}/'
    label = meta(l)['labels']['dropdown']
    entry = f'<a href="{apath}">{label}</a>'
    if entry in html:
        return html, False
    m = re.search(r'<a class="all" href="[^"]*">', html)
    if not m:
        raise SystemExit(f'no "all guides" link in {l}')
    return html[:m.start()] + entry + '\n' + html[m.start():], True

# ---------------------------------------------------------------- 2. live card
CARD_RE = re.compile(
    r'<span class="gcard soon">(<img src="/img/partner-gyg-800\.webp".*?)'
    r'<span class="tag">[^<]*</span>(</div>)</span>', re.S)

def go_live(html, l):
    apath = f'/{SLUG}/' if l == 'en' else f'/{l}/{SLUG}/'
    tag   = f'<span class="tag live">{READ[l]} &rarr;</span>'
    def rep(m):
        return f'<a class="gcard" href="{apath}">{m.group(1)}{tag}{m.group(2)}</a>'
    out, n = CARD_RE.subn(rep, html, count=1)
    return out, n

CARD_CSS = ('.gcard .tag{display:inline-block;margin-top:8px;font-size:11px;font-weight:700;'
            'text-transform:uppercase;letter-spacing:.5px;color:#fff;background:#3f6b39;'
            'border-radius:20px;padding:3px 10px}\n')

def add_card_css(html):
    anchor = '.gcard.soon{opacity:.62;pointer-events:none}'
    if '.gcard .tag{' in html:
        return html, False
    return html.replace(anchor, CARD_CSS + anchor, 1), True


if __name__ == '__main__':
    log = []
    for l in LANGS:
        for p in pages(l):
            h = open(p, encoding='utf-8').read()
            m1 = False
            n2 = 0
            if p.endswith('guides/index.html'):
                h, ok = add_card_css(h)
                h, n2 = go_live(h, l)
            else:
                h, m1 = add_to_menu(h, l)
            open(p, 'w', encoding='utf-8').write(h)
            log.append(f'{os.path.relpath(p, ROOT):38} menu={"+" if m1 else "="} card={n2}')
    print('\n'.join(log))
