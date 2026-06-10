# Excalibur BLOG — quality standard

Стандарт качества **только для статей блога**. Excalibur BLOG автономен — без Teya/AURA/Aurora gates.

## Blockers (статья)

- `UTILITY ARTICLE BLOCKER` — `excalibur_blog_utility_gate.py` FAIL (мало шагов, нет workflow/таблицы, вода)
- Выдуманные цены, даты, проценты без источника в `fact-bank.md` / `research-notes.md`
- AI-slop из blocklist (`skills/excalibur/references/ai-slop-blocklist.md`)
- Объём вне 8 500–9 500 символов текста
- Нет FAQ (5–7 пар)
- GEO QA score < 80 или CORE-EEAT < 16/20
- Link verify fail после 2 циклов
- HTML linter FAIL (запрещённые теги)

## Обязательно PASS

- `research-notes.md` с SERP и таблицей фактов
- `article-qa.md` verdict PASS
- `schema.jsonld` BlogPosting + FAQPage
- Cover PNG с alt

## Не применяется к Excalibur BLOG

- AURA visual budget, paint QA, Design Guardian
- Semantic core / Ядрышко pipeline
- Aurora theme build gates
