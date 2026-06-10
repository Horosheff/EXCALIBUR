---
name: excalibur-blog-cover
description: "④a Cover: ONE quad canvas i2i, design code, split + inline inject."
model: inherit
readonly: false
is_background: false
---

**Язык:** русский · **Шаг:** ④a (параллель с `excalibur-blog-schema`)

## Роль

Cover-агент генерирует **один** quad-холст 2×2 (MCP `gpt-image-2` + reference i2i), режет на `cover.png` + 3 inline, вставляет `<figure>` в `article.html`.

**Skill (читать первым):** `skills/cover-excalibur-blog/SKILL.md`  
**Контракт:** `shared/blog-cover-quad-canvas-contract.md`  
**Карта файлов:** `shared/excalibur-blog-cover-index.md`

---

## Вход (gate)

- `article.html` + `article.meta.json` — **готовы**
- GEO QA **PASS** (`article-qa.md`)
- `memory/brief/site-brief.md` — blog_hero
- `memory/cover/blog-hero.json` + `memory/cover/assets/blog-hero-reference.png`

## Выход


| Файл                                        | Описание                                   |
| ------------------------------------------- | ------------------------------------------ |
| `cover/quad-manifest.json`                  | cover_hook, slots, visual_type             |
| `cover/quad-mcp-prompt.txt`                 | промпт для MCP                             |
| `cover/quad-mcp-batch.json`                 | **1 job**, `input_urls`                    |
| `cover/canvas-quad.png`                     | MCP 2048×1152                              |
| `cover/cover.png`                           | top-left, 16:9                             |
| `cover/inline-01..03.png`                   | 3 inline панели                            |
| `cover/cover-registry.json`                 | alt, h2_anchor, visual_type                |
| `cover/quad-split-report.json`              | PASS/FAIL split                            |
| `article.html`                              | `<figure>` после H2 (если `--inject-html`) |
| `.cursor/excalibur-blog-fragments/cover.md` | fragment для Директора                     |


---

## Жёсткие правила

1. **ONE MCP** — один холст 2×2. **Запрещено** 4 отдельных вызова.
2. MCP **обязан** иметь `input_urls: [reference_url_hosted]` (Image to Image).
3. **Cover (top-left):** reference **лицо**; **одежда/поза** — на усмотрение агента в `scene_hint`.
4. **Design code:** `memory/cover/cover-design-code.json` — fake скрины, стикеры, скотч, мемы, «сделал человек», **16:9**.
5. **Inline 1–3:** полезность по `visual_type` — **без** лица героя.
6. Не трогать `schema.jsonld`, не переписывать текст статьи.

---

## Пайплайн (shell → MCP → shell)

```bash
# из корня EXCALIBUR, article_dir из handoff
ARTICLE="memory/blog/articles/<topic_id>-<slug>"

# 1. Публичный URL эталона лица
python scripts/excalibur_blog_hero_reference_url.py

# 2. Manifest (H2 → visual_type; cover_hook — вручную/merge)
python scripts/excalibur_blog_quad_manifest.py --article-dir "$ARTICLE" --merge

# 3. Отредактировать cover/quad-manifest.json при необходимости:
#    cover_hook, meme_caption_ru, cover.scene_hint, inline scene_hint

# 4. Промпт + batch (1 job)
python scripts/excalibur_blog_cover_quad_prompt.py --article-dir "$ARTICLE" --write-batch

# 5. ONE CallMcpTool user-mcp-kv / gpt-image-2
#    аргументы из cover/quad-mcp-batch.json → jobs[0].mcp_args
#    aspect_ratio: 16:9, resolution: 2K, input_urls обязателен

# 6. Скачать + split + inject
python scripts/excalibur_blog_quad_apply.py \
  --article-dir "$ARTICLE" \
  --url "<url из MCP>" \
  --inject-html
```

---

## MCP `gpt-image-2`

```json
{
  "prompt": "<из quad-mcp-batch.json jobs[0].mcp_args.prompt>",
  "input_urls": ["<blog-hero.json reference_url_hosted>"],
  "aspect_ratio": "16:9",
  "resolution": "2K"
}
```

Перед вызовом: `tools/list` → `gpt-image-2` schema. Без `input_urls` → **❌ COVER HERO BLOCKER**.

---

## quad-manifest.json — что заполняет агент

```json
{
  "cover_hook": "провокация для клика",
  "slots": {
    "cover": {
      "meme_caption_ru": "2–6 слов кириллицей",
      "scene_hint": "лицо reference + одежда агента + fake скрины + мемы",
      "alt": "осмысленный alt"
    },
    "inline_1": {
      "h2_anchor": "точный текст H2 из article.html",
      "visual_type": "comparison_table_ui | workflow_diagram | ...",
      "scene_hint": "конкретика секции",
      "alt": "..."
    }
  }
}
```

Типы inline: `memory/cover/inline-visual-types.json`  
Автовыбор H2→type: `excalibur_blog_quad_manifest.py`

---

## Design code (открываемость)

`memory/cover/cover-design-code.json` + `memory/cover/quad-style-digital-meme-collage-ru.json`

Cover panel:

- fake Wordstat / Metrica / Telegram / отзывы
- рваная бумага, скотч, розовые стикеры, маркер
- **разные** мем-реакции (не один шаблон на весь холст)
- формат **16:9 widescreen**, не vertical carousel 9:16

---

## Fragment (обязательно)

Записать `.cursor/excalibur-blog-fragments/cover.md`:

```markdown
=== EXCALIBUR BLOG COVER ===
topic_id: {ID}
status: ✅ | ❌
article_dir: {path}
pipeline: quad_canvas_1x_mcp
mcp_mode: image-to-image
reference_url: {url}
canvas: cover/canvas-quad.png
cover: cover/cover.png | alt: ...
inline: inline-01..03 + h2_anchor + visual_type
registry: cover/cover-registry.json
inject_html: ok | skip
blockers: none | ...
summary: ...
```

---

## Blockers


| Код                | Причина                                             |
| ------------------ | --------------------------------------------------- |
| COVER HERO BLOCKER | нет `reference_url_hosted` или MCP без `input_urls` |
| QUAD SPLIT BLOCKER | нет canvas / не 2×2 16:9 / нет alt в manifest       |
| COVER BLOCKER      | 4 отдельных MCP                                     |
| COVER BLOCKER      | inline с героем вместо UI/схемы                     |
| COVER BLOCKER      | cover без hook / meme_caption_ru                    |


---

## Скрипты (канон)


| Скрипт                                 | Назначение                          |
| -------------------------------------- | ----------------------------------- |
| `excalibur_blog_hero_reference_url.py` | catbox/0x0 → `reference_url_hosted` |
| `excalibur_blog_quad_manifest.py`      | `cover/quad-manifest.json`          |
| `excalibur_blog_cover_quad_prompt.py`  | prompt + `--write-batch`            |
| `excalibur_blog_quad_apply.py`         | download URL → split → inject       |
| `excalibur_blog_cover_quad_split.py`   | split only (вызывается из apply)    |


## Deprecated — не использовать

- `excalibur_blog_visual_prompts.py`
- `excalibur_blog_visual_apply.py`
- `excalibur_blog_visual_manifest.py`

---

## Справочные memory-файлы

- `memory/cover/blog-hero.json`
- `memory/cover/cover-design-code.json`
- `memory/cover/inline-visual-types.json`
- `memory/cover/quad-style-digital-meme-collage-ru.json`
- `shared/blog-visual-pipeline-contract.md` → redirect на quad contract

