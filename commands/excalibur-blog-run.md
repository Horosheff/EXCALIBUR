---
description: Excalibur BLOG — полный прогон статьи через оркестратор и субагентов.
---

# Excalibur BLOG — запуск пайплайна

Откройте workspace с плагином **EXCALIBUR** и выполните команду или напишите:

«Запусти Excalibur BLOG для темы **B01**» / «publish: yes»

## Параметры

- `topic_id`: B01 | all | P0-only
- `publish`: yes | no (default: no)

## Оркестратор

Директор — **основной агент чата** (не Task). Сценарий: [skills/director-excalibur-blog/SKILL.md](../skills/director-excalibur-blog/SKILL.md).

Handoff: `shared/excalibur-blog-handoff.md`
