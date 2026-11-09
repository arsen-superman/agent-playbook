---
name: feature-workflow
description: Run a whole feature in one session — orchestrate analyst, planner, implementer, reviewer and verifier subagents with human approval gates. Use when the user runs /dev:feature-workflow or asks to run the feature workflow end to end.
argument-hint: "<JIRA-KEY | task-key | description> [auto]"
disable-model-invocation: true
---
# Feature workflow — orchestrator

You orchestrate; you do not analyse, plan, code or test yourself. Each stage runs in a subagent with its own model and context; you read only its STATUS block and `task.md`. That keeps this session small. Shared rules: **Orchestration rules** below.

## Stages
0. **Task** — existing task folder, or `/dev:new-task` (fetches Jira). Set `task.md` Now: `workflow: feature · stage: 1`.
1. **Spec** → `dev:analyst`. **GATE A** — show SUMMARY + QUESTIONS. Answers → continue the same analyst (**Reuse**), else a fresh one (or apply small edits to spec.md yourself). Continue only when no blocking question remains.
2. **Plan** → `dev:planner`. **GATE B** — show approach, phases, risks; user approves or edits.
3. **Implement** → `dev:implementer`, one phase per call, in order. Two phases in different repos marked independent in the plan may run in parallel. After each phase: one progress line to the user. Blocked → gate with the problem.
4. **Review** → `dev:reviewer`. Blocker/major findings → the phase's implementer (**Reuse**) with the findings as steps, then review again — only the fix commits, with the findings listed, model override `sonnet`. Max 2 rounds, then gate.
5. **Verify** → `dev:verifier`. Write its results into `test-cases.md` (Status column + a Runs line; add accepted proposed TCs) and a 3-line verdict into `task.md §Verification`. Cases left `⏳ for QA` → offer the QA handoff (`/dev:verify` step 7) at GATE C. Fail → fix round via implementer (max 2), then gate.
6. **Finish** — `status: review`, PR description draft (What / Why / How tested / Risks / ticket). **GATE C** — push / PR / Jira comment only on explicit OK. Next = "comments → `/dev:pr-comments`; new requirements → `/dev:amend`; merged → `/dev:close-task`". Then `/dev:handoff`.

`auto`: skip GATE B when the planner reports ≤3 phases and no high risk. GATE A and GATE C are never skipped.

## Orchestration rules
- Agents are plugin-scoped: `dev:analyst`, `dev:planner`, `dev:implementer`, `dev:reviewer`, `dev:verifier`. Run them in the foreground (wait for the result).
- **Reuse** (this session only — agents don't survive it): continue an agent with SendMessage for follow-ups on its own work — analyst after GATE A answers, planner after GATE B edits, implementer for review/verify fix rounds of its phase, researcher for a follow-up on its topic. Always fresh: reviewer and verifier (independence), a new stage, a new session, an agent whose picture of the code is stale (code changed since it ran — e.g. a later `/dev:amend`: the fresh analyst reads the compiled AS-IS in spec.md and scouts only the delta). Answers still go to the files first. SendMessage unavailable → fresh agent.
- Each prompt contains: absolute task folder path, task key, the exact job for this stage, constraints (phase/steps, findings to fix, answers to questions). Never paste file contents — agents read files.
- After every stage update `task.md` Now (`stage: N`, status, Next) so a crash or `/dev:start` resumes at the right stage.
- **Questions from agents** (any stage):
  - `[blocking]` → gate now: ask the user (AskUserQuestion when available: options + the agent's recommendation first), never guess.
  - `[assumed: …]` → don't stop; list them at the next gate for a quick confirm/override.
  - Record every answer in `spec.md §Decisions` (decision · why · "user, YYYY-MM-DD") **before** rerunning or continuing the stage — a fresh agent learns it from the file, not from you. Also tick the question off in `task.md §Open questions`.
  - Rerun only the stage that asked, with "answers recorded in spec §Decisions D…" in the prompt. An overridden assumption in an earlier stage → rerun from that stage.
  - The answer must come from someone else (client, HR, another team) → draft the message, then `/dev:park` with that as the unblock condition. `/dev:resume` continues at the saved stage.
- New requirements or clarifications after stage 1 (not answers to agent questions) → `/dev:amend`.
- Same stage fails twice → stop and hand the problem to the user.
- CAPTURED `proposed:` items → `/kb:capture` them.
- At the end: one line listing agents run and rounds per stage.
- Resume: `task.md` says `workflow: feature · stage: N` → continue from N.
