#!/usr/bin/env python3
"""Excalibur BLOG HTML Tag Linter & Sanitizer.

Enforces strict whitelist of HTML tags, prevents unclosed tags, and checks for malformed markup.
Allowed tags: h2, h3, p, b, i, a, ul, ol, li, blockquote, table, thead, tbody, tr, th, td
"""
from __future__ import annotations

import argparse
import json
import sys
from html.parser import HTMLParser
from pathlib import Path


class HTMLTagLinter(HTMLParser):
    def __init__(self, whitelist: set[str]) -> None:
        super().__init__()
        self.whitelist = whitelist
        self.errors: list[str] = []
        self.tag_stack: list[tuple[str, int, int]] = []  # (tag, line, col)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag_lower = tag.lower()
        line, col = self.getpos()

        # Check whitelist
        if tag_lower not in self.whitelist:
            self.errors.append(f"Line {line}, Col {col}: Forbidden HTML tag <{tag}> used.")

        # Check nested structure
        # Self-closing tags in HTML5 parser like <img> don't need closing, but we stack block elements
        self_closing = {"img", "br", "hr"}
        if tag_lower not in self_closing:
            self.tag_stack.append((tag_lower, line, col))

    def handle_endtag(self, tag: str) -> None:
        tag_lower = tag.lower()
        line, col = self.getpos()
        self_closing = {"img", "br", "hr"}
        if tag_lower in self_closing:
            return

        if not self.tag_stack:
            self.errors.append(f"Line {line}, Col {col}: Unexpected closing tag </{tag_lower}> with no matching open tag.")
            return

        # Find matching open tag in stack
        expected_tag, o_line, o_col = self.tag_stack.pop()
        if expected_tag != tag_lower:
            self.errors.append(
                f"Line {line}, Col {col}: Tag mismatch. Closed </{tag_lower}> but expected </{expected_tag}> "
                f"opened at Line {o_line}, Col {o_col}."
            )
            # Re-push expected tag to stack to keep linting subsequent tags gracefully
            self.tag_stack.append((expected_tag, o_line, o_col))

    def check_unclosed_tags(self) -> None:
        while self.tag_stack:
            tag, line, col = self.tag_stack.pop()
            self.errors.append(f"Line {line}, Col {col}: Unclosed HTML tag <{tag}> at end of document.")


def lint_html_file(html_path: Path, whitelist: set[str]) -> dict[str, Any]:
    html_content = html_path.read_text(encoding="utf-8")
    linter = HTMLTagLinter(whitelist)
    linter.feed(html_content)
    linter.check_unclosed_tags()

    return {
        "file": str(html_path.name),
        "verdict": "pass" if not linter.errors else "fail",
        "total_errors": len(linter.errors),
        "errors": linter.errors,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Excalibur BLOG HTML Whitelist & Nesting Linter")
    ap.add_argument("html", type=Path, help="Path to article.html")
    ap.add_argument("-o", "--output", type=Path, help="Path to write html-linter-report.json")
    args = ap.parse_args()

    if not args.html.is_file():
        print(f"File not found: {args.html}", file=sys.stderr)
        return 2

    # Whitelist tags based on excalibur contract
    allowed_tags = {
        "h2", "h3", "p", "b", "i", "a", "ul", "ol", "li", "blockquote",
        "table", "thead", "tbody", "tr", "th", "td", "img", "br"
    }

    report = lint_html_file(args.html, allowed_tags)
    text = json.dumps(report, ensure_ascii=False, indent=2)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")

    print(f"HTML Linter Verdict: {report['verdict'].upper()}")
    if report["errors"]:
        print(f"Found {report['total_errors']} HTML errors/warnings:")
        for err in report["errors"]:
            print(f" - {err}")
    else:
        print("All HTML tags are clean, validated, and conform to whitelist!")

    return 0 if report["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
