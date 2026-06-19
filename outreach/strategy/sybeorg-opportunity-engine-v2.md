# SYBEORG Opportunity Engine v2 — Smarter Angles + Easier Closes

Status: strategy proposal for upgrading the daily cron.  
Created: 2026-06-19 03:31 CDT.  
Scope: **SYBEORG only**. Radi / House of Meroë remains excluded.

## Core idea

The daily cron should stop thinking only in terms of “website or GMB.” Those are still important, but the easier close comes from finding the prospect’s **nearest money leak** and presenting SYBEORG as the lowest-friction fix.

The winning angle is usually not “you need a website.” It is:

> “You are probably losing this specific type of lead because this specific public path is broken/weak. I made the fix visible.”

That gives Stark a sharper, easier close: not abstract web design, but a concrete revenue/lead-flow problem.

---

## Expanded opportunity categories

### 1. No website / fake website / social-only presence

**Signal:** No official domain, only Facebook, directory pages, Google listing, a broken/parked domain, or a generic portal page.

**Offer angle:** “You need a real home base that turns searchers into calls.”

**Best deliverable:** Full one-page website mockup.

**Close difficulty:** Medium. They may be low-budget, but if they have good reviews/service demand, this is a clean pitch.

### 2. Bad mobile conversion path

**Signal:** Phone hard to tap, CTA below fold, no sticky call bar, confusing nav, forms too long, emergency visitors forced to scroll.

**Offer angle:** “Most of your emergency leads are on mobile. The site should make calling/requesting service instant.”

**Best deliverable:** Mobile-first landing page mockup.

**Close difficulty:** Low-medium. This is one of the best trades/home-service angles.

### 3. GMB / local profile leakage

**Signal:** Missing website/phone/hours/category, wrong domain, weak photos, no services, no appointment link, inconsistent NAP, no service areas, unclaimed/weak directory profiles.

**Offer angle:** “People are finding you, but the profile path is leaking calls before they reach you.”

**Best deliverable:** Local presence cleanup checklist + landing page if website is weak.

**Close difficulty:** Low if the issue is visible and specific.

### 4. Reputation mismatch

**Signal:** Great Google reviews but website looks weak, outdated, generic, stock-heavy, no reviews above fold, no owner/team story.

**Offer angle:** “Your reputation is stronger than your website. We should make the website match the trust you’ve already earned.”

**Best deliverable:** Trust-first homepage/landing mockup using verified public proof.

**Close difficulty:** Low. This is friendly and non-insulting.

### 5. Paid-ad readiness gap

**Signal:** Business is in a high-CPC/high-intent vertical but has no proper landing page, no conversion-focused offer, no fast CTA, no service-specific page.

**Offer angle:** “Before spending on Google Ads, you need a page that can actually convert the clicks.”

**Best deliverable:** Paid-search landing page mockup + basic campaign concept.

**Close difficulty:** Low-medium if they are growth-minded. This creates a larger upsell path: site → landing page → Google Ads.

### 6. Urgent bug / broken public path

**Signal:** Placeholder text, broken form, dead nav link, wrong title/domain, SSL error, 404 service page, broken email/phone link, request-service page broken.

**Offer angle:** “I noticed a specific thing that looks broken publicly. I made a quick fix/mockup so you can see the cleaner version.”

**Best deliverable:** Short bug note + visual mockup.

**Close difficulty:** Low if done politely. This is the “helpful alert” play.

### 7. Service-page gap

**Signal:** They offer high-value services but have no dedicated page for each service: emergency plumbing, water heater replacement, AC repair, roof storm damage, brake repair, etc.

**Offer angle:** “You don’t need a whole rebrand first — you need one focused page for the jobs people search with buying intent.”

**Best deliverable:** Service-specific landing page mockup.

**Close difficulty:** Low. Easier than selling a full website.

### 8. Seasonal urgency gap

**Signal:** HVAC before heat/cold waves, roofing after storms, plumbing freeze season, landscaping spring, garage doors winter, tax/accounting season, etc.

**Offer angle:** “This is the time window where search demand spikes. You should have a simple page ready before the rush.”

**Best deliverable:** Seasonal campaign page mockup.

**Close difficulty:** Medium-low when timed right.

### 9. Hiring / capacity signal

**Signal:** Business is hiring technicians, installers, front desk, etc. That suggests growth/cashflow and also a possible recruiting page gap.

**Offer angle:** “If you’re hiring, your site should help recruit and convert customers at the same time.”

**Best deliverable:** Careers/recruiting section + trust homepage upgrades.

**Close difficulty:** Medium. Not always the primary hook, but a strong buying-capacity signal.

### 10. Review/reputation management gap

**Signal:** Low rating but enough volume, unanswered negative reviews, no fresh reviews, strong reviews not reused on website, competitor has better review profile.

**Offer angle:** “You already have proof / or you need a review engine. Let’s make reviews turn into calls.”

**Best deliverable:** Review widget mockup + review request system proposal.

**Close difficulty:** Medium. Good upsell, not always first email hook.

### 11. Competitor gap / local outranked angle

**Signal:** Competitors have better GMB, service pages, booking, photos, review presentation, or ads.

**Offer angle:** “Your competitors make the next step easier online. I mocked up what closing that gap could look like.”

**Best deliverable:** Side-by-side competitor mini-audit + mockup.

**Close difficulty:** Medium. Must avoid being too negative.

### 12. Tracking / measurement gap

**Signal:** Site has forms/phone but no obvious tracking, no thank-you flow, no call tracking, no dedicated ad landing page.

**Offer angle:** “If you run ads or plan to, you need to know which calls/forms are turning into jobs.”

**Best deliverable:** Landing page + measurement setup offer.

**Close difficulty:** Higher for cold first touch, better as second-touch upsell.

### 13. Booking / automation gap

**Signal:** No online booking, no quote form, no urgency tagging, no SMS/call triage, slow manual forms.

**Offer angle:** “A simple request-service flow can catch after-hours leads and sort emergency vs flexible jobs.”

**Best deliverable:** Request-service form/page mockup.

**Close difficulty:** Low-medium in emergency/service verticals.

### 14. Brand trust / owner story gap

**Signal:** Family-owned, years in business, veteran-owned, local crew, strong photos — but buried or absent on website.

**Offer angle:** “Your local trust story should be above the fold, not hidden.”

**Best deliverable:** Story/trust-forward homepage mockup.

**Close difficulty:** Low. Friendly and effective.

### 15. Contact-route gap

**Signal:** Gmail/Outlook address instead of domain email, broken mailto, no form, no email, only Facebook, phone absent from GMB.

**Offer angle:** “Make it easier and more professional for customers/property managers to reach you.”

**Best deliverable:** Domain email + contact page + CRM/light automation proposal.

**Close difficulty:** Medium. Good add-on.

---

## Lead scoring model for the cron

Each lead should get an Opportunity Score out of 100:

| Factor | Points | Why it matters |
|---|---:|---|
| Clear public pain / bug | 0–20 | Easier personalized hook. |
| High-intent vertical | 0–15 | More money per lead. |
| Good contact route | 0–15 | Easier to reach without manual hunting. |
| Strong proof/reviews | 0–10 | Easier to build trust-focused mockup. |
| Weak/outdated website | 0–15 | Strong website/landing offer. |
| GMB/profile gap | 0–10 | Local SEO/reputation angle. |
| Paid-ad/service-page opportunity | 0–10 | Upsell path beyond website. |
| Owner-operated/local fit | 0–5 | Easier close than corporate/franchise. |

Classification:

- `80–100`: hot lead, create mockup now, draft first-touch copy.
- `65–79`: good lead, draft copy; create mockup if angle is visual.
- `50–64`: nurture/research; no mockup unless easy template reuse.
- `<50`: skip unless a later signal appears.

---

## New daily batch structure

Instead of just “5 leads,” the cron should produce a balanced batch:

1. **2 hot leads with mockups** — best monetizable angles.
2. **1 urgent bug/helpful alert lead** — placeholder/broken form/dead link/wrong domain.
3. **1 paid-ad/service-page opportunity** — landing page angle with possible ads upsell.
4. **1 GMB/reputation/local profile opportunity** — profile cleanup/reviews/contact leakage.

This gives Stark different close types instead of five identical website pitches.

---

## Better process: triage before build

The cron should not automatically build mockups for all 5. It should run a triage:

1. **Discovery pass:** collect 10–15 possible businesses.
2. **Score pass:** assign opportunity scores and category.
3. **Select top 5:** choose based on closeability, not just bad website.
4. **Mockup decision:** build only for leads where a visual sample makes the pitch stronger.
5. **Draft decision:** write email/form/phone scripts based on actual contact route.
6. **Approval packet:** save exact copy, never send.

This prevents wasted mockups for weak leads.

---

## Outreach angle ladder

Use the highest available verified angle:

1. **Public urgent bug** — strongest if true.
2. **No/weak contact path** — phone/form/email/GMB leakage.
3. **Emergency/mobile conversion** — trades/home-services money path.
4. **Reputation mismatch** — strong reviews but weak site.
5. **Service-page gap** — high-intent service page missing.
6. **GMB/profile leakage** — missing/weak/inconsistent local profile fields.
7. **Paid-ad readiness** — landing page before Google Ads.
8. **Brand/story gap** — local proof buried.
9. **General redesign** — last resort, weakest.

Never lead with “we make websites” if there is a more specific money leak.

---

## Offer ladder for easier close

Do not always sell the full website first. The easier close is usually a smaller first win:

1. **Free bug/helpful note** — gets reply.
2. **One-page landing page** — easier yes than full website.
3. **GMB/profile cleanup** — concrete local visibility fix.
4. **Review/trust section upgrade** — uses proof they already have.
5. **Service-specific page pack** — water heater, AC repair, storm damage, etc.
6. **Full website refresh** — only when trust is built or existing site is clearly weak.
7. **Google Ads + landing page** — higher-ticket upsell after page/measurement exists.
8. **Monthly growth package** — website + GMB + ads + reporting.

---

## What the cron should add to each lead record

Add these fields to daily JSON boards:

```json
{
  "opportunityScore": 0,
  "primaryAngleCategory": "urgent_bug|mobile_conversion|reputation_mismatch|service_page_gap|gmb_leak|paid_ad_readiness|no_website|contact_route_gap|seasonal_urgency|booking_gap|brand_trust_gap|skip",
  "secondaryAngles": [],
  "evidenceQuality": "strong|good|fair|weak",
  "verifiedEvidence": [],
  "unsafeOrUnverifiedClaims": [],
  "recommendedOffer": "bug_fix|landing_page|gmb_cleanup|service_page|review_system|full_site|ads_landing_page|nurture",
  "mockupDecisionReason": "",
  "closeDifficulty": "low|medium|high",
  "nextBestAction": "email_draft|contact_form_draft|phone_script|manual_research|skip",
  "upsellPath": ["landing_page", "gmb_cleanup", "google_ads"]
}
```

---

## Vertical-specific hooks

### HVAC

- Emergency AC/heat calls need one-tap mobile CTA.
- Seasonal tune-up page.
- Financing/rebate page.
- Maintenance plan page.
- Same-day/emergency inconsistency across site/GMB/directories.

### Plumbing

- Emergency leak/water heater page.
- After-hours CTA.
- Service area page.
- Domain email/contact professionalism.
- Trust/review proof above fold.

### Roofing / storm damage

- Storm damage inspection page.
- Insurance claim guidance page.
- Recent storm timing.
- GMB photos/reviews/service area.
- Fast “request inspection” CTA.

### Auto repair

- Appointment booking friction.
- Service-specific pages: brakes, tires, oil, diagnostics, AC.
- Reviews not visible on site.
- Weak coupons/offers.
- Google profile photos/services missing.

### Garage doors

- Emergency repair page.
- Same-day spring replacement CTA.
- Before/after photos.
- Service area gaps.

### Electricians

- Emergency/service panel/EV charger pages.
- Licensing/trust proof.
- Quote request friction.
- Commercial/residential split unclear.

### Dental / med spa

- Booking friction.
- Treatment/service pages weak.
- Before/after/gallery trust.
- Review proof.
- Premium design mismatch.

---

## Proposed cron v2 instruction changes

1. Research 10–15 candidates, not just 5.
2. Score them using Opportunity Score.
3. Select the best 5 with varied angle types.
4. Create 1–3 mockups/day, not necessarily 5.
5. Prioritize leads with an easier first close:
   - public bug,
   - strong reputation mismatch,
   - no/weak mobile CTA,
   - missing service page for expensive jobs,
   - contact/GMB leakage.
6. Add a `why_this_should_close` note for each lead.
7. Add `first_offer` and `upsell_path` fields.
8. Keep all outputs draft-only and approval-gated.

---

## Recommendation

Upgrade the cron from “daily mockup generator” into a **daily opportunity engine**:

- find 10–15,
- score/select 5,
- build mockups only where visual proof helps,
- draft the easiest close angle,
- preserve upsell paths,
- push live mockups,
- never contact without approval.

Best default daily mix:

- 2 website/landing page mockups,
- 1 bug/helpful-alert lead,
- 1 GMB/profile/reputation lead,
- 1 paid-ad/service-page opportunity.

That creates more varied, sharper, easier-to-close lead packets for Stark instead of a pile of generic “your website could be better” pitches.
