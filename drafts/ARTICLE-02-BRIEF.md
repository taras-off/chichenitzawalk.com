# Article #2 — localization brief (chichenitzawalk.com)

Master: `drafts/02-body-EN.html` — the EN article body fragment, already live at
`public/chichen-itza-tour/index.html`.

You produce TWO files for your language `<L>`:
1. `drafts/02-body-<L>.html` — the localized body fragment
2. `meta/02_<L>.json`        — the localized page metadata

## THE ONE RULE

**Read `tr/LOCALIZATION-BRIEF.md` first, in full.** Everything in it applies here:
retell don't translate, short sentences, varied rhythm, verbs over nouns, active voice,
show don't tell, hook in the first two sentences, no clichés, no filler, consistent
politeness register, the glossary, the hard product facts.

Localization is often SHORTER than the EN original. Do not pad.

## STRUCTURAL CONTRACT — this is a machine-consumed file

The output must be the **same HTML skeleton** as `02-body-EN.html`, in the same order,
with the same classes, ids and element types. The build script parses it. Specifically:

- Keep every `class=` and `id=` value **exactly** as in EN (`arthero`, `crumbs`, `sub`,
  `byline`, `hbtns`, `lead`, `facts`, `fgrid`, `disc`, `tablewrap`, `cmp`, `faq`,
  `related`, `final`, `product`, `audio`, `options`, `btn`, `bokunButton`, `block`,
  `outline`, `pc-*`, `features`, `badge`, `star`).
- Keep the same number of `<h2>`, `<h3>`, `<p>`, `<li>`, `<tr>`, `<td>` and
  `<details>` elements. Same table shape: 5 columns, 8 body rows. Same 8 FAQ entries,
  in the same order.
- Keep every `<svg>…</svg>` byte-identical.
- Keep `<img>` `src`, `width`, `height`, `loading`, `decoding` identical; localize `alt`.
- Anchor targets `#audio` and `#product` stay as-is.
- Use HTML entities the same way EN does (`&euro;`, `&rarr;`, `&amp;`, `&middot;`).
- **Do not** add a `<style>`, `<head>`, `<html>` or `<body>` tag. Body fragment only.

## LINKS — rewrite these for your language

Internal (root-absolute, replace the leading `/`):
- `href="/"`         → `href="/<L>/"`
- `href="/guides/"`  → `href="/<L>/guides/"`

Affiliate — swap the locale segment, keep every query parameter byte-identical:
- GetYourGuide: `https://www.getyourguide.com/<GYG>/chichen-itza-l785/?partner_id=0M4BUCG&amp;utm_medium=travel_agent`
- Tiqets:       `https://www.tiqets.com/<TQ>/chichen-itza-tickets-l146416/?partner=touringbee_limited-180893&amp;tq_campaign=chichenitzawalk`
- Booking cars: `https://www.booking.com/cars/index.<BK>.html?aid=1437498`

Bókun — add the language parameter to all three buttons:
- `href="https://widgets.bokun.io/online-sales/028dc54f-646b-4b9d-a0f0-e1c5746da99a/experience/790505?lang=<L>"`
- `data-src="https://widgets.bokun.io/online-sales/028dc54f-646b-4b9d-a0f0-e1c5746da99a/experience/790505?partialView=1&amp;lang=<L>"`

Per-language values:

| L  | GYG   | TQ | BK |
|----|-------|----|----|
| es | es-es | es | es |
| fr | fr-fr | fr | fr |
| de | de-de | de | de |
| it | it-it | it | it |
| pt | pt-pt | pt | pt |
| pl | pl-pl | pl | pl |
| ru | ru-ru | ru | ru |

## FACTS THAT MUST SURVIVE EXACTLY

- Entry 2026: **697 MXN** foreign adult = INAH 105 + Yucatán state 592, two windows.
  Children 3–12: 105 MXN. Mexicans ~300 MXN with ID.
- Hours 8:00–17:00, last entry / ticket sales 16:00. Coaches arrive 10:30–11:00.
- Gate guide 800–2,000 MXN **per group**, 1.5–2 h. One quote in March 2026: 1,300 MXN.
- Coach tour from Cancún €55–75 pp; small group €85–110; early access US$35–100.
- Private tour US$295–450+ (≈€180–300 pp).
- ADO Cancún 400–500 MXN each way, ~2.5 h, ~08:30 departure → ~11:00 arrival.
  Valladolid colectivo 100–150 MXN, 45 min.
- Car: €30–45/day + €15–25 insurance + ~300 MXN tolls each way on the 180D +
  €15–25 fuel + 80–100 MXN parking.
- Ball court acoustics carry **168 metres**. 2.5 million visitors a year.
- Yucatán is one hour behind Quintana Roo.
- **Audio guide: €9.99, 16 stops, ~1.5 h, 8 languages, offline, iOS + Android,
  1 year access, 4.6 / 18 reviews on Viator & Tripadvisor, used by 6,022 travellers.**
- **An offline GPS map shows your position; the user starts each recording themselves
  at the spot.** It never "plays automatically". This wording is non-negotiable.
- The route is maintained and updates reach the app on its own — no repurchase.
  Never write anything critical about our audio guide beyond the one structural
  limitation stated in EN: a recording cannot answer a question.

Money format: follow your language's norm (RU/FR/PL/DE/IT/PT/ES: `9,99 €` — number
first, comma decimal, space before the sign; never `€9.99`). MXN stays `697 MXN`
(or the natural local form for pesos). Keep `US$` where EN has it.

The pull quote (`<blockquote>`) is a real Tripadvisor review by **Albert Parson** —
translate the sentence, keep the name and "Tripadvisor" unchanged.

## meta/02_<L>.json — copy the EN file's shape exactly

```json
{
  "slug": "chichen-itza-tour",
  "title": "… | TouringBee",          ≤ 60 chars INCLUDING " | TouringBee"
  "desc": "…",                         ~155 chars
  "site_name": "…",                    localized site name (EN: Chichén Itzá Walk)
  "og_title": "…",                     the H1, or close to it
  "og_desc": "…",                      ~100 chars
  "sticky": {
    "sticky_title": "…",               e.g. "Chichén Itzá Audio Guide"
    "sticky_sub": "· from 9,99 € · offline · in <language>",   keep the leading "· "
    "sticky_btn": "…9,99 €",
    "bokun_href": "…?lang=<L>",
    "bokun_src":  "…?partialView=1&amp;lang=<L>"
  },
  "labels": {
    "menu": "…",        header dropdown word (ES Guías, FR Guides, DE Guides,
                        IT Guide, PT Guias, PL Przewodniki, RU Гиды)
    "dropdown": "…",    short label for this article in the menu, ≤ 34 chars
    "all": "…"          "All guides" (ES Todas las guías, FR Tous les guides,
                        DE Alle Guides, IT Tutte le guide, PT Todos os guias,
                        PL Wszystkie przewodniki, RU Все гиды)
  },
  "crumbs": {
    "home": "…", "guides": "…",
    "self": "…",          breadcrumb leaf, matches the H1 topic
    "attraction": "…"     Chichén Itzá in your language (RU: Чичен-Ица)
  }
}
```

The `<nav class="crumbs">` line inside the body must use the SAME words as
`crumbs.home` / `crumbs.guides`, and its third segment is a short category word
(EN "Tours").

## SEO

The main keyword — your language's natural phrasing of *Chichén Itzá tour /
excursion / guided visit* — belongs in the H1, the first paragraph and one H2.
Naturally. No stuffing. The `<title>` must differ from the H1 wording enough to
read as a search result, and stay ≤ 60 characters.

## Self-check before you finish

1. `grep -c '<h2'`, `'<h3'`, `'<details>'`, `'<tr>'` match the EN counts.
2. Zero English sentences left (proper nouns and brand names excepted).
3. Three `bokunButton`, each with `?lang=<L>`.
4. Nine `rel="noopener sponsored"` links, all carrying your locale.
5. No cliché from the banned list. Read the lead aloud — does it hook?
6. Every number in the FACTS section above appears unchanged.
