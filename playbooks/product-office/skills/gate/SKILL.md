---
name: gate
description: "Run a product gate — one page of evidence, a fresh skeptic attacks it, the user decides go / pivot / kill / not yet; record the decision and move the stage. Manual: /product:gate [G1-G7]."
argument-hint: "[G<n>]"
disable-model-invocation: true
---
# Gate — orchestrator

A gate is the user's decision, prepared so it takes five minutes. You never decide it and never skip it. Follow `templates/shared/orchestration.md` in this plugin (two levels up from this skill's folder; read it first), with `workflow: gate`. State file = `.ai/product/product.md` §Now; decisions file = `product.md §Answers and assumptions`. Gate list and required evidence: `templates/stages.md`; page: `templates/gate.md` in this plugin.

## Stages
0. **Which gate** — the argument, else `gate:` in `product.md`. A gate ahead of the current stage → refuse and name the gate that is due.
1. **Page** → `product:strategist`: "gate page G<n>". It writes `.ai/product/gates/G<n>.md` (≤60 lines) from the product folder: recommendation first, every number with its source and date, what we do not know, the cost of going on. Evidence that `templates/stages.md` requires and that does not exist is listed as missing — never smoothed over.
2. **Attack** → a fresh `product:skeptic` (never the same run that wrote anything): it reads the page and the sources behind it and writes only the page's *Objections* and *What would make it a no* sections.
3. **GATE** — show the user: the question, the recommendation, the three strongest objections, what is missing, the cost of going on. Ask (AskUserQuestion when available): **go** · **pivot** (what changes) · **kill** · **not yet** (which evidence first). Money about to be spent (ads, a batch, paid tools) is named in the question with its amount.
4. **Record** the decision the user made, in their words:
   - the page's *Decision* section;
   - a decision record `.ai/decisions/NNNN-<product>-g<n>.md` (next free number; frontmatter `status: accepted`, `date`, `decided-by`; sections Context · Decision · Consequences · Alternatives rejected) — it supersedes an earlier record of the same gate (`status: superseded`, `superseded-by`);
   - `product.md`: a line in *Decided so far*; **go** → `stage` +1 and the next `gate`, *Current bet* rewritten for the new stage; **pivot** → `stage` back to the one that must be redone, what changed in *One line* / *For whom*; **kill** → `stage: killed`, the idea card's verdict updated; **not yet** → nothing moves, *Now* lists the evidence to get.
5. **Compress** (on go at G4 and later, ask first) — working files of the finished stages (`research/` findings, interview notes) → `.ai/archive/product-<stage>/`; `research/summary.md`, `gates/` and the decision records stay.
6. Reply ≤6 lines: the decision, what moved, the next command from `templates/stages.md` §Who runs a stage.
