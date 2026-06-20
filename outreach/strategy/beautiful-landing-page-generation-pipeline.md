# Beautiful Landing Page Generation Pipeline

Status: research + operating standard for SYBEORG prospect/mockup redesigns.  
Goal: produce beautiful, art-directed landing pages — not generic AI website generation.

## Stark directive

For landing-page work, optimize for **beautiful design** first: custom visual systems, taste, composition, motion, local authenticity, and conversion. Use skills and MCP tooling where it improves the design process, including Figma pipelines if they materially raise quality.

## Skills loaded / standing workflow

Use these skills before serious website/landing-page generation:

1. `claude-design`
   - Design-process skill for high-fidelity artifacts, landing pages, prototypes, decks, and interaction studies.
   - Relevant rules: gather context first, define a design system, avoid AI-design slop, produce variants when exploring, verify in browser.
   - SYBEORG-specific rule: if a batch feels templated, stop rollout, rebuild one representative v3 quality-bar page, then customize each remaining page.

2. `popular-web-designs`
   - 54 real design systems as HTML/CSS references: Stripe, Linear, Vercel, Apple, BMW, Webflow, Framer, Airbnb, Runway, ElevenLabs, etc.
   - Use for visual vocabulary only — never clone a brand. Pull posture/principles: typography, density, spacing, motion, contrast, surface treatment.

3. `sketch`
   - Use when direction is not locked: build 2–3 divergent HTML variants, not color swaps.
   - For outreach mockups, load `references/local-business-outreach-mockups.md` and apply the quality gate.

4. `design-md` when needed
   - Use when a reusable design-token spec is valuable, especially if a client/project needs persistent visual rules.

5. `comfyui`
   - Use for custom hero art, cinematic textures, background plates, service-themed illustrations, or brand mood assets when public imagery is weak.
   - Current local stack has ComfyUI available; do not rely on generic stock-image hero sections by default.

## Current MCP tool baseline in Hermes

Already configured/enabled:

- `playwright` via `npx -y @playwright/mcp`
  - Use for browser QA, visual inspection, screenshots, console/network checks, responsive testing.
- `filesystem`
  - Local file operations.
- `time`
  - Date/time verification.
- `memory_graph`
  - Structured knowledge graph if needed.
- `sequential_thinking`
  - Useful for complex design strategy reasoning.
- `comfyui` via `npx -y comfyui-mcp`
  - Image/video/audio generation, workflow execution, model/node management.

## MCP/Figma research findings

### Best candidates for a real Figma pipeline

1. **Figma Developer MCP / Framelink** — `figma-developer-mcp`
   - NPM description: gives coding agents access to Figma data to implement designs in one shot.
   - Best use: **design-to-code** when Stark/client provides a Figma file/frame. It simplifies Figma API payloads so agents can implement accurately.
   - Requires: Figma personal access token (`FIGMA_API_KEY`) and a Figma file/frame link.
   - Hermes config shape:
     ```yaml
     mcp_servers:
       figma_developer:
         command: "npx"
         args: ["-y", "figma-developer-mcp", "--stdio"]
         env:
           FIGMA_API_KEY: "figd_..."
     ```
   - Recommendation: install when we have Figma token + actual files to implement.

2. **Figma Console MCP** — `figma-console-mcp`
   - NPM description: comprehensive Figma MCP for tokens, variables, components, write tools, version history diff, accessibility audits, screenshots, FigJam, Slides.
   - Best use: **design-system + bidirectional Figma work**: create/modify frames, manage variables/tokens, take screenshots, accessibility audits.
   - Requires: Figma Desktop for full local bridge/write mode, Figma token, plugin bridge. Remote mode is read-only/limited.
   - Strongest candidate if we want Hermes to make/edit Figma files, not just read them.
   - Hermes config shape:
     ```yaml
     mcp_servers:
       figma_console:
         command: "npx"
         args: ["-y", "figma-console-mcp@latest"]
         env:
           FIGMA_ACCESS_TOKEN: "figd_..."
           ENABLE_MCP_APPS: "true"
     ```
   - Recommendation: best serious Figma bridge, but set up only with Stark approval because it needs Figma Desktop/plugin/token workflow.

3. **figma-ui-mcp** — `figma-ui-mcp`
   - Bidirectional bridge: AI can draw UI on Figma canvas and read designs back.
   - Tools include `figma_write`, `figma_read`, `figma_status`, `figma_docs`, `figma_rules`, `get_design_context`, and CSS extraction.
   - Requires Figma Desktop plugin over localhost.
   - Best use: fast AI-to-Figma sketching and reading back CSS/context.
   - Recommendation: possible lightweight alternative to Figma Console if we mainly need draw/read, but Figma Console is broader.

4. **MCP Figma Toolkit** — `mcp-figma-toolkit`
   - Lets agents manipulate Figma documents: shapes, text, styles, variables, components.
   - Requires global install or npx plus Figma Desktop plugin.
   - Recommendation: useful, but lower priority than Figma Console / figma-ui-mcp unless its tool ergonomics prove better.

5. **Vibma** — `@ufira/vibma`
   - Aims at structurally sound Figma files with auto-layout, tokens, components.
   - README says it is no longer under active development and recommends Figma native MCP updates.
   - Recommendation: research reference only; do not make this primary pipeline.

### Non-Figma MCPs/tools that matter for beauty

- **Playwright MCP**
  - Essential for responsive QA and screenshot/console validation.
  - For website generation, use it after every design pass: desktop + mobile snapshots, no horizontal overflow, no console errors, CTA visible.

- **ComfyUI MCP**
  - Use for bespoke visual assets: hero textures, local-service cinematic plates, abstract motifs, before/after style art, not fake proof.
  - Especially useful when public business imagery is poor or absent.

- **Filesystem MCP + repo tools**
  - Use for preserving design research, writing standards, and updating pages.

## Recommended SYBEORG beautiful-page pipeline

### 1. Research the exact business first

Before touching HTML/CSS:

- official site/domain
- logo/favicon/assets
- public colors and type clues
- real service areas/cities
- actual services
- public reviews only if attributable
- existing site weaknesses / money leak
- competitor/reference sites in the same vertical

No fake badges, fake review counts, invented owner names, or synthetic testimonials.

### 2. Pick a design stance, not a template

Every page needs a named stance:

- cinematic emergency triage
- rural owner/operator dispatch
- family heritage proof page
- premium home-systems concierge
- county craftsman/heritage trust
- Google Business conversion bridge
- single-service high-intent landing page

If the same stance could fit all six current mockups, it is too generic.

### 3. Pull visual vocabulary from real design systems

Use `popular-web-designs` as reference vocabulary:

- Premium/local luxury: Apple, BMW, Stripe, Webflow, Framer.
- Dark cinematic: Runway, ElevenLabs, Linear, Superhuman.
- Friendly/local: Airbnb, Intercom, Notion, Zapier.
- Technical/dispatch: Linear, Sentry, Raycast, IBM.

Transform principles; do not clone branded UI.

### 4. Create a mini design system per page

Define before building:

- palette: neutrals + one real accent + one utility color max
- typography: display/body/mono accents
- section rhythm: chapters, panels, maps, strips, editorial breaks
- motif: custom SVG, map line, route, tool mark, pressure gauge, service van grid, etc.
- interaction: issue selector, route selector, mobile call dock, estimate path, proof reveal, service filter

### 5. Build fewer, better sections

Avoid the repeated contractor-template structure:

- hero + right form
- stat strip
- three service cards
- fake reviews
- final CTA

Prefer page-specific compositions:

- diagnostic selector
- real service-area map module
- local proof ledger
- dispatch board
- before/after issue flow
- editorial trust chapter
- sticky mobile CTA

### 6. Use Figma when it improves quality

Use Figma/MCP pipeline when:

- Stark wants a polished visual concept before code
- client/prospect already has Figma/brand files
- we need a reusable design-system board
- we need to hand off to a human designer/developer
- layout needs stronger spatial exploration than direct HTML coding

Do not add Figma ceremony if the fastest path is direct HTML + Playwright QA.

### 7. Visual QA is mandatory

For every final/presented page:

- serve locally
- check route returns `200`
- validate JSON/tracker if edited
- mobile viewport around 390px: no horizontal overflow, CTA visible
- desktop viewport: no broken composition, no console errors
- inspect with browser/screenshot/vision tools
- compare against the quality gate: does it look custom or AI-generated?

## Tooling install decision

Do **not** blindly add Figma MCP servers yet. They require secrets and/or Figma Desktop/plugin setup. Recommended sequence:

1. Keep using current stack immediately: `claude-design` + `popular-web-designs` + Playwright MCP + ComfyUI MCP.
2. When Stark approves Figma setup, add **Figma Console MCP** first for broad token/write/screenshot capabilities.
3. Add **figma-developer-mcp** second if design-to-code from existing Figma files becomes common.
4. Keep `figma-ui-mcp` as an alternate if Figma Console feels too heavy.

## Immediate application to current six mockups

M&P Plumbing is the current v3 quality-bar prototype. Before rolling out, each remaining page should receive its own stance:

- `8-finger-hvac`: rural owner/operator dispatch, field route map, warm utility/weather posture.
- `bunch-heating-cooling`: HVAC/plumbing split-control room, red/blue system diagnostic, paid-search landing energy.
- `five-seasons-hvac`: family/local trust, seasonal comfort editorial, warmer proof-first page.
- `platinum-phc`: premium one-call home systems, polished concierge dashboard, high-ticket trust.
- `richardson-plumbing`: heritage/craftsman county trust, restrained type, service ledger/map.

Each should be redesigned one-by-one with visual QA, not mass-recolored from M&P.
