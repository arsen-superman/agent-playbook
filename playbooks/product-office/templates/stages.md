# Product stages and gates

<!-- One source for /product:next and /product:gate. The stage is `stage:` in .ai/product/product.md. A stage ends only with the user's decision at its gate: go / pivot / kill / not yet. -->

| # | Stage | software | channel (channels, bots) | goods | Gate that ends it |
|---|---|---|---|---|---|
| 0 | Idea | idea card with a verdict (`/kb:brainstorm`) | same | same | **G1** — worth a week of research? |
| 1 | Discovery | market, competitors, narrowest segment and its pain | niche demand, competing channels, audience | demand volume, competition density, price range, seasonality, supply, regulation | **G2** — is there a segment with a pain it pays for (goods: demand you can take)? |
| 2 | Validation | hypotheses with thresholds; landing + waitlist, interviews, pre-sale | pilot posts or a pilot channel, subscriber cost, 7-day retention | unit economics before any purchase; test ads to a landing or listing; pre-orders | **G3** — is demand confirmed by numbers named before the test? |
| 3 | Scope | MVP slices, business rules, metrics, price hypothesis | format, cadence, bot scenarios, metrics | smallest test batch that proves sell-through, channels, budget cap | **G4** — scope frozen? (goods: the first gate that spends money) |
| 4 | Foundation | stack decision, walking skeleton on staging, design system | hosting, bot skeleton, posting pipeline | supplier, logistics, legal minimum, landing skeleton | **G5** — does the foundation hold? |
| 5 | Build | slice by slice | bot and backend slices, a stock of content | landing, listings, creatives | **G6** — go live? |
| 6 | Launch | release, analytics, launch plan | channel launch | selling starts | — (continuous) |
| 7 | Learn | weekly review → next bet | same | sales, returns, margin by channel | **G7** — on demand: continue alone / raise money / pivot / stop |

## Who runs a stage
| Stage | Command | Until that playbook is installed |
|---|---|---|
| 0 | `/kb:brainstorm`, then `/product:init` | — |
| 1 | `/product:discover` | — |
| 2 | `/product:validate` (landing: `/growth:landing`) | landing or pilot bot = a LOCAL task via `/dev:new-task` |
| 3 | `/product:scope`, then `/dev:requirements` per slice | — |
| 4 | `/ops:stack`, `/ops:bootstrap`, `/design:system` | stack decision = `/dev:spike-workflow`; skeleton = LOCAL tasks; goods: the checklist in `scope.md` |
| 5 | `/dev:feature-workflow` per slice (design: `/design:brief`, `/design:handoff`) | — |
| 6 | `/ops:release`, `/growth:plan` | the launch checklist on the G6 page |
| 7 | `/product:review` weekly | — |

A command of a playbook that is not installed is never suggested as the next step — use the right-hand column.

## Evidence a gate page must carry
- **G1** — the idea card: verdict, cheapest test, what would make it a no.
- **G2** — market size signal with a source; 5–8 competitors or alternatives with prices; the segment and where it gathers; the skeptic's objections. Goods: search volume and trend, number and price range of sellers, landed cost estimate, certification or customs blockers.
- **G3** — every top hypothesis: threshold named before the test, the actual number, the period, the source of the number. Goods: the unit-economics table with a positive margin at the measured cost per sale.
- **G4** — the list of must-have slices, the feature specs or business rules of the first slice, north star and 3–5 events, price hypothesis, `deferred.md`. Goods: batch size and cost, channels, budget cap, stop rule.
- **G5** — stack and hosting decisions with monthly cost; an empty end-to-end slice already on staging through CI; design system in place. Goods: supplier confirmed, delivery and returns arranged, legal minimum.
- **G6** — launch checklist: backups with a tested restore, error tracking, event analytics, privacy policy and terms, payments, launch plan, security review. Goods: stock on hand, listings and landing live in draft, ad accounts ready, returns process.
- **G7** — funnel and retention (goods: sales, returns, margin) for the period, results of the bets, money and hours spent; the options with what each costs.
