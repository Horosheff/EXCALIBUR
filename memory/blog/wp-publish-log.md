# Excalibur BLOG — WP publish log

## 2026-06-11 — B02 avtomatizaciya-n8n-ai-agents

| Field | Value |
|-------|-------|
| topic_id | B02 |
| slug | avtomatizaciya-n8n-ai-agents |
| verdict | **FAIL** |
| post_id | — |
| permalink | — |

### Preconditions

- article-qa.md: PASS (93/100)
- link-verify.json: pass
- schema.jsonld: present
- cover/cover.png + alt: present
- EXCALIBUR_BLOG_ALLOW_PUBLISH: yes

### Attempt

```bash
python scripts/excalibur_blog_wp_publish.py --article-dir memory/blog/articles/B02-avtomatizaciya-n8n-ai-agents --dry-run  # OK
python scripts/excalibur_blog_wp_publish.py --article-dir memory/blog/articles/B02-avtomatizaciya-n8n-ai-agents       # FAIL
```

### Blockers

1. **Network:** HTTPS к `mayai.ru:443` недоступен из локальной среды (WinError 10060). FTP (порт 21) работает, HTTP-триггер bootstrap — нет.
2. **FTP path:** аккаунт `mrrutrnc_blog` видит только `/index.php` + `/cgi-bin/`, **без** `wp-load.php`. WordPress на `https://mayai.ru/blog/` — другой document root.
3. **Bootstrap 404:** загруженный `excalibur-blog-publish-once.php` (и тестовый `excalibur-test-once.php`) отдают HTTP 404 снаружи, хотя `index.php` в том же FTP root отдаётся на главной.

### Cleanup

Временные bootstrap-файлы удалены с FTP после диагностики.

### Next steps (для оператора)

1. Обновить `memory/site.env.local`: FTP_USER/FTP_PASS + `FTP_ROOT=/` (корень FTP после login, где `wp-load.php`). Путь панели Beget: `FTP_PANEL_PATH=/mrrutrnc.beget.tech/public_html/`.
2. Либо запустить publish с машины/сети, где `curl https://mayai.ru` отвечает < 5 с.
3. Альтернатива: WP Application Password + REST API / MCP WordPress blob publish.

---

## 2026-06-11 (retry) — B02 avtomatizaciya-n8n-ai-agents — **PASS**

| Field | Value |
|-------|-------|
| topic_id | B02 |
| slug | avtomatizaciya-n8n-ai-agents |
| verdict | **PASS** |
| post_id | 13324 |
| featured_image_id | 13325 |
| permalink | https://mayai.ru/avtomatizaciya-n8n-ai-agents/ |
| FTP_ROOT | `/` |

### Fix applied

- Обновлены FTP credentials в `memory/site.env.local`
- `FTP_ROOT=/` (wp-load.php в корне аккаунта после login)
- `excalibur_blog_wp_publish.py` — поддержка `FTP_ROOT` из env

### Result

```
OK post=13324 slug=avtomatizaciya-n8n-ai-agents
OK featured_image=13325
OK schema_meta=1
permalink=https://mayai.ru/avtomatizaciya-n8n-ai-agents/
```

---

## 2026-06-11 — B03 podklyuchenie-mcp-cursor — **PASS**

| Field | Value |
|-------|-------|
| topic_id | B03 |
| slug | podklyuchenie-mcp-cursor |
| verdict | **PASS** |
| post_id | 13335 |
| featured_image_id | 13336 |
| inline_images | 13337, 13338, 13339 |
| permalink | https://mayai.ru/podklyuchenie-mcp-cursor/ |
| trigger | `/excalibur-blog-run topic_id: B03 publish: yes` (publish вручную после fix оркестратора) |

### Result

```
OK post=13335 slug=podklyuchenie-mcp-cursor
OK featured_image=13336
OK schema_meta=1
OK inline_image_upload=13337 src=cover/inline-01.png
OK inline_image_upload=13338 src=cover/inline-02.png
OK inline_image_upload=13339 src=cover/inline-03.png
permalink=https://mayai.ru/podklyuchenie-mcp-cursor/
```
