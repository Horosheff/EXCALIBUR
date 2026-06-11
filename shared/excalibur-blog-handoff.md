# Excalibur BLOG — handoff

`pipeline_started_at`: 2026-06-11 05:11 MSK
`topic_id`: B03
`article_dir`: memory/blog/articles/B03-podklyuchenie-mcp-cursor
`publish`: yes

---

## Статус пайплайна


| Шаг | Агент                                         | Статус                 | Время      |
| --- | --------------------------------------------- | ---------------------- | ---------- |
| 🔍  | excalibur-blog-scout                          | ✅ PASS                 | 05:11      |
| 0   | shell research_start + utility gate           | ✅ PASS                 | 05:12      |
| 1   | excalibur-blog-research                       | ✅ PASS                 | 11.06.2026 |
| 2   | excalibur-blog-writer                         | ✅ PASS                 | 11.06.2026 |
| 3   | excalibur-blog-geo-qa                         | ✅ PASS                 | 11.06.2026 |
| 4   | excalibur-blog-cover || excalibur-blog-schema | ✅ PASS                 | 11.06.2026 |
| 5   | excalibur-blog-indexer                        | ✅ PASS                 | 11.06.2026 |
| 6   | excalibur-blog-publish                        | ✅ PASS                 | 11.06.2026 |


---

## Контекст запуска

- Команда: `/excalibur-blog-run topic_id: B03 publish: yes`
- Предыдущий прогон ошибочно пропустил publish → исправлено правилами оркестратора + ручной publish B03
- B01 и B02 уже завершены → запускаем Scout для новой P0-темы (B03+)
- Site: Maya AI / Ковчег — [https://mayai.ru/blog/](https://mayai.ru/blog/)

---

=== EXCALIBUR BLOG RESEARCH ===

**topic_id:** B03  
**slug:** podklyuchenie-mcp-cursor  
**article_dir:** memory/blog/articles/B03-podklyuchenie-mcp-cursor  
**research_date:** 2026-06-11  
**utility_verdict:** PASS  
**search_intent:** how_to | **article_mode:** B  

**primary_query:** cursor mcp (630 показов/мес)  
**secondary_queries:** mcp сервер для cursor (32), как подключить mcp к cursor (12), cursor ai mcp (61), настройка mcp сервера (74)

**reader_outcome:** Читатель подключит первый MCP-сервер в Cursor через UI или mcp.json, проверит статус в Tools & MCP, вызовет tool из Agent с настройкой безопасности и починит типичные ошибки через MCP Logs.

**action_outline (9 шагов):** обновить Cursor → выбрать global/project mcp.json → one-click или ручной stdio/url → перезапуск → тест в Agent → allowlist → troubleshooting → стек 2–3 серверов для автоматизации.

**SERP gap:** мало русских пошаговых how-to под «как подключить mcp к cursor»; конкуренты — docs EN, топ-серверы, 1С-ниша. Угол «Ковчег»: не-программист + контент-завод/Make.

**Ключевые источники:** cursor.com/ru/help/customization/mcp, cursor.com/docs/mcp, cursor.com/blog/dynamic-context-discovery, anthropic.com/news/model-context-protocol.

**Артефакты:** research-notes.md (22 факта, Wordstat, FAQ 7, GEO hooks)  
**Wordstat:** OK (MCP user-mcp-kv, без auth warning)

**Writer next:** excalibur-blog-writer — карточка B03, h2_outline из blog-topics.md, internal link B02 + mayai MCP-create guide.

**Blockers:** нет

---

=== EXCALIBUR BLOG WRITER ===

**topic_id:** B03  
**slug:** podklyuchenie-mcp-cursor  
**article_dir:** memory/blog/articles/B03-podklyuchenie-mcp-cursor  
**article_mode:** B (how_to)  
**char_count:** 9018 (текст без HTML-тегов)  
**hook_len:** 373 символа  

**Артефакты:** article.html, article.meta.json  
**author_id:** artur-horoshev  

**Структура:** TL;DR blockquote → TOC (10 якорей) → 9 секций H2 → 2 таблицы → workflow blockquote → 10 нумерованных шагов (2× ol) → чеклист 10 пунктов → Fact Check → FAQ 7 пар  

**Internal links:** /avtomatizaciya-n8n-ai-agents/ (×3: контекст, next-steps, FAQ); mayai.ru MCP-create guide (×1)  
**CTA:** kv-ai.ru/obuchenie-po-make (×2), t.me/maya_pro (×1), kv-ai.ru/artur-horosheff (×1 в Fact Check)  

**meta_ab:** title_seo / title_ctr / title_aeo / description_* заполнены  
**primary_query:** cursor mcp  

**Writer gate:** PASS (8500–9500, режим B, FAQ 7, шаги ≥5, таблица + workflow)  

**QA next:** excalibur-blog-geo-qa  
**Blockers:** нет

---

=== EXCALIBUR BLOG GEO QA ===

**topic_id:** B03  
**slug:** podklyuchenie-mcp-cursor  
**article_dir:** memory/blog/articles/B03-podklyuchenie-mcp-cursor  
**qa_date:** 2026-06-11  
**verdict:** PASS  
**score_total:** 94/100  
**core_eeat_lite:** 19/20  

**Gates:** link-verify pass | utility gate (article) pass | html-linter pass | fact-check pass | cannibalization pass  

**Script reports:** fact-check-report.json, link-verify.json, html-linter-report.json, slop-detector-report.json (WARNING, 0 cliches), cannibalization-report.json, utility-gate-report.json  

**Fix cycle 1:** `<pre><code>` → blockquote (контракт HTML); cursor.directory href → plain text (HTTP 429 в QA)  

**Cover||Schema next:** excalibur-blog-cover || excalibur-blog-schema (параллельно)  
**Indexer next:** excalibur-blog-indexer  
**Blockers:** нет  

**Optional перед publish:** восстановить href `https://cursor.directory`; добавить `<img>` с alt; повторить link-verify с `--site-base https://mayai.ru`

---

=== EXCALIBUR BLOG INDEXER ===

**topic_id:** B03  
**slug:** podklyuchenie-mcp-cursor  
**article_dir:** memory/blog/articles/B03-podklyuchenie-mcp-cursor  
**indexer_date:** 2026-06-11  
**verdict:** PASS  

**Interlinker:** `excalibur_blog_interlinker.py --apply --blog-dir memory/blog/articles --site-base https://mayai.ru`  
**opportunities_found:** 0 (автовставок нет)  
**article.html internal links (сохранены от Writer):** `/avtomatizaciya-n8n-ai-agents/` ×3 (контекст, next-steps, FAQ)  

**LLMs:** `excalibur_blog_llms_generator.py --out-dir memory/blog --site-base https://mayai.ru`  
**Артефакты:** `memory/blog/llms.txt` (3 статьи), `memory/blog/llms-full.txt`, `memory/blog/interlink-suggestions.json`  

**Promotion:** `memory/blog/articles/B03-podklyuchenie-mcp-cursor/promotion-checklist.md`  

**Publish next:** excalibur-blog-publish (если `publish=yes`)  
**Blockers:** нет  

**Post-publish:** перезапустить interlinker для inbound B02→B03; проверить live internal links (200)

---

=== EXCALIBUR BLOG COVER ===
topic_id: B03
status: ✅
article_dir: memory/blog/articles/B03-podklyuchenie-mcp-cursor
pipeline: quad_canvas_1x_mcp
cover: cover/cover.png
inline: inline-01.png, inline-02.png, inline-03.png
inject_html: ok (3 figure)
blockers: none

---

=== EXCALIBUR BLOG SCHEMA ===
topic_id: B03
verdict: PASS
file: memory/blog/articles/B03-podklyuchenie-mcp-cursor/schema.jsonld
graph: Organization, Person, BlogPosting, FAQPage (7), HowTo (7 steps)
url: [https://mayai.ru/blog/podklyuchenie-mcp-cursor/](https://mayai.ru/blog/podklyuchenie-mcp-cursor/)

---

=== EXCALIBUR BLOG PUBLISH ===

**topic_id:** B03  
**slug:** podklyuchenie-mcp-cursor  
**article_dir:** memory/blog/articles/B03-podklyuchenie-mcp-cursor  
**publish_date:** 2026-06-11  
**verdict:** PASS  

**permalink:** https://mayai.ru/podklyuchenie-mcp-cursor/  
**post_id:** 13335  
**featured_image:** 13336  
**inline_images:** 13337, 13338, 13339  
**schema_meta:** ok  

**Script:** `excalibur_blog_wp_publish.py` (dry-run OK → publish OK)  
**Ledger:** `shared/published-articles.md`  

**Blockers:** нет  

---

=== EXCALIBUR BLOG (PIPELINE DONE) ===
topic_id: B03
article_dir: memory/blog/articles/B03-podklyuchenie-mcp-cursor
qa: PASS (94/100)
publish: https://mayai.ru/podklyuchenie-mcp-cursor/