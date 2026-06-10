---
name: indexer-excalibur-blog
description: Excalibur BLOG Indexer — interlink между статьями + llms.txt для AI crawlers.
---

# Excalibur BLOG — Indexer

После cover + schema.

## Shell

```bash
python scripts/teya_excalibur_interlinker.py --apply \
  --article-dir memory/blog/articles/<topic_id>-<slug>

python scripts/teya_excalibur_llms_generator.py \
  --blog-dir memory/blog/articles
```

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
