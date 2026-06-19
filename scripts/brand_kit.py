#!/usr/bin/env python3
"""Extract lightweight brand kits from prospect websites.

The goal is practical outreach mockups: find a public logo/favicon, pull usable brand
colors, and store the result in mockups.json so generators can use the prospect's
own visual DNA instead of generic palettes.

No required third-party dependencies. If Pillow is installed, raster logo color
extraction is enabled; SVG + HTML/CSS color extraction works with stdlib only.
"""
from __future__ import annotations

import argparse
import collections
import colorsys
import datetime as dt
import html
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable

USER_AGENT = "Mozilla/5.0 (compatible; SYBEORGBrandKit/1.0; +https://sybeorg.com)"
NEUTRAL_NAMES = {"transparent", "currentcolor", "inherit", "initial", "unset", "none"}
COLOR_RE = re.compile(r"#(?:[0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})\b|rgba?\([^)]*\)")


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def fetch(url: str, timeout: int = 18) -> tuple[bytes, str, str]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,image/*,*/*;q=0.8"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            ctype = resp.headers.get("content-type", "")
            final_url = resp.geturl()
            return resp.read(2_000_000), ctype, final_url
    except urllib.error.HTTPError as exc:
        # Some small-business hosts return 403 while still serving the full public page.
        # Keep the body if present so brand extraction can still use visible logo/CSS cues.
        blob = exc.read(2_000_000)
        ctype = exc.headers.get("content-type", "") if exc.headers else ""
        if blob and ("html" in ctype or "image" in ctype or url.lower().endswith((".svg", ".png", ".jpg", ".jpeg", ".webp", ".ico"))):
            return blob, ctype, exc.geturl()
        raise


def normalize_url(base: str, candidate: str | None) -> str | None:
    if not candidate:
        return None
    candidate = html.unescape(candidate.strip())
    if candidate.startswith("data:") or candidate.startswith("mailto:") or candidate.startswith("tel:"):
        return None
    return urllib.parse.urljoin(base, candidate)


class AssetParser(HTMLParser):
    def __init__(self, base_url: str):
        super().__init__()
        self.base_url = base_url
        self.assets: list[dict] = []
        self.inline_css: list[str] = []
        self.in_style = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]):
        a = {k.lower(): v for k, v in attrs}
        if tag == "style":
            self.in_style = True
        if tag == "link":
            rel = (a.get("rel") or "").lower()
            href = normalize_url(self.base_url, a.get("href"))
            if href and any(x in rel for x in ["icon", "apple-touch-icon", "mask-icon"]):
                self.assets.append({"url": href, "kind": rel or "icon", "score": 45})
        if tag == "meta":
            prop = (a.get("property") or a.get("name") or "").lower()
            content = normalize_url(self.base_url, a.get("content"))
            if content and prop in {"og:image", "twitter:image", "twitter:image:src"}:
                self.assets.append({"url": content, "kind": prop, "score": 35})
        if tag == "img":
            src = normalize_url(self.base_url, a.get("src") or a.get("data-src") or a.get("data-lazy-src"))
            if not src:
                return
            text = " ".join(str(a.get(k) or "") for k in ["alt", "class", "id", "title", "src"]).lower()
            score = 20
            if "logo" in text:
                score += 60
            if "brand" in text:
                score += 25
            if "header" in text or "nav" in text:
                score += 10
            if any(x in src.lower() for x in ["logo", "brand"]):
                score += 50
            self.assets.append({"url": src, "kind": "img", "score": score})

    def handle_endtag(self, tag: str):
        if tag == "style":
            self.in_style = False

    def handle_data(self, data: str):
        if self.in_style and data.strip():
            self.inline_css.append(data)


def normalize_color(raw: str) -> str | None:
    raw = raw.strip().lower()
    if raw in NEUTRAL_NAMES:
        return None
    if raw.startswith("#"):
        h = raw[1:]
        if len(h) in (3, 4):
            h = "".join(ch * 2 for ch in h[:3])
        elif len(h) in (6, 8):
            h = h[:6]
        else:
            return None
        return f"#{h}"
    m = re.match(r"rgba?\(([^)]*)\)", raw)
    if m:
        parts = [p.strip() for p in m.group(1).split(",")]
        if len(parts) < 3:
            return None
        vals = []
        for p in parts[:3]:
            if p.endswith("%"):
                vals.append(round(float(p[:-1]) * 2.55))
            else:
                vals.append(round(float(re.sub(r"[^0-9.]", "", p) or "0")))
        vals = [max(0, min(255, v)) for v in vals]
        return "#%02x%02x%02x" % tuple(vals)
    return None


def rgb(color: str) -> tuple[int, int, int]:
    color = color.lstrip("#")
    return int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)


def is_neutral(color: str) -> bool:
    r, g, b = rgb(color)
    mx, mn = max(r, g, b), min(r, g, b)
    if mx < 28 or mn > 238:
        return True
    if mx - mn < 18:
        return True
    return False


def color_score(color: str, count: int) -> float:
    r, g, b = [v / 255 for v in rgb(color)]
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    # Prefer saturated, visible brand colors over dominant antialiased tans/grays.
    saturation_boost = max(0.08, s) ** 2.2
    value_boost = 0.35 + min(v, 0.9)
    return count * saturation_boost * value_boost


def extract_text_colors(text: str) -> collections.Counter[str]:
    c: collections.Counter[str] = collections.Counter()
    for raw in COLOR_RE.findall(text or ""):
        color = normalize_color(raw)
        if color and not is_neutral(color):
            c[color] += 1
    return c


def extract_raster_colors(blob: bytes) -> collections.Counter[str]:
    try:
        from PIL import Image  # type: ignore
        from io import BytesIO
    except Exception:
        return collections.Counter()
    try:
        img = Image.open(BytesIO(blob)).convert("RGBA")
        img.thumbnail((180, 180))
        # Composite transparent logos over white and dark backgrounds to avoid alpha artifacts.
        pixels = []
        pixel_iter = img.get_flattened_data() if hasattr(img, "get_flattened_data") else img.getdata()
        for r, g, b, a in pixel_iter:
            if a < 35:
                continue
            if a < 255:
                r = round((r * a + 255 * (255 - a)) / 255)
                g = round((g * a + 255 * (255 - a)) / 255)
                b = round((b * a + 255 * (255 - a)) / 255)
            color = "#%02x%02x%02x" % (r, g, b)
            if not is_neutral(color):
                # Bucket slightly so antialiasing does not create hundreds of near-identical colors.
                rb, gb, bb = (round(v / 16) * 16 for v in (r, g, b))
                pixels.append("#%02x%02x%02x" % (min(255, rb), min(255, gb), min(255, bb)))
        return collections.Counter(pixels)
    except Exception:
        return collections.Counter()


def sorted_palette(counter: collections.Counter[str], limit: int = 6) -> list[str]:
    ranked = sorted(counter.items(), key=lambda kv: color_score(kv[0], kv[1]), reverse=True)
    out: list[str] = []
    for color, _count in ranked:
        if all(distance(color, existing) > 38 for existing in out):
            out.append(color)
        if len(out) >= limit:
            break
    return out


def distance(a: str, b: str) -> float:
    ar, ag, ab = rgb(a)
    br, bg, bb = rgb(b)
    return ((ar - br) ** 2 + (ag - bg) ** 2 + (ab - bb) ** 2) ** 0.5


def lighten(color: str, amount: float) -> str:
    r, g, b = [v / 255 for v in rgb(color)]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    l = min(1, l + (1 - l) * amount)
    rr, gg, bb = colorsys.hls_to_rgb(h, l, s)
    return "#%02x%02x%02x" % (round(rr * 255), round(gg * 255), round(bb * 255))


def darken(color: str, amount: float) -> str:
    r, g, b = [v / 255 for v in rgb(color)]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    l = max(0, l * (1 - amount))
    rr, gg, bb = colorsys.hls_to_rgb(h, l, s)
    return "#%02x%02x%02x" % (round(rr * 255), round(gg * 255), round(bb * 255))


def build_palette(colors: list[str]) -> dict:
    def saturation(color: str) -> float:
        r, g, b = [v / 255 for v in rgb(color)]
        return colorsys.rgb_to_hsv(r, g, b)[1]

    saturated = [c for c in colors if saturation(c) >= 0.28]
    primary = saturated[0] if saturated else (colors[0] if colors else "#2563eb")
    remaining = [c for c in colors if c != primary]
    secondary = remaining[0] if remaining else darken(primary, 0.28)
    accent = remaining[1] if len(remaining) > 1 else lighten(primary, 0.28)
    return {
        "primary": primary,
        "secondary": secondary,
        "accent": accent,
        "background": lighten(primary, 0.92),
        "surface": "#ffffff",
        "text": darken(primary, 0.72),
        "muted": "#667085",
    }


def extract_brand_kit(url: str, max_assets: int = 8, logo_url: str | None = None) -> dict:
    page_blob, page_type, final_url = fetch(url)
    page_text = page_blob.decode("utf-8", errors="ignore")
    parser = AssetParser(final_url)
    parser.feed(page_text)

    asset_seen = set()
    assets = []
    if logo_url:
        explicit = normalize_url(final_url, logo_url)
        if explicit:
            assets.append({"url": explicit, "kind": "explicit-logo", "score": 999})
            asset_seen.add(explicit)
    for asset in sorted(parser.assets, key=lambda a: a["score"], reverse=True):
        if asset["url"] not in asset_seen:
            asset_seen.add(asset["url"])
            assets.append(asset)

    colors = extract_text_colors("\n".join(parser.inline_css) + "\n" + page_text[:200_000])
    logo_used = None
    asset_notes = []

    for asset in assets[:max_assets]:
        try:
            blob, ctype, final_asset_url = fetch(asset["url"], timeout=12)
            asset_text = blob[:500_000].decode("utf-8", errors="ignore") if ("svg" in ctype or final_asset_url.lower().endswith(".svg")) else ""
            logo_colors = extract_text_colors(asset_text) if asset_text else extract_raster_colors(blob)
            if logo_colors:
                # Logo colors are more important than broad site CSS colors.
                for color, count in logo_colors.items():
                    colors[color] += count * 8
                if not logo_used:
                    logo_used = final_asset_url
            asset_notes.append({"url": final_asset_url, "kind": asset["kind"], "colorsFound": len(logo_colors)})
        except Exception as exc:
            asset_notes.append({"url": asset["url"], "kind": asset["kind"], "error": str(exc)[:140]})

    extracted = sorted_palette(colors)
    return {
        "sourceUrl": final_url,
        "extractedAt": now_iso(),
        "extractionStatus": "ok" if extracted else "fallback_no_colors_found",
        "logoUsed": logo_used,
        "logoCandidates": asset_notes[:max_assets],
        "colors": extracted,
        "palette": build_palette(extracted),
        "notes": "SVG/HTML colors extracted with stdlib; raster logo colors require Pillow if no SVG/logo CSS colors are present.",
    }


def load_tracker(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_tracker(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Extract prospect brand colors/logos into mockups.json")
    ap.add_argument("--tracker", default="mockups.json")
    ap.add_argument("--slug", help="Only update this currentProspects id")
    ap.add_argument("--url", help="Override source URL for --slug or one-off extraction")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    tracker_path = Path(args.tracker)
    data = load_tracker(tracker_path)
    updated = 0
    errors = []

    for prospect in data.get("currentProspects", []):
        if args.slug and prospect.get("id") != args.slug:
            continue
        source_url = args.url or prospect.get("officialSiteChecked") or prospect.get("website")
        logo_url = prospect.get("logoUrl") or prospect.get("brandKit", {}).get("manualLogoUrl")
        if not source_url or source_url == "none_found":
            continue
        try:
            kit = extract_brand_kit(source_url, logo_url=logo_url)
            prospect["brandKit"] = kit
            updated += 1
            print(f"OK {prospect.get('id')}: {kit['palette']['primary']} from {kit.get('logoUsed') or kit['sourceUrl']}")
        except (urllib.error.URLError, TimeoutError, ValueError, OSError) as exc:
            errors.append({"id": prospect.get("id"), "url": source_url, "error": str(exc)})
            print(f"ERR {prospect.get('id')}: {exc}", file=sys.stderr)

    data["lastUpdated"] = dt.date.today().isoformat()
    data.setdefault("automation", {})["brandKit"] = {
        "script": "scripts/brand_kit.py",
        "lastRun": now_iso(),
        "updatedProspects": updated,
        "errors": errors,
    }

    if args.dry_run:
        print(json.dumps(data.get("automation", {}).get("brandKit"), indent=2))
    else:
        save_tracker(tracker_path, data)
    return 0 if not errors else 2


if __name__ == "__main__":
    raise SystemExit(main())
