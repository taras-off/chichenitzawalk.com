#!/usr/bin/env python3
"""Assemble an article page from the landing chrome + a body fragment."""
import re, os, io, json, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
LAND = open(os.path.join(ROOT, 'public/index.html'), encoding='utf-8').read()

def slice_between(s, a, b, inc=True):
    i = s.find(a); j = s.find(b, i)
    return s[i:j+len(b)] if inc else s[i+len(a):j]

CSS    = slice_between(LAND, '<style>', '</style>', inc=False)
HEADER = slice_between(LAND, '<header', '</header>')
FOOTER = slice_between(LAND, '<footer', '</footer>')

ART_CSS = """
/* ---- article page ---- */
.arthero{background:var(--soft);border-bottom:1px solid var(--line);padding:34px 0 30px}
.arthero h1{font-size:38px;line-height:1.15;margin:.15em 0 .2em;max-width:24ch}
.arthero .sub{font-size:19px;color:#33402f;max-width:60ch;margin:0 0 14px}
.crumbs{font-size:13px;color:var(--muted)}
.crumbs a{color:var(--muted);text-decoration:none}
.crumbs a:hover{color:var(--brand-d)}
.byline{display:flex;align-items:center;gap:10px;font-size:14px;color:var(--muted);margin:0 0 16px}
.byline img{width:34px;height:34px;border-radius:50%;object-fit:cover;flex:0 0 auto}
.hbtns{display:flex;flex-wrap:wrap;gap:2px;margin:0 -6px}
.facts{background:var(--soft);border:1px solid var(--line);border-radius:14px;padding:20px 22px;margin:1.8em 0}
.facts h2{font-size:19px;margin:0 0 12px}
.fgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px 22px}
.fgrid div{font-size:15px;line-height:1.45}
.fgrid b{display:block;font-size:13px;text-transform:uppercase;letter-spacing:.4px;color:var(--brand-d)}
.disc{font-size:13px;color:var(--muted);background:#fbfaf5;border-left:3px solid var(--brand);padding:10px 14px;border-radius:0 8px 8px 0}
.prose h2{margin:1.7em 0 .4em}
.prose blockquote{margin:1.4em 0;padding:14px 18px;background:var(--soft);border-left:3px solid var(--brand);border-radius:0 10px 10px 0;font-style:italic;color:#33402f}
.prose blockquote cite{display:block;margin-top:8px;font-style:normal;font-size:13px;color:var(--muted)}
.tablewrap{overflow-x:auto;margin:1.5em 0;-webkit-overflow-scrolling:touch}
table.cmp{border-collapse:collapse;width:100%;min-width:680px;font-size:14.5px}
table.cmp th,table.cmp td{border:1px solid var(--line);padding:10px 12px;text-align:left;vertical-align:top}
table.cmp thead th{background:var(--soft);font-size:13.5px}
table.cmp tbody td:first-child{background:#fbfaf5;white-space:nowrap}
ul.related{list-style:none;padding:0;margin:.6em 0 0}
ul.related li{padding:10px 0;border-bottom:1px solid var(--line);font-size:15px}
ul.related a{font-weight:600;text-decoration:none}
ul.related a:hover{text-decoration:underline}
@media(max-width:640px){.arthero h1{font-size:29px}.arthero .sub{font-size:17px}.hbtns .btn{width:100%;text-align:center}}
"""

LANGS = ['en','es','fr','de','it','pt','pl','ru']
BASE  = 'https://chichenitzawalk.com'
def path_for(lang, slug):
    return f'/{slug}/' if lang == 'en' else f'/{lang}/{slug}/'

STICKY = """<div class="stickybuy" id="stickybuy">
<div class="p">{sticky_title} <small>{sticky_sub}</small></div>
<a class="btn bokunButton" href="{bokun_href}" data-src="{bokun_src}">{sticky_btn}</a>
</div>
<script>(function(){{var b=document.getElementById('stickybuy');if(!b)return;function s(){{if(window.scrollY>800){{b.classList.add('show')}}else{{b.classList.remove('show')}}}}window.addEventListener('scroll',s,{{passive:true}});s();}})();</script>

<script>/* Lazy-load Bokun engine only on first user interaction so it never blocks page load / Lighthouse */(function(){{var l=0;function b(){{if(l)return;l=1;var s=document.createElement('script');s.async=true;s.src='https://widgets.bokun.io/assets/javascripts/apps/build/BokunWidgetsLoader.js?bookingChannelUUID=028dc54f-646b-4b9d-a0f0-e1c5746da99a';document.body.appendChild(s);}}['mouseover','touchstart','scroll','keydown','pointerdown'].forEach(function(e){{window.addEventListener(e,b,{{once:true,passive:true}});}});}})();</script>"""


# ---------------------------------------------------------------- chrome
SHORT = {  # dropdown label per language, filled by the caller
}

def chrome(lang, slug, labels):
    """Return (header, footer) localized for `lang` with the new guide in the menu."""
    root  = '/' if lang == 'en' else f'/{lang}/'
    gpath = root + 'guides/'
    apath = path_for(lang, slug)

    h = HEADER
    h = h.replace('<a class="brand" href="/">', f'<a class="brand" href="{root}">')
    h = h.replace('<summary>Guides ', '<summary>%s ' % labels['menu'])
    h = h.replace('<a class="all" href="/guides/">All guides &rarr;</a>',
                  f'<a href="{apath}">{labels["dropdown"]}</a>\n'
                  f'<a class="all" href="{gpath}">{labels["all"]} &rarr;</a>')
    nav = ''.join(
        '<a%s href="%s">%s</a>' % (' class="on"' if l == lang else '', path_for(l, slug), l.upper())
        for l in LANGS)
    h = re.sub(r'<nav class="lang">.*?</nav>', '<nav class="lang">%s</nav>' % nav, h, flags=re.S)

    f = FOOTER
    f = f.replace('href="#inside"',  f'href="{root}#inside"')
    f = f.replace('href="#preview"', f'href="{root}#preview"')
    f = f.replace('href="/guides/"', f'href="{gpath}"')
    return h, f


def build(meta, body, lang='en', labels=None):
    slug = meta['slug']
    url  = BASE + path_for(lang, slug)
    alts = '\n'.join(
        f'<link rel="alternate" hreflang="{l}" href="{BASE}{path_for(l, slug)}">' for l in LANGS
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{BASE}{path_for("en", slug)}">'
    oglocalt = '\n'.join(f'<meta property="og:locale:alternate" content="{l}">' for l in LANGS if l != lang)

    head = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{meta['title']}</title>
<meta name="description" content="{meta['desc']}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="{meta['site_name']}">
<meta property="og:title" content="{meta['og_title']}">
<meta property="og:description" content="{meta['og_desc']}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/img/hero-1536.webp">
<meta property="og:locale" content="{lang}">
{oglocalt}
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{meta['og_title']}">
<meta name="twitter:description" content="{meta['og_desc']}">
<meta name="twitter:image" content="{BASE}/img/hero-1536.webp">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/favicon-180.png">
<link rel="canonical" href="{url}">
{alts}
<style>
{CSS}{ART_CSS}</style>
<script type="application/ld+json">
{meta['jsonld']}
</script>
</head>
<body>
"""
    sticky = STICKY.format(**meta['sticky'])
    hdr, ftr = chrome(lang, slug, labels)
    return head + '\n' + hdr + '\n\n' + body.strip() + '\n\n' + ftr + '\n\n' + sticky + '\n</body>\n</html>\n'
