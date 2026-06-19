# SYBEORG Mockup Quality Standard

Status: required quality gate for prospect mockups.  
Scope: **SYBEORG only**. Radi / House of Meroë excluded.

## Why this exists

The current mockups are conversion-focused, but several look too similar and too AI-generated: dark generic emergency pages, oversized gradient headlines, right-side quote forms, three service cards, stat strips, synthetic reviews, and placeholder letter logos.

That can backfire. If a local owner sees a page that feels like a generic AI template, the mockup weakens trust instead of creating curiosity.

The daily cron must optimize for **fewer, better, more believable mockups** — not maximum mockup count.

## Core principle

A SYBEORG mockup should feel like a thoughtful first draft for a real local business, not a reskinned landing-page template.

The page should answer:

> “Why does this exact business need this exact design?”

If the same layout could be reused by swapping business name, phone, and colors, it fails.

---

## Quality bar

A mockup must pass at least 8 of these 12 checks before it is worth pushing live:

1. **Distinct concept:** The layout/design stance is different from recent mockups.
2. **Authentic local proof:** Uses verified public facts: city, service area, years, owner/team, address, real services.
3. **No fabricated claims:** No invented review counts, jobs completed, license numbers, awards, certifications, guarantees, or owner names.
4. **Visual credibility:** Includes real public imagery if available, or believable photo-direction placeholders; not just cards/icons.
5. **Brand specificity:** Logo/wordmark/type/color choices feel related to that business/vertical, not generic.
6. **Clear money-leak fix:** The design visibly solves the diagnosed issue: mobile CTA, GMB leakage, service-page gap, booking, trust, bug, etc.
7. **Human copy:** Copy sounds like a local business, not SaaS/AI marketing. Specific beats punchy.
8. **Trust system:** Reviews/proof are attributed or clearly marked as placeholder; trust badges are verified or omitted.
9. **Mobile-first:** Phone/service action is obvious on mobile and not hidden behind generic form friction.
10. **Design restraint:** Avoids overuse of gradients, emojis, glass cards, generic stats, and fake urgency.
11. **Accessibility:** Strong contrast, readable type, visible focus/hover states, semantic HTML.
12. **Differentiation note:** Daily lead board explains why this design direction was chosen.

Hard fail if:

- It fabricates real-world proof.
- It repeats the same hero/form/cards/reviews structure from the previous mockup without a reason.
- It uses fake testimonials as if real.
- It looks like a generic AI-generated contractor site.

---

## Anti-patterns to avoid

Do not default to:

- dark charcoal background + orange/red gradient headline for every trade business;
- right-side quote form hero for every page;
- three service cards + three fake reviews + final CTA as the whole page;
- emoji-style icons as primary visuals;
- fake numbers like “5,000+ jobs” or “120+ reviews” unless verified;
- vague badges: “Licensed & insured” without source/context;
- invented owners, misspelled names, synthetic stories;
- generic lines like “We pick up. We show up. We fix it.” unless it matches the brand.

These patterns are usable, but repeated together they scream AI template.

---

## Preferred design directions

Pick a design direction based on the prospect’s strongest angle.

### A. Local Heritage / Family Trust

Use when: business has years in market, family/local story, strong community presence.

Visual feel:

- warm neutral/light palette;
- editorial sections;
- real/team/van photo emphasis;
- timeline/history block;
- large local service-area proof;
- less “startup landing page,” more established local company.

Best for: family-owned HVAC/plumbing/roofing/electricians.

### B. Emergency Dispatch / Same-Day Response

Use when: emergency service is the money path.

Visual feel:

- dispatch/status panel;
- “choose your issue” problem selector;
- service-area map;
- call-first mobile sticky CTA;
- process cards: call → dispatch → diagnose → fix;
- urgency without fake countdowns.

Best for: HVAC emergency, plumbing leaks, garage doors, storm damage.

### C. Reputation Match / Proof-First

Use when: great reviews but weak site.

Visual feel:

- Google/profile proof module;
- real review excerpts with source/date if available;
- customer story blocks;
- owner/team proof;
- simple high-trust layout.

Best for: businesses with 4.7–5.0 ratings and generic/outdated websites.

### D. Service-Specific Landing Page

Use when: high-value service lacks a dedicated page.

Visual feel:

- one job-to-be-done per page;
- specific symptoms/problems;
- before/after/service process;
- pricing/estimate expectations if public;
- FAQ objections;
- booking/call CTA.

Best for: water heaters, AC repair, roof inspections, brake repair, EV chargers.

### E. Premium Local Brand Refresh

Use when: business is good but design feels outdated/cheap.

Visual feel:

- clean Apple/Stripe/Webflow-level spacing;
- high-quality typography;
- restrained palette;
- custom sections;
- proof and CTA, not clutter.

Best for: dental, med spa, higher-ticket home services.

### F. GMB / Local Profile Conversion Page

Use when: GMB exists but the click path is weak.

Visual feel:

- map/service-area section;
- hours/contact consistency;
- review/profile proof;
- “from Google search to booked job” flow;
- local SEO/service pages.

Best for: businesses with decent listing but bad website or no service pages.

---

## Vertical-specific design requirements

### HVAC

Must consider:

- no heat/no cool paths;
- seasonal tune-up/maintenance;
- repair vs replacement guidance;
- financing/rebate section if public;
- brands/certifications only if verified;
- emergency mobile CTA.

Avoid making every HVAC site red/orange emergency dark mode.

### Plumbing

Must consider:

- emergency leak/water heater/drain paths;
- trust/licensing/proof;
- service area;
- after-hours clarity;
- domain email/contact professionalism;
- simple booking/quote flow.

Avoid fake master-plumber claims unless verified.

### Roofing / Storm Damage

Must consider:

- storm inspection CTA;
- insurance process guide;
- before/after imagery;
- service-area map;
- urgency tied to recent weather only if verified.

Avoid fearmongering.

### Auto Repair

Must consider:

- appointment booking;
- service-specific pages;
- trust/reviews;
- coupons/offers if public;
- local shop photos.

Avoid generic “mechanic hero + three services.”

### Garage Doors

Must consider:

- same-day spring repair;
- emergency stuck door CTA;
- before/after photos;
- service truck/local proof;
- safety messaging.

### Electricians

Must consider:

- licensed/trust proof;
- panel upgrades, EV chargers, emergency repairs;
- residential/commercial split;
- quote request clarity.

---

## Mockup creation workflow v2

1. **Research and score first.** Do not build before the angle is clear.
2. **Pick the design stance.** Choose one of the design directions above.
3. **Collect real proof.** Official site, GMB, public photos, real reviews, service areas, owner/team, years, hours.
4. **Write a mini creative brief** in the daily batch file:
   - prospect;
   - opportunity score;
   - primary angle;
   - design direction;
   - proof available;
   - what not to claim;
   - first offer / upsell path.
5. **Build only if visual proof helps.** Default target is 1–3 mockups/day, not 5.
6. **Use different compositions.** Do not repeat the last mockup’s structure unless there is a reason.
7. **Run visual QA.** Use browser screenshot/vision when possible and write quality notes.
8. **Push live only after passing quality gate.** Otherwise save as draft/research only.

---

## Required fields in daily JSON for mockups

```json
{
  "mockupNeed": "create_now|revise_existing|research_only|skip",
  "designDirection": "local_heritage|emergency_dispatch|reputation_match|service_specific|premium_refresh|gmb_conversion",
  "designDifferentiation": "How this differs from recent mockups",
  "qualityGateScore": 0,
  "qualityGatePassed": false,
  "realAssetsFound": {
    "photos": [],
    "logo": null,
    "reviews": [],
    "ownerOrTeam": [],
    "serviceAreas": []
  },
  "unverifiedClaimsAvoided": [],
  "visualQaNotes": "",
  "revisionNeededBeforeOutreach": true
}
```

---

## Redesign priority for existing mockups

Current existing mockups should be treated as **prototype v1**, not final outreach assets.

Recommended order:

1. **M&P Plumbing** — public email route exists, but current page needs authenticity/trust cleanup.
2. **Platinum PHC** — strong reviews; should become a reputation-match page, not generic emergency dark template.
3. **Five Seasons** — urgent bug angle; should be a helpful site-fix concept, not generic HVAC page.
4. **Bunch** — should lean family/local since 1993 or emergency dispatch, but not same M&P layout.
5. **8 Finger HVAC** — should lean owner/operator reputation and raw authenticity.
6. **Richardson Plumbing** — should lean heritage/trust, not generic emergency funnel.

---

## Practical rule for outreach

If the mockup looks generic, do not lead with it.

Use a text-only helpful bug note or research angle instead, and mark the mockup as `revisionNeededBeforeOutreach: true`.

A weak mockup is worse than no mockup because it signals low taste.

---

## Quality target

The best SYBEORG mockups should feel like:

- a sharp local business consultant noticed the exact problem;
- a tasteful designer made a credible first draft;
- a growth operator understood the lead-flow economics;
- and Stark can confidently say: “I had my team mock this up for you.”

That is the bar.
