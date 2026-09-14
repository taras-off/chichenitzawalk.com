# chichenitzawalk.com — EN landing bundle (4 Aug 2026)

## What's in `public/`  — 8 languages, 16 pages
- `index.html` + `<lang>/index.html` ×7 — the pillar landing in EN/ES/FR/DE/IT/PT/PL/RU.
- `guides/index.html` + `<lang>/guides/index.html` ×7 — the guides index with all 29 planned articles as "Coming soon" cards.
- `audio/cancunt1_<lang>_intro.mp3` ×8 — the preview player, self-hosted so it works in every language.
- `privacy-policy.html`, `affiliate-disclosure.html` — own legal pages.
- `robots.txt`, `llms.txt`, `sitemap.xml`
- `favicon.ico` / `favicon-32.png` / `favicon-180.png` — generated from IMG/favicon.png
- `img/` — 14 WebP images generated from the cancunt1 photo set + `logo.webp` + `author-eugene.webp`
- `audio/cancunt1_en_intro.mp3` — the 30-sec preview player source (self-hosted, so it works in every language)

## ✅ Bókun wired and live
Channel UUID **028dc54f-646b-4b9d-a0f0-e1c5746da99a** (channel `chichenitzawalk.com`),
product **790505** — read off the generated Button widget code in the Bókun dashboard on 4 Aug 2026.
All 6 buy CTAs + the lazy loader now carry the real UUID. Nothing left to fill in.

Widget URL pattern in use:
`https://widgets.bokun.io/online-sales/028dc54f-646b-4b9d-a0f0-e1c5746da99a/experience/790505?partialView=1`
(add `&lang=<code>` on the localized pages; English omits it.)

## IDs confirmed for this site
| Item | Value |
|---|---|
| Bókun product | #790505 · cancunt1 · Chichen Itza Audioguide |
| Bókun channel UUID | **028dc54f-646b-4b9d-a0f0-e1c5746da99a** ✅ вставлен |
| TouringBee EN product | https://touringbee.com/product/chichen-itza-tour/ |
| TouringBee ES | /es/product/chichen-itza-tour-es/ |
| TouringBee FR | /fr/product/chichen-itza-tour-fr/ |
| TouringBee DE | /de/product/chichen-itza-tour-de/ |
| TouringBee IT | /product/chichen-itza-tour-it/ |
| TouringBee PT | /product/excursao-a-chichen-itza/ |
| TouringBee PL | /pl/product/chichen-itza-tour-pl/ |
| TouringBee RU | /ru/product/chichen-itza-tour-ru/ |
| GetYourGuide location | chichen-itza-**l785** |
| Tiqets venue | chichen-itza-tickets-**l146416** · tq_campaign=chichenitzawalk |
| Booking | aid=1437498 (hotels Valladolid + cars) |
| Headout | no Chichén Itzá page found → third partner slot = Booking (cars/hotels) |
| SNCF | N/A (Mexico) — removed, per the brief |

## Facts fact-checked for 2026
- Entry: INAH federal **105 MXN** + Yucatán state (CULTUR) **592 MXN** = **~697 MXN** (~€35/$40) for foreign adults, paid at two windows.
- Hours: **08:00–17:00**, ticket booths + last entry **16:00**.
- Climbing banned since **2006**.
- Equinox serpent: ~**20 March** / ~**22 September**.
- Product: **€9.99**, 16 stops, ~1.5 h, 8 languages, **6,022 users** (from the cancunt1 ID table).
- Reviews: 6 verbatim Tripadvisor reviews taken from Reviews.docx.
- **Rating: 4.6 from 18 reviews**, read off the product's own Viator listing
  ("Chichen Itza Walking Tour with Audioguide (no ticket)", supplied by TouringBee —
  https://www.viator.com/tours/Chichen-Itza/Chichen-Itza-Self-Guided-Audio-Tour-for-your-smartphone/d50526-366784P6).
  Shown visibly in the hero ("4.6 on Viator") and in the product card with the count, and
  mirrored in the Product schema as `aggregateRating` — real figure, real count, visible on
  the page, which is exactly what the playbook requires. Re-check the count before each
  release; if it moves, update both the visible strings and the schema together.

## Next steps
1. Deploy + one real test order → confirm the activation email arrives.
2. Infra: GitHub repo + Cloudflare Pages (output dir `public`) + point chichenitzawalk.com.
3. Localise the landing to 7 languages (gen.py-style) once EN is approved.
4. Start P0 articles from the 30-topic plan; slugs are already fixed in /guides/.


---

## Localization (added 4 Aug 2026)

Seven languages generated from the EN master: **ES, FR, DE, IT, PT, PL, RU**.
Localized, not translated — per the house localization guide: short sentences, active
voice, no clichés, units and number formats per market, one consistent politeness
register per language, the monument glossary held identical across each page.

### Build
- `localize.py` — shared single-pass substitution helper.
- `gen_land.py` — landings. `gen_guides.py` — /guides/ pages.
- `tr/strings_en.json` (231 landing strings) + `tr/strings_guides_en.json` (80).
- `tr/tr_<lang>.json`, `tr/trg_<lang>.json` — the text maps.
- `tr/postfix.json` — proofreading fixes that span markup, applied after substitution.
- Rebuild: `python3 gen_land.py && python3 gen_guides.py`. Both report `missing 0`.

### ⚠️ Generator bug found and fixed — do not reintroduce
The first version applied the text map with repeated `str.replace()`, longest key first.
That re-scans text that was already translated, so the short key `Map` matched inside the
freshly produced `Mapa GPS` and yielded **`Mapaa GPS`**; `Address` ate the schema.org type
name inside `PostalAddress` and produced `PostalDirección` / `PostalАдрес`, silently killing
the address node; `Google Maps` became `Google Mapas`. It hit six of seven languages.

`localize.py` now does ONE regex pass over the original string, longest alternative first,
so output is never re-scanned, plus a `PROTECT` list of literals (schema.org type names,
brand names) that resolve to themselves. Any future generator must use `apply_map()`.

### Per-language swaps the generator makes
`<html lang>`, canonical, `og:url`, `og:locale`, active flag in the language switcher,
audio preview file, `&lang=<code>` on every Bókun URL (English omits it), the TouringBee
product + shop URL for that language, Tiqets locale path, GetYourGuide `<xx-xx>` path,
Booking `searchresults.<lang>.html` and `cars/index.<lang>.html`, `/<lang>/guides/` links,
JSON-LD `@id`s and `inLanguage`. IT additionally gets the localized Tulum and Teotihuacán
cross-sell products; the other languages fall back to EN where no localized product exists.

### QA
Three independent proofreaders swept all 14 localized pages against the English master.
115 findings: 31 were the generator bug (fixed at the source), 84 were real language fixes
(19 errors, 65 style) — all back-ported into the text maps, so a clean rebuild keeps them.
Verified after rebuild: every number matches the master, the GPS wording is correct in all
8 languages, register is consistent per language, all JSON-LD parses, no leftover English.

### sitemap.xml
18 `<loc>` — 8 landings + 8 guides pages + 2 legal — each with 8 hreflang alternates + x-default.

---

## Article #2 — `/chichen-itza-tour/` (13 September 2026)

**Slug:** `chichen-itza-tour` · 8 languages · EN master ~2,950 words.
Title: *Chichén Itzá Tour: Coach, Guide or Audio?*

### Build pipeline

    build_article.py      # shared chrome: pulls <style>, <header>, <footer> out of
                          # public/index.html, adds the article-only CSS, localizes
                          # the header (brand href, menu word, dropdown entry,
                          # lang nav pointing at the article in each language)
    gen_article.py <lang> meta/02_<lang>.json drafts/02-body-<lang>.html
                          # builds the <head>, derives the FAQPage JSON-LD FROM the
                          # on-page <details> so the two can never drift, and writes
                          # public/[<lang>/]chichen-itza-tour/index.html
    wire_article.py       # adds the article to the Guides dropdown on all 8 landings
                          # and flips the /guides/ card from "Coming soon" to a live
                          # link in all 8 languages. Idempotent.

Rebuild everything:

    for L in en es fr de it pt pl ru; do
      python3 gen_article.py $L meta/02_$L.json \
        drafts/02-body-$(  [ $L = en ] && echo EN || echo $L ).html
    done
    python3 wire_article.py

### Decisions worth remembering

- **Root-absolute asset paths (`/img/…`) in articles**, not the Playbook v3 §6
  relative `../img/`. The rest of the site already uses root-absolute, it behaves
  identically on the server, and it removes the `../` vs `../../` bug class from
  the localizer entirely — localized pages need no path rewriting at all.
- **The localized body is a full HTML fragment per language, not a string map.**
  A 3,000-word article cannot be localized key-by-key without turning into a
  translation. Each language got the whole body; the structural contract
  (identical tag sequence to the EN master) is what the build script enforces.
  Verify with:

      python3 -c "
      import re
      def t(f): return [x.split()[0].lower() for x in re.findall(r'<(/?[a-zA-Z][^>]*)>', open(f,encoding='utf-8').read())]
      ref=t('drafts/02-body-EN.html')
      for L in ['es','fr','de','it','pt','pl','ru']: print(L, t(f'drafts/02-body-{L}.html')==ref)"

- **FAQ JSON-LD is generated from the page, never written by hand.**
- The RU body reuses the wording of the WordPress draft (post #18381) that is
  with the editor; the sections the EN master has and that draft did not
  (byline, at-a-glance grid, product card, final CTA) were written fresh from
  the approved landing-page strings in `tr/tr_ru.json`.

### Proofreading round

Three adversarial native-editor passes over the 7 localizations produced 96
findings; all were applied. The notable ones:

- **DE** had a meaning reversal in FAQ 1 — *"Ganz ohne hineinzugehen ist die
  Variante, von der wir abraten"* said we advise against entering at all.
- **PL** mixed 2sg and 2pl address in five places, twice inside one sentence.
- **IT** called both entry fees *statali* two clauses after saying one is federal.
- **PT** put the accredited guides at the ticket office instead of the entrance,
  and turned the cenote under El Castillo into a *gruta*.
- **PL and RU** both mistranslated Thompson's dredging of the Sacred Cenote as
  deepening / baling it dry.
- **ES and IT** both produced the same tautology from "unlocks the 8:00 opening"
  (*abre la apertura* / *apre l'apertura*).
- The EN lead did not contain the main keyword; fixed in EN and mirrored in all 7.

### Fix, 14 September 2026 — in-page anchors

The body had **two** `href="#audio"` links. The second sat *inside* the
`<h3 id="audio">` section, so it pointed at its own heading and did nothing —
and because its link text names the product ("the TouringBee Chichén Itzá audio
walk"), a reader clicking it expected the Bókun widget and got a no-op.
It now points at `#product`, which scrolls to the product card with the rating,
the price and the Bókun button. The first `#audio` link, in the lead, still
jumps to the section that explains the option — that one is correct.

Also added `[id]{scroll-margin-top:72px}` to the article CSS: the header is
`position:sticky` at 56px, so before this any anchor jump parked the target
heading underneath it.

**Superseded the same day, by request:** both in-text links whose text names the
product now open the Bókun widget directly instead of scrolling anywhere. They
carry `class="bokunButton inlinebuy"` with the usual `data-src` (`&lang=` per
language) — the same hook the three CTA buttons use, so Bókun binds to them
identically; `.inlinebuy` styles them as a weighted, green-underlined text link
rather than a button, so they still read as prose.

Two safety nets, because an in-text link can be clicked earlier in the page
life than a CTA button:

- the lazy loader now also fires on `setTimeout(b,3000)`, not only on first
  interaction, so the engine is bound well before anyone reaches mid-article;
- the inline links carry `target="_blank" rel="noopener"`, so on the rare early
  click where Bókun has not bound yet, the real `href` opens the checkout in a
  new tab and the reader keeps the article. The three CTA buttons are unchanged.

Note the `id="audio"` and `id="product"` anchors still exist and are still the
scroll targets used by `scroll-margin-top`; nothing links to them from the body
any more.

Rule for future articles: a link whose text names the product is a
`bokunButton`, not an anchor. Check with

    python3 -c "
    import re,glob,os
    for p in glob.glob('public/**/*.html',recursive=True):
        h=open(p,encoding='utf-8').read()
        for u in re.findall(r'href=\"([^\"]*#[^\"]+)\"',h):
            if u.startswith('http'): continue
            path,frag=u.split('#',1)
            t=p if path=='' else 'public'+path+('index.html' if path.endswith('/') else '')
            if not os.path.exists(t) or f'id=\"{frag}\"' not in open(t,encoding='utf-8').read():
                print('BROKEN',p,u)"

### Still open

- The DE H1 keeps `allein` for *self-guided*. It reads as headline compression
  rather than "travelling solo", and matches `og_title` — flagged, not changed.
