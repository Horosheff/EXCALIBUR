#!/usr/bin/env python3
"""Build MCP prompt + batch for ONE quad canvas (4 panels) with hero i2i reference."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def inline_panel_prompt(slot: dict, types_catalog: dict, design_code: dict) -> str:
    type_id = slot.get("visual_type") or "infographic_card"
    type_def = (types_catalog.get("types") or {}).get(type_id) or {}
    parts = [
        f"[{type_def.get('label_ru', type_id)}]",
        type_def.get("prompt_prefix", "").strip(),
        f"H2: «{slot.get('h2_anchor', '')}».",
        slot.get("scene_hint", "").strip(),
        type_def.get("prompt_suffix", "").strip(),
        "NO blog host face.",
        (design_code.get("inline_human_touch") or "").strip(),
        f"Negative: {type_def.get('negative', '')}",
    ]
    return " ".join(p for p in parts if p)


def build_prompt(manifest: dict, style: dict, hero: dict, types_catalog: dict, design_code: dict) -> str:
    slots = manifest.get("slots") or {}

    def slot(key: str) -> dict:
        return slots.get(key) or {}

    cover = slot("cover")
    i1, i2, i3 = slot("inline_1"), slot("inline_2"), slot("inline_3")

    lines = [
        style.get("global_prompt_prefix", "").strip(),
        "Single canvas 2048x1152 pixels, exact 2x2 grid, four equal 16:9 panels (1024x576 each), thin white gutters.",
        "",
        "REFERENCE FACE (top-left cover ONLY): preserve EXACT likeness from input reference photo —",
        hero.get("prompt_fragment", "").strip(),
        (hero.get("outfit_rule") or "Outfit is agent choice for the hook — not locked to reference photo.").strip(),
        "",
        f'Top-left COVER — hook "{manifest.get("cover_hook", "")}":',
        (design_code.get("cover_panel_prompt_block") or "").strip(),
        cover.get("scene_hint", ""),
        f'Cyrillic meme caption: "{cover.get("meme_caption_ru", "")}".',
        "Different meme reactions than inline panels. Fake screenshots encouraged.",
        "",
        f"Top-right — {inline_panel_prompt(i1, types_catalog, design_code)}",
        "",
        f"Bottom-left — {inline_panel_prompt(i2, types_catalog, design_code)}",
        "",
        f"Bottom-right — {inline_panel_prompt(i3, types_catalog, design_code)}",
        "",
        style.get("global_prompt_suffix", "").strip(),
        "Inline panels (top-right, bottom-left, bottom-right): editorial UI/diagram only — NO host face on those three panels.",
        f"Negative: {style.get('global_negative_prompt', '')}, {design_code.get('global_negative', '')}, extra faces on inline panels",
    ]
    return "\n".join(line for line in lines if line)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--manifest", default="cover/quad-manifest.json")
    ap.add_argument("--write-batch", action="store_true", help="Write cover/quad-mcp-batch.json")
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    manifest_path = Path(args.manifest)
    if not manifest_path.is_absolute():
        manifest_path = article_dir / manifest_path
    if not manifest_path.is_file():
        print(f"❌ PROMPT BLOCKER: {manifest_path} not found", file=sys.stderr)
        return 1

    manifest = load_json(manifest_path)
    hero = load_json(root / manifest.get("blog_hero", "memory/cover/blog-hero.json"))
    style = load_json(root / manifest.get("style_file", "memory/cover/quad-style-digital-meme-collage-ru.json"))
    types_path = root / manifest.get("inline_types_catalog", "memory/cover/inline-visual-types.json")
    types_catalog = load_json(types_path) if types_path.is_file() else {"types": {}}
    design_code_path = root / style.get("design_code", "memory/cover/cover-design-code.json")
    design_code = load_json(design_code_path) if design_code_path.is_file() else {}

    ref_url = (hero.get("reference_url_hosted") or "").strip()
    if not ref_url:
        print(
            "❌ COVER HERO BLOCKER: reference_url_hosted missing. Run excalibur_blog_hero_reference_url.py",
            file=sys.stderr,
        )
        return 1

    prompt = build_prompt(manifest, style, hero, types_catalog, design_code)
    prompt_path = article_dir / "cover" / "quad-mcp-prompt.txt"
    prompt_path.write_text(prompt + "\n", encoding="utf-8")
    print(f"OK prompt={prompt_path}")

    if args.write_batch:
        batch = {
            "pipeline": "quad_canvas_1x_mcp",
            "reference_url_hosted": ref_url,
            "output_canvas": "cover/canvas-quad.png",
            "jobs": [
                {
                    "slot": "canvas_quad",
                    "tool": "gpt-image-2",
                    "note": "ONE call only — 4 panels inside, then excalibur_blog_cover_quad_split.py",
                    "mcp_args": {
                        "prompt": prompt,
                        "input_urls": [ref_url],
                        "aspect_ratio": "16:9",
                        "resolution": "2K",
                    },
                }
            ],
        }
        batch_path = article_dir / "cover" / "quad-mcp-batch.json"
        save_json(batch_path, batch)
        print(f"OK batch={batch_path} jobs=1 input_urls=1")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
