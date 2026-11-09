---
name: new-task
description: Create a task folder for a Jira ticket or ad-hoc work (feature, bug, research, chore), or link a ticket to a LOCAL task. Triggers: a ticket key or URL, new task, нова задача, work with no ticket yet.
argument-hint: "<JIRA-KEY | short description> [from LOCAL-n]"
---
# Create a task

Templates: `templates/doc/` in this plugin (two levels up from this skill's folder).

1. Key: Jira key/URL → fetch the issue with the Atlassian connector (summary, description, type, priority, epic, links, comments that add requirements). No key → `LOCAL-<n>` (next free number).
2. Folder `.ai/tasks/<KEY>-<3-5-word-kebab-slug>/`. Stop if the key already exists.
3. `task.md` from `templates/doc/task.md`: frontmatter, Goal (your 2-line paraphrase), `repos:` (which repos are likely touched), `status: spec`, Next = `/dev:spec` (bug → `/dev:fix-bug`, research → `/dev:research`).
4. `spec.md` from `templates/doc/spec.md` with only **Raw requirement** (verbatim) and links. No analysis yet.
5. Branch name per the project CLAUDE.md convention → `branch:`. Don't create the branch. Same repo already busy with another active task → suggest a worktree at `worktrees/<repo>--<KEY>/` (KB rules).
6. Add a row to `.ai/STATUS.md` → Active (Repos = `repos:` from task.md).
7. Reply: folder, goal in 2 lines, next command.

## No ticket yet → LOCAL task
Works exactly like a ticket task (spec, plan, workflows, park, close) with key `LOCAL-<n>` and `jira:` empty. Branch: `feature/LOCAL-<n>-<slug>` until a ticket exists.

## LOCAL task gets a ticket (`<JIRA-KEY> from LOCAL-n`)
1. Fetch the issue; merge anything new into `spec.md §Raw requirement` (keep the original text too).
2. Rename the folder to `<JIRA-KEY>-<slug>`, set `id:` and `jira:`, fix links in `STATUS.md` and other tasks.
3. Branch already exists → suggest the rename command (`git branch -m`), don't run it without OK.
4. Want a ticket created from the LOCAL task instead → draft it (summary, type, description from Goal + spec) and create it in Jira only after explicit OK, then continue with steps 1-3.

