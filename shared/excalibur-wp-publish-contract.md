# Excalibur BLOG — WordPress publish contract

Excalibur BLOG готовит артефакты локально; публикация — через `scripts/excalibur_blog_wp_publish.py` и FTP bootstrap.

## Prerequisites

- `article.html`, `article.meta.json`, `article-qa.md` (verdict PASS)
- `schema.jsonld`
- `cover/cover.png` + `cover-registry.json` (alt)
- `link-verify.json` (verdict pass)
- `memory/site.env.local` — FTP + `FTP_ROOT` (корень WP, где `wp-load.php`) + `PUBLIC_SITE_URL` + `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes`

## Скрипт

```bash
python scripts/excalibur_blog_link_verify.py \
  memory/blog/articles/B01-slug/article.html \
  -o memory/blog/articles/B01-slug/link-verify.json \
  --site-base https://example.com

python scripts/excalibur_blog_wp_publish.py \
  --article-dir memory/blog/articles/B01-slug
```

`--dry-run` — проверка payload без FTP.

## Что делает publish

1. `wp_insert_post` / `wp_update_post` — title, slug, content, excerpt
2. Featured image из `cover/cover.png` + alt
3. **Inline images** — все локальные `<img src="cover/...">` загружаются в Media Library, `src` заменяется на WP URL
4. Post meta `_excalibur_blog_schema_jsonld` — JSON-LD для `single.php`

## Артефакты после publish

```text
memory/blog/articles/<topic_id>-<slug>/wp-publish-result.json
memory/blog/wp-publish-log.md
```

## Schema в теме WP

```php
$schema = get_post_meta(get_the_ID(), '_excalibur_blog_schema_jsonld', true);
if ($schema) {
    echo '<script type="application/ld+json">' . wp_kses_post($schema) . '</script>';
}
```

## Blockers

- `❌ PUBLISH BLOCKER` — QA не PASS, link-verify fail, нет credentials
- Production HTML не должен содержать MCP URLs — только WP media для featured image

Skill: `skills/publish-excalibur-blog/SKILL.md` (alias: `skills/excalibur-wp-publish/SKILL.md`)
