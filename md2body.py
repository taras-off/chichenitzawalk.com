#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Собрать HTML-тело статьи сайта из markdown-мастера статьи №3."""
import re, sys, html as H

BK = 'https://widgets.bokun.io/online-sales/028dc54f-646b-4b9d-a0f0-e1c5746da99a/experience/790505'

def inline(t):
    """markdown inline -> html, с сохранением уже готовых сущностей"""
    t = t.replace('&', '\x00').replace('<', '&lt;').replace('>', '&gt;')
    t = re.sub(r'\x00(#?\w{2,8};)', r'&\1', t)   # вернуть готовые &euro; &amp; &rarr; &#9733;
    t = t.replace('\x00', '&amp;')
    t = re.sub(r'\[\*\*(.+?)\*\*\]\((.+?)\)', r'[[BTN:\2|\1]]', t)
    t = re.sub(r'\[(.+?)\]\((.+?)\)', r'[[LNK:\2|\1]]', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\w)\*(?!\s)(.+?)(?<!\s)\*(?!\w)', r'<em>\1</em>', t)
    def lnk(m):
        u, txt = m.group(1), m.group(2)
        u = u.replace('&amp;', '&amp;')
        ext = ' target="_blank" rel="noopener sponsored"' if u.startswith('http') and 'bokun' not in u else ''
        return f'<a href="{u}"{ext}>{txt}</a>'
    t = re.sub(r'\[\[LNK:(.+?)\|(.+?)\]\]', lnk, t)
    t = re.sub(r'\[\[BTN:(.+?)\|(.+?)\]\]', lnk, t)
    t = t.replace('€', '&euro;').replace('→', '&rarr;').replace('·', '&middot;')
    return t

def parse(md):
    """-> список блоков (тип, данные)"""
    body = md.split('\n---\n', 1)[1]
    out, buf, i = [], [], 0
    lines = body.split('\n')
    while i < len(lines):
        ln = lines[i]
        if ln.startswith('## '):   out.append(('h2', ln[3:].strip()))
        elif ln.startswith('### '): out.append(('h3', ln[4:].strip()))
        elif ln.startswith('|'):
            tbl = []
            while i < len(lines) and lines[i].startswith('|'):
                tbl.append(lines[i]); i += 1
            out.append(('table', tbl)); continue
        elif ln.startswith('> '):
            q = []
            while i < len(lines) and (lines[i].startswith('>')):
                q.append(lines[i].lstrip('>').strip()); i += 1
            out.append(('quote', [x for x in q if x])); continue
        elif ln.startswith('- '):
            li = []
            while i < len(lines) and lines[i].startswith('- '):
                li.append(lines[i][2:].strip()); i += 1
            out.append(('ul', li)); continue
        elif ln.strip() == '---': out.append(('hr', None))
        elif ln.strip(): out.append(('p', ln.strip()))
        i += 1
    return out


# ---------------------------------------------------------------- шаблоны
SVG = {
 'off':'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M2 2l20 20"/><path d="M5 12.5a11 11 0 0 1 14 0"/><path d="M8.5 16a6 6 0 0 1 7 0"/><circle cx="12" cy="19.5" r="1"/></svg>',
 'gps':'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-7-6-7-11a7 7 0 0 1 14 0c0 5-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/></svg>',
 'lang':'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a15 15 0 0 1 0 18M12 3a15 15 0 0 0 0 18"/></svg>',
 'phone':'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="7" y="3" width="10" height="18" rx="2"/><line x1="11" y1="18" x2="13" y2="18"/></svg>',
 'clock':'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
}

def facts_grid(tbl, title):
    rows = [r for r in tbl if not re.match(r'^\|[\s\-|]+\|$', r)]
    cells = []
    for r in rows:
        p = [x.strip() for x in r.strip('|').split('|')]
        if len(p) < 2 or not p[0]: continue
        k = re.sub(r'\*\*(.+?)\*\*', r'\1', p[0])
        cells.append(f'<div><b>{inline(k)}</b>{inline(p[1])}</div>')
    return (f'<div class="facts">\n<h2>{inline(title)}</h2>\n<div class="fgrid">\n'
            + '\n'.join(cells) + '\n</div>\n</div>')

def cmp_table(tbl):
    rows = [r for r in tbl if not re.match(r'^\|[\s\-|]+\|$', r)]
    head = [x.strip() for x in rows[0].strip('|').split('|')]
    out = ['<div class="tablewrap"><table class="cmp">',
           '<thead><tr>' + ''.join(f'<th>{inline(h)}</th>' for h in head) + '</tr></thead>', '<tbody>']
    for r in rows[1:]:
        p = [x.strip() for x in r.strip('|').split('|')]
        tds = ''.join(f'<td>{inline(re.sub(chr(42)*2+"(.+?)"+chr(42)*2, r"<b>"+chr(92)+"1</b>", x))}</td>'
                      if False else f'<td>{inline(x)}</td>' for x in p)
        tds = tds.replace('<td><strong>', '<td><b>').replace('</strong></td>', '</b></td>')
        out.append('<tr>' + tds + '</tr>')
    out += ['</tbody></table></div>']
    return '\n'.join(out)

def product_card(L):
    lang = '' if L['lang'] == 'en' else f'&amp;lang={L["lang"]}'
    href = BK if L['lang'] == 'en' else BK + f'?lang={L["lang"]}'
    ds = BK + '?partialView=1' + lang
    feats = '\n'.join(f'<li>{SVG[k]} {inline(v)}</li>' for k, v in L['features'])
    return f'''<section id="product"><div class="wrap">
<div class="product-card">
<img class="pc-img" width="1024" height="768" loading="lazy" decoding="async" src="/img/product-audioguide.webp" alt="{L['img_alt']}">
<div class="pc-body" style="text-align:left">
<div class="pc-rating"><b style="color:var(--ink)"><span class="star" aria-hidden="true">&#9733;</span> {inline(L['rating'])}</b> &middot; {inline(L['used_by'])}</div>
<h3>{inline(L['product_name'])}<span class="badge">{inline(L['badge'])}</span></h3>
<div class="pc-price">{inline(L['price'])} <small>&middot; {inline(L['access'])}</small></div>
<ul class="features">
{feats}
</ul>
<a class="btn bokunButton block" href="{href}" data-src="{ds}">{inline(L['buy'])}</a>
</div>
</div>
</div></section>'''


def build(md, L):
    blocks = parse(md)
    lang = L['lang']
    q    = '' if lang == 'en' else f'?lang={lang}'
    dsq  = '?partialView=1' if lang == 'en' else f'?partialView=1&amp;lang={lang}'
    root = '/' if lang == 'en' else f'/{lang}/'

    def bokun_inline(txt):
        return (f'<a class="bokunButton inlinebuy" target="_blank" rel="noopener" '
                f'href="{BK}{q}" data-src="{BK}{dsq}">{inline(txt)}</a>')
    def bokun_btn(txt, cls='btn bokunButton'):
        return f'<a class="{cls}" href="{BK}{q}" data-src="{BK}{dsq}">{inline(txt)}</a>'

    # --- шапка статьи ---
    h1 = next(b for t, b in blocks if t == 'h2')
    out = [f'''<div class="arthero"><div class="wrap">
<nav class="crumbs"><a href="{root}">{inline(L['home'])}</a> &rsaquo; <a href="{root}guides/">{inline(L['guides'])}</a> &rsaquo; {inline(L['crumb3'])}</nav>
<h1>{inline(h1)}</h1>
<p class="sub">{inline(L['sub'])}</p>
<div class="byline"><img src="/img/author-eugene.webp" width="34" height="34" loading="lazy" alt="{inline(L['author_alt'])}"><span>{L["byline"]}</span></div>
<div class="hbtns">
{bokun_btn(L['hero_buy'])}
<a class="btn outline" href="{L['gyg']}" target="_blank" rel="noopener sponsored">{inline(L['hero_gyg'])}</a>
<a class="btn outline" href="{L['tiqets']}" target="_blank" rel="noopener sponsored">{inline(L['hero_tiqets'])}</a>
</div>
</div></div>

<section><div class="wrap prose">
''']

    open_sec = True
    first_p  = True
    i = 0
    while i < len(blocks):
        t, b = blocks[i]
        if t == 'h2' and b == h1:
            i += 1; continue

        # секция товара: h2 + проза + карточка
        if t == 'h2' and b == L['product_h2_md']:
            out.append('</div></section>\n\n<section><div class="wrap prose">\n')
            out.append(f'<h2>{inline(b)}</h2>\n')
            i += 1
            while i < len(blocks) and blocks[i][0] in ('p',):
                txt = blocks[i][1]
                if txt.startswith('[**'):
                    i += 1; continue          # финальный CTA блока -> кнопка карточки
                out.append(f'<p>{inline(txt)}</p>\n'); i += 1
            out.append('</div></section>\n\n')
            out.append(product_card(L) + '\n\n<section><div class="wrap prose">\n')
            continue

        if t == 'hr':
            i += 1; continue

        if t == 'h2':
            # FAQ и «читать дальше» — особые
            if b == L['faq_h2_md']:
                out.append(f'<h2>{inline(b)}</h2>\n<div class="faq">\n')
                i += 1
                while i < len(blocks) and blocks[i][0] == 'p':
                    txt = blocks[i][1]
                    if txt.startswith('[**'): break
                    m = re.match(r'^\*\*(.+?)\*\*\s*(.*)$', txt, re.S)
                    if m:
                        qq, aa = m.group(1), m.group(2).strip()
                        if not aa and i + 1 < len(blocks) and blocks[i+1][0] == 'p':
                            i += 1; aa = blocks[i][1]
                        out.append(f'<details><summary>{inline(qq)}</summary><p>{inline(aa)}</p></details>\n')
                    i += 1
                out.append('</div>\n')
                continue
            if b == L['related_h2_md']:
                out.append(f'<h2>{inline(b)}</h2>\n<ul class="related">\n')
                i += 1
                while i < len(blocks) and blocks[i][0] == 'ul':
                    for it in blocks[i][1]:
                        out.append(f'<li>{inline(it)}</li>\n')
                    i += 1
                out.append('</ul>\n')
                continue
            out.append(f'<h2>{inline(b)}</h2>\n')

        elif t == 'h3':
            if b == L['glance_h3_md']:
                if blocks[i+1][0] == 'table':
                    out.append(facts_grid(blocks[i+1][1], b) + '\n'); i += 2; continue
            anchor = ' id="audio"' if b == L.get('audio_h3_md') else ''
            out.append(f'<h3{anchor}>{inline(b)}</h3>\n')

        elif t == 'table':
            out.append(cmp_table(b) + '\n')

        elif t == 'quote':
            txt = ' '.join(x for x in b if not x.startswith('[**'))
            cta = next((x for x in b if x.startswith('[**')), None)
            lead = re.match(r'^\*\*(.+?)\*\*\s*(.*)$', txt, re.S)
            head, rest = (lead.group(1), lead.group(2)) if lead else ('', txt)
            out.append(f'<div class="midcta">\n<p class="price">{inline(head)}</p>\n<p>{inline(rest)}</p>\n')
            if cta:
                m = re.match(r'\[\*\*(.+?)\*\*\]', cta)
                out.append(bokun_btn(m.group(1)) + '\n')
            out.append('</div>\n')

        elif t == 'ul':
            out.append('<ul>\n' + '\n'.join(f'<li>{inline(x)}</li>' for x in b) + '\n</ul>\n')

        elif t == 'p':
            if b.startswith('[**') and 'bokun' in b and i + 1 < len(blocks) and blocks[i+1] == ('hr', None) \
               and i + 2 < len(blocks) and blocks[i+2][1] == L['related_h2_md']:
                i += 1; continue          # финальный CTA перед «читать дальше» — его делает section.final
            if b.startswith('[**') and 'bokun' in b:
                m = re.match(r'\[\*\*(.+?)\*\*\]', b)
                out.append(f'<p>{bokun_inline(m.group(1))}</p>\n')
            elif b.startswith('*') and not b.startswith('**') and b.endswith('*'):
                out.append(f'<p class="disc">{inline(b.strip("*"))}</p>\n')
            else:
                cls = ' class="lead"' if first_p else ''
                out.append(f'<p{cls}>{inline(b)}</p>\n'); first_p = False
                i += 1; continue
        i += 1

    out.append('</div></section>\n\n')
    out.append(f'''<section class="final"><div class="wrap">
<h2>{inline(L['final_h2'])}</h2>
<p>{inline(L['final_p'])}</p>
{bokun_btn(L['final_btn'])}
</div></section>''')
    return ''.join(out)
