# Article #3 — localization brief (chichenitzawalk.com)

Master: `drafts/03-body-EN.html` — the EN article body fragment, already live at
`public/chichen-itza-day-trip-from-cancun/index.html`.

You produce TWO files for your language `<L>`:
1. `drafts/03-body-<L>.html` — the localized body fragment
2. `meta/03_<L>.json`        — the localized page metadata

## THE ONE RULE

**Read `tr/LOCALIZATION-BRIEF.md` first, in full.** Retell, don't translate. Short
sentences, varied rhythm, verbs over nouns, active voice, hook in the first two
sentences, no clichés, no filler, consistent politeness register, the glossary.
Localization is often SHORTER than the original. Do not pad.

Also read `drafts/02-body-<L>.html` — the published article #2 in your language.
Match its register, glossary and rhythm. This must read as the same hand.

## STRUCTURAL CONTRACT — machine-parsed

Same HTML skeleton as `03-body-EN.html`, same order, same classes and ids.
Keep the same number of `<h2>`, `<h3>`, `<p>`, `<li>`, `<tr>`, `<td>`, `<details>`.
Keep every `<svg>…</svg>` byte-identical. Keep `<img>` attributes; localize `alt`.
Entities as in EN (`&euro;`, `&rarr;`, `&amp;`, `&middot;`, `&rsaquo;`, `&#9733;`).
No `<style>`, `<head>`, `<html>`, `<body>`. Body fragment only.

Verify with:

    python3 -c "
    import re
    def t(f): return [x.split()[0].lower() for x in re.findall(r'<(/?[a-zA-Z][^>]*)>', open(f,encoding='utf-8').read())]
    print(t('drafts/03-body-<L>.html')==t('drafts/03-body-EN.html'))"

## LINKS

Internal: `href="/"` → `/<L>/`, `href="/guides/"` → `/<L>/guides/`.

Affiliate — swap the locale segment, keep every query parameter byte-identical:
- GetYourGuide `https://www.getyourguide.com/<GYG>/chichen-itza-l785/?partner_id=0M4BUCG&amp;utm_medium=travel_agent`
- Tiqets `https://www.tiqets.com/<TQ>/chichen-itza-tickets-l146416/?partner=touringbee_limited-180893&amp;tq_campaign=chichenitzawalk`
- Booking cars `https://www.booking.com/cars/index.<BK>.html?aid=1437498`

Bókun — five buttons, each with the language parameter:
- `href="…/experience/790505?lang=<L>"`
- `data-src="…/experience/790505?partialView=1&amp;lang=<L>"`

| L | GYG | TQ | BK |
|---|-----|----|----|
| es | es-es | es | es |
| fr | fr-fr | fr | fr |
| de | de-de | de | de |
| it | it-it | it | it |
| pt | pt-pt | pt | pt |
| pl | pl-pl | pl | pl |
| ru | ru-ru | ru | ru |

## FACTS — transfer exactly

~200 km (196–205) · 180D toll road · about three hours each way, 2.5 at best ·
180 libre slower, estimates range from +30 min each way to twice the driving time ·
Yucatán UTC−6, Quintana Roo UTC−5, **one hour behind**, no DST · site 08:00–17:00
local, last tickets 16:00 · entry 697 MXN foreign adult (INAH 105 + state 592),
**one ticket at one window since the Boleto Único replaced the two-counter system
in spring 2026**, in the new CATVI visitor centre; children 3–12 ~105 MXN; Mexicans
~310 MXN · coach pick-up 06:30–08:00, on site 10:30–12:00, 12–14 h door to door ·
coach ~US$57 + US$44 admission ≈ US$101; early-access US$140–200, pick-up 04:30 ·
car hire US$40–60/day all-in, mandatory third-party liability US$20–30/day ·
toll ~500 MXN each way (180D rose 4.6% in April 2026) · fuel 700–790 MXN return ·
parking 50–120 MXN · **toll booths take cash pesos only** · few exits and fuel
stations on the 180D, fill up first · ADO from Cancún Centro 08:45 → 11:10, one-way
US$29–30, return around 16:00, no later bus · Tren Maya station 3 km from the gate,
westbound ~10:46, eastbound ~17:47, shuttle 50–55 MXN · Ik Kil 3 km, 180–200 MXN;
Yokdzonot 7 km, 60 MXN; Choo-Ha 45 km, 80 MXN · 4 km of walking, 33–35 °C March to
September, UV 11 · closed 18 May – 1 June 2026 · Ángeles Verdes 078.

**Safety section — transfer exactly:** Yucatán most peaceful state nine years running
(Mexico Peace Index) · 33 homicides in 2025, 1.03 per 100,000 against 12.9–17.5
nationally · US State Dept **Level 1**, only two such states, Chichén Itzá named in
the advisory as unrestricted · UK and Canada place no restriction on Yucatán or
Quintana Roo · carjacking warnings are geolocated to the Pacific coast and northern
border, not this corridor — and say plainly that this is an absence of reports, not
a proven zero · **276 road deaths in Yucatán in 2025, eight times the homicides** ·
touts in uniform shirts with STOP signs 2–5 km before the entrance, not police,
drive on to the official municipal car park 50 m from the ticket office, cameras,
state police, 50–120 MXN · Quintana Roo abolishing the traffic-police role, fines
moving to automatic cameras, rollout to 2027, June 2026 Cancún case of an officer
demanding US$630 · if stopped: do not hand over money or your passport, ask for a
copy of the fine, ask for ID · Profeco closed ten Quintana Roo petrol stations in
October 2025 for short measure.

**Product facts, non-negotiable:** an offline GPS map shows where you are and
**the user starts each recording themselves** at the spot — never "plays
automatically". 16 stops, ~1.5 h, &euro;9.99, offline, 8 languages, iOS and Android,
1 year access, 4.6 from 18 reviews, used by 6,022 travellers. The only permitted
criticism is that a recording cannot answer a question.

Money format: your language's norm (`9,99 €`, number first). `US$` stays but takes
your language's position. MXN as pesos in the natural local form.

## TONE — what the editor already rejected once

Do not assert what cannot be checked. No "most people notice on the way home", no
"the only way", no "that is fiction", no "terminals go offline regularly", no
"two litres minimum", no "the co-operative keeps tour groups out", no "loses on
every axis", no guarantees that the ball court will be empty. The EN master is
already written this way — follow it, do not re-inflate it.

Chichén Itzá in a visiting context is **the archaeological zone / the site**, not
"the city".

## meta/03_<L>.json — copy the shape of `meta/03_en.json`

`title` ≤ 60 chars including " | TouringBee" · `desc` ~155 · `og_desc` ~100 ·
`labels.dropdown` ≤ 34 chars · `crumbs.self` matches the H1 topic · `crumbs.attraction`
is Chichén Itzá in your language. `slug` stays `chichen-itza-day-trip-from-cancun`
in every language. `site_name` stays "Chichén Itzá Walk".

The `sticky` block: `sticky_sub` keeps the leading "· " and names your language.
`bokun_href` ends `?lang=<L>`, `bokun_src` ends `?partialView=1&amp;lang=<L>`.

## SEO

Your language's natural phrasing of *Chichén Itzá day trip from Cancún* belongs in
the H1, the first paragraph and at least one H2. Naturally. The `<title>` should
read as a search result and differ from the H1 wording.

## Self-check

1. Tag sequence identical to EN (command above prints True).
2. Zero English sentences.
3. Five `bokunButton`, each with `?lang=<L>`.
4. Five `rel="noopener sponsored"` links, all in your locale.
5. Nine `<details>` in the FAQ.
6. Every number above present and unchanged.
7. No banned cliché. Read the lead aloud.
