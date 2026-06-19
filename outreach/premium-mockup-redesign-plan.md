# Premium Mockup Redesign Plan

Updated: 2026-06-19  
Owner: Hermes for Stark / SYBEORG

## Problem

The current prospect mockups are functional, but some still read as AI-generated because they share too much structure: hero, cards, generic service paths, CTA block, repeated urgency copy. For cold outreach, that can hurt trust. A weak/generic mockup is worse than no mockup.

## Goal

Turn SYBEORG mockups into premium sales assets that feel custom-built for each prospect and look crisp on both phone and laptop.

## Design Standard

Each mockup must feel like a real landing page a premium local agency could sell, not a generated template.

Required quality bars:

1. Distinct concept per prospect.
2. Verified public business facts only; no fake stats/testimonials/awards.
3. Official logo when available; graceful fallback if not.
4. Premium responsive spacing: mobile-first, laptop-polished.
5. Real visual system: no emoji-icon slop.
6. At least one custom visual aid per page.
7. Meaningful interactions: hover, focus, issue selector, reveal/scroll animations where tasteful.
8. Loading/intro treatment using logo/brand when not annoying.
9. QA at mobile and laptop widths before outreach.
10. The page must answer: why does this exact business need this exact design?

## Premium Components to Add

### 1. Brand Loader / Custom Entry

Purpose: make the prospect feel the page is custom.

Pattern:
- subtle logo preload screen
- “Sample concept for {Business}”
- 600–900ms max, then fades out
- no blocking if JS fails

Use only on prospect pages, not the gallery.

### 2. Interactive Issue / Service Selector

Replace static service cards with an input-driven mini module.

For trades:
- “What happened?” buttons: no heat, leak, water heater, drain backup
- changing panel updates: urgency, expected next step, call CTA

For restaurants/video prospects:
- “What campaign do you need?” buttons: catering, weekend promo, hiring, brand commercial

### 3. Local Service Area Visual

No fake map API needed.

Build CSS/SVG map cards with editable variables:
- primary city
- service radius
- neighborhoods/counties
- response promise wording if verified

### 4. Premium Proof Strip

Use real verified facts only:
- years in business if confirmed
- public service areas
- real categories/services
- public phone
- real logo/photos

If fact is not verified, omit it.

### 5. Visual Aid Modules

Input-able variables per lead:

- ROI / missed-call calculator
- Ad funnel diagram: Google search → landing page → phone call
- Emergency response timeline
- Before/after website gap cards
- Seasonal service calendar
- Campaign asset grid: commercial, reels, landing page, ad copy

### 6. Premium Motion

Lightweight, no framework:
- hover depth on cards
- CTA magnetic hover / gradient border
- scroll reveal via IntersectionObserver
- selected-state transitions
- sticky mobile call bar
- reduced-motion support

### 7. Responsive QA Requirements

Test each page at:
- mobile: 390 x 844
- laptop: 1440 x 900

Check:
- no cramped hero
- no tiny CTA
- no overflow
- buttons reachable with thumb
- logo visible but not distorted
- visual aid readable
- final CTA above fold enough on mobile

## Design Directions by Prospect Type

### Owner-operator / small town
Visual stance: local, human, understated premium.
Avoid: techy SaaS gloss.
Use: owner trust, local service area, call-first flow.

### Multi-service HVAC/plumbing
Visual stance: routing dashboard / one-call convenience.
Use: segmented service selector, dispatch-style visual, service-area proof.

### Family-owned HVAC
Visual stance: editorial trust / warm premium.
Use: family/local proof, quiet spacing, reliability timeline.

### Plumbing emergency
Visual stance: triage tool.
Use: “what happened?” module, water shutoff guidance, direct call CTA.

### Premium PHC
Visual stance: premium home systems concierge.
Use: one-call system map, home comfort categories, polished neutral typography.

### Heritage plumber
Visual stance: craftsman/local legacy.
Use: restrained color, tactile textures, service area, credibility story.

## Suggested Free Tools / MCPs Stark Could Add

Not strictly required — Hermes can already build this with HTML/CSS/JS + browser QA — but these would help.

### Highest value

1. **Context7 MCP**
   - Free docs MCP.
   - Helps pull current docs for libraries like GSAP, Framer Motion, shadcn, Tailwind, etc.
   - Useful if we add more advanced motion/components.

2. **Playwright MCP or BrowserTools MCP**
   - Free local browser automation/debugging.
   - Better responsive QA, screenshots, console/network capture.
   - Hermes already has browser tools, but this may help if integrated globally.

3. **Figma MCP / Framelink Figma MCP**
   - Free if Stark has Figma files or makes a quick design board.
   - Lets Hermes read Figma frames/tokens/assets.
   - Best if Stark starts collecting premium references or SYBEORG brand components.

### Useful non-MCP free assets

4. **Iconify / Lucide icons**
   - Free icon systems.
   - Better than emoji/AI-looking icons.

5. **Pexels / Unsplash free API keys**
   - Free stock photo/video discovery.
   - Useful for non-prospect-owned visuals, but must be careful not to imply photos are the client’s actual team/work.

6. **GSAP free tier / vanilla IntersectionObserver**
   - GSAP is free for most standard web animations.
   - Use sparingly; premium motion, not gimmicks.

## Recommended Implementation Architecture

Replace the current single generic generator with a componentized premium generator:

```txt
scripts/generate_premium_mockups.py
scripts/design_tokens.py
scripts/prospect_assets.py
components rendered as Python functions
```

Suggested data additions in `mockups.json`:

```json
{
  "designDirection": "emergency_dispatch|local_heritage|premium_refresh|triage_tool|one_call_concierge",
  "facts": {
    "verifiedServices": [],
    "serviceAreas": [],
    "yearsInBusiness": null,
    "ownerTeam": null,
    "sourceUrls": []
  },
  "visualAid": {
    "type": "roi_calculator|service_area|dispatch_timeline|campaign_grid",
    "variables": {}
  },
  "qualityGate": {
    "score": 0,
    "passed": false,
    "visualQaNotes": ""
  }
}
```

## Execution Plan

### Phase 1 — Build premium design system

- Create shared CSS tokens: spacing, type scale, radius, shadows, breakpoints.
- Add Lucide/Iconify style SVG icon helper.
- Add scroll reveal and reduced-motion JS.
- Add logo loader component.
- Add responsive QA checklist.

### Phase 2 — Build 3 premium page archetypes

1. Emergency Dispatch / Triage Tool
2. Local Heritage / Proof-first
3. Premium One-call Concierge

Each archetype should look meaningfully different.

### Phase 3 — Rebuild six current mockups

Assign archetypes:
- 8 Finger: Local owner-operator dispatch
- Bunch: Multi-service dispatch router
- Five Seasons: Warm family proof
- M&P: Plumbing emergency triage
- Platinum: Premium one-call home systems
- Richardson: Heritage craftsman trust

### Phase 4 — Visual QA

For each page:
- browser inspect laptop
- browser inspect mobile
- screenshot/vision QA
- route probe
- no console errors
- no fake claims

### Phase 5 — Outreach update

Only send pages that pass the premium quality gate. If a page still looks generic, mark it revision-needed and do not use it in outreach.

## Decision

Proceed even without new MCPs. The blocker is not tooling — it is raising the design bar, varying the concepts, and adding richer business-specific components.

If Stark wants to install free extras, prioritize:

1. Context7 MCP
2. Playwright/BrowserTools MCP
3. Figma MCP if he wants to provide design boards/reference frames
