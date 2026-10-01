#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Собрать L/04_<lang>.json: хром и карточку товара берём из статьи №3, строки статьи №4 — из OVER."""
import re, io, json

LANGS = ['es','fr','de','it','pt','pl','ru']
SVGKEY = ['off','gps','lang','phone','clock']

OVER = {
 'es': dict(crumb3='Por tu cuenta',
   sub='La entrada se movió en 2026 y casi todas las descripciones del recorrido siguen hablando de la antigua. Orden, distancias, horarios y tiempos honestos.',
   byline='Por <strong>Eugene</strong> &middot; actualizado el 1 de octubre de 2026 &middot; 13 min de lectura',
   product_h2_md='A quién le conviene el paseo autoguiado con audioguía',
   hero_gyg='Comparar visitas guiadas en GetYourGuide'),
 'fr': dict(crumb3='En autonomie',
   sub="L'entrée a changé de place en 2026 et presque toutes les descriptions d'itinéraire décrivent encore l'ancienne. Ordre, distances, horaires et durées honnêtes.",
   byline='Par <strong>Eugene</strong> &middot; mis à jour le 1er octobre 2026 &middot; 13 min de lecture',
   product_h2_md="À qui convient la visite audio en autonomie",
   hero_gyg='Comparer les visites guidées sur GetYourGuide'),
 'de': dict(crumb3='Auf eigene Faust',
   sub='Der Eingang ist 2026 umgezogen, und fast alle Rundgangsbeschreibungen beschreiben noch den alten. Reihenfolge, Entfernungen, Öffnungszeiten und ehrliche Zeiten.',
   byline='Von <strong>Eugene</strong> &middot; aktualisiert am 1. Oktober 2026 &middot; 13 Min. Lesezeit',
   product_h2_md='Für wen der selbstgeführte Audiorundgang passt',
   hero_gyg='Führungen auf GetYourGuide vergleichen'),
 'it': dict(crumb3='In autonomia',
   sub="L'ingresso si è spostato nel 2026 e quasi tutte le descrizioni del percorso parlano ancora di quello vecchio. Ordine, distanze, orari e tempi onesti.",
   byline='Di <strong>Eugene</strong> &middot; aggiornato il 1 ottobre 2026 &middot; 13 min di lettura',
   product_h2_md="A chi conviene la visita in autonomia con audioguida",
   hero_gyg='Confronta le visite guidate su GetYourGuide'),
 'pt': dict(crumb3='Por conta própria',
   sub='A entrada mudou de lugar em 2026 e quase todas as descrições do percurso continuam a descrever a antiga. Ordem, distâncias, horários e tempos honestos.',
   byline='Por <strong>Eugene</strong> &middot; atualizado a 1 de outubro de 2026 &middot; 13 min de leitura',
   product_h2_md='A quem se adequa o passeio autoguiado com áudio',
   hero_gyg='Comparar visitas guiadas no GetYourGuide'),
 'pl': dict(crumb3='Samodzielnie',
   sub='Wejście przeniesiono w 2026 roku, a niemal wszystkie opisy trasy wciąż opisują stare. Kolejność, odległości, godziny i uczciwe czasy.',
   byline='Autor: <strong>Eugene</strong> &middot; aktualizacja 1 października 2026 &middot; 13 min czytania',
   product_h2_md='Komu pasuje samodzielny spacer z audioprzewodnikiem',
   hero_gyg='Porównaj wycieczki z przewodnikiem na GetYourGuide'),
 'ru': dict(crumb3='Самостоятельно',
   sub='Вход переехал в 2026 году, и почти все описания маршрута до сих пор ведут через старый. Порядок обхода, расстояния, часы и честное время.',
   byline='Автор: <strong>Евгений</strong> &middot; обновлено 1 октября 2026 &middot; 13 мин чтения',
   product_h2_md='Кому подойдёт самостоятельная прогулка с аудиогидом',
   hero_gyg='Сравнить экскурсии с гидом на GetYourGuide'),
}

def g(s, p, grp=1):
    m = re.search(p, s, re.S)
    return m.group(grp).strip() if m else None

for L in LANGS:
    s = io.open(f'drafts/03-body-{L}.html', encoding='utf-8').read()
    o = OVER[L]
    crumbs = re.search(r'<nav class="crumbs">(.*?)</nav>', s, re.S).group(1)
    a = re.findall(r'<a[^>]*>(.*?)</a>', crumbs)
    rating_blk = g(s, r'<div class="pc-rating">(.*?)</div>')
    rating = g(rating_blk, r'</span>\s*(.*?)</b>')
    used_by = rating_blk.split('</b>')[1].lstrip(' &middot;').strip()
    feats_html = re.findall(r'<li><svg.*?</svg>\s*(.*?)</li>', s, re.S)
    d = {
      'lang': L,
      'home': a[0], 'guides': a[1], 'crumb3': o['crumb3'],
      'sub': o['sub'],
      'author_alt': g(s, r'<div class="byline"><img[^>]*alt="([^"]*)"'),
      'byline': o['byline'],
      'hero_buy': g(s, r'<div class="hbtns">\s*<a class="btn bokunButton"[^>]*>(.*?)</a>'),
      'hero_gyg': o['hero_gyg'],
      'hero_tiqets': g(s, r'<a class="btn outline" href="https://www\.tiqets\.com[^"]*"[^>]*>(.*?)</a>'),
      'gyg': g(s, r'<a class="btn outline" href="(https://www\.getyourguide\.com[^"]*)"'),
      'tiqets': g(s, r'<a class="btn outline" href="(https://www\.tiqets\.com[^"]*)"'),
      'glance_h3_md': g(s, r'<div class="facts">\s*<h2>(.*?)</h2>'),
      'product_h2_md': o['product_h2_md'],
      'faq_h2_md': g(s, r'<h2>([^<]*?)</h2>\s*<div class="faq">'),
      'related_h2_md': g(s, r'<h2>([^<]*?)</h2>\s*<ul class="related">'),
      'img_alt': g(s, r'<img class="pc-img"[^>]*alt="([^"]*)"'),
      'rating': rating, 'used_by': used_by,
      'product_name': g(s, r'<div class="pc-body"[^>]*>.*?<h3>(.*?)<span class="badge">'),
      'badge': g(s, r'<span class="badge">(.*?)</span>'),
      'price': g(s, r'<div class="pc-price">(.*?)\s*<small>'),
      'access': g(s, r'<div class="pc-price">.*?<small>&middot;\s*(.*?)</small>'),
      'buy': g(s, r'<a class="btn bokunButton block"[^>]*>(.*?)</a>'),
      'features': [[k, v] for k, v in zip(SVGKEY, feats_html)],
      'final_h2': g(s, r'<section class="final">.*?<h2>(.*?)</h2>'),
      'final_p': g(s, r'<section class="final">.*?<h2>.*?</h2>\s*<p>(.*?)</p>'),
      'final_btn': g(s, r'<section class="final">.*?<a class="btn bokunButton"[^>]*>(.*?)</a>'),
    }
    miss = [k for k, v in d.items() if v in (None, '', [])]
    assert not miss, (L, miss)
    assert len(d['features']) == 5, (L, len(d['features']))
    io.open(f'L/04_{L}.json', 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2))
    print(L, 'ok')
