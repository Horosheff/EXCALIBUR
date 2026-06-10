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

