# Excalibur BLOG — Cloud Automation Setup

Настройка запуска в **Cursor Cloud Agents / Automations** по образцу [kovcheg-office-cloud](https://github.com/Horosheff/kovcheg-office-cloud).

## Что запускаем

Пайплайн одной статьи:

```text
today + research_start → research → writer → geo-qa → cover||schema → indexer → publish?
```

## Структура репозитория (как у Kovcheg Cloud)

```text
<PROJECT_ROOT>/
  AGENTS.md                          ← инструкции Cloud Agent
  CLOUD-AUTOMATION.md                ← этот файл
  .env.example
  .cursor/
    agents/                          ← Task types для Cloud
    skills/
    rules/
    excalibur-blog-handoff.md        ← runtime, не в git
    excalibur-blog-fragments/        ← cover + schema parallel
  agents/                            ← исходники плагина
  skills/
  shared/
  scripts/
  memory/
  .cursor-plugin/plugin.json
```

## Cursor docs

- [Cloud Agents setup](https://cursor.com/docs/cloud-agent/setup.md)
- [Secrets / env vars](https://cursor.com/docs/cloud-agent/setup.md#environment-variables-and-secrets)
- [Automations](https://cursor.com/docs/cloud-agent/automations.md)
- [Self-hosted pool](https://cursor.com/docs/cloud-agent/self-hosted-pool.md)
- [MCP in Cloud](https://cursor.com/docs/cloud-agent/capabilities.md#mcp-tools)

## Self-hosted worker

Нужен, если в облаке Cursor нет:

- MCP KV (`gpt-image-2` для обложек);
- FTP к WordPress;
- стабильного web search для research.

```powershell
cd "<PROJECT_ROOT>"
$env:CURSOR_API_KEY="YOUR_KEY"
$env:EXCALIBUR_PROJECT_ROOT="<PROJECT_ROOT>"
agent worker start --pool --pool-name excalibur-blog --idle-release-timeout 600
```

## Secrets / env vars

Из `.env.example` + Cloud Dashboard:

| Variable | Зачем |
|----------|-------|
| `PUBLIC_SITE_URL` | link verify, recent WP posts |
| `FTP_*` | `excalibur_blog_wp_publish.py` |
| `EXCALIBUR_BLOG_ALLOW_PUBLISH` | `yes` только когда готовы публиковать |
| `EXCALIBUR_TOPIC_ID` | опционально фиксировать тему (иначе today.py предложит P0) |
| `EXCALIBUR_PROJECT_ROOT` | корень репо на worker |

Не коммитить: `memory/site.env.local`, реальные ключи MCP.

## Automation schedule

Cursor Automation → Schedule, пример:

```text
0 10,15,20 * * *
```

- Repository: ваш fork `excalibur-blog` / EXCALIBUR
- Worker pool: `excalibur-blog`
- Branch: `main`

## Automation prompt (шаблон)

```text
Ты работаешь в репозитории Excalibur BLOG.

Запусти полный пайплайн SEO/GEO статьи через оркестратора (Директор), не выполняя роли сам.

0. Прочитай AGENTS.md и shared/agent-pipeline-pitfalls.md.
1. python3 scripts/excalibur_blog_today.py — зафиксируй дату и topic_id.
2. Сбрось .cursor/excalibur-blog-handoff.md одной строкой "# Excalibur BLOG — новая сессия".
3. Очисти .cursor/excalibur-blog-fragments/.
4. python3 scripts/excalibur_blog_research_start.py --topic-id <из EXCALIBUR_SUGGESTED_TOPIC_ID или env>.
5. Task(excalibur-blog-research) → research-notes.md.
6. Task(excalibur-blog-writer) → article.html + meta.
7. Task(excalibur-blog-geo-qa) → PASS + все QA JSON.
8. ПАРАЛЛЕЛЬНО Task(excalibur-blog-cover) + Task(excalibur-blog-schema).
   Cover/schema пишут во fragments; перенеси в handoff.
9. Task(excalibur-blog-indexer).
10. Если EXCALIBUR_BLOG_ALLOW_PUBLISH=yes → Task(excalibur-blog-publish) и обнови shared/published-articles.md.

Fallback: если Task types недоступны — generalPurpose per role (см. AGENTS.md).

Запрещено: single-agent pipeline, cover до QA PASS, секреты в handoff.

Финальный ответ: article_dir + QA verdict + publish URL или блокер.
```

## После каждого прогона

Проверь изменения:

- `shared/published-articles.md` (если publish)
- `memory/blog/excalibur-blog-run-log.md`
- артефакты в `memory/blog/articles/<topic_id>-<slug>/`

Если Automation через PR — merge PR, чтобы следующий run видел ledger.

## Локальная разработка плагина

Правки agents/skills делай в `agents/` и `skills/`, затем **синхронизируй в `.cursor/`**:

```powershell
Copy-Item agents\* .cursor\agents\ -Force
Copy-Item skills\* .cursor\skills\ -Recurse -Force
Copy-Item rules\* .cursor\rules\ -Force
```

Или добавь script `scripts/sync_cursor_cloud.ps1` при необходимости.
