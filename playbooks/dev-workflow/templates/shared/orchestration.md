# Orchestration rules
<!-- Source of truth: shared/orchestration.md in the agent-playbook repo. scripts/sync_shared.py copies it into each plugin's templates/shared/ — edit the source, never the copy. -->

For every orchestrator skill — a workflow run in the main session, because it needs the user at the gates. The skill names its stage agents, its **state file** (where the current stage is saved) and its **decisions file** (where answers are recorded). In `dev` workflows: state = `task.md` Now, decisions = `spec.md §Decisions`, open questions = `task.md §Open questions`.

- You orchestrate; you do not do a stage's work yourself. Each stage runs in a subagent with its own model and context; you read only its STATUS block and the state file. That keeps this session small.
- Agents are plugin-scoped (`<plugin>:<agent>`). Run them in the foreground (wait for the result).
- **Reuse** (this session only — agents don't survive it): continue an agent with SendMessage for follow-ups on its own work — after the user's answers or edits at a gate, for fix rounds of its own phase, for a follow-up on its own research topic. Always fresh: reviewing and verifying agents (independence), a new stage, a new session, an agent whose picture of the work is stale (code or files changed since it ran). Answers still go to the files first. SendMessage unavailable → fresh agent.
- Each prompt contains: absolute work folder path (in `dev`: the task folder), its key, the exact job for this stage, constraints (phase/steps, findings to fix, answers to questions). Never paste file contents — agents read files.
- After every stage update the state file (`stage: N`, status, Next) so a crash or a new session resumes at the right stage.
- **Questions from agents** (any stage):
  - `[blocking]` → gate now: ask the user (AskUserQuestion when available: options + the agent's recommendation first), never guess.
  - `[assumed: …]` → don't stop; list them at the next gate for a quick confirm/override.
  - Record every answer in the decisions file (decision · why · "user, YYYY-MM-DD") **before** rerunning or continuing the stage — a fresh agent learns it from the file, not from you. Also tick the question off where open questions are listed.
  - Rerun only the stage that asked, with "answers recorded in <decisions file> D…" in the prompt. An overridden assumption in an earlier stage → rerun from that stage.
  - The answer must come from someone else (client, HR, another team) → draft the message, then pause the work with that as the unblock condition (in `dev`: `/dev:pause-task`; `/dev:start-task` continues at the saved stage).
- **Gates**: blocking questions and anything external (push, PR, tracker or chat posts, publishing, deploy, spending money) are never skipped; external actions only on explicit OK.
- Same stage fails twice → stop and hand the problem to the user.
- CAPTURED `proposed:` items → `/kb:capture` them.
- At the end: one line listing agents run and rounds per stage.
- Resume: the state file says `workflow: <name> · stage: N` → continue from N.
