---
name: brainstorm
description: Think an idea through with the user — goal, options, risks, the cheapest test — then record its status, verdict and next step in the idea file, and optionally promote it to a task or project. Use when the user says brainstorm, let's think about an idea, обміркуймо ідею, подумаймо над ідеєю, розбери ідею, or names an idea from ideas/.
argument-hint: "[idea]"
---
# Brainstorm an idea

**Locate the KB root:** the nearest `.ai/` folder from the current directory upward (a project knowledge base); if there is none, the personal vault from `~/.claude/CLAUDE.md` (`Personal vault:` line); no file system (claude.ai) → Drive mode; none of these → ask. Work in that one KB only — never list or mix ideas from other KBs. Vault service folders carry a `_` prefix: there `inbox/`, `ideas/`, `raw/`, `stash/` below mean `_inbox/`, `_ideas/`, `_raw/`, `_stash/`.

**Drive mode:** Google Drive connector, folder `Vault` (or the `Personal vault (Drive):` name); search by title and full text. Create files with `contentMimeType: text/markdown` and `disableConversionToGoogleType: true` — never Google Docs. To change a file, create the new version with the same title in the same folder, then trash the old one.

Idea file format: `templates/idea.md` in this plugin.

1. **Pick.** Argument → match it in `<kb>/ideas/` (file name, title, tags; an idea card is `ideas/<slug>.md` or, in the vault, `_ideas/<slug>/<slug>.md`); several matches → ask. Not there → offer to capture it as an idea first (`/kb:capture`). No argument → list the idea cards as a table: title · status · verdict · updated — `raw` first, then `explored`, oldest first; leave out `promoted` and `dropped`. Ask which one to take.
2. **Read** the idea. In a project KB, read only what the options need (`context/`, `decisions/`, code — through `dev:scout` if available).
3. **Brainstorm** with the user, a few questions at a time, not a questionnaire:
   - the goal, who benefits, what "done" looks like;
   - 2–4 options including the simplest one and "do nothing", with pros and cons;
   - risks, unknowns, dependencies; what would make it a no;
   - the cheapest test that teaches the most.
   Give your own view and recommendation; push back on weak points.
4. **Record.** Show the proposed Verdict section and frontmatter; on OK rewrite the file in current-truth form: `## Idea` untouched; `## Why / context`, `## Brainstorm` (≤40 lines) and `## Verdict` rewritten; frontmatter `status` (`explored`, or `shelved` / `dropped` if the user decides so), `verdict` with reason, `value`, `effort`, `next`, `updated`.
   **Vault: material that outgrows the card** (research, competitors, MVP scope, sketches) → the idea becomes a folder: move the card to `_ideas/<slug>/<slug>.md` (Obsidian CLI `move` when available) and put each piece of material beside it as its own file, linked from the card. The card stays ≤80 lines.
5. **Next.** Offer: promote — project KB → `/dev:new-task` from the idea; vault → a new project folder (`/dev:init-project`; the idea folder's material moves into its `.ai/`, the card stays in the vault) or a vault note — then set `status: promoted` and `promoted-to:` with the link; or keep it `explored`; or shelve. Never promote without an explicit OK.
6. Reply in ≤5 lines: verdict, next step, file path.
