#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Собрать public/sitemap.xml. Единственное место, где перечислены страницы сайта.
Добавляя статью, дописывай строку в ARTICLES — иначе она не попадёт в карту сайта."""
import io, os

BASE  = 'https://chichenitzawalk.com'
LANGS = ['en','es','fr','de','it','pt','pl','ru']

LANDING = ('', '2026-08-04', 'weekly', '1.0')
GUIDES  = ('guides/', '2026-08-04', 'weekly', '0.7')

# слаг, lastmod, changefreq, priority
ARTICLES = [
    ('chichen-itza-tour',                 '2026-09-13', 'monthly', '0.8'),
    ('chichen-itza-day-trip-from-cancun', '2026-09-25', 'monthly', '0.8'),
    ('chichen-itza-self-guided-tour',     '2026-10-01', 'monthly', '0.8'),
]

LEGAL = [('privacy-policy.html', '2026-08-04', '0.2'),
         ('affiliate-disclosure.html', '2026-08-04', '0.2')]

def url_for(lang, path):
    return f'{BASE}/{path}' if lang == 'en' else f'{BASE}/{lang}/{path}'

def block(lang, path, lastmod, changefreq, priority):
    out = ['<url>', f'<loc>{url_for(lang, path)}</loc>', f'<lastmod>{lastmod}</lastmod>']
    if changefreq: out.append(f'<changefreq>{changefreq}</changefreq>')
    out.append(f'<priority>{priority}</priority>')
    for l in LANGS:
        out.append(f'<xhtml:link rel="alternate" hreflang="{l}" href="{url_for(l, path)}"/>')
    out.append(f'<xhtml:link rel="alternate" hreflang="x-default" href="{url_for("en", path)}"/>')
    out.append('</url>')
    return '\n'.join(out)

def main():
    parts = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
             'xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for path, lm, cf, pr in [LANDING, GUIDES]:
        for l in LANGS:
            parts.append(block(l, path, lm, cf, pr))
    for slug, lm, cf, pr in ARTICLES:
        for l in LANGS:
            p = f'public/{slug}/index.html' if l == 'en' else f'public/{l}/{slug}/index.html'
            if not os.path.exists(p):
                print(f'   !! нет страницы, пропускаю: {p}'); continue
            parts.append(block(l, f'{slug}/', lm, cf, pr))
    for f, lm, pr in LEGAL:
        parts += ['<url>', f'<loc>{BASE}/{f}</loc>', f'<lastmod>{lm}</lastmod>',
                  f'<priority>{pr}</priority>', '</url>']
    parts.append('</urlset>')
    xml = '\n'.join(parts) + '\n'
    io.open('public/sitemap.xml', 'w', encoding='utf-8').write(xml)
    print(f'sitemap.xml: {xml.count("<url>")} URL, {len(xml)} байт')

if __name__ == '__main__':
    main()
