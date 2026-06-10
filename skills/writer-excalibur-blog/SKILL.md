# Excalibur BLOG — Writer

## Вход

- `research-notes.md` с **utility_verdict: PASS**
- `shared/excalibur-article-writing-contract.md`
- `shared/editorial-utility-only.md`
- `memory/brief/site-brief.md`, `conversion-map.md`

## Задача

1. **Только режим B** — инструкция/гайд/чеклист/comparison. Режим A запрещён.
2. Outline H2 = подзадачи с **действием** (не «вообще про тему»).
3. **ПРОСТОЙ ЧЕЛОВЕЧЕСКИЙ ЯЗЫК (ГЛАВНОЕ ПРАВИЛО):** Пиши максимально понятно и доступно для простого человека (предпринимателя, новичка, не-программиста). Исключай сложный технический снобизм. Любой используемый термин (API, RAG, Self-hosted, Docker) **обязан** иметь моментальную расшифровку и объяснение «на пальцах» (на простых аналогиях).
4. Hook 350–500 символов: боль → ответ → **что сделает читатель**.
5. Минимум **5** нумерованных шагов `<ol>` + workflow (`→`) или таблица.
6. Каждый H2: рекомендация «делать / не делать».
7. Body 8 500–9 500 знаков, FAQ 5–7 пар — **ответы-действия**.
8. `article.meta.json`: `article_mode: B`, `char_count`, `meta_ab` с A/B/AEO оптимизацией:
   - `title_seo`: 35–75 симв, точный `primary_query` в начале + триггер.
   - `title_ctr`: 40–100 симв, кликабельный крючок, обязательно эмодзи (например 💻, 🚀) или знаки ?, !
   - `title_aeo`: 35–90 симв, сформулирован как вопрос ИИ-поисковику (начинается с "Как", "Что", "Почему" или содержит "?").
   - `description_seo`: 100–180 симв.
9. Подзаголовки H2 должны начинаться с **глаголов действия** (создайте, настройте, проверьте) или содержать **маркеры действия** (как, чеклист, сравнение, выбор, пошагово). Минимум 3 H2 должны быть активными.

## Выход

```text
memory/blog/articles/<topic_id>-<slug>/article.html
memory/blog/articles/<topic_id>-<slug>/article.meta.json
```

## Blockers

- нет research-notes.md
- utility-only нарушен (вода, нет шагов)
- объём вне диапазона после 1 правки

References: `article-archetypes.md` (§ B only), `geo-writing-checklist.md`, `ai-slop-blocklist.md`
