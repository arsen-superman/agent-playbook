---
name: init
description: "Start a product in a project folder — create .ai/product/ from an idea, set its type, stage and limits. Manual: /product:init idea or description."
argument-hint: "<idea name | description>"
disable-model-invocation: true
---
# Start a product

Templates: `templates/` in this plugin (two levels up from this skill's folder). Stages and gates: `templates/stages.md`.
A product = a project folder whose `.ai/` has a `product/` folder. One product per project folder.

1. **Project KB first.** No `.ai/` in the current project folder → stop: "run `/dev:init-project` first — answer *no code yet* and profile `product`; it also works with no repositories". `.ai/product/product.md` already exists → stop and point to `/product:next`.
2. **The idea.** Argument → find it in this project's `.ai/ideas/`, then in the personal vault's `_ideas/` (a card or a folder with material; vault path: `Personal vault:` in `~/.claude/CLAUDE.md`). Not found → take the description the user gives. An idea card still `status: raw` → say that G1 is its `/kb:brainstorm` verdict and offer to run it first; continue only on the user's OK.
3. **Ask one batch**, only what the idea does not already answer:
   - type — `software` (an app with its own interface), `channel` (channels, bots: the interface is someone else's platform), `goods` (a physical product to sell);
   - who it is for and what hurts them today;
   - limits — money per month (infrastructure; ads or purchases), hours per week, markets and language;
   - anything already decided (name, stack, supplier, platform).
4. **Create** `.ai/product/`:
   - `product.md` from `templates/product.md` — `type`, `stage: 1`, `gate: G2`, One line, For whom, Limits, Current bet = "find out whether <segment> has <pain> badly enough to pay", Decided so far = `G1 <date> go — <idea verdict> — <link to the idea>`;
   - `hypotheses.md` from `templates/hypotheses.md`, seeded with what the idea assumes; `.ai/assumptions.md` exists (a discovery-phase project) → move its rows in and delete that file on OK;
   - `deferred.md` from `templates/deferred.md` (empty table);
   - folders `research/`, `gates/`, `metrics/`.
5. **Idea material.** A vault idea folder → copy its files: sources and exports verbatim into `.ai/raw/`, notes and sketches into `.ai/product/research/`. The card stays in the vault: set `status: promoted`, `promoted-to: <project folder>`. A project idea → the same two fields, the file stays.
6. **Project settings** — lines in the project `CLAUDE.md`, outside the managed block; show the diff and write on OK, never overwrite a value the user set: `- Profile: product`, `- Tracker: none`, `- Delivery: self-merge`.
7. Reply ≤8 lines: what was created, the limits recorded, and the next step — `/product:discover`.

Never start research, validation or code here.
