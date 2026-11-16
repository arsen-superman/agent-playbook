---
name: validate
description: "Plan and record validation — the riskiest hypotheses, the cheapest test for each, a threshold named before the test, budget and stop rule; later record results against the thresholds. Manual: /product:validate [results]."
argument-hint: "[results]"
disable-model-invocation: true
---
# Validation

Run in the main session with the user — it is a negotiation about what counts as proof. Files: `.ai/product/hypotheses.md` (`templates/hypotheses.md` in this plugin), `product.md`, `research/summary.md`.
The rule that makes validation worth anything: **the threshold is written before the test and never moved after it.**

## Plan (no argument)
1. Read `product.md` (type, limits), `research/summary.md`, `hypotheses.md`.
2. Rank hypotheses by *risk if wrong*. Take the top 3–5; the rest wait.
3. **Goods: unit economics first.** Fill the table in `hypotheses.md` for a pessimistic and a realistic scenario: price − landed cost − marketplace or payment fees − delivery − returns − ad cost per sale. Margin negative in the realistic scenario → stop and say so: no test that spends money until the numbers change. Inputs without a source → ask for them or mark the row as an assumption.
4. For each hypothesis propose the cheapest test that could refute it, your recommendation first:
   - **software** — landing page with a waitlist or pre-sale and capped paid traffic · 5–10 problem interviews (write the script to `research/interview-script.md`: past behaviour, not opinions) · a fake door · doing the service by hand for 3 customers;
   - **channel** — a two-week pilot (a set number of posts, organic plus a small paid push): cost per subscriber, 7-day retention, views per post;
   - **goods** — test ads to a landing page or a listing with pre-order or "notify me": cost per click, cost per order intent; a tiny purchase only after the ad test.
   Each test gets: threshold (number · period), budget and duration within `product.md` Limits, stop rule.
5. **GATE** — show the plan as a table. The user confirms thresholds and budgets; anything that spends money or publishes needs an explicit OK.
6. Record: rows in `hypotheses.md` → 🧪. A test that must be built (landing, pilot bot) → `/dev:new-task` with `source:` = `../../product/hypotheses.md`; with the growth playbook installed → `/growth:landing`. `product.md` §Now: what is running, when results are due.

## Results (`results`)
1. The user gives the numbers or notes; long material and exports → `/kb:ingest` first. Interviews → one line per conversation in `research/interviews.md`: who, what they do today, what they paid or tried, the quote that matters.
2. Fill *Result* and *Evidence*; set ✅ or ❌ strictly against the written threshold. Close to the line is ❌ with a note, not ✅.
3. Refuted → one line under *Refuted and what we learned*, and 2–3 pivot options (other segment, other promise, other price) for the user — don't pick one.
4. Every top hypothesis resolved → `product.md` §Now: Next = `/product:gate G3`. Reply ≤8 lines: the table of results, what it means, next step.
