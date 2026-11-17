# Research workflow templates — invented-data starter

Optional prompts for Modules 6-11. Use the sections you need in your existing
plan or notes; do not create another report. Blank fields are not evidence.
Use invented examples only. Keep real records, secrets and confidential methods out.

## Scientific contract (before asking for code)
Classroom rule: integer scores 1-10 or blank; omit blank scores from means,
retain separate total/observed/missing counts, label all-missing means undefined,
report blank groups separately, and stop on invalid scores. Real research needs
its own authorized analysis decisions.

- Research question and unit of analysis:
- Independently invented input schema and minimum necessary fields:
- Outcome, groups, inclusion/exclusion and denominator:
- Missing-data policy and all-missing behavior:
- Expected output (columns, grouping, units, ordering):
- A small example with expected result and scientific reason:
- Data/tool/model/recipient authorization checked by:
- Allowed files and actions; prohibited files/actions:
- Human stopping/review point:

## Analysis plan (before implementation)
1. Inspect the invented input and report types/missingness.
2. State transformations and their effect on the research question.
3. Describe the grouped summary. A plot is optional after the summary passes.
4. List small checks, edge cases and expected observations.
5. Choose the next bounded change and required review.

- Chosen practice language (Python / R / neither):
- Dependencies and verified installation source (if needed):
- Proposed steps, files and acceptance evidence:
- Assumptions to challenge with a reviewer:
- Explicit approval to implement (person/checkpoint):

## Session or agent handoff (after review)
- Current task, agreed rules and checkpoint:
- Accepted files/change and one challenged suggestion:
- Command/check | expected | observed or not run:
- Unknown or failed check:
- Next single task, allowed files/actions and stop point:

In Modules 6-8, keep this record in analysis_plan.md. In Module 9, turn the current
record into SESSION_NOTES.md. README holds run instructions; project instructions
hold stable rules. Do not copy the same session summary into every file.
Only when a command may still be running, add its host, status evidence,
authorized stop control and any setting restored. Unknown stays unknown.

Do not pre-fill “all tests passed”. A supplied example or expected output is not
an executed result. A fresh session must verify the handoff against the files.
