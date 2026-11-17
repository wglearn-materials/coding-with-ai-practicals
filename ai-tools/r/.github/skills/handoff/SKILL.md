---
name: handoff
description: Save a short evidence-based session handoff for a fresh research chat. Use when asked to save a handoff.
---
1. Read analysis_plan.md, the chosen greeting, relevant rules/agent files and actual
   check evidence. Read [the handoff template](./handoff-template.md).
2. Propose outputs/SESSION_NOTES.md, following the existing generated-note rule.
   Check whether it exists before writing. If absent, ask approval to create it.
   If it exists, preserve it and ask for a fresh filename under outputs/.
   Check the chosen path is absent before asking approval to create it.
   Never overwrite an existing note, even with approval. Keep the project rule unchanged.
3. After approval, create the new note from the template with concise actual state,
   evidence, checks not run and one next action. Distinguish expected from observed
   results. No chat dump, secrets, private inputs or invented execution. If evidence
   is missing, say NOT RUN.
4. Show the actual saved path and ask approval to append its path and brief status to
   the existing analysis_plan.md, preserving earlier text. outputs/ is ignored in the
   prepared workspace: keep the note local, do not stage or force-add it or change ignores.
5. Tell the user to start a fresh chat and explicitly read that actual note path,
   the same plan and relevant greeting/configuration. Filesystem memory is not
   guaranteed to load automatically. This skill does not grant tools or run commands.
