# Site brief — Excalibur BLOG

Заполните перед первым прогоном. Excalibur BLOG читает этот файл вместо Teya research dossier.

## Сайт

- **site_name:** Пример Блога
- **site_url:** [https://example.com](https://example.com)
- **blog_path:** /blog/
- **language:** ru
- **niche:** (EdTech / SaaS / local service / …)

## Ниша и редакция

- **editorial_policy:** utility-only — только how-to, чеклисты, comparison, troubleshooting (`shared/editorial-utility-only.md`)
- **article_mode:** B (инструкция/гайд). Новости и «размышления» — не публикуем
- **gate:** `scripts/excalibur_blog_utility_gate.py` на теме и на статье

## Голос и тон

- **author_voice:** редакция бренда | editorial first-person
- **tone:** практично, по-человечески, без корпоративной воды
- **audience:** (кто читает, уровень)

## Главный герой визуала (обложки и inline)

- **blog_hero_id:** `blog-host`
- **reference:** `memory/cover/assets/blog-hero-reference.png`
- **lock:** `memory/cover/blog-hero.json`
- **правило:** на обложке — узнаваемое **лицо** с reference; **одежду** агент меняет свободно под крючок/тему (не копировать костюм с фото)
- **обложка:** обязателен **крючок** (кликбайт-намёк) + **русская meme-подпись** на картинке

## Офферы и CTA

См. также `conversion-map.md`. Кратко: главный оффер, Telegram/WhatsApp, форма — что можно упоминать в статьях.

## Запреты

- VPN, обход блокировок
- Выдуманные цены и статистика
- Эмодзи в тексте статей

## Обложки (если cover-concept ещё пуст)

- **preferred_cover_family:** brand_collage
- **brand_colors:** #FAFAF7, #1A1A2E, #E85D4C
- **visual_notes:** 16:9, узнаваемая серия; на meme-коллажах — **русские подписи** и герой из `blog-hero.json`