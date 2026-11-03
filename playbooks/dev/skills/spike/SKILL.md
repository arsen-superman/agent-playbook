---
name: spike
description: Run a time-boxed spike (technical or product investigation) in one session — frame the question, fan out parallel researcher subagents, synthesise a recommendation, record the decision. Use when the user runs /dev:spike or asks to investigate options before committing to a solution.
argument-hint: "<question | JIRA-KEY> [timebox]"
disable-model-invocation: true
---
# Spike workflow — orchestrator

You orchestrate; research runs in `dev:researcher` subagents. Follow the **Orchestration rules** of `/dev:feature`, with `workflow: spike`.

## Stages
0. **Frame** (you) — task via `/dev:new-task` with `type: research`. In `spec.md` write: the question, the decision it unblocks, success criteria, timebox (default: this session), and 2-5 independent sub-questions (e.g. per option, per constraint: performance / cost / effort / risk / fit with current code).
   **GATE A** — confirm framing and sub-questions.
1. **Research** → one `dev:researcher` per sub-question, **in parallel** (all Agent calls in one message). Each prompt: task folder, its sub-question, its topic file name `research/<slug>.md`, a scratch folder for prototypes, turn budget.
2. **Synthesise** (you) — from the SUMMARY blocks (open a topic file only where answers conflict) write `research/spike-summary.md`: answer, options table (option · pros · cons · effort · risk), recommendation, confidence, what would change it.
3. **Gaps** — a critical sub-question with low confidence → one follow-up researcher round (max 1), then synthesise again.
4. **Decide** — **GATE B**: present the recommendation in ≤10 lines. On OK: decision record in `.ai/decisions/` (alternatives rejected + why), follow-up tasks or `/kb:capture` items, ticket drafts (create only on OK).
5. **Close** — `/dev:close-task` (spikes are short-lived; the decision and context outlive them).
