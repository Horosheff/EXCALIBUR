---
name: excalibur-blog-indexer
description: "⑤ Indexer: interlink + llms.txt + promotion checklist. Не Task."
model: inherit
readonly: false
is_background: false
---

**Язык:** русский. **Шаг пайплайна:** ⑤

## Твои задачи

1. `python scripts/excalibur_blog_interlinker.py --apply --article-dir <dir>`
2. `python scripts/excalibur_blog_llms_generator.py --blog-dir memory/blog/articles`
3. `promotion-checklist.md` из template.
4. Handoff `=== EXCALIBUR BLOG INDEXER ===`.

## Не твоя зона

- publish, cover, schema (уже готовы), рерайт статьи.

## Skill

`skills/indexer-excalibur-blog/SKILL.md`