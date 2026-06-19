#!/usr/bin/env python3
"""Generate SYBEORG static mockup pages from mockups.json.

Uses prospect brandKit palettes when available, then falls back to curated palettes.
Run after scripts/brand_kit.py to make pages inherit colors pulled from public logos/sites.
"""
from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

FALLBACKS = {
    "8-finger-hvac": ["#fbf7ef", "#20302a", "#d86b2c", "#f0b35a", "#ffffff", "#5f6f65"],
    "bunch-heating-cooling": ["#f6fbff", "#10243a", "#0f7a9b", "#f97316", "#ffffff", "#60758a"],
    "five-seasons-hvac": ["#fffaf2", "#17223b", "#2f6f9f", "#e0a13a", "#ffffff", "#687487"],
    "mp-plumbing": ["#f5f9ff", "#0d2b45", "#1677a3", "#f59e0b", "#ffffff", "#5f7485"],
    "platinum-phc": ["#f8f7f4", "#171717", "#9a7b38", "#2b5c88", "#ffffff", "#6f6f6f"],
    "richardson-plumbing": ["#fbf4e8", "#24342e", "#a85522", "#d7b98a", "#ffffff", "#70695f"],
}

CREATIVE = {
    "8-finger-hvac": {
        "short": "8 Finger", "layout": "rural-dispatch",
        "title": "Small-town HVAC help without the call-center feel",
        "concept": "Owner-operator dispatch board for rural emergency heat/cooling calls.",
        "hero": "No heat, no cool, or system acting up around Martelle?",
        "sub": "A phone-first concept for a local HVAC shop: fewer generic service cards, more “call Bobby and get a real answer” energy.",
        "proof": ["Martelle / Eastern Iowa focus", "Phone-first emergency path", "Built for owner-operator trust"],
        "services": ["No-heat troubleshooting", "AC repair calls", "Seasonal tune-ups", "Replacement guidance"],
        "money": "The mockup makes the phone call the product — ideal for small-town urgent searches where trust beats polish.",
        "cta": "Call the shop",
    },
    "bunch-heating-cooling": {
        "short": "Bunch", "layout": "split-service",
        "title": "A sharper mobile emergency funnel for an already credible local company",
        "concept": "Paid-search landing page that routes HVAC and plumbing visitors by problem before asking for a form.",
        "hero": "Heating, cooling, or plumbing issue in the Marion area?",
        "sub": "A cleaner conversion page concept that lets urgent visitors choose their issue and call fast — without replacing the main website.",
        "proof": ["Marion / Cedar Rapids service area", "HVAC + plumbing under one roof", "Best as a dedicated ad landing page"],
        "services": ["Furnace / AC repair", "Plumbing leaks", "Water heater help", "Maintenance requests"],
        "money": "The gap is not credibility — it is speed. This design gives emergency traffic a simpler path to a call.",
        "cta": "Get service started",
    },
    "five-seasons-hvac": {
        "short": "Five Seasons", "layout": "family-proof",
        "title": "Family-owned HVAC presented with calm, licensed confidence",
        "concept": "Proof-first refresh with clean same-day service lanes and fewer dark-template patterns.",
        "hero": "Local HVAC service that feels established before the first call.",
        "sub": "A warmer homepage/landing concept built around family-owned trust, service clarity, and mobile same-day calls.",
        "proof": ["Family-owned positioning", "Hiawatha / Cedar Rapids market", "Licensed/local trust angle"],
        "services": ["AC repair", "Furnace repair", "System replacement", "Seasonal maintenance"],
        "money": "For a strong local operator, the mockup should not scream emergency template — it should make reliability visible.",
        "cta": "Request service",
    },
    "mp-plumbing": {
        "short": "M&P", "layout": "leak-triage",
        "title": "Emergency plumbing page built around the first 60 seconds of panic",
        "concept": "Leak/water-heater decision tree with trust-first copy and no fake plumber claims.",
        "hero": "Leak, clog, or water heater problem in the Des Moines area?",
        "sub": "A service-specific landing concept that gets visitors from “water is where it should not be” to a phone call fast.",
        "proof": ["Urbandale / Des Moines market", "Emergency leak + water heater focus", "Public phone and email-ready outreach angle"],
        "services": ["Leak repair", "Water heaters", "Drain problems", "Fixture installs"],
        "money": "Plumbing leads convert when the page names the exact problem. This design turns vague traffic into a specific call.",
        "cta": "Talk to M&P",
    },
    "platinum-phc": {
        "short": "Platinum PHC", "layout": "premium-onecall",
        "title": "One-call home systems page with premium Des Moines positioning",
        "concept": "Polished multi-trade page that sells convenience without clutter: plumbing, HVAC, electrical-style routing.",
        "hero": "One call for the home systems that cannot wait.",
        "sub": "A more premium concept for a multi-service operator — built for emergency clarity, not a generic contractor grid.",
        "proof": ["Des Moines metro focus", "One-call convenience angle", "Plumbing + HVAC service breadth"],
        "services": ["Plumbing repairs", "Heating & cooling", "Water heaters", "Home comfort fixes"],
        "money": "The mockup differentiates Platinum from single-trade competitors by making convenience feel valuable and professional.",
        "cta": "Call Platinum",
    },
    "richardson-plumbing": {
        "short": "Richardson", "layout": "heritage-craftsman",
        "title": "A craftsman-style plumbing page that feels earned, not flashy",
        "concept": "Local heritage layout for a forty-year trust story; restrained, respectful, and call-first.",
        "hero": "Plumbing help with the kind of trust people remember.",
        "sub": "A respectful concept for a long-running local plumber: warmer type, county coverage, and simple repair paths.",
        "proof": ["Des Moines + surrounding counties", "Craftsman/trust positioning", "Built to avoid agency-bro sales tone"],
        "services": ["General plumbing", "Water heater help", "Leaks & repairs", "Fixture updates"],
        "money": "The opportunity is tone. A heritage-style page can make the business feel established before the customer calls.",
        "cta": "Call Richardson",
    },
}


def tel(phone: str) -> str:
    return "".join(ch for ch in phone if ch.isdigit())


def colors_for(prospect: dict) -> list[str]:
    kit = prospect.get("brandKit", {}).get("palette") or {}
    if kit.get("primary"):
        return [
            kit.get("background", "#f7f8fb"),
            kit.get("text", "#101828"),
            kit.get("primary", "#2563eb"),
            kit.get("accent", kit.get("secondary", "#f59e0b")),
            kit.get("surface", "#ffffff"),
            kit.get("muted", "#667085"),
        ]
    return FALLBACKS.get(prospect["id"], ["#f7f8fb", "#101828", "#2563eb", "#f59e0b", "#ffffff", "#667085"])


def page(prospect: dict) -> str:
    p = {**prospect, **CREATIVE[prospect["id"]]}
    bg, ink, accent, accent2, surface, muted = colors_for(prospect)
    phone = p.get("phone", "")
    telnum = tel(phone)
    service_cards = "".join(
        f'<article class="service"><span>{i:02d}</span><strong>{html.escape(s)}</strong><p>{html.escape(p["market"])} visitors can self-identify the issue quickly before calling.</p></article>'
        for i, s in enumerate(p["services"], 1)
    )
    proof = "".join(f"<li>{html.escape(x)}</li>" for x in p["proof"])
    selector = "".join(f"<button>{html.escape(s)}</button>" for s in p["services"])
    source = p.get("brandKit", {}).get("sourceUrl")
    logo = p.get("brandKit", {}).get("logoUsed")
    logo_candidates = p.get("brandKit", {}).get("logoCandidates") or []
    logo = logo or (logo_candidates[0].get("url") if logo_candidates else None)
    fallback_mark = html.escape(p['short'][0])
    logo_mark = (
        f'<img src="{html.escape(logo)}" alt="{html.escape(p["business"])} logo" loading="lazy" '
        f'onerror="this.remove();this.parentElement.textContent=\'{fallback_mark}\';">'
        if logo else fallback_mark
    )
    source_note = f"<!-- Brand cues pulled from public site{': ' + html.escape(source) if source else ''}{' · logo: ' + html.escape(logo) if logo else ''} -->"
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(p['business'])} — SYBEORG redesign concept</title>
<meta name="description" content="Custom SYBEORG landing-page mockup concept for {html.escape(p['business'])} in {html.escape(p['market'])}.">
<style>
  :root {{ --bg:{bg}; --ink:{ink}; --accent:{accent}; --accent2:{accent2}; --surface:{surface}; --muted:{muted}; }}
  * {{ box-sizing:border-box; margin:0; padding:0; }}
  html {{ scroll-behavior:smooth; }}
  body {{ font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background:var(--bg); color:var(--ink); line-height:1.55; }}
  a {{ color:inherit; }}
  .mockup-note {{ background:var(--ink); color:var(--bg); text-align:center; padding:9px 18px; font-size:12px; letter-spacing:.08em; text-transform:uppercase; }}
  .nav {{ position:sticky; top:0; z-index:10; display:flex; justify-content:space-between; align-items:center; gap:18px; padding:18px clamp(18px,4vw,56px); background:color-mix(in srgb, var(--bg) 88%, white); border-bottom:1px solid color-mix(in srgb, var(--ink) 12%, transparent); backdrop-filter:blur(16px); }}
  .brand {{ display:flex; align-items:center; gap:12px; font-weight:900; letter-spacing:-.04em; }}
  .mark {{ width:42px; height:42px; display:grid; place-items:center; border-radius:16px; background:linear-gradient(135deg,var(--accent),var(--accent2)); color:white; box-shadow:0 14px 30px color-mix(in srgb, var(--accent) 28%, transparent); overflow:hidden; }}
  .mark img {{ max-width:100%; max-height:100%; object-fit:contain; background:white; padding:4px; width:100%; height:100%; }}
  .nav small {{ display:block; color:var(--muted); font-weight:650; letter-spacing:.08em; text-transform:uppercase; font-size:10px; }}
  .phone {{ display:inline-flex; align-items:center; gap:8px; background:var(--accent); color:white; padding:12px 17px; border-radius:999px; text-decoration:none; font-weight:850; box-shadow:0 12px 30px color-mix(in srgb, var(--accent) 22%, transparent); }}
  .hero {{ padding:clamp(52px,8vw,92px) clamp(18px,4vw,56px) 42px; }}
  .hero-grid {{ max-width:1180px; margin:auto; display:grid; grid-template-columns:minmax(0,1.08fr) minmax(320px,.72fr); gap:34px; align-items:center; }}
  .eyebrow {{ display:inline-flex; gap:8px; align-items:center; color:var(--accent); font-weight:900; font-size:12px; text-transform:uppercase; letter-spacing:.16em; margin-bottom:18px; }}
  .eyebrow:before {{ content:""; width:34px; height:2px; background:var(--accent); }}
  h1 {{ font-size:clamp(42px,7vw,78px); line-height:.94; letter-spacing:-.07em; max-width:850px; }}
  .sub {{ margin-top:22px; color:var(--muted); font-size:clamp(17px,2vw,21px); max-width:680px; }}
  .hero-actions {{ display:flex; flex-wrap:wrap; gap:12px; margin-top:28px; }}
  .btn {{ display:inline-flex; justify-content:center; align-items:center; padding:14px 19px; border-radius:14px; font-weight:900; text-decoration:none; }}
  .btn.primary {{ background:var(--accent); color:white; }} .btn.secondary {{ border:1px solid color-mix(in srgb, var(--ink) 16%, transparent); background:rgba(255,255,255,.45); }}
  .diagnostic {{ background:var(--surface); border:1px solid color-mix(in srgb, var(--ink) 12%, transparent); border-radius:28px; padding:24px; box-shadow:0 24px 80px rgba(0,0,0,.10); }}
  .diagnostic h2 {{ font-size:22px; letter-spacing:-.04em; }} .diagnostic p {{ color:var(--muted); margin-top:8px; }}
  .issue-grid {{ display:grid; grid-template-columns:1fr 1fr; gap:9px; margin-top:18px; }}
  .issue-grid button {{ border:1px solid color-mix(in srgb, var(--accent) 22%, transparent); background:color-mix(in srgb, var(--accent) 8%, white); color:var(--ink); padding:12px; border-radius:14px; font-weight:800; text-align:left; }}
  section {{ padding:42px clamp(18px,4vw,56px); }} .wrap {{ max-width:1180px; margin:auto; }}
  .proof {{ display:grid; grid-template-columns:1fr 1fr; gap:22px; align-items:start; }}
  .proof-card, .money-card {{ background:var(--surface); border:1px solid color-mix(in srgb, var(--ink) 11%, transparent); border-radius:26px; padding:25px; }}
  .proof h2, .services h2, .final h2 {{ font-size:clamp(30px,4vw,48px); line-height:1; letter-spacing:-.055em; }}
  ul {{ list-style:none; margin-top:18px; display:grid; gap:12px; }}
  li {{ padding-left:28px; position:relative; color:var(--muted); }} li:before {{ content:""; position:absolute; left:0; top:.55em; width:12px; height:12px; border-radius:50%; background:var(--accent2); }}
  .services-grid {{ display:grid; grid-template-columns:repeat(4,1fr); gap:14px; margin-top:22px; }}
  .service {{ background:color-mix(in srgb, var(--surface) 86%, var(--accent) 14%); border:1px solid color-mix(in srgb, var(--ink) 10%, transparent); border-radius:22px; padding:20px; min-height:190px; }}
  .service span {{ color:var(--accent); font-weight:950; font-size:12px; }} .service strong {{ display:block; margin-top:22px; font-size:20px; letter-spacing:-.04em; }} .service p {{ margin-top:10px; color:var(--muted); font-size:14px; }}
  .route {{ margin-top:28px; display:grid; grid-template-columns:repeat(3,1fr); gap:14px; }}
  .step {{ padding:18px; border-radius:22px; border:1px dashed color-mix(in srgb, var(--accent) 35%, transparent); }} .step b {{ display:block; margin-bottom:6px; }} .step p {{ color:var(--muted); font-size:14px; }}
  .video-offer {{ margin-top:28px; background:linear-gradient(135deg, color-mix(in srgb, var(--ink) 92%, black), color-mix(in srgb, var(--accent) 34%, var(--ink))); color:var(--bg); border-radius:26px; padding:25px; display:grid; grid-template-columns:1fr auto; gap:18px; align-items:center; box-shadow:0 22px 60px rgba(0,0,0,.16); }}
  .video-offer b {{ display:block; color:var(--accent2); text-transform:uppercase; letter-spacing:.12em; font-size:11px; margin-bottom:8px; }}
  .video-offer h3 {{ font-size:clamp(24px,3vw,36px); line-height:1; letter-spacing:-.055em; color:var(--bg); }}
  .video-offer p {{ margin-top:9px; opacity:.78; max-width:760px; }}
  .video-offer a {{ background:var(--bg); color:var(--ink); padding:13px 17px; border-radius:14px; text-decoration:none; font-weight:950; white-space:nowrap; }}
  .brand-source {{ max-width:1180px; margin:0 auto; color:var(--muted); font-size:12px; opacity:.75; padding:0 clamp(18px,4vw,56px) 12px; overflow-wrap:anywhere; }}
  .final {{ padding-bottom:96px; }} .final-box {{ background:var(--ink); color:var(--bg); border-radius:30px; padding:clamp(28px,5vw,48px); display:grid; grid-template-columns:1fr auto; gap:24px; align-items:center; }} .final .phone {{ background:var(--bg); color:var(--ink); }}
  .sticky-mobile {{ display:none; position:fixed; left:12px; right:12px; bottom:12px; z-index:20; text-align:center; background:var(--accent); color:white; padding:14px; border-radius:18px; text-decoration:none; font-weight:950; box-shadow:0 18px 38px rgba(0,0,0,.24); }}
  @media (max-width:840px) {{ .hero-grid,.proof,.final-box {{ grid-template-columns:1fr; }} .services-grid,.route {{ grid-template-columns:1fr; }} .nav {{ align-items:flex-start; }} .phone.nav-phone {{ display:none; }} .sticky-mobile {{ display:block; }} h1 {{ font-size:44px; }} .hero {{ padding-top:38px; }} }}
</style>
</head>
<body class="{html.escape(p['layout'])}">
  <div class="mockup-note">SYBEORG sample concept — not the official website of {html.escape(p['business'])}</div>
  <nav class="nav"><div class="brand"><div class="mark">{logo_mark}</div><div>{html.escape(p['business'])}<small>{html.escape(p['vertical'])} · {html.escape(p['market'])}</small></div></div><a class="phone nav-phone" href="tel:{telnum}">{html.escape(phone)}</a></nav>
  <main>
    {source_note}
    <section class="hero"><div class="hero-grid"><div><div class="eyebrow">{html.escape(p['concept'])}</div><h1>{html.escape(p['hero'])}</h1><p class="sub">{html.escape(p['sub'])}</p><div class="hero-actions"><a class="btn primary" href="tel:{telnum}">{html.escape(p['cta'])}: {html.escape(phone)}</a><a class="btn secondary" href="#services">See service paths</a></div></div><aside class="diagnostic"><h2>Fast issue routing</h2><p>Instead of a generic quote form, this mockup lets a mobile visitor identify the problem and call with confidence.</p><div class="issue-grid">{selector}</div></aside></div></section>
    <section><div class="wrap proof"><div class="proof-card"><h2>{html.escape(p['title'])}</h2><ul>{proof}</ul></div><div class="money-card"><span class="eyebrow">Money-leak fix</span><p style="font-size:20px;color:var(--ink);font-weight:750;letter-spacing:-.03em">{html.escape(p['money'])}</p></div></div></section>
    <section id="services" class="services"><div class="wrap"><h2>Service paths designed for real calls.</h2><div class="services-grid">{service_cards}</div><div class="route"><div class="step"><b>1. Pick the problem</b><p>Visitor sees the exact service language they searched for.</p></div><div class="step"><b>2. Call or request help</b><p>The phone CTA stays visible and avoids form friction on urgent jobs.</p></div><div class="step"><b>3. Book the job</b><p>The page supports follow-up ads, GMB clicks, and outreach credibility.</p></div></div><div class="video-offer"><div><b>Commercial/video ad add-on</b><h3>Turn this page into a full campaign.</h3><p>SYBEORG can pair the landing page with a polished 30–60 second business commercial and short vertical ad cuts for Facebook, Instagram, TikTok, YouTube, or the website.</p></div><a href="../video-commercial/">View video offer →</a></div></div></section>
    <section class="final"><div class="wrap final-box"><div><span class="eyebrow" style="color:var(--accent2)">Ready to polish</span><h2>{html.escape(p['business'])} could own this lane.</h2><p style="margin-top:12px;opacity:.78">This is a redesign concept for outreach: specific to the business, mobile-first, and built to feel believable to a local owner.</p></div><a class="phone" href="tel:{telnum}">{html.escape(phone)}</a></div></section>
  </main>
  <a class="sticky-mobile" href="tel:{telnum}">Call {html.escape(p['short'])}: {html.escape(phone)}</a>
</body>
</html>
'''


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tracker", default="mockups.json")
    ap.add_argument("--slug", action="append", help="Generate only selected slug(s); default: six current redesigned mockups")
    args = ap.parse_args()
    root = Path(args.tracker).resolve().parent
    data = json.loads(Path(args.tracker).read_text(encoding="utf-8"))
    slugs = set(args.slug or CREATIVE.keys())
    count = 0
    for prospect in data.get("currentProspects", []):
        if prospect.get("id") not in slugs or prospect.get("id") not in CREATIVE:
            continue
        out = root / prospect["mockupPath"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(prospect), encoding="utf-8")
        count += 1
        source = "brandKit" if prospect.get("brandKit", {}).get("palette") else "fallback"
        print(f"generated {prospect['id']} using {source}")
    print(f"generated {count} mockup(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
