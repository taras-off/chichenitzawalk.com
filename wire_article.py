#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Привязать опубликованные статьи к навигации сайта.

Идемпотентно и обратимо: карточки на /guides/ ищутся по ЗАГОЛОВКУ, а не по картинке
(картинки повторяются — старая версия скрипта из-за этого включила чужую карточку).
Всё, чего нет в PUBLISHED, возвращается в состояние «Coming soon».
"""
import re, os, json

ROOT  = os.path.dirname(os.path.abspath(__file__))
LANGS = ['en', 'es', 'fr', 'de', 'it', 'pt', 'pl', 'ru']

# опубликованные статьи: слаг + английский заголовок карточки на /guides/
PUBLISHED = [
    {'slug': 'chichen-itza-tour',                 'card_en': 'Guided, Self-Guided or Audio Guide?'},
    {'slug': 'chichen-itza-day-trip-from-cancun', 'card_en': 'Day Trip from Cancún'},
]

READ = {'en':'Read the guide','es':'Leer la guía','fr':'Lire le guide','de':'Guide lesen',
        'it':'Leggi la guida','pt':'Ler o guia','pl':'Czytaj przewodnik','ru':'Читать'}

CARD_CSS = ('.gcard .tag{display:inline-block;margin-top:8px;font-size:11px;font-weight:700;'
            'text-transform:uppercase;letter-spacing:.5px;color:#fff;background:#3f6b39;'
            'border-radius:20px;padding:3px 10px}\n')

def jload(p): return json.load(open(os.path.join(ROOT, p), encoding='utf-8'))

def tr_guides(lang):
    """английская строка -> строка языка (для en — тождество)"""
    if lang == 'en':
        return {s: s for s in jload('tr/strings_guides_en.json')}
    return jload(f'tr/trg_{lang}.json')

def path_for(lang, slug):
    return f'/{slug}/' if lang == 'en' else f'/{lang}/{slug}/'

def meta_for(slug, lang):
    n = '02' if slug == 'chichen-itza-tour' else '03'
    return jload(f'meta/{n}_{lang}.json')

# ------------------------------------------------------------------ 1. меню
def sync_menu(html, lang):
    """Привести выпадающее меню к списку PUBLISHED, сохранив порядок."""
    m = re.search(r'(<div class="dropdown">\s*)(.*?)(\s*<a class="all" )', html, re.S)
    if not m:
        return html, 'нет меню'
    entries = []
    for art in PUBLISHED:
        label = meta_for(art['slug'], lang)['labels']['dropdown']
        entries.append(f'<a href="{path_for(lang, art["slug"])}">{label}</a>')
    new = m.group(1) + '\n'.join(entries) + '\n'
    before = m.group(2).strip()
    html = html[:m.start()] + new + html[m.start(3):].lstrip('\n')
    return html, ('=' if before == '\n'.join(entries) else '+')

# ------------------------------------------------------------- 2. карточки
CARD = re.compile(
    r'<(?P<tag>span|a) class="gcard(?P<cls>[^"]*)"(?: href="(?P<href>[^"]*)")?>'
    r'(?P<inner><img[^>]*>.*?<h3>(?P<title>.*?)</h3>.*?)'
    r'<span class="tag[^"]*">(?P<tagtext>[^<]*)</span>(?P<rest></div>)'
    r'</(?P=tag)>', re.S)

def sync_cards(html, lang):
    tg   = tr_guides(lang)
    soon = tg.get('Coming soon', 'Coming soon')
    live = {tg.get(a['card_en'], a['card_en']): a['slug'] for a in PUBLISHED}
    n_live = n_revert = 0

    def rep(m):
        nonlocal n_live, n_revert
        title = m.group('title')
        if title in live:
            n_live += 1
            href = path_for(lang, live[title])
            return (f'<a class="gcard" href="{href}">{m.group("inner")}'
                    f'<span class="tag live">{READ[lang]} &rarr;</span>{m.group("rest")}</a>')
        if m.group('tag') == 'a':
            n_revert += 1
        return (f'<span class="gcard soon">{m.group("inner")}'
                f'<span class="tag">{soon}</span>{m.group("rest")}</span>')

    html = CARD.sub(rep, html)
    if '.gcard .tag{' not in html:
        html = html.replace('.gcard.soon{opacity:.62;pointer-events:none}',
                            CARD_CSS + '.gcard.soon{opacity:.62;pointer-events:none}', 1)
    return html, n_live, n_revert


if __name__ == '__main__':
    for lang in LANGS:
        base = 'public/' if lang == 'en' else f'public/{lang}/'
        # меню — на лендинге и на всех страницах статей
        pages = [base + 'index.html'] + [base + a['slug'] + '/index.html' for a in PUBLISHED]
        for rel in pages:
            p = os.path.join(ROOT, rel)
            h = open(p, encoding='utf-8').read()
            h, flag = sync_menu(h, lang)
            open(p, 'w', encoding='utf-8').write(h)
        # карточки — на /guides/
        gp = os.path.join(ROOT, base + 'guides/index.html')
        h = open(gp, encoding='utf-8').read()
        h, nl, nr = sync_cards(h, lang)
        open(gp, 'w', encoding='utf-8').write(h)
        print(f'{lang}: меню на {len(pages)} стр. · карточек живых {nl}' +
              (f' · возвращено в «скоро» {nr}' if nr else ''))
