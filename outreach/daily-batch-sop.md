# SYBEORG Daily Prospect + Mockup Batch SOP

Status: active operating procedure for autonomous daily batches.  
Scope: **SYBEORG only**. Do not inspect, modify, reference, or blend Radi / House of Meroë assets, drafts, accounts, files, or target lists.

## Prime directive

Each daily batch should produce **5 researched leads** with a specific, evidence-backed angle and a clear next action:

- `needs_website`: no real website, broken/parked website, social-only presence, directory-only presence, or placeholder portal.
- `needs_better_website`: website exists but is outdated, slow/confusing, weak mobile CTA, weak proof, bad service page, broken nav/form, generic stock/AI imagery, SEO/title/meta issue, poor local trust presentation.
- `needs_gmb`: Google Business Profile is missing, weak, inconsistent, missing phone/website/hours/category, or not matching official site/contact info.
- `bug_or_urgent_fix`: public website bug, placeholder text, broken request form, dead nav link, wrong domain/title, broken phone/email link, inconsistent emergency/hours/service claims.
- `skip_or_nurture`: acceptable presence, no strong angle, bad fit, duplicate, too large/corporate, no reachable contact route.

## Daily output requirement

For each of the 5 prospects, save:

1. Business name.
2. Vertical and market.
3. Official website URL, or `none_found`.
4. Google Maps / GMB-style evidence available publicly: rating if visible, category, phone, website, hours, missing fields.
5. Contact route: public email, contact form, phone/manual, or research-needed.
6. Source of public email if found: official site mailto/schema/header/footer preferred.
7. Website/GMB diagnosis.
8. Best outreach hook.
9. Recommended outreach channel.
10. Mockup need level: `create_now`, `existing_template_enough`, `research_only`, or `skip`.
11. Exact draft copy if outreach-ready.
12. Approval status: always `pending_stark_review` unless Stark has explicitly approved.
13. Send status: always `not_sent` unless Stark explicitly approves and a separate send task is run.

## Prospect sourcing priorities

Rotate through high-intent local service verticals in Iowa / nearby Midwest markets:

1. HVAC.
2. Plumbing.
3. Roofing / storm damage.
4. Auto repair.
5. Garage doors.
6. Electricians.
7. Foundation/waterproofing.
8. Landscaping/tree service.
9. Dental / med spa only if trades pipeline is thin.

Prefer businesses that are:

- Local owner-operated or small multi-truck shops.
- Actively serving residential/emergency needs.
- Big enough to pay for a website/landing page but not so polished that the angle is weak.
- Have proof signals: years in business, good reviews, strong photos, service area, family/local story.
- Have clear website/GMB gaps.

Avoid:

- National franchises unless the local branch clearly controls its own marketing.
- Businesses with polished modern websites and clean GMB unless a specific bug exists.
- Prospects with no reachable contact route after reasonable research.
- Any Radi / House of Meroë targets or files.

## Research workflow

For each candidate:

1. Search web/maps for the vertical + market.
2. Open/inspect official website, contact page, and service pages.
3. Inspect Google Maps/Business listing in browser limited view where possible.
4. Extract public facts only: phone, website, public email, service area, category, visible rating, hours, obvious missing fields.
5. Confirm any bug/claim from the official site before using it in copy.
6. Classify angle using the categories above.
7. Decide whether a mockup is needed.

## Mockup workflow

If `mockup_need = create_now`:

1. Create a slug under repo root: `business-name-market/`.
2. Use existing templates as inspiration:
   - `templates/trades-emergency/index.html`
   - `templates/auto-shop/index.html`
   - `templates/sybeorg-classic/index.html`
3. Create a standalone `index.html` with:
   - business-specific hero and CTA,
   - phone/contact route if public,
   - trust proof based only on verified public facts,
   - service area,
   - mobile-first CTA,
   - clear sample/mockup framing if needed.
4. Do not fabricate review quotes, review counts, awards, certifications, or years in business.
5. Add the mockup to `index.html` root gallery if appropriate.
6. Update `mockups.json` or a daily lead board with the new prospect.
7. Commit and push so Vercel can deploy automatically.
8. Verify the live Vercel URL returns `200 OK` after push/deploy if possible.

If `mockup_need != create_now`, still save the lead research and draft angle; do not force a mockup.

## Draft workflow

Use old audit drafts as intelligence only, not direct copy. First-touch copy must be:

- local and helpful,
- precise,
- low-pressure,
- non-accusatory,
- based on freshly verified observations,
- mockup framed as a sample/concept,
- one CTA: “Worth polishing this up for you?” or similar,
- include opt-out line: “Reply NO and I will not follow up.”

Do **not** send Gmail, submit contact forms, call, or DM. Draft only.

## Files to update

Daily run should update/create:

- `outreach/daily-batches/YYYY-MM-DD-batch-N.md` — human-readable research and draft packet.
- `outreach/daily-batches/YYYY-MM-DD-batch-N.json` — machine-readable lead board.
- `mockups.json` — add new live mockup records when mockups are created.
- root `index.html` — add links to created mockups when appropriate.
- prospect `slug/index.html` files — only for created mockups.

## Git / Vercel

When files are changed:

1. Run lightweight sanity checks:
   - JSON parse for `.json` files.
   - Basic URL/file existence checks.
2. `git status --short`.
3. Commit with a conventional message, e.g. `feat: add daily sybeorg prospect batch`.
4. Push to `origin main` so Vercel can deploy.
5. Verify live URLs if new mockups were created.

If git push fails due auth or remote issues, save all files locally and report the blocker.

## Safety rules

- No outbound email sends.
- No contact form submissions.
- No phone calls.
- No Radi / House of Meroë files/accounts/targets.
- No fabricated facts.
- No stale claims in draft copy.
- Do not expose secrets.
- If uncertain whether a claim is true, phrase it as an internal note, not as copy.
