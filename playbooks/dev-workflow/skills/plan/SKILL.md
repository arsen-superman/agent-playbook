---
name: plan
description: Turn an approved spec into plan.md — phased, commit-sized, verifiable steps. Use when the spec has no blocking questions and the user asks for a plan or approach.
argument-hint: "[task-key]"
---
# Write the plan

Templates: `templates/doc/plan.md`, checklist `templates/checklists/risk-classes.md` in this plugin.

1. Read `task.md`, `spec.md`, and `<repo>/REVIEW.md` + `<repo>/CLAUDE.md` for each repo in `repos:` (team conventions shape the design). Blocking open questions → list them and stop.
2. **Scout before designing** — `dev:scout` in parallel, one question each: existing services, helpers, endpoints or permission checks that already do part of this (reuse them, never re-implement); size and responsibilities of each class you would change; callers and how often the touched code runs (app start, every page, per item); every endpoint/DTO returning the entities you change; the closest existing feature of the same kind and its layers/files.
3. **Approach** (≤10 lines): what changes, what deliberately doesn't, why; follow the closest feature's pattern and say why where you deviate. ASCII diagram welcome. A real choice between approaches → **Options** above it: 2–3 lines `option · trade-off · effort`, your pick marked; the rejected ones → `spec.md §Rejected` once approved. **Placement** (≤5 lines): where new code lives and how each touched class grows; past ~300 lines or a second responsibility → a new service, per repo convention.
4. **Cross-cutting** — walk risk classes 1, 3–15: each that applies → one row `class · how this change meets it · step N or D#`. Skip ones that don't apply.
5. **Phases**: Phase 0 for changes to existing logic = pin current behaviour (characterisation test / reproduction that must fail once the fix lands). Last phase = verify every AC + regression.
6. **Test design first** — write `test-cases.md` (`templates/doc/test-cases.md`): at least one case per AC, plus negatives, spec edge cases and "unaffected users" regression; a permission matrix in spec → a case per distinct outcome; batch rules → a case where items break the rule only together. Choose the lowest level that proves the behaviour (unit → integration → e2e); `manual` only for what can't be automated here (UI without e2e framework, external systems). Use the repo's existing test frameworks — new ones only with the user's OK.
7. Each step: `- [ ] <one commit-sized action, naming files and repo> — verify: <command or observable check>`. Steps that add tests name the TC IDs they automate.
8. **Follow-ups** — deliberately not done here; each also `/kb:capture`.
9. **Risks** ≤5 bullets, each closed: `→ step N` that removes or detects it, or `→ accept?` (a question for the approval gate; the answer goes to spec §Decisions). Every user decision in spec §Decisions that restricts behaviour → a plan step or an explicit `accepted: <consequence>` risk. Set `**Next:**` at the top.
**Amend mode** (prompt says amend): never rewrite done phases or renumber TCs. Covered + tested items → add/adjust the TC with `Automated by` = the existing test; others → new TCs and steps in one phase `## Phase N — Amend YYYY-MM-DD`, placed before the final Verify phase.

10. Ask for approval — show Options (if any), Approach, Placement, Cross-cutting and every `accept?` risk. On OK: `status: planned`, Next = first step.
