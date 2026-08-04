#!/usr/bin/env python3
"""Generate the 7 localized landings of chichenitzawalk.com from the EN master.

EN master = public/index.html  (single source of truth)
Text maps = tr/tr_<lang>.json  (localized, not translated)

Order: config/URL swaps first, then the text map applied longest-key-first.
"""
import json, os, re, sys
from localize import apply_map, unused_keys

ROOT = os.path.dirname(os.path.abspath(__file__))
PUB  = os.path.join(ROOT, 'public')
TR   = os.path.join(ROOT, 'tr')

DOMAIN = 'https://chichenitzawalk.com'
TB     = 'https://touringbee.com'

# per-language config
CFG = {
 'fr': dict(locale='fr_FR', tiqets='fr', gyg='fr-fr', booking='fr',
            product=f'{TB}/fr/product/chichen-itza-tour-fr/', shop=f'{TB}/fr/shop-tbee-fr/'),
 'de': dict(locale='de_DE', tiqets='de', gyg='de-de', booking='de',
            product=f'{TB}/de/product/chichen-itza-tour-de/', shop=f'{TB}/de/shop-tbee-de/'),
 'es': dict(locale='es_ES', tiqets='es', gyg='es-es', booking='es',
            product=f'{TB}/es/product/chichen-itza-tour-es/', shop=f'{TB}/es/shop-tbee-es/'),
 'it': dict(locale='it_IT', tiqets='it', gyg='it-it', booking='it',
            product=f'{TB}/product/chichen-itza-tour-it/', shop=f'{TB}/shop-tbee/'),
 'pt': dict(locale='pt_PT', tiqets='pt', gyg='pt-pt', booking='pt',
            product=f'{TB}/product/excursao-a-chichen-itza/', shop=f'{TB}/shop-tbee/'),
 'pl': dict(locale='pl_PL', tiqets='pl', gyg='pl-pl', booking='pl',
            product=f'{TB}/pl/product/chichen-itza-tour-pl/', shop=f'{TB}/pl/shop-tbee-pl/'),
 'ru': dict(locale='ru_RU', tiqets='ru', gyg='ru-ru', booking='ru',
            product=f'{TB}/ru/product/chichen-itza-tour-ru/', shop=f'{TB}/ru/shop-tbee-ru/'),
}

# cross-sell products that have a localized version; everything else falls back to EN
CROSS_LOCALIZED = {
  'it': {
    f'{TB}/product/tulum-ruins-walking-tour/': f'{TB}/product/visita-a-piedi-delle-rovine-di-tulum/',
    f'{TB}/product/mexico-pyramids-of-teotihuacan/': f'{TB}/product/citta-del-messico-audioguida-alle-piramidi-di-teotihuacan/',
  },
}

# Bits the text map cannot carry: a bare price span with no unique wrapper,
# the header menu word, and (RU) the Cyrillic form of the attraction name.
EXTRA = {
 'fr': {'>From &euro;9.99<': '>Dès 9,99 &euro;<', '<summary>Guides ': '<summary>Guides '},
 'de': {'>From &euro;9.99<': '>Ab 9,99 &euro;<',  '<summary>Guides ': '<summary>Guides '},
 'es': {'>From &euro;9.99<': '>Desde 9,99 &euro;<', '<summary>Guides ': '<summary>Guías '},
 'it': {'>From &euro;9.99<': '>Da 9,99 &euro;<',  '<summary>Guides ': '<summary>Guide '},
 'pt': {'>From &euro;9.99<': '>A partir de 9,99 &euro;<', '<summary>Guides ': '<summary>Guias '},
 'pl': {'>From &euro;9.99<': '>Od 9,99 &euro;<',  '<summary>Guides ': '<summary>Przewodniki '},
 'ru': {'>From &euro;9.99<': '>От 9,99 &euro;<',  '<summary>Guides ': '<summary>Гиды ',
        '"@type":"TouristAttraction","name":"Chichén Itzá"':
        '"@type":"TouristAttraction","name":"Чичен-Ица"'},
}

POSTFIX = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'tr','postfix.json'), encoding='utf-8'))

BOKUN_BASE = 'https://widgets.bokun.io/online-sales/028dc54f-646b-4b9d-a0f0-e1c5746da99a/experience/790505'


def localize(html: str, lang: str, tmap: dict) -> str:
    c = CFG[lang]
    h = html

    # ---- 1. document language + canonical + og ----
    h = h.replace('<html lang="en">', f'<html lang="{lang}">', 1)
    h = h.replace(f'<link rel="canonical" href="{DOMAIN}/">',
                  f'<link rel="canonical" href="{DOMAIN}/{lang}/">', 1)
    h = h.replace(f'<meta property="og:url" content="{DOMAIN}/">',
                  f'<meta property="og:url" content="{DOMAIN}/{lang}/">', 1)
    h = h.replace('<meta property="og:locale" content="en">',
                  f'<meta property="og:locale" content="{c["locale"]}">', 1)

    # ---- 2. nav language switcher: move the active marker ----
    h = h.replace('<a class="on" href="/">EN</a>', '<a href="/">EN</a>', 1)
    h = h.replace(f'<a href="/{lang}/">{lang.upper()}</a>',
                  f'<a class="on" href="/{lang}/">{lang.upper()}</a>', 1)

    # ---- 3. audio preview ----
    h = h.replace('/audio/cancunt1_en_intro.mp3', f'/audio/cancunt1_{lang}_intro.mp3')

    # ---- 4. Bokun: append the page language (English omits it) ----
    h = h.replace(f'{BOKUN_BASE}?partialView=1', f'{BOKUN_BASE}?partialView=1&amp;lang={lang}')
    h = h.replace(f'href="{BOKUN_BASE}"', f'href="{BOKUN_BASE}?lang={lang}"')

    # ---- 5. TouringBee product + shop under the page language ----
    h = h.replace(f'"url":"{TB}/product/chichen-itza-tour/"', f'"url":"{c["product"]}"')
    h = h.replace(f'{TB}/shop-tbee/?wpam_id=40', f'{c["shop"]}?wpam_id=40')
    h = h.replace(f'href="{TB}/shop-tbee/"', f'href="{c["shop"]}"')
    for en_url, loc_url in CROSS_LOCALIZED.get(lang, {}).items():
        h = h.replace(en_url, loc_url)

    # ---- 6. OTA partners under the page language ----
    h = h.replace('https://www.tiqets.com/en/chichen-itza-tickets-l146416/',
                  f'https://www.tiqets.com/{c["tiqets"]}/chichen-itza-tickets-l146416/')
    h = h.replace('https://www.getyourguide.com/chichen-itza-l785/',
                  f'https://www.getyourguide.com/{c["gyg"]}/chichen-itza-l785/')
    h = h.replace('https://www.booking.com/searchresults.en.html',
                  f'https://www.booking.com/searchresults.{c["booking"]}.html')
    h = h.replace('https://www.booking.com/cars/index.html',
                  f'https://www.booking.com/cars/index.{c["booking"]}.html')

    # ---- 7. internal links one level down ----
    h = h.replace('href="/guides/"', f'href="/{lang}/guides/"')

    # ---- 8. JSON-LD graph ids + inLanguage ----
    h = h.replace(f'"{DOMAIN}/#org"', f'"{DOMAIN}/{lang}/#org"')
    h = h.replace(f'"{DOMAIN}/#site"', f'"{DOMAIN}/{lang}/#site"')
    h = h.replace(f'"{DOMAIN}/#author"', f'"{DOMAIN}/{lang}/#author"')
    h = h.replace(f'"url":"{DOMAIN}/","publisher"', f'"url":"{DOMAIN}/{lang}/","publisher"')
    h = h.replace('"inLanguage":"en"', f'"inLanguage":"{lang}"')
    h = h.replace(f'"item":"{DOMAIN}/"', f'"item":"{DOMAIN}/{lang}/"')

    # ---- 9. text map, ONE pass (see localize.py for why) ----
    missing = unused_keys(h, tmap)
    h = apply_map(h, tmap)

    # ---- 10. strings the map cannot express (bare price span, chrome words) ----
    for k, v in EXTRA[lang].items():
        h = h.replace(k, v)

    # ---- 11. proofreading fixes that span markup (see tr/postfix.json) ----
    for k, v in POSTFIX.get(lang, {}).get('land', {}).items():
        h = h.replace(k, v)
    return h, missing


def main():
    master = open(os.path.join(PUB, 'index.html'), encoding='utf-8').read()
    report = {}
    for lang in CFG:
        tmap = json.load(open(os.path.join(TR, f'tr_{lang}.json'), encoding='utf-8'))
        out, missing = localize(master, lang, tmap)
        d = os.path.join(PUB, lang)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(out)
        report[lang] = dict(keys=len(tmap), missing=len(missing), bytes=len(out))
        print(f'{lang}: {len(tmap)} keys, missing {len(missing)}, {len(out)} bytes')
        for m in missing[:5]:
            print('   !! not found:', repr(m[:80]))
    return report


if __name__ == '__main__':
    main()
