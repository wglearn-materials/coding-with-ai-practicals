# Module 7 Python reference

Supplied starting examples, not evidence of a live AI run. Use the same prepared
/workspace/work, hello_copilot.py with Module 6's Noor addition, and analysis_plan.md.
No clone, installation, new analysis or original-exercise change is needed.

## Create and check

In VS Code Explorer, create missing folders with New Folder, then New File in the
destination folder. Read each example before pasting and saving it. Inspect and
merge existing files manually; never overwrite them blindly. Paths below are
relative to /workspace/work, not this gallery's directory. Do not copy this README
into the project just to complete the exercise.

| Destination | Trigger and check |
| --- | --- |
| .github/copilot-instructions.md | Fresh chat: request customisation-note.md without repeating the output rule. Inspect outputs/customisation-note.md; an existing note must not be replaced. |
| .github/instructions/greeting.instructions.md | Attach hello_copilot.py and request a proposed comment, no edit. Compare inclusion with a fresh chat about README.md or analysis_plan.md, which do not match applyTo. |
| .github/prompts/explain-file.prompt.md | Legacy Local only: select explain-file from Prompts in the slash menu, with the greeting attached. If absent, mark unavailable; do not install an older runtime. |
| .github/skills/explain-file/SKILL.md | Core Copilot: select explain-file from Skills in the slash menu, or ask to use the explain-file skill. Expect three explanation bullets, no edits or execution. |
| .github/skills/check-output/SKILL.md | Invoke check-output manually with the greeting attached. Inspect resource reads; approve only python3 hello_copilot.py from /workspace/work after reviewing the script. |
| .github/skills/check-output/expected-output.txt | Keep beside SKILL.md. Compare actual exit status and all five output lines; do not change the fixture to force PASS. |

Run Chat: Open Customizations and inspect Instructions / Skills for discovery.
Check References or Agent Debug Logs for inclusion. Inspect actual files and tool
activity for behavior. A file listing is not proof of inclusion or compliance.
The session environment loads these files; selecting a model does not switch it.
AGENTS.md is an alternative project-rules format, not a second required copy.
Instructions do not govern inline autocomplete or enforce tool permissions.
Use actual read-only controls for explanation requests, and execution approvals
for checks; do not enable auto-approval or share research records or secrets.

## Repeat and carry forward

The check skill reports PASS only for actual exit 0 and the five expected lines,
FAIL for a failed run or mismatch, and NOT RUN without complete execution evidence.
Append this one line to its SKILL.md, save, and repeat the same manual invocation
in a fresh chat: "End the report with one short Next step bullet based on the
observed status." Approve only the same command; inspect the added bullet, not
identical model wording. Test automatic selection separately without naming the
skill; selection is not guaranteed.

Append brief actual results or explicit gaps to the existing analysis_plan.md.
Reference-only or partial Module 6 work is not live Module 7 completion. Preserve
the greeting; review a local checkpoint of only these six configuration/resource
files and the plan. Keep the generated note local under ignored outputs/ and
record its actual path and observed result in the plan. Do not stage the note,
force-add files or change ignore rules. Check already staged changes first.
Use Module 5's individual-file staging procedure; no push or publication.
Module 8 at ../../../modules/05-multi-agent.html will reuse the toolkit and plan
for the research team and context handoff. Do not create agent files yet.

Official guidance checked 2026-11-17:
- https://code.visualstudio.com/docs/agent-customization/custom-instructions
- https://code.visualstudio.com/docs/agent-customization/prompt-files
- https://code.visualstudio.com/docs/agent-customization/agent-skills

## Module 8: Research team and context

The earlier "Do not create agent files yet" applies to Module 7 only. In Module 8,
reuse this greeting, the same analysis_plan.md and the six core files above.
Create only missing files; read and merge existing files manually, never blindly
replace .github. No new clone, installation, pipeline or student-written tests.

Add .github/agents/research-orchestrator.agent.md, analysis-agent.agent.md and
reproducibility-reviewer.agent.md in that agents folder. First discover Reviewer
with user-invocable temporarily true; do not change its tools for picker visibility.
Save its final false again. Research Orchestrator is the only team picker entry;
both workers are hidden but model-invocable. Inspect actual supported tool aliases,
named worker activity and permissions in your installed harness; model choice does
not select the harness. If unsupported, mark NOT RUN; do not simulate delegation.

Follow the lesson's exact prompts: Analysis Agent adds only the supplied comment
above the existing greeting function. Inspect the actual diff. Reviewer reads it,
then uses the existing check-output skill after your approval for exactly
python3 hello_copilot.py from /workspace/work. PASS needs accepted diff scope,
actual exit 0 and all five fixture lines without extras; capture full stdout.
FAIL / NOT RUN are not completion. No executable code or fixture changes.

Create .github/skills/handoff/SKILL.md and handoff-template.md beside it.
Invoke handoff in the main chat. It checks outputs/SESSION_NOTES.md before writing:
create only if absent and approved. If it exists, preserve it and ask for a fresh
filename under outputs/. Check the chosen path is absent before approving creation.
Never overwrite an existing note, even with approval; keep the project rule unchanged.
Record actual state, evidence, checks not run and one next action;
no secrets, private inputs or chat dump. Inspect the saved note in Explorer.

Do not stage the note under ignored outputs/, force-add it or change ignore rules.
Append its actual path and brief status to the same analysis_plan.md after approval,
preserving earlier text. In a fresh chat explicitly read that actual path, the same
plan and relevant greeting/config.
Judge recovery against the actual records, not answers pasted into the prompt.
Filesystem memory is not guaranteed to load automatically. Review every file and
command before running or checkpointing; do not commit partial or failed results.
Carry this workspace, toolkit, evidence and handoff into Module 9's capstone at
../../../modules/08-features-best-practices.html. The HTML lesson does not verify
native VS Code delegation or execution. A toolkit ZIP may await these additions;
the lesson's manual templates are complete without it.

Official role/delegation guidance checked 2026-11-17:
- https://code.visualstudio.com/docs/agent-customization/custom-agents
- https://code.visualstudio.com/docs/agents/run/subagents
