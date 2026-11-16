---
name: discover
description: "Product discovery in one session — frame the questions, run parallel product researchers (market, competitors, segment, demand), synthesise with the strategist, prepare gate G2. Manual: /product:discover [focus]."
argument-hint: "[focus or extra question]"
disable-model-invocation: true
---
# Discovery — orchestrator

You orchestrate; research runs in `product:researcher` subagents, synthesis in `product:strategist`. Follow `templates/shared/orchestration.md` in this plugin (two levels up from this skill's folder; read it first), with `workflow: discover`. In this plugin: state file = `.ai/product/product.md` §Now; decisions file = `product.md §Answers and assumptions`; work folder = `.ai/product/`.
This is product research — market, people, demand. A technical question (framework, performance, security) is `/dev:spike-workflow`.

## Stages
0. **Frame** (you) — read `product.md` and `hypotheses.md`. Take the sub-questions for the product's `type` below, drop what the idea material already answers with a source, add the user's focus. 3–5 questions, each independent.
   **GATE A** — confirm the questions and where the numbers will come from.
1. **Research** → one `product:researcher` per sub-question, **in parallel** (all Agent calls in one message). Each prompt: the absolute path of `.ai/product/`, its one question, its file `research/<slug>.md`, the markets and language from `product.md`, the list of raw files in `.ai/raw/` it may read.
2. **Synthesise** → `product:strategist`: "discovery synthesis" — writes `research/summary.md` (the answer to G2's question, the narrowest segment to start with, 2–3 options with trade-offs, confidence, what would change it) and adds or rewrites rows in `hypotheses.md` (riskiest first).
3. **Gaps** — a sub-question critical for G2 came back with low confidence or open "Needs an export" lines → show the user exactly which export is needed (tool, query); with the export saved through `/kb:ingest`, one follow-up researcher round (max 1), then synthesise again.
4. **Finish** — `product.md` §Now: Next = `/product:gate G2`. Reply ≤8 lines: the answer, confidence, top 3 hypotheses, what is still missing.

## Sub-questions by type
- **software** — market: who has the pain, how many, how they solve it today, what they pay for that · competitors: 5–8 direct and indirect, prices, positioning, what their users complain about · segment: the narrowest group to start with and where it gathers · channels: how products like this got their first 100 users, cost signals · risks: legal, platform dependence, why similar products failed.
- **channel** — niche: search and trend signals for the topic · competing channels: size, growth, cadence, engagement, what they don't cover · audience: who reads, where they come from · monetisation: models used in the niche and typical rates · platform rules and what gets channels restricted.
- **goods** — demand: search volume, trend, seasonality · competition: number of sellers, price range, how the leaders differ, review complaints · supply: suppliers, minimum order, landed cost · selling costs: marketplace fees, delivery, typical return rate · regulation: certification, customs, restricted categories.

## Numbers from tools
Search volumes, marketplace sales and ad costs live in tools behind a login (keyword planners, trends, marketplace analytics). The user exports them; `/kb:ingest` saves the export to `.ai/raw/`; researchers read it from there. A number nobody exported is reported as "needs an export", never estimated.
