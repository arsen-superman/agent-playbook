---
name: research
description: Investigate a question (code behaviour, data, technology choice, market, competitors) and produce a conclusion with evidence and confidence. Use for investigate, find out, why does, compare, is it true that, market or competitor research.
argument-hint: "<question> [task-key]"
---
# Research

Template: `templates/doc/research.md` in this plugin.

1. **Frame** — `research/<kebab-topic>.md` inside the task (or `.ai/context/` research for project-wide questions): question, what decision it unblocks, what "answered" means. First grep `.ai/decisions/`, `.ai/context/`, existing research.
2. **Gather** — subagents in parallel for broad sweeps, one focused question each, asking for conclusions with evidence. Web → cite URLs. Data → read-only queries; query + output to `research/raw/<topic>-<n>.txt`.
3. **Conclude** — Answer first, Evidence (`file:line`, link, raw file), Confidence and what would change it, Implications.
4. **Overturned** → rewrite the doc to the new truth; the old conclusion becomes one line under *Rejected hypotheses* with the reason. Never `-v2` files or chronological series.
5. Settles a choice → propose a decision (spec §Decisions or `.ai/decisions/`).
6. Reply ≤6 lines: answer, confidence, what it unblocks.
