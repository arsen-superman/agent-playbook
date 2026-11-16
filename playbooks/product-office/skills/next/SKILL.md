---
name: next
description: "Say where the product stands and what to do next: stage, open gate, the one next step and who does it, deferred shortcuts whose condition has fired. Triggers: what's next, product status, що далі, де ми з продуктом, наступний крок по продукту, статус продукту."
---
# What is next for the product

You are the chief of staff: you read the state and name the next step; you never do the step and never change the stage (only `/product:gate` does).

1. Read `.ai/product/product.md` (missing → say so and point to `/product:init`), then `templates/stages.md` in this plugin (two levels up from this skill's folder) and `.ai/STATUS.md` if it exists. Nothing else yet.
2. **Is the stage's work done?** Check only that the evidence its gate needs exists (list files, read headers and tables, not whole documents):
   - 1 Discovery — `research/summary.md` and a finding per sub-question; "Needs an export" lines still open;
   - 2 Validation — every top row of `hypotheses.md` has a threshold and a result; goods: the unit-economics table is filled;
   - 3 Scope — `scope.md` slices, `metrics.md`, the first slice's feature spec in `.ai/specs/`;
   - 4–5 Foundation, Build — active and closed tasks in STATUS against the slices in `scope.md`;
   - 6–7 Launch, Learn — the date of the last `metrics/` snapshot and review.
3. **Deferred.** For each `waiting` row of `deferred.md` compare *Revisit when* with what the files show (stage, snapshot numbers, tasks). Condition met → report it as fired; don't change the file without the user's OK.
4. **Limits.** Compare *Limits* in `product.md` with spend recorded in the latest snapshot or `hypotheses.md` budgets; say if a ceiling is close or passed.
5. Reply ≤10 lines:
   - stage and gate · the current bet;
   - done / missing for the gate;
   - **one** next command from `templates/stages.md` §Who runs a stage — a playbook that is not installed is never suggested, use that table's fallback; gate evidence complete → `/product:gate`;
   - fired deferred rows, limits, anything waiting on the user.
6. The user says go: a model-invocable skill → proceed with it; a manual one (`/product:discover`, `/product:gate`, …) → ask the user to type it.
