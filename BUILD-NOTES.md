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

---

## Правка фактов: Boleto Único (24 сентября 2026)

Весной 2026 года в Чичен-Ице отменили двухкассовую систему. **Boleto Único** — один
билет, один платёж, одна касса, в новом визит-центре **CATVI** (открылся в марте
2026). Сумма не изменилась: 697 песо для взрослого иностранца, из них 105 — доля
INAH, 592 — доля штата Юкатан, просто их больше не собирают порознь.

На сайте это встречалось в **семи** разных местах, и все они были устаревшими:

1. `drafts/02-body-<lang>.html` — сетка «Коротко» (строка про вход)
2. то же — абзац про логистику автобусного тура («в какую из двух касс идти сначала»)
3. то же — абзац с ценой входа + следующее предложение про терминалы
4. то же — подпись к партнёрской ссылке Tiqets («без второй очереди»)
5. то же — ответ FAQ про самостоятельное посещение
6. `tr/strings_en.json` + все `tr/tr_<lang>.json` — три строки лендинга
   (сетка фактов, ответ FAQ на странице и он же внутри JSON-LD) и строка списка
   вещей («обе кассы принимают карты»)
7. `tr/strings_guides_en.json` + `tr/trg_<lang>.json` — подпись карточки «Билеты»
   на `/guides/` («как пропустить вторую очередь»)

Плюс `public/llms.txt` и список фактов в `tr/LOCALIZATION-BRIEF.md`.

**Урок на будущее.** Один факт разошёлся по трём слоям: тела статей, карты строк
лендинга, карты строк guides — и ни один grep по `public/` не нашёл бы источник,
потому что `public/` собирается. Искать надо в источниках, и по всем трём картам
сразу. Команда для проверки любого факта:

    grep -rn "<фраза>" drafts/ tr/ public/llms.txt

**Важно:** упоминания двух касс, которые остались в текстах, — намеренные. Они
описывают отменённую систему («Boleto Único заменил прежнюю систему с двумя
кассами»), и это как раз freshness signal. Не вычищать их автоматически.

### Как пересобрать после правки источников

    python3 gen_land.py && python3 gen_guides.py
    for L in en es fr de it pt pl ru; do
      B=drafts/02-body-$([ $L = en ] && echo EN || echo $L).html
      python3 gen_article.py $L meta/02_$L.json $B
    done
    python3 wire_article.py

## Статья №3 — `/chichen-itza-day-trip-from-cancun/` (в работе)

Черновики: `drafts/03-day-trip-from-cancun-EN.md` и `-RU.md`. На сайт ещё не собрана,
на WordPress не публиковалась. Русский вариант ушёл редактору в Google Doc
(редакция 2, после 27 замечаний).

**Что решено по встраиванию продукта** — эту архитектуру применять и в следующих
статьях, она заметно сильнее одного блока в конце:

1. **Лид**, сразу после главной мысли статьи — короткий абзац про аудиогид + CTA.
   Логика связки: главное преимущество самостоятельного приезда — ранний вход;
   аудиогид позволяет этим преимуществом воспользоваться и начать сразу.
2. **Таблица «Коротко»** — одна строка: `TouringBee · 16 остановок · ~1,5 ч ·
   офлайн · 9,99 €`. Без блока продаж.
3. **Сразу после сравнительной таблицы** — короткая врезка + CTA. Самая сильная
   точка конверсии на странице: читатель только что выбрал способ добраться.
4. **Большой продуктовый блок** с заголовком-аргументом, а не описанием:
   «Приехали раньше групп? Экскурсия начинается вместе с вами».
5. **После FAQ** — финальный короткий CTA.

Главная продающая мысль, вокруг которой строится вся интеграция: *вы потратили силы
и деньги, чтобы приехать раньше экскурсионных автобусов — не ждите экскурсию после
этого.* Это сильнее, чем «офлайн-аудиогид за 9,99 €».

### Редакционные правила, выведенные при вычитке №3

Не утверждать того, что нельзя проверить. Типовые ловушки, которые редактор снял:

- «большинство замечает это на обратном пути», «люди приходят к кассе через час
  после закрытия» — выдуманная массовая ошибка → «эту разницу легко пропустить»
- «единственный способ» там, где статья сама выше называет другой способ
- «это фикция» про рекламную цену → «это не финальная цена»
- «терминалы регулярно уходят в офлайн», «два литра воды минимум», «связь слабая»
- «групп сюда не пускают», «толпа сюда не доезжает» — про сеноты
- «проигрывает по всем статьям» — абсолютный вердикт вместо причины
- гарантии вида «площадка двадцать минут только ваша», «кадр без очереди»
- «исторически не принимает карты» — «исторически» ничего не говорит о 2026

Ещё: **Чичен-Ица в туристическом контексте — «археологическая зона», а не «город»**.

### Свежесть данных

Статья про транспорт и цены протухает быстрее всего на сайте. В тексте стоит строка
«Цены и расписания проверены 24 сентября 2026 года», обновлять раз в 2–3 месяца.
Требуют сверки в первую очередь: тариф платной дороги (расчётный, официального
CAPUFE по пунктам получить не удалось), аренда авто со страховкой (единственный
источник), расписание ADO (живая продажа, официальный сайт противоречит сам себе),
16:00 против 16:30 на обратный рейс, Tren Maya (динамические тарифы), Ик-Киль
180/200, парковка 80/100/120.

---

## Статья №3 — `/chichen-itza-day-trip-from-cancun/` (25 сентября 2026)

8 языков, опубликована в бандле. EN-мастер ~4 200 слов, локализации от 3 700 (PL)
до 4 600 (FR). 9 вопросов в FAQ, две таблицы, раздел о безопасности за рулём.

### Новое в пайплайне: `md2body.py`

Статья №2 писалась сразу в HTML. Статья №3 писалась в markdown (так удобнее
редактору и Google Doc), поэтому появился конвертер:

    md2body.py   # markdown-мастер -> HTML-тело в разметке сайта
    L/03_en.json # строки, которых нет в markdown: шапка, карточка товара, финал

Конвертер сам собирает `.arthero`, превращает таблицу «At a glance» в `.facts`,
цитату `>` в `.midcta`, вторую таблицу в `.tablewrap > table.cmp`, блок FAQ в
`<details>`, «Continue exploring» в `ul.related`, и приклеивает `section.final`.

Три грабли, на которые он наступил и которые уже исправлены:
- `inline()` экранировал `&` и ломал готовые сущности в файле локали
  (`&euro;` → `&amp;euro;`). Теперь после экранирования сущности восстанавливаются.
- Байлайн содержит `<strong>` — его нельзя гнать через `inline()`, иначе теги
  вылезают текстом. Выводится сырым.
- Правило `.disc` ловило абзацы в `**жирном**` наравне с `*курсивом*`. Теперь
  только одиночная звёздочка.

### Пять точек продукта — архитектура, утверждённая заказчиком

Применять в следующих статьях, она заметно сильнее одного блока в конце:

1. шапка — кнопка `.btn bokunButton`
2. лид — **текстовая** ссылка `.bokunButton.inlinebuy` сразу после главной мысли
3. после сравнительной таблицы — `.midcta` с кнопкой; самая сильная точка
   конверсии: читатель только что выбрал способ добраться
4. `#product` под заголовком-аргументом, а не описанием
5. `section.final`

CTA, который в markdown стоит между FAQ и «читать дальше», в HTML **не переносится** —
его работу делает `section.final`. Конвертер выбрасывает его сам.

### `wire_article.py` переписан — старая версия портила чужие карточки

Было: карточка на `/guides/` искалась регуляркой по имени картинки
(`partner-gyg-800.webp`) с `count=1`. Картинки на странице повторяются, и после
того как карточка статьи №2 стала `<a>`, повторный запуск включил **следующую**
карточку с той же картинкой — «From Playa del Carmen» начала вести на статью №2.

Стало: карточки ищутся **по заголовку `<h3>`**, локализованный заголовок берётся
из `trg_<lang>.json` по английскому ключу. Список публикаций — в константе
`PUBLISHED` (слаг + английский заголовок карточки). Скрипт идемпотентен и
обратим: всё, чего нет в `PUBLISHED`, возвращается в «Coming soon». Меню тоже
пересобирается целиком из `PUBLISHED`, а не дописывается.

Добавляя статью, правь только `PUBLISHED` — и прогоняй:

    python3 wire_article.py    # должен показать «живых 2», без «возвращено»

### Порядок сборки всего сайта

    python3 gen_land.py && python3 gen_guides.py
    for L in en es fr de it pt pl ru; do
      S=$([ $L = en ] && echo EN || echo $L)
      python3 gen_article.py $L meta/02_$L.json drafts/02-body-$S.html
      python3 gen_article.py $L meta/03_$L.json drafts/03-body-$S.html
    done
    python3 wire_article.py

`gen_guides.py` перетирает карточки — `wire_article.py` всегда запускать после него.

### Что вычитка нашла в этом круге

Три пары глаз, 60+ правок. Показательные:
- **PL** смешивал несклоняемое `cenote` со склоняемым `cenotę` в семи местах и
  вешал женское согласование на несклоняемую форму. В статье №2 принято
  склоняемое `cenota` — унифицировано.
- **IT** и **FR** одинаково сломали сравнение в разделе безопасности:
  «12,9–17,5, более чем в десять раз больше» вместо «ниже».
- **IT** и **FR** одинаково перевели «about three hours each way» как «три часа
  туда» — потеряли «в каждую сторону».
- **DE** «zu wenig im Tank» вместо недолива на заправке — смысл ушёл в «мало
  бензина».
- **ES/IT/PT** переводили carjacking как «кража авто» — это разные вещи.
- Главный ключ отсутствовал в H2 у ES, IT, PT и DE.

### Расхождение с утверждённым русским текстом — одно

В markdown, который читал заказчик, стоит «630 долларов». В HTML — «630 US$»,
ради единого формата денег по всей статье (`57 US$`, `44 US$`, `101 US$`).
Если возвращать «доллары», менять надо все четыре места сразу.
