# Excalibur BLOG — Quad Canvas (1 MCP → 4 панели)

Cover-агент работает **после** `article.html` + GEO QA PASS.

## Главное правило

**Один** вызов MCP `gpt-image-2` → один холст `2048×1152` (2×2, каждая панель 16:9) → split в `cover.png` + `inline-01..03.png`.

| Панель | Роль | Герой |
|--------|------|-------|
| **top-left cover** | Крючок + RU-мем | **да**, лицо с reference (`input_urls`); **одежда — на усмотрение агента** |
| **3 inline** | Полезность по H2: таблица, workflow, чеклист, UI | **нет** |

## Workflow

```bash
# 1. Публичный URL эталона (обязательно для i2i)
python scripts/excalibur_blog_hero_reference_url.py

# 2. Manifest: cover_hook + visual_type для inline
python scripts/excalibur_blog_quad_manifest.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> --merge

# 3. Промпт + MCP batch (1 job)
python scripts/excalibur_blog_cover_quad_prompt.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> --write-batch

# 4. ONE CallMcpTool gpt-image-2 по cover/quad-mcp-batch.json
#    input_urls: [reference_url_hosted] — обязательно

# 5. Скачать canvas + split
python scripts/excalibur_blog_quad_apply.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --url "<mcp_url>" --inject-html
```

## Раскладка 2×2

```text
+------------------+------------------+
|  cover (hero)    |  inline_1 (UI)   |
|  top_left        |  top_right       |
+------------------+------------------+
|  inline_2        |  inline_3        |
|  bottom_left     |  bottom_right    |
+------------------+------------------+
```

## Файлы

| Файл | Кто |
|------|-----|
| `memory/cover/blog-hero.json` | `reference_url_hosted` |
| `memory/cover/inline-visual-types.json` | типы inline-панелей |
| `cover/quad-manifest.json` | cover + inline slots |
| `cover/quad-mcp-batch.json` | **1 job**, `input_urls` |
| `cover/canvas-quad.png` | MCP результат |
| `cover/cover.png`, `inline-01..03.png` | split script |
| `cover/cover-registry.json` | split script |

## Design code (открываемость)

`memory/cover/cover-design-code.json` — human hook collage для cover panel:

- fake скрины (Wordstat, отзывы, Telegram, analytics)
- рваная бумага, скотч, розовые стикеры, маркер
- разные мем-реакции (не один Drake на весь холст)
- 16:9 widescreen, **не** vertical carousel

Inline panels: полезный UI + лёгкий human layer (стикер, tape, mini screenshot).

См. `memory/cover/inline-visual-types.json`. Выбор по keywords H2 в `excalibur_blog_quad_manifest.py`.

## Blockers

- `❌ COVER HERO BLOCKER` — нет `reference_url_hosted` или MCP без `input_urls`
- **4 отдельных MCP** на cover+inline — запрещено
- inline-панель с meme/host вместо UI/схемы
- обложка без крючка / без `meme_caption_ru`
