# SYBEORG Brand-Kit Mockup System

Updated: 2026-06-19

## What changed

- `scripts/brand_kit.py` discovers public logo/favicon/image assets and extracts usable brand colors from site CSS, SVGs, and raster images when Pillow is available.
- `scripts/generate_mockups.py` regenerates the six current mockups using each prospect’s `brandKit.palette` and public logo when available.
- `mockups.json` now stores `officialSiteChecked`, extraction metadata, logo candidates, final palette, and automation status.

## Current six brand kits

| Prospect | Source | Status | Logo used | Primary | Secondary | Accent |
|---|---|---|---|---:|---:|---:|
| 8 Finger HVAC | https://8fingerhvacllc.com/ | fallback_no_colors_found | none | `#2563eb` | `#1043b3` | `#628ff1` |
| Bunch Heating and Cooling | https://bunchheatingandcooling.com | ok | https://bunchheatingandcooling.com/wp-content/uploads/2022/05/ME-logo-primary-300.png | `#00a0e0` | `#ff0000` | `#5090f0` |
| Five Seasons Heating & Cooling | https://www.fiveseasonsheatingandcooling.com/ | ok | https://le-cdn.hibuwebsites.com/dafdf57d69904851868c44de9036848b/dms3rep/multi/opt/logo-086a5fbf-300w.png | `#f04030` | `#604020` | `#a08070` |
| M&P Plumbing | https://www.mp-plumbing.com/ | ok | https://du9m0k402rjmo.cloudfront.net/images/P_48287/c58d33f2-8571-4127-9f21-93c8013e6535.jpg | `#202060` | `#706050` | `#908060` |
| Platinum Plumbing, Heating & Cooling | https://platinumphcdsm.com/ | ok | none | `#226d7a` | `#22b8d1` | `#b0e0e9` |
| Richardson Plumbing | https://www.richardsonplumbing.net/ | ok | https://www.richardsonplumbing.net/wp-content/uploads/2026/01/logo.png | `#90d0ff` | `#1080c0` | `#705040` |

## Commands

```bash
# Extract/update a single prospect
python scripts/brand_kit.py --slug bunch-heating-cooling

# Extract all prospects with officialSiteChecked
python scripts/brand_kit.py

# Regenerate current six mockups from tracker data
python scripts/generate_mockups.py
```

## Notes / guardrails

- If a site has no official colors, the extractor writes `fallback_no_colors_found` and the generator uses a safe fallback palette.
- For prospects with no website, add `officialSiteChecked` or a direct `logoUrl` before extraction.
- Avoid using brand-derived colors as fake endorsement. The top bar still labels pages as SYBEORG sample concepts, not official sites.
- Outbound emails/forms still require Stark approval.
