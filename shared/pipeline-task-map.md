# Excalibur BLOG — карта задач и субагентов

Директор **не** Task. Все роли ниже — `Task(<name>)`.

## Схема

```text
[Д] Директор (чат)
  │
  ├─ shell: excalibur_blog_today.py
  ├─ shell: excalibur_blog_research_start.py
  │
  ├─ ① Task(excalibur-blog-research)
  ├─ ② Task(excalibur-blog-writer)
  ├─ ③ Task(excalibur-blog-geo-qa)
  │
  ├─ ④a Task(excalibur-blog-cover)  ─┐ параллель
  ├─ ④b Task(excalibur-blog-schema) ─┘
  │
  ├─ ⑤ Task(excalibur-blog-indexer)
  └─ ⑥ Task(excalibur-blog-publish)   ← только publish=yes
```

## Таблица распределения

| Шаг | Кто | Task name | Задачи | Артефакты | Handoff / fragment |
|-----|-----|-----------|--------|-----------|-------------------|
| 0 | **Директор** | — (shell) | дата, SERP, **utility gate темы**, article_dir | research-context.json, research-serp.json | обновить таблицу статуса |
| ① | **Research** | `excalibur-blog-research` | SERP + web, факты с источниками, угол, FAQ-кандидаты | research-notes.md | handoff `=== RESEARCH ===` |
| ② | **Writer** | `excalibur-blog-writer` | longread 8.5–9.5k, FAQ HTML, meta_ab | article.html, article.meta.json | handoff `=== WRITER ===` |
| ③ | **GEO QA** | `excalibur-blog-geo-qa` | 5 QA-скриптов + **utility gate**, score ≥80 | *-report.json, utility-gate-report.json, article-qa.md | handoff `=== GEO QA ===` |
| ④a | **Cover** | `excalibur-blog-cover` | ONE MCP quad 2×2 i2i + design code + split → cover + 3 inline | canvas-quad.png, cover.png, inline-01..03, registry | fragment cover.md |
| ④b | **Schema** | `excalibur-blog-schema` | BlogPosting + FAQPage JSON-LD | schema.jsonld | fragment schema.md |
| ⑤ | **Indexer** | `excalibur-blog-indexer` | interlink --apply, llms.txt | article.html (links), llms*.txt, promotion-checklist | handoff `=== INDEXER ===` |
| ⑥ | **Publish** | `excalibur-blog-publish` | FTP WP post, featured, schema meta | wp-publish-result.json | handoff `=== PUBLISH ===` + published-articles.md |

## Кто чем НЕ занимается

| Роль | Запрещено |
|------|-----------|
| Research | писать article.html |
| Writer | QA-скрипты, cover, schema, publish |
| GEO QA | править текст статьи (только FIX цикл → writer) |
| Cover | schema, HTML статьи |
| Schema | cover, HTML статьи |
| Indexer | publish, переписывать body с нуля |
| Publish | писать/редактировать longread |

## Параллель (только одна пара)

**④a Cover || ④b Schema** — после ③ QA PASS.

Нельзя параллелить: ①→②→③, ⑤ после ④, ⑥ после ⑤.

## Промпты для Директора (копировать в Task)

### ① Research

```text
Ты excalibur-blog-research. topic_id: {ID}. article_dir из handoff.
Прочитай agents/excalibur-blog-research.md + skills/excalibur-research/SKILL.md + shared/editorial-utility-only.md.
Сначала utility gate темы. Угол только практический (how-to/чеклист). Выход: research-notes.md с utility_verdict PASS.
Блок === EXCALIBUR BLOG RESEARCH ===. Не пиши article.html.
```

### ② Writer

```text
Ты excalibur-blog-writer. topic_id: {ID}.
Прочитай agents/excalibur-blog-writer.md + skills/writer-excalibur-blog/SKILL.md + shared/editorial-utility-only.md.
Только режим B: шаги, рекомендации, без воды. 8500–9500 символов.
Блок === EXCALIBUR BLOG WRITER ===. Не запускай QA и cover.
```

### ③ GEO QA

```text
Ты excalibur-blog-geo-qa. topic_id: {ID}.
Прочитай agents/excalibur-blog-geo-qa.md + skills/excalibur-geo-qa/SKILL.md.
Запусти все QA-скрипты + excalibur_blog_utility_gate.py. article-qa.md verdict PASS обязателен.
Блок === EXCALIBUR BLOG GEO QA ===. Не делай cover/schema.
```

### ④a Cover (параллель)

```text
Ты excalibur-blog-cover. topic_id: {ID}. article_dir из handoff.
Прочитай agents/excalibur-blog-cover.md + skills/cover-excalibur-blog/SKILL.md + shared/blog-cover-quad-canvas-contract.md.
1) excalibur_blog_hero_reference_url.py
2) excalibur_blog_quad_manifest.py --merge
3) правка cover/quad-manifest.json (hook, scene_hint, outfit агента)
4) excalibur_blog_cover_quad_prompt.py --write-batch
5) ONE CallMcpTool gpt-image-2 по quad-mcp-batch.json (input_urls обязателен)
6) excalibur_blog_quad_apply.py --url ... --inject-html
Fragment .cursor/excalibur-blog-fragments/cover.md (=== EXCALIBUR BLOG COVER ===). Не 4 MCP. Не трогай schema.
```

### ④b Schema (параллель)

```text
Ты excalibur-blog-schema. topic_id: {ID}.
Прочитай agents/excalibur-blog-schema.md + skills/schema-excalibur-blog/SKILL.md.
schema.jsonld BlogPosting+FAQPage. Fragment .cursor/excalibur-blog-fragments/schema.md (=== EXCALIBUR BLOG SCHEMA ===). Не делай cover.
```

### ⑤ Indexer

```text
Ты excalibur-blog-indexer. topic_id: {ID}.
Прочитай agents/excalibur-blog-indexer.md + skills/indexer-excalibur-blog/SKILL.md.
interlinker --apply + llms generator. Блок === EXCALIBUR BLOG INDEXER === в handoff.
```

### ⑥ Publish

```text
Ты excalibur-blog-publish. topic_id: {ID}.
Прочитай agents/excalibur-blog-publish.md + skills/excalibur-wp-publish/SKILL.md.
Dry-run затем publish. Обнови shared/published-articles.md. Блок === EXCALIBUR BLOG PUBLISH ===.
```

## Файлы субагентов

| name | agent-md |
|------|----------|
| excalibur-blog-research | [agents/excalibur-blog-research.md](../agents/excalibur-blog-research.md) |
| excalibur-blog-writer | [agents/excalibur-blog-writer.md](../agents/excalibur-blog-writer.md) |
| excalibur-blog-geo-qa | [agents/excalibur-blog-geo-qa.md](../agents/excalibur-blog-geo-qa.md) |
| excalibur-blog-cover | [agents/excalibur-blog-cover.md](../agents/excalibur-blog-cover.md) |
| excalibur-blog-schema | [agents/excalibur-blog-schema.md](../agents/excalibur-blog-schema.md) |
| excalibur-blog-indexer | [agents/excalibur-blog-indexer.md](../agents/excalibur-blog-indexer.md) |
| excalibur-blog-publish | [agents/excalibur-blog-publish.md](../agents/excalibur-blog-publish.md) |

Cloud: те же имена в `.cursor/agents/`.
