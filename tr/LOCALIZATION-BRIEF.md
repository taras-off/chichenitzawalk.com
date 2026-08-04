# Localization brief — chichenitzawalk.com landing page

You are localizing the EN master landing page of a niche travel-guide site about
**Chichén Itzá** (Yucatán, Mexico) into ONE target language.

## THE ONE RULE: localize, do NOT translate

We do not translate words — we **retell the meaning and the feeling** the way a living,
knowledgeable local guide-writer would say it in that language. A good localized text reads
as if it was written in that language from the start.

Test: read the paragraph aloud. If you got bored, stumbled or yawned — cut and rewrite.
If a word can be removed without changing the meaning — remove it.

### Voice and tone
- Write like a knowledgeable friend who guides — warm, interested, to the point.
  Not a museum label, not an ad brochure, not Wikipedia.
- Confident and concrete. No "perhaps", "it is generally considered", "it should be noted that".
- Lead the reader: "imagine", "step out onto", "don't leave without seeing…". Direct address works.
- A little character and light irony is fine. Clichés and pathos are not.

### Short. Rhythm. Air.
- Short sentences. A long multi-clause sentence → break into 2–3 short ones.
- Vary length. A run of equally long phrases puts people to sleep. Long — short — medium.
  A short sentence lands.
- One thought, one sentence. Don't glue two ideas with "while", "at the same time", "as well as".
- Paragraph = 2–4 sentences.
- Cut filler: "actually", "in general", "it should be taken into account", "is", "represents".

### Verbs, not nouns. Active, not passive.
- ✗ "the ascent of the staircase is carried out" → ✓ "you climb the stairs"
- ✗ "tickets can be purchased online" → ✓ "buy tickets online"
- Concrete verbs instead of "to be / to be located".

### Show, don't tell
Replace judgements ("beautiful", "impressive", "dangerous") with a concrete fact-picture the
reader draws their own conclusion from.

### Openings hook immediately
No warm-up. Don't start with "Chichén Itzá is…". Come in through a story, a detail, a paradox.

### Clichés to cut (per language, the local equivalents too)
EN: nestled, hidden gem, must-see, boasts, in the heart of, stunning/breathtaking everywhere,
a feast for the senses, picture-perfect, steeped in history.
RU: жемчужина, изюминка, must-see, атмосферный, затерянный уголок, поистине,
величественный/великолепный пачками, не оставит равнодушным, окунуться в атмосферу, сердце города.
Same idea in FR/DE/ES/IT/PT/PL — kill the local equivalents.
If you can't make it sound good without a cliché, you need a concrete detail, not an epithet.

### Cultural adaptation
- Units, currency, date format — for the market. Metres/kilometres, €, 24-hour clock for RU/DE/PL.
- Reference points and comparisons the reader actually understands.
- Explain what needs explaining for THAT audience, drop what they already know.
- Never translate idioms literally — use the target-language equivalent or drop them.

### Names, terms, register
- The full name always: **Chichén Itzá** (RU: Чичен-Ица). Never shortened to "Chichén".
- Proper nouns: transliteration + original in brackets on first mention where the language
  normally does that (RU). Then transliteration only. Decline naturally.
- Politeness register consistent throughout: RU «вы» lowercase, DE Sie, FR vous, ES usted→ better
  informal "tú" is NOT used — use the neutral impersonal/usted register consistently; PL Pan/Pani
  avoided — use the impersonal/"Ty"-free neutral form consistently. Pick one and hold it.
- Glossary, keep consistent across the whole page:
  El Castillo · Temple of Kukulkán · the Great Ball Court · the Sacred Cenote · El Caracol
  (the observatory) · Tzompantli (the skull platform) · Temple of the Warriors ·
  the Group of a Thousand Columns · cenote · sacbeob (the white roads) · Xibalba.

### Length
Localization is often SHORTER than the original. Don't pad to hit a word count.
RU and DE run long by nature — fight it: cut participial constructions, doublets, filler words.

### SEO inside living language
The main keyword ("Chichén Itzá" + the local words for tickets / guide / visit) belongs in
the H1, the first paragraph and one H2. Naturally, no stuffing.
The `<title>` must stay ≤ 60 characters including " | TouringBee". The meta description ~155 chars.

## FACTS THAT MUST TRANSFER EXACTLY (do not "localize" these)

TouringBee product facts:
- Self-guided audio tour, played on your phone as you walk.
- **The GPS rule — never get this wrong:** the guide HAS an offline GPS map that shows where you
  are, but it does **NOT** auto-play anything. The user starts each recording themselves on
  reaching the spot. NEVER write "GPS launches the story automatically / auto-plays".
- 100% offline after one download. Works on iOS and Android.
- One payment, instant access, no subscription, access for 1 year. **From €9.99.**
- 8 languages. **16 stops, about 1.5 hours** for this tour. 6,022 travellers have used it.

Chichén Itzá facts (2026), transfer the numbers exactly:
- Entry for foreigners: INAH federal 105 MXN + Yucatán state 592 MXN = ~697 MXN (~€35 / $40),
  paid at two separate windows.
- Hours 8:00–17:00; ticket booths and last entry 16:00.
- Climbing banned since 2006.
- Equinox serpent ~20 March and ~22 September.
- El Castillo 30 m high, four staircases of 91 steps.
- Great Ball Court: 168 m, largest in Mesoamerica; ball weighed 3–5 kg.
- Sacred Cenote ~60 m across, 300 m north of the pyramid. Ik Kil 3 km south.
- ~2h30 from Cancún (180D toll road, cash pesos only), 40 min from Valladolid, ~1h45 from Mérida.

## HTML — CRITICAL

Each string may contain HTML and entities. **Preserve them byte-for-byte** in the output:
- tags: `<a href="#inside">…</a>`, `<strong>`, `<em>`, `<small>`, `<b>`, `<br>`
- closing fragments at the end of a string: `</div>`, `</li>`
- a LEADING SPACE at the start of a string — keep it
- entities: `&amp;` `&euro;` `&middot;` `&mdash;` `&rarr;` `&middot;`
- If the string is `" GPS map</div>"` your output must also start with a space and end with `</div>`.
- Never introduce raw `&`, `<` or `>` — use `&amp;` etc.
- Do not change any URL, class name or attribute.

## Reviews
The six review quotes are real traveller reviews. Localize them so they read naturally in the
target language (keep the quotation marks and the meaning), the way a review site shows
auto-translated reviews. Keep them short and spoken.

## Output format

Read `/home/claude/chichenitzawalk/tr/strings_en.json` — a JSON array of 230 English strings.

Write `/home/claude/chichenitzawalk/tr/tr_<LANG>.json` — a JSON **object** mapping every one of
those 230 English strings (exact key, byte-for-byte) to its localized value.

- All 230 keys must be present. No extras.
- Some values legitimately stay identical (proper nouns like "El Castillo", "Tzompantli",
  "Instant access" if the language uses it, "Home" → localize it though).
- "English", "Español", "Français", "Deutsch", "Italiano", "Русский" are the language names in the
  footer language list — render each in its OWN language (they are endonyms), i.e. they normally
  stay as they are in every localization.
- Write the file with `json.dump(..., ensure_ascii=False, indent=1)` or equivalent UTF-8.

Verify before finishing: load your JSON, assert the key set equals the key set of strings_en.json.
Report only: the language, the number of keys, and any string you deliberately left unchanged.
