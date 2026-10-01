#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Собрать meta/04_<lang>.json: хром из статьи №3, SEO-строки — здесь."""
import json, io

SLUG = 'chichen-itza-self-guided-tour'
PUB  = '2026-10-01'

S = {
 'en': dict(
   title='Chichén Itzá Self-Guided Tour: Route and Order | TouringBee',
   desc='The entrance moved in 2026 and most route descriptions still describe the old one. Walking order, distances, opening hours and honest timings.',
   og_title='Chichén Itzá Self-Guided Walking Tour: Route, Order and Timing',
   og_desc='The entrance moved in 2026. Here is the walk as it actually works now.',
   dropdown='Self-guided tour', self='Chichén Itzá self-guided tour'),
 'es': dict(
   title='Chichén Itzá por tu cuenta: ruta y orden | TouringBee',
   desc='La entrada se movió en 2026 y casi todas las descripciones siguen hablando de la antigua. Orden de recorrido, distancias, horarios y tiempos honestos.',
   og_title='Chichén Itzá por tu cuenta: la ruta, el orden y los tiempos',
   og_desc='La entrada se movió en 2026. Así funciona el recorrido ahora.',
   dropdown='Por tu cuenta', self='Chichén Itzá por tu cuenta'),
 'fr': dict(
   title='Chichén Itzá en autonomie : itinéraire | TouringBee',
   desc="L'entrée a changé de place en 2026 et presque tous les itinéraires décrivent encore l'ancienne. Ordre de visite, distances, horaires et durées honnêtes.",
   og_title="Chichén Itzá en autonomie : l'itinéraire, l'ordre et les durées",
   og_desc="L'entrée a changé de place en 2026. Voici la visite telle qu'elle fonctionne.",
   dropdown='En autonomie', self='Chichén Itzá en autonomie'),
 'de': dict(
   title='Chichén Itzá auf eigene Faust: Route | TouringBee',
   desc='Der Eingang ist 2026 umgezogen, fast alle Rundgänge beschreiben noch den alten. Reihenfolge, Entfernungen, Öffnungszeiten und ehrliche Zeiten.',
   og_title='Chichén Itzá auf eigene Faust: Route, Reihenfolge und echte Zeiten',
   og_desc='Der Eingang ist 2026 umgezogen. So läuft der Rundgang heute wirklich.',
   dropdown='Auf eigene Faust', self='Chichén Itzá auf eigene Faust'),
 'it': dict(
   title='Chichén Itzá in autonomia: percorso | TouringBee',
   desc="L'ingresso si è spostato nel 2026 e quasi tutti i percorsi descrivono ancora quello vecchio. Ordine di visita, distanze, orari e tempi onesti.",
   og_title="Chichén Itzá in autonomia: il percorso, l'ordine e i tempi",
   og_desc="L'ingresso si è spostato nel 2026. Ecco come funziona la visita oggi.",
   dropdown='In autonomia', self='Chichén Itzá in autonomia'),
 'pt': dict(
   title='Chichén Itzá por conta própria: percurso | TouringBee',
   desc='A entrada mudou de lugar em 2026 e quase todos os percursos descrevem ainda a antiga. Ordem de visita, distâncias, horários e tempos honestos.',
   og_title='Chichén Itzá por conta própria: o percurso, a ordem e os tempos',
   og_desc='A entrada mudou de lugar em 2026. É assim que o percurso funciona agora.',
   dropdown='Por conta própria', self='Chichén Itzá por conta própria'),
 'pl': dict(
   title='Chichén Itzá samodzielnie: trasa i czasy | TouringBee',
   desc='Wejście przeniesiono w 2026 roku, a większość opisów trasy wciąż opisuje stare. Kolejność zwiedzania, odległości, godziny i uczciwe czasy.',
   og_title='Chichén Itzá samodzielnie: trasa, kolejność i uczciwe czasy',
   og_desc='Wejście przeniesiono w 2026 roku. Tak ta trasa wygląda dzisiaj.',
   dropdown='Samodzielnie', self='Chichén Itzá samodzielnie'),
 'ru': dict(
   title='Чичен-Ица самостоятельно: маршрут 2026 | TouringBee',
   desc='Вход переехал в 2026 году, и почти все описания маршрута ведут через старый. Порядок обхода, расстояния, часы работы и честное время.',
   og_title='Чичен-Ица самостоятельно: маршрут, порядок обхода и время',
   og_desc='Вход переехал в 2026 году. Вот как прогулка устроена теперь.',
   dropdown='Самостоятельно', self='Чичен-Ица самостоятельно'),
}

for L, s in S.items():
    base = json.load(io.open(f'meta/03_{L}.json', encoding='utf-8'))
    d = {
      'slug': SLUG,
      'title': s['title'], 'desc': s['desc'],
      'site_name': base['site_name'],
      'og_title': s['og_title'], 'og_desc': s['og_desc'],
      'published': PUB, 'modified': PUB,
      'sticky': base['sticky'],
      'labels': {'menu': base['labels']['menu'], 'dropdown': s['dropdown'], 'all': base['labels']['all']},
      'crumbs': {'home': base['crumbs']['home'], 'guides': base['crumbs']['guides'],
                 'self': s['self'], 'attraction': base['crumbs']['attraction']},
    }
    io.open(f'meta/04_{L}.json', 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2))
    print(f"{L}  title {len(s['title']):>3}  desc {len(s['desc']):>3}  og_t {len(s['og_title']):>3}  og_d {len(s['og_desc']):>3}")
