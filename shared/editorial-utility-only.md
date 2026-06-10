# Excalibur BLOG — только полезные статьи (utility-only)

Канон: `memory/brief/editorial-policy.json`

## Принцип

**Публикуем только то, что даёт действие.** После прочтения читатель знает *что сделать* — не «вообще про тему».

| ✅ Берём | ❌ Не берём |
|---------|------------|
| How-to, пошаговый гайд | Новости, «вышло обновление» |
| Чеклист перед действием | Мнение без инструкции |
| Comparison с таблицей и выбором | «Что такое X» на 9k без шагов |
| Troubleshooting / fix | Trend-посты, размышления |
| Workflow (A→B→C) | Корпоративная вода, мотивация |

## Gate 1 — тема (`blog-topics.md`)

Перед research:

```bash
python scripts/excalibur_blog_utility_gate.py --topic-id B01
```

**Blocker `UTILITY TOPIC BLOCKER`** — тему не пускаем в пайплайн.

Обязательные поля карточки:

- `search_intent`: `how_to` | `checklist` | `comparison` | `troubleshooting` | `workflow` | `parent_guide`
- `article_mode`: **B** (инструкция/гайд)
- `h1` / `primary_query`: глагол действия («как…», «чек-лист…», «сравнение…»)

## Gate 2 — research

Research-агент **отклоняет** угол без практики. В `research-notes.md`:

- `utility_verdict: PASS`
- `reader_outcome`: одно предложение — что сможет сделать читатель
- `action_outline`: 5–9 шагов или чеклист-пунктов

## Gate 3 — writer

Контракт: `shared/excalibur-article-writing-contract.md`

- Каждый H2 = подзадача + **рекомендация** (делать / не делать)
- Минимум **5** нумерованных шагов ИЛИ чеклист 10+ пунктов
- Workflow-схема (`→`) или таблица (comparison)
- FAQ — короткие **ответы-действия**, не пересказ

## Gate 4 — GEO QA

```bash
python scripts/excalibur_blog_utility_gate.py \
  --article-dir memory/blog/articles/<topic_id>-<slug>
```

**Blocker `UTILITY ARTICLE BLOCKER`** — writer правит (FIX), QA не PASS.

Плюс slop-detector (вода/штампы).

## Как провернуть без воды (чеклист редактора)

1. **Island test:** вырежь H2 — остаётся ли actionable кусок?
2. **So what test:** каждый абзац — «и что мне с этим делать?»
3. **Lead:** боль + ответ + результат (не «в этой статье»)
4. **Нет режима A** в utility-only блоге
5. **Цифры** только из research / fact-bank
6. **CTA ≤ 3**, не подменяет пользу

## Связанные файлы

- `memory/brief/site-brief.md` — niche + editorial
- `skills/excalibur/references/article-archetypes.md` — скелет B
- `skills/excalibur/references/ai-slop-blocklist.md` — вода/штампы
- `shared/quality-blog.md` — blockers
