---
name: excalibur-wp-publish
description: Excalibur BLOG WP Publish — публикация статьи в WordPress (post, featured, schema meta).
---

# Excalibur BLOG — WP Publish

## Когда

После `✅ ARTICLE OK` и явного `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` в `memory/site.env.local`.

## Контракт

`shared/excalibur-wp-publish-contract.md`

## Preconditions

- `article-qa.md` → PASS
- `link-verify.json` → pass
- `cover/cover.png` + alt
- `memory/site.env.local` — FTP_*, PUBLIC_SITE_URL

## Шаги

```bash
python scripts/excalibur_link_verify.py <article.html> -o link-verify.json --site-base $PUBLIC_SITE_URL

python scripts/excalibur_blog_wp_publish.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> --dry-run

python scripts/excalibur_blog_wp_publish.py \
  --article-dir memory/blog/articles/<topic_id>-<slug>
```

Запиши `memory/blog/wp-publish-log.md`.

## Schema в теме WP

Post meta `_excalibur_blog_schema_jsonld` — вывести в `single.php` темы сайта.

## Blockers

- `❌ PUBLISH BLOCKER` — QA / links / credentials / cover
