---
name: scope
description: "Cut the MVP — what it must prove, thin end-to-end slices, metrics, price hypothesis, and everything else into the deferred register; create the first tasks. Manual: /product:scope."
argument-hint: ""
disable-model-invocation: true
---
# MVP scope — orchestrator

The draft is written by `product:strategist`; you run the gates and create tasks. Follow `templates/shared/orchestration.md` in this plugin (two levels up from this skill's folder; read it first), with `workflow: scope`. State file = `.ai/product/product.md` §Now; decisions file = `product.md §Answers and assumptions`. Templates: `templates/scope.md`, `templates/metrics.md`, `templates/deferred.md` in this plugin.

## Stages
0. **Check** — `hypotheses.md` has confirmed rows and G3 is passed (`product.md` Decided so far). Not yet → say what is missing; continue only on the user's explicit OK.
1. **Draft** → `product:strategist`: "MVP scope". It writes:
   - `scope.md` — what the MVP must prove (one sentence, one number); slices, thin and end-to-end, the first usable alone; goods: the test batch (quantity, landed cost, 2–3 channels, budget cap, stop rule, dates); channel: format, cadence, bot scenarios;
   - `metrics.md` — north star, funnel, 3–5 events, guardrails;
   - `deferred.md` — one row for everything cut: why it is safe now, the condition that brings it back;
   - the price hypothesis as a row in `hypotheses.md`.
   Its rule for cutting: a slice stays only if the MVP cannot prove its sentence without it. Never cut: backups, secrets outside the repo, sign-in through a ready-made service, event analytics, the legal minimum for collecting data and taking payments.
2. **GATE B** — show the sentence, the slices in order, what was deferred and the metrics. The user reorders, cuts or adds; edits go back to the same strategist (Reuse).
3. **Specify the first slice** — business rules belong in a feature spec: ask the user to run `/dev:requirements "<slice>"` (it writes `.ai/specs/<feature>.md`), or run it now if the user says go. Later slices are specified when their turn comes — not the whole backlog up front.
4. **Tasks** — on OK create tasks for the first slice only with `/dev:new-task` (`source:` = its feature spec, else `../../product/scope.md`); put the keys into the Task column of `scope.md`.
5. **Finish** — `product.md` §Now: Next = `/product:gate G4`. Reply ≤8 lines: the sentence, slice count, deferred count, first tasks.

After G4 the scope changes only through `/product:review` (a new bet) — not by adding slices on the way.
