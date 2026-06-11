---
name: excalibur-geo-qa
description: Excalibur BLOG GEO QA — fact-check, link verify, linter, slop, cannibalization, article-qa PASS.
---

# Excalibur BLOG — GEO QA

## Когда

После `article.html` + `article.meta.json` от Writer. **До** cover/schema (их делает директор параллельно после PASS).

## Скрипты (обязательно)

```bash
python scripts/excalibur_blog_fact_checker.py \
  memory/blog/articles/<dir>/article.html \
  -o memory/blog/articles/<dir>/fact-check-report.json

python scripts/excalibur_link_verify.py \
  memory/blog/articles/<dir>/article.html \
  -o memory/blog/articles/<dir>/link-verify.json \
  --site-base https://YOUR_SITE

python scripts/excalibur_blog_html_linter.py \
  memory/blog/articles/<dir>/article.html \
  -o memory/blog/articles/<dir>/html-linter-report.json

python scripts/excalibur_blog_slop_detector.py \
  memory/blog/articles/<dir>/article.html \
  -o memory/blog/articles/<dir>/slop-detector-report.json

python scripts/excalibur_blog_cannibalization_guard.py \
  --article-dir memory/blog/articles/<dir>
```

## Выход

- `article-qa.md` verdict **PASS**
- handoff: `=== EXCALIBUR BLOG GEO QA ===`

**Pass:** score ≥ 80, CORE-EEAT ≥ 16/20, link-verify pass.

Schema и cover — **не** твоя зона (отдельные субагенты после PASS).
