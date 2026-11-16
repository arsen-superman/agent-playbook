---
name: review
description: "Weekly product review after launch — read the metrics snapshot, feedback and what shipped, judge the last bets, propose 1-3 bets for the next cycle; the user picks. Manual: /product:review."
argument-hint: "[period]"
disable-model-invocation: true
---
# Product review — orchestrator

Numbers are read by `product:metrics-analyst`, bets are proposed by `product:strategist`, the user chooses. Follow `templates/shared/orchestration.md` in this plugin (two levels up from this skill's folder; read it first), with `workflow: review`. State file = `.ai/product/product.md` §Now; decisions file = `product.md §Answers and assumptions`. Definitions: `.ai/product/metrics.md` (`templates/metrics.md` in this plugin).

## Stages
0. **Snapshot** — the newest `.ai/product/metrics/YYYY-Www.md`. None for this period → ask the user for the numbers (an export, a pasted table, a screenshot's figures); exports go through `/kb:ingest`; write the snapshot yourself in the format from `metrics.md` (≤40 lines), marking every number's origin and what is missing. No numbers at all → run the review on feedback and shipped work only and say so.
1. **Read the numbers** → `product:metrics-analyst`: this period's and the previous snapshots only. It writes `metrics/review-YYYY-Www.md` (≤40 lines): north star and guardrails against the previous period, the funnel step that loses most, what changed after last cycle's bets, what the data cannot tell.
2. **Gather** (you, counts and titles only) — inbox items with `area: product` and type `bug` / `finding` / `idea` since the last review; tasks closed since then (STATUS); `deferred.md` rows whose condition fired; a channel review if `.ai/growth/` has one for the period.
3. **Bets** → `product:strategist`: "review bets" with the paths from 1–2. It judges each bet of the last cycle (kept its promise or not, by the number named then) and proposes 1–3 bets: bet · the metric it should move and by how much · cost in hours and money · how we will know. Within `product.md` Limits.
4. **GATE** — show the review in ≤12 lines and the bets as a table. The user picks, edits or says "nothing new, keep going".
5. **Record** — `product.md` *Current bet* (with its number and date to check); new hypotheses → `hypotheses.md`; work → `/dev:requirements` for a new feature or `/dev:new-task` for a slice; fired deferred rows → `scheduled → task` or back to `waiting` with a new condition.
6. **G7** — north star flat or falling for three reviews in a row, limits exhausted, or the user asks → Next = `/product:gate G7`.
7. Reply ≤6 lines: the bet chosen, tasks created, the date of the next review.
