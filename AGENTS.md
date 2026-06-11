# Excalibur BLOG Cloud Instructions

Язык работы: русский.

## Главное правило

Для полной SEO/GEO статьи **нельзя** выполнять весь пайплайн одним Cloud Agent.

Cloud Agent обязан оркестрировать через **Директора** (роль в чате, не Task) и запускать субагентов:

```text
shell today + research_start
  → excalibur-blog-research
  → excalibur-blog-writer
  → excalibur-blog-geo-qa
  → excalibur-blog-cover || excalibur-blog-schema
  → excalibur-blog-indexer
  → excalibur-blog-publish (автоматически после Indexer; skip только publish:no)
```

## Cloud Task fallback

Если Cloud API не принимает `excalibur-blog-research`, `excalibur-blog-writer`, … как Task types:

- **отдельный `Task(generalPurpose)` на каждую роль**;
- передай путь `.cursor/agents/<role>.md` и `.cursor/skills/<skill>/SKILL.md`;
- короткий контракт: входные файлы, маркер результата, запреты;
- один Task = одна роль;
- параллель `cover || schema` — **два отдельных Task** в одном сообщении.

Если недоступен даже `generalPurpose` Task:

`❌ БЛОКЕР: Cloud Agent не может запускать отдельные Task/subagents даже через generalPurpose. Single-agent pipeline запрещён.`

## Что считать ошибкой

- Parent сам пишет `article.html` вместо Task writer.
- Parent сам делает cover/schema вместо параллельных Task.
- Parent запускает cover||schema **до** GEO QA PASS.
- Publish без обновления `shared/published-articles.md`.

## Handoff и fragments

- Handoff: `.cursor/excalibur-blog-handoff.md`
- Параллельные роли (cover, schema) пишут во фрагменты:
  - `.cursor/excalibur-blog-fragments/cover.md`
  - `.cursor/excalibur-blog-fragments/schema.md`
- Директор переносит фрагменты в handoff.

Маркеры:

- `=== EXCALIBUR BLOG RESEARCH ===`
- `=== EXCALIBUR BLOG WRITER ===`
- `=== EXCALIBUR BLOG GEO QA ===`
- `=== EXCALIBUR BLOG COVER ===`
- `=== EXCALIBUR BLOG SCHEMA ===`
- `=== EXCALIBUR BLOG INDEXER ===`
- `=== EXCALIBUR BLOG PUBLISH ===`
- `=== EXCALIBUR BLOG (PIPELINE DONE) ===`

## Канонические пути

`<PROJECT_ROOT>` — корень репозитория (без `C:\Users\...`).

| Артефакт | Путь |
|----------|------|
| Плагин / контракты | `agents/`, `skills/`, `shared/`, `scripts/` |
| Runtime memory | `memory/` |
| Журнал публикаций | `shared/published-articles.md` |
| Cloud agents | `.cursor/agents/` |
| Cloud skills | `.cursor/skills/` |

Перед пайплайном прочитай `shared/agent-pipeline-pitfalls.md`.

## Preflight (обязательно)

```bash
python3 scripts/excalibur_blog_today.py
python3 scripts/excalibur_blog_research_start.py --topic-id B01
```

Используй `EXCALIBUR_RUN_DATE`, `EXCALIBUR_SUGGESTED_TOPIC_ID` из today.py.
Если `python` недоступен — `python3`.

## Секреты

Только Cloud Secrets / env vars. Не печатать FTP/API ключи в handoff, PR, ответах.

- `FTP_*`, `PUBLIC_SITE_URL`, `EXCALIBUR_BLOG_ALLOW_PUBLISH`
- MCP через `${env:...}` в mcp.json

## Git hygiene

**Не коммитить:** `.cursor/excalibur-blog-handoff.md`, `shared/excalibur-blog-handoff.md`, `.cursor/excalibur-blog-fragments/`, `memory/site.env.local`, абсолютные пути Windows/macOS в отчётах.

**Коммитить после publish:** `shared/published-articles.md`, при необходимости артефакты статьи в `memory/blog/`.

## Субагенты (.cursor/agents)

| name | skill |
|------|-------|
| excalibur-blog-research | excalibur-research |
| excalibur-blog-writer | writer-excalibur-blog |
| excalibur-blog-geo-qa | excalibur-geo-qa |
| excalibur-blog-cover | cover-excalibur-blog |
| excalibur-blog-schema | schema-excalibur-blog |
| excalibur-blog-indexer | indexer-excalibur-blog |
| excalibur-blog-publish | excalibur-wp-publish |

Директор: `.cursor/agents/excalibur-blog-director.md` + `director-excalibur-blog` skill — **не Task**.

Полная настройка worker/automation: `CLOUD-AUTOMATION.md`.
