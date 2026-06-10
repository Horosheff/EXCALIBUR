# Excalibur BLOG — handoff

`pipeline_started_at`:
`topic_id`:
`article_dir`:
`publish`:

---

## Статус пайплайна

| Шаг | Агент | Статус | Время |
| --- | --- | --- | --- |
| 0 | shell research_start + **utility gate темы** | | |
| 1 | excalibur-blog-research | | |
| 2 | excalibur-blog-writer | | |
| 3 | excalibur-blog-geo-qa (+ utility gate статьи) | | |
| 4 | excalibur-blog-cover \|\| excalibur-blog-schema | | |
| 5 | excalibur-blog-indexer | | |
| 6 | excalibur-blog-publish | | |

---

## Editorial

**Utility-only:** только how-to, чеклисты, comparison, workflow. См. `shared/editorial-utility-only.md`.

```bash
python scripts/excalibur_blog_utility_gate.py --topic-id <ID>
python scripts/excalibur_blog_utility_gate.py --article-dir <article_dir>
```

---

<!-- Агенты дописывают блоки ниже: === EXCALIBUR BLOG RESEARCH === и т.д. -->
