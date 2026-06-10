---
name: excalibur-research
description: Excalibur BLOG Research — topic research перед статьёй (SERP, факты, угол). Gate до article.html.
---

# Excalibur BLOG — Research

## Когда

**Шаг 0 (скрипт, обязательно):** перед любым research — зафиксировать дату и собрать свежий SERP.

```bash
python scripts/excalibur_blog_research_start.py --topic-id B01
```

Создаёт в папке статьи:

- `research-context.json` — сегодняшняя дата, год, окно свежести, тема, список поисковых запросов
- `research-serp.json` — результаты web-поиска по запросам с `{year}` и текущим месяцем

`--dry-run` — только дата и запросы без HTTP.

Перед **каждой** статьей затем пиши `research-notes.md`. Без него нельзя утверждать цены, даты, версии, статистику.

## Вход

- Карточка из `memory/topics/blog-topics.md`
- `memory/brief/site-brief.md`, `fact-bank.md`
- `shared/quality-blog.md`
- MCP сервер `user-mcp-kv` со всеми инструментами `wordstat_*`

## Выход

`memory/blog/articles/<topic_id>-<slug>/research-context.json`  
`memory/blog/articles/<topic_id>-<slug>/research-serp.json`  
`memory/blog/articles/<topic_id>-<slug>/research-notes.md` (с разделом по Вордстату!)

## Обязательное использование Yandex Wordstat MCP

Каждый прогон исследования **обязан** задействовать инструмент `wordstat_get_top_requests` сервера `user-mcp-kv` для анализа спроса:

1. Вызови `wordstat_get_top_requests` для `primary_query` и ключевых `secondary_queries`.
2. Если вызов вернул `401 Unauthorized` (токен устарел):
   - Запиши в `research-notes.md` предупреждение: `⚠️ WORDSTAT AUTH WARNING: Токен Wordstat устарел. Обновите токен через: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40`
   - Сделай экспертную оценку семантики, но явно укажи, что точные объемы спроса не получены из-за авторизации.
3. Если вызов успешен:
   - Сформируй в `research-notes.md` таблицу спроса: Фраза | Показы в месяц.
   - Выдели сопутствующие LSI-запросы из топа выдачи Вордстата для использования копирайтером.

## Правила

0. **Сначала** `excalibur_blog_research_start.py` — дата/год и SERP на сегодня.
1. Web research 15–25 мин; используй `research-serp.json` + доп. источники; приоритет `fact-bank.md`.
2. Микро-исследование Wordstat через `user-mcp-kv` -> `wordstat_get_top_requests` (см. выше).
3. Минимум 3 конкурента в SERP.
4. Каждая цифра → таблица фактов или не использовать.
5. Не копировать структуру конкурента 1:1.

## Blockers

- `❌ RESEARCH BLOCKER` — тема не найдена и не создана из запроса пользователя
- `❌ RESEARCH BLOCKER` — нет источников для ключевых утверждений
