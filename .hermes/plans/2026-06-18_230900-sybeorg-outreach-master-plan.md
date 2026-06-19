# SYBEORG Outreach Master Plan — Inventory + Launch Path

Created: 2026-06-18 23:09 CDT  
Owner: Stark / Hermes  
Status: planning only; **nothing should be sent without Stark approval**.

## 1. Goal

Recover and consolidate every SYBEORG-related outreach asset we can access, confirm live mockups/email access, and turn the work into a controlled outbound plan that starts with a small safe batch instead of blasting everything.

## 2. Source coverage inspected

### Local project/repo

Canonical mockup repo:

- `C:/Users/TAHA/workspace/github/sybeorg-mockups`
- Git remote: `https://github.com/majidtaha99-prog/sybeorg-mockups.git`
- Recent commits visible locally:
  - `b325f24 chore: update outreach drafts with live mockup links`
  - `b9f8f99 feat: add prospect mockup tracker and outreach drafts`

Key local files:

- `README.md` — project summary / live root.
- `mockups.json` — root tracker for prospects, mockup URLs, status, next-batch queue.
- `index.html` — root gallery page.
- `outreach/current-prospect-drafts.md` — main current-prospect local outreach drafts.
- `outreach/first-batch-send-pack.md` — newly prepared review pack for first 3 sends.
- `outreach/send-queue.json` — newly prepared structured queue.

Completed prospect mockup folders:

- `8-finger-hvac/index.html`
- `bunch-heating-cooling/index.html`
- `five-seasons-hvac/index.html`
- `mp-plumbing/index.html`
- `platinum-phc/index.html`
- `richardson-plumbing/index.html`

Reusable templates:

- `templates/sybeorg-classic/index.html`
- `templates/trades-emergency/index.html`
- `templates/restaurant-warm/index.html`
- `templates/auto-shop/index.html`

### Live mockup verification

All 6 current public mockup URLs returned HTTP 200:

- `https://sybeorg-mockups.vercel.app/8-finger-hvac/`
- `https://sybeorg-mockups.vercel.app/bunch-heating-cooling/`
- `https://sybeorg-mockups.vercel.app/five-seasons-hvac/`
- `https://sybeorg-mockups.vercel.app/mp-plumbing/`
- `https://sybeorg-mockups.vercel.app/platinum-phc/`
- `https://sybeorg-mockups.vercel.app/richardson-plumbing/`

Root `index.html` already links the six prospect mockups plus four templates, so the completed work is surfaced from the gallery.

### Gmail/Himalaya access

Himalaya executable:

- `C:/Users/TAHA/AppData/Local/hermes/bin/himalaya.exe`

Configured accounts:

- `sybeorg` — `sybeorg@gmail.com`, default account, IMAP/SMTP works.
- `majidclawbot` — Hermes account, IMAP/SMTP works.
- `radi` — House of Meroë/Radi account, IMAP/SMTP works.

SYBEORG Gmail folders verified:

- `INBOX`
- `[Gmail]/Drafts`
- `[Gmail]/Sent Mail`
- others: All Mail, Important, Spam, Starred, Trash.

Important rule: email access is live, but outbound sends must remain blocked until Stark approves exact recipient, subject, body, links, and attachments.

### Gmail drafts found in `sybeorg@gmail.com`

SYBEORG Gmail has **26 drafts**. Important business/outreach drafts include:

#### Active trades/home-services drafts

- ID `520` — M&P Plumbing: `quick thing about your site title — Al & Micheal`, to `mpplumbingia@gmail.com`.
- ID `521` — Platinum PHC: `saw a few things on platinumphcdsm.com — Eric`, to `eric@platinumphcdsm.com`.
- ID `522` — Richardson Plumbing: `40 years of experience, hidden behind a form — John`, missing visible recipient.
- ID `523` — Five Seasons: `your website is showing developer placeholder text to customers`, missing visible recipient.
- ID `524` — Bunch: `your "24/7 emergency" isn't tappable on mobile — Bunch`, missing visible recipient.
- ID `525` — 8 Finger HVAC: `your reviews > your website — Bobby`, to `bobbyghvac86@outlook.com`.
- ID `526` — M&P Plumbing alternate: `your google tab says "Tempo Apartments" — Al & Micheal`, to `mpplumbingia@gmail.com`.
- ID `527` — 8 Finger HVAC alternate: `your reviews are better than your website — Bobby`, to `bobbyghvac86@outlook.com`.
- ID `528` — Platinum PHC alternate: `the hero image on platinumphcdsm.com is AI — Eric`, to `eric@platinumphcdsm.com`.

#### Restaurant/local-business drafts

- ID `529` — Le Crave: `lecraveic.com returns a 403 — Maryam`, placeholder recipient `FILL-IN@lecraveic.com`.
- ID `530` — Zolly's Grill: `your site says © 2024 and old hours — Shiv`, placeholder recipient `FILL-IN@zollysgrill.com`.
- ID `531` — 401 Oak: `you're renting traffic from yelp — 401 Oak`, placeholder recipient `FILL-IN-401oak@gmail.com`.
- ID `532` — Trumpet Blossom/Katy: `your seasonal menu is hidden — Katy`, to `trumpetblossom@gmail.com`.
- ID `533` — Tribute: `no online reservations is costing you covers — Tribute`, placeholder recipient `FILL-IN@tributecoralville.com`.
- ID `534` — Copper Boar: `your brunch deserves its own page — Copper Boar`, placeholder recipient `FILL-IN@copperboar.com`.

#### Radi / House of Meroë draft

- ID `535` — Anghami: `Radi Barakat x Anghami — retainer proposal for MENA reach`, to `partnerships@anghami.com`.

#### Other recent business draft

- ID `546` — Tyler Vande Lune reply: `Re: Video Production Support for your Business`, to `vandelunefilms@gmail.com`.

### Sent folder reality check

`[Gmail]/Sent Mail` does contain older SYBEORG emails and a self-test message. Recent visible sends include:

- `Hermes send test - sybeorg` to self, 2026-06-19.
- `Re: Video Production Support for your Business` to Tyler, 2026-06-14.
- Older 2025/2024 SYBEORG business/client/logistics messages.

For the current recovered mockup campaign: I did **not** find visible sent messages matching the Bunch/Five Seasons/M&P/8 Finger/Platinum/Richardson outbound draft subjects in the first 100 sent messages. Treat current campaign as **drafted, not launched**.

## 3. Recovered campaign buckets

### Bucket A — Current mockup-first trades/home-services campaign

Source of truth:

- Local repo: `C:/Users/TAHA/workspace/github/sybeorg-mockups`
- Local draft file: `outreach/current-prospect-drafts.md`
- Tracker: `mockups.json`
- Gmail drafts IDs: `520`–`528`, with alternates for M&P, 8 Finger, and Platinum.

Prospects:

| Priority | Prospect | Vertical | Public mockup | Known/likely email status |
|---|---|---|---|---|
| High | Bunch Heating and Cooling | HVAC + plumbing | live | recipient missing in Gmail draft; local send pack needs email |
| High | Five Seasons Heating & Cooling | HVAC | live | recipient missing in Gmail draft; local send pack needs email |
| High | M&P Plumbing | Plumbing | live | `mpplumbingia@gmail.com` in Gmail draft |
| Medium | 8 Finger HVAC | HVAC | live | `bobbyghvac86@outlook.com` in Gmail draft |
| Medium | Platinum Plumbing, Heating & Cooling | Plumbing + HVAC | live | `eric@platinumphcdsm.com` in Gmail draft |
| Medium | Richardson Plumbing | Plumbing | live | recipient missing in Gmail draft |

Two copy styles exist:

1. **Older Gmail drafts** — sharper, more direct audit/problem-led copy.
2. **Newer local `current-prospect-drafts.md` copy** — safer, lower-pressure mockup-first copy.

Recommendation: use the newer mockup-first copy for first outreach because it avoids sounding too aggressive and leads with proof. Keep the older Gmail drafts as angle/reference material.

### Bucket B — Restaurant/local business campaign

Source of truth found so far:

- Gmail drafts IDs `529`–`534`.
- No matching local markdown/html files found during local file search for Le Crave/Zolly/401 Oak/Tribute/Copper Boar/Trumpet Blossom.

Prospects/drafts:

- Le Crave — recipient placeholder.
- Zolly's Grill — recipient placeholder.
- 401 Oak — recipient placeholder.
- Trumpet Blossom/Katy — has `trumpetblossom@gmail.com`.
- Tribute — recipient placeholder.
- Copper Boar — recipient placeholder.

Recommendation: park this bucket until the trades campaign is organized. Then either build matching mockups using the existing restaurant template or convert these into pure audit emails after verifying every claim.

### Bucket C — Radi / House of Meroë brand-deal outreach

Source of truth:

- `C:/Users/TAHA/Desktop/house of meroe/radi-outreach-pack/`
- `radi-working-brief.md`
- `radi-proofread-email-drafts.md`
- `radi-target-list-60.csv`
- `radi-platform-ranking.md`
- `radimediakit.pdf`
- Gmail draft ID `535` for Anghami.

First batch in local brief:

1. Anghami
2. Shahid
3. Tabby
4. Careem
5. Tamara

Rate card:

- Single Reel: $1,500 floor
- Reel + 3 Stories: $2,250
- 3-Reel Campaign: $4,050
- UGC Single: $700
- UGC 3-Pack: $1,650
- Monthly Retainer: $3,750/mo
- Whitelisting 30d: +$750

Recommendation: keep Radi campaign separate from SYBEORG local-services campaign because it uses a different sender (`radibarakat.mgmt@gmail.com`), positioning, assets, and sales motion.

### Bucket D — Creator/platform setup

Source:

- `radi-platform-ranking.md`

Top setup priorities:

1. Instagram / Meta Creator Marketplace
2. Collabstr
3. Aspire Creator Platform
4. Upfluence Creator Marketplace
5. Insense
6. Shopify Collabs

Recommendation: this is a separate revenue lane from SYBEORG local-service emails. It can run in parallel but should not distract from the first SYBEORG sends.

## 4. Current access status

### Confirmed

- Local SYBEORG mockup repo accessible.
- Live Vercel mockups accessible.
- Root gallery exposes completed mockups.
- Gmail IMAP/SMTP accessible for `sybeorg`, `majidclawbot`, and `radi`.
- Local Radi outreach pack accessible.
- Gmail draft folder accessible and has a substantial backlog.

### Not yet confirmed / gaps

- Recipient emails for Bunch, Five Seasons, Richardson are still missing/blank in current Gmail drafts.
- Restaurant campaign appears to live mostly in Gmail drafts, not local project files.
- Some restaurant recipients are placeholders and cannot be sent as-is.
- Older Gmail drafts contain aggressive claims that must be reverified before sending.
- GitHub push/write access was not verified in this planning pass.
- The repo currently has local uncommitted changes from tracker/send-pack preparation; do not push until Stark approves the consolidated structure.

## 5. Recommended operating model from here

### Rule 1 — No automatic sends

Every outbound message needs an approval packet:

- From account
- To / Cc
- Subject
- Final body
- Links
- Attachments, if any
- Why this recipient is safe/valid

### Rule 2 — One active campaign at a time

Start with SYBEORG trades/home-services because:

- Mockups are already live.
- There are 6 completed assets.
- The offer is concrete.
- The CTA is low-pressure.
- It directly supports SYBEORG revenue.

Radi can run as a second lane after the SYBEORG first batch is clean or while waiting for replies.

### Rule 3 — First batch must be small

First SYBEORG batch should be 3 prospects max:

1. M&P Plumbing — email exists, mockup live, high priority.
2. Platinum PHC or 8 Finger HVAC — email exists, mockup live, medium priority but ready.
3. Bunch or Five Seasons — only after recipient is verified.

Alternative: if Stark wants fastest launch without contact research, send first to the three with known emails:

1. M&P Plumbing — `mpplumbingia@gmail.com`
2. 8 Finger HVAC — `bobbyghvac86@outlook.com`
3. Platinum PHC — `eric@platinumphcdsm.com`

This is the cleanest immediate test batch because the recipient fields are already present in Gmail drafts.

## 6. Step-by-step launch plan

### Phase 0 — Freeze and consolidate

1. Treat `C:/Users/TAHA/workspace/github/sybeorg-mockups` as the canonical SYBEORG mockup/outreach workspace.
2. Do not edit Gmail drafts directly until the source-of-truth copy is chosen.
3. Keep Gmail draft IDs documented in this plan so older work is not lost.
4. Keep `outreach/current-prospect-drafts.md` as the safer review source for mockup-first messages.

### Phase 1 — Build the master send board

Create or update one CSV/JSON board with these columns:

- Campaign bucket
- Prospect/business
- Contact name
- Recipient email
- Recipient confidence: verified / likely / placeholder / missing
- Mockup URL
- Mockup URL status
- Draft source: local / Gmail draft ID
- Chosen subject
- Chosen body source
- Risk notes
- Approval status
- Sent status
- Reply status
- Follow-up date

Seed it with:

- 6 trades/home-service prospects.
- 6 restaurant prospects from Gmail drafts.
- Top 5 Radi brand prospects.

### Phase 2 — Choose copy style for trades

For each trades prospect, compare:

- Existing Gmail draft copy, especially IDs `520`–`528`.
- Newer local mockup-first copy in `outreach/current-prospect-drafts.md`.

Recommended default:

- Use mockup-first copy as final body.
- Pull only 1–2 verified concrete observations from older Gmail drafts if helpful.
- Avoid unsupported claims like review counts unless reverified on official/reliable pages.
- Avoid harsh lines like “your website is costing you calls” in first touch unless Stark wants aggressive style.

### Phase 3 — Verify missing contacts

Need contact research for:

- Bunch Heating and Cooling
- Five Seasons Heating & Cooling
- Richardson Plumbing
- Restaurant placeholders: Le Crave, Zolly's, 401 Oak, Tribute, Copper Boar

Validation hierarchy:

1. Official website contact page.
2. Google Business Profile / visible public listing.
3. Facebook/Instagram business contact field.
4. Public directory only if official source unavailable.
5. If uncertain, mark as `needs_human_check` instead of sending.

### Phase 4 — First send packet for Stark approval

Prepare a Discord approval packet with exactly 3 proposed emails.

Recommended first packet if we want fastest launch:

1. M&P Plumbing — known email.
2. 8 Finger HVAC — known email.
3. Platinum PHC — known email.

Recommended first packet if we want highest strategic priority:

1. Bunch — after email verification.
2. Five Seasons — after email verification.
3. M&P Plumbing — known email.

Each packet should include full final copy and links. Stark replies `approved` or edits.

### Phase 5 — Send manually through tool only after approval

After approval, send with Himalaya from `sybeorg@gmail.com`. Use the command form where `--account` is passed after the subcommand, e.g.:

```bash
himalaya template send --account sybeorg < message.eml
```

After each send:

1. Verify the message appears in `[Gmail]/Sent Mail`.
2. Update the send board.
3. Do not send the next batch until the first batch is confirmed delivered/sent.

### Phase 6 — Follow-up cadence

If no reply:

- Follow-up 1: 3 business days later.
- Follow-up 2: 7 business days later.
- Then stop unless there is a clear reason to re-engage.

Follow-ups should stay short and permission-based.

## 7. Immediate next action

Recommended next action for Hermes:

1. Build the master send board from all recovered assets.
2. Research and verify missing emails.
3. Compare Gmail draft copy vs local mockup-first copy for the three fastest send-ready prospects.
4. Bring Stark a 3-email approval packet.

Recommended decision for Stark:

Choose first-batch mode:

- **Fastest launch:** M&P, 8 Finger, Platinum — all have known emails.
- **Highest priority:** Bunch, Five Seasons, M&P — requires email research first.

## 8. Safety constraints

- No cold outreach sends without Stark approval.
- No placeholder recipients.
- No dead links.
- No unverifiable claims.
- No attachments unless explicitly listed and approved.
- No mixing Radi/House of Meroë sender identity with SYBEORG local-service outreach.

## 9. Summary

We have more than just a few drafts. The recovered work includes:

- 6 live SYBEORG trades/home-service mockups.
- 4 reusable website/mockup templates.
- A local mockup-first outreach draft pack.
- 9 active trades Gmail drafts/alternates.
- 6 restaurant Gmail drafts.
- A complete Radi/House of Meroë brand-deal pack with 60 targets, media kit, rates, and first-batch drafts.
- Working Gmail access for all three relevant accounts.

The best move is not to send everything. The best move is to consolidate the backlog, choose the safest first 3, get Stark approval, send, then learn from replies before scaling.
