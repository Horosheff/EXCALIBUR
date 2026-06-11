# Blog topics — Excalibur BLOG

Формат карточек. **Utility-only:** см. `shared/editorial-utility-only.md`.

**Разрешённые `search_intent`:** `how_to`, `checklist`, `comparison`, `troubleshooting`, `workflow`, `parent_guide`  
`**article_mode`:** только **B** (гайд/инструкция). Режим A (новости) — не публикуем.

Перед research:

```bash
python scripts/excalibur_blog_utility_gate.py --topic-id <ID>
```

---

## B01 — Пример темы

- **priority:** P0
- **slug:** primer-seo-stati
- **h1:** Как писать SEO-статьи, которые читают люди
- **primary_query:** как писать seo статьи
- **secondary_queries:** seo текст для блога, geo оптимизация статьи
- **search_intent:** how_to
- **article_mode:** B
- **h2_outline:**
  1. Зачем SEO и GEO в одной статье
  2. Структура longread
  3. FAQ и schema
  4. Чеклист перед публикацией
- **faq_hints:** сколько символов в seo статье; что такое geo в seo
- **internal_links:** /
- **cover_scene_hint:** редактор за ноутбуком, блокнот, тёплый свет

---

## B02 — Автоматизация процессов на n8n

- **priority:** P0
- **slug:** avtomatizaciya-n8n-ai-agents
- **h1:** Как настроить ИИ-агентов в n8n: пошаговое руководство по автоматизации бизнеса
- **primary_query:** автоматизация n8n
- **secondary_queries:** автоматизация ии n8n, примеры автоматизации n8n, ии агенты и автоматизация с n8n, автоматизация бизнеса n8n
- **search_intent:** how_to
- **article_mode:** B
- **h2_outline:**
  1. Почему n8n стал лидером автоматизации с ИИ в 2026 году
  2. Пошаговая настройка первого ИИ-агента в ноде AI Agent
  3. Подключение памяти и векторных баз данных (RAG) без кода
  4. Реальные примеры автоматизации n8n для бизнеса
  5. Сравнение n8n self-hosted и Make: что выбрать в 2026 году
- **faq_hints:** как устроен ai agent node в n8n; чем отличается n8n от make в 2026; как подключить базу знаний к ии в n8n
- **internal_links:** /services/
- **cover_scene_hint:** робот собирает конструктор из кубиков-интеграций (нод), яркие розовые стикеры с надписями "LangChain" и "AI Agent", неоновый свет, diy коллаж

---

## B03 — Подключение MCP в Cursor

- **priority:** P0
- **slug:** podklyuchenie-mcp-cursor
- **h1:** Как подключить MCP-серверы в Cursor: пошаговая инструкция для автоматизации
- **primary_query:** cursor mcp
- **secondary_queries:** mcp сервер для cursor, как подключить mcp к cursor, cursor ai mcp, настройка mcp сервера
- **search_intent:** how_to
- **article_mode:** B
- **h2_outline:**
  1. Что такое MCP и зачем подключать серверы в Cursor в 2026 году
  2. Где лежит конфиг: ~/.cursor/mcp.json и .cursor/mcp.json в проекте
  3. Пошаговое подключение stdio-сервера через npx (пример mcp.json)
  4. Проверка в Settings → Tools & MCP и настройка безопасности (auto-run, allowlist)
  5. Топ MCP-серверов для автоматизации: браузер, Wordstat, WordPress, Figma
  6. Troubleshooting: красный статус, spawn ENOENT, ошибки JSON и логи Output
- **faq_hints:** как подключить mcp к cursor; какие mcp серверы лучше для cursor; почему mcp сервер не подключается в cursor
- **internal_links:** /avtomatizaciya-n8n-ai-agents/
- **cover_scene_hint:** ноутбук с IDE Cursor, вокруг экрана «кубики-плагины» MCP-серверов, стикеры Browser/WordPress/Wordstat, неоновый diy-коллаж

---

