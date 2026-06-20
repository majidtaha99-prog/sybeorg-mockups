#!/usr/bin/env python3
"""Static QA gate for SYBEORG mockup pages.

Checks the outreach mockup repo for lightweight security/performance hygiene:
- JSON files parse cleanly.
- HTML pages avoid plain http:// asset URLs.
- New-tab links include rel="noopener noreferrer".
- Embedded maps/iframes include title, lazy loading, referrer policy, and sandbox.
- No external JavaScript includes are used.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".vercel", "node_modules"}


def iter_files(pattern: str):
    for path in ROOT.rglob(pattern):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def attrs(tag: str) -> dict[str, str | bool]:
    out: dict[str, str | bool] = {}
    for match in re.findall(r"([:\w-]+)(?:\s*=\s*(?:\"([^\"]*)\"|'([^']*)'|([^\s>]+)))?", tag):
        key = match[0]
        values = match[1:]
        if key.lower() in {"a", "iframe", "script", "link", "meta", "img"}:
            continue
        out[key.lower()] = next((v for v in values if v), True)
    return out


def fail(errors: list[str], path: Path, message: str) -> None:
    errors.append(f"{path.relative_to(ROOT)}: {message}")


def check_json(errors: list[str]) -> None:
    for path in iter_files("*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001 - QA script should report all parse failures.
            fail(errors, path, f"invalid JSON: {exc}")


def check_html(errors: list[str]) -> None:
    for path in iter_files("*.html"):
        text = path.read_text(encoding="utf-8", errors="replace")

        # Plain HTTP assets can create mixed-content problems on Vercel. Allow tel links and comments naturally.
        for match in re.finditer(r"(?:src|href)=[\"']http://", text, flags=re.I):
            fail(errors, path, f"plain http:// URL in asset/link near offset {match.start()}")

        # Avoid remote script supply-chain risk in static prospect pages.
        for tag in re.findall(r"<script\b[^>]*>", text, flags=re.I):
            data = attrs(tag)
            if "src" in data:
                fail(errors, path, "external <script src> is not allowed")

        for tag in re.findall(r"<a\b[^>]*target=[\"']_blank[\"'][^>]*>", text, flags=re.I):
            data = attrs(tag)
            rel = str(data.get("rel", "")).lower()
            if "noopener" not in rel or "noreferrer" not in rel:
                fail(errors, path, "target=_blank link missing rel=\"noopener noreferrer\"")

        for tag in re.findall(r"<iframe\b[^>]*>", text, flags=re.I):
            data = attrs(tag)
            for required in ("title", "loading", "referrerpolicy", "sandbox"):
                if required not in data:
                    fail(errors, path, f"iframe missing {required}")
            if str(data.get("loading", "")).lower() != "lazy":
                fail(errors, path, "iframe should use loading=\"lazy\"")


def main() -> int:
    errors: list[str] = []
    check_json(errors)
    check_html(errors)
    if errors:
        print("Static QA failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Static QA passed: JSON, links, scripts, iframes, and mixed-content checks clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
