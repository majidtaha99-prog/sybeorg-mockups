# M&P Plumbing outreach draft

_Last prepared: 2026-06-20 02:24 CDT_

## Status

- Sender account: `sybeorg` / `sybeorg@gmail.com`
- Recipient: `mpplumbingservice@gmail.com`
- Recipient source: official site mailto/schema tracked in `outreach/master-send-board.json`
- Mockup URL: <https://sybeorg-mockups.vercel.app/mp-plumbing/>
- Send status: ready pending Stark approval
- Do not send until Stark approves exact recipient + subject + body.

## Recommended subject

quick mockup idea for M&P Plumbing

## Email body

Hey M&P team — I’m Majid from SYBEORG.

I put together a quick sample landing-page concept for M&P Plumbing because plumbing visitors usually decide in the first minute whether they’re calling or bouncing — especially for leaks, water heaters, and drain problems.

Mockup: https://sybeorg-mockups.vercel.app/mp-plumbing/

I kept it clearly marked as a sample concept, not an official page. The direction is a mobile-first call path: issue buttons up front, a real Urbandale / Des Moines map section, and no fake reviews or made-up claims.

If it feels useful, I can polish it around your real photos, proof, and whichever service brings in the best calls.

Worth refining for you, or should I leave it alone?

— Majid
SYBEORG

## Ready-to-send Himalaya command

From repo root:

```bash
cat outreach/drafts/mp-plumbing-email.eml | '/c/Users/TAHA/AppData/Local/hermes/bin/himalaya.exe' template send --account sybeorg
```

Only run after Stark explicitly approves sending.
