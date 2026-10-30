# Eleven-module exercise map

Visible course numbers are authoritative; historical filenames are preserved.
Use copies in `write-repo`. Python and R are alternatives, not language lessons.
Expected outputs below are acceptance targets, not claims of executed student work.

| Module | Starter / record | Expected evidence |
| --- | --- | --- |
| 1 LLM foundations | llm_verification_record.md; ai_workflow_practice.py | Predictions versus supplied/observed evidence; complete/missing/all-missing cases, scientific and permission limits |
| 2 Data decisions | research_data_decision_template.md; research_workflow_templates.md; data_preparation_demo.py or .R; synthetic_data_practice.py | Processing/disclosure decision; invented before/after checks; 600 test rows, A/B300 each,30 missing each; no anonymity claim |
| 3 Native VS Code setup | module01_setup_check.R or ai_workflow_practice.py | Hello from Copilot / Hello from Ada; approved client and reviewed diff |
| 4 Agent risk and containment | sandbox/ recipes; sandbox_boundary_record.md; greeting.py created by prepare_work.py | Tool policy or unavailable status; strict SSH learner; reference-write denial; host-visible work; Alex/Sam/empty tests; restart persistence |
| 5 Git checkpoints | module02_git_checkpoint.R or ai_workflow_practice.py | Local checkpoint, reviewed diff and recovery; own private push destination checked, no instructor-origin push |
| 6 Planning | module03_analysis_plan_template.R; patient_survey_messy.csv | Written analysis plan, missing-data decision, output/tests before implementation |
| 7 Implementation | module04_analysis_pipeline_starter.R or ai_workflow_practice.py; patient_survey_messy.csv | Small reviewed loading/cleaning/summary steps with missingness and group counts |
| 8 Multi-agent | module05_multi_agent_starter.R or ai_workflow_practice.py | Bounded planner/coder/reviewer handoff, independent evidence, no implied access isolation |
| 9 Memory/context | module06_context_handoff_starter.R; research_workflow_templates.md | Concise handoff: decisions, actual tests, unresolved issues and next action |
| 10 Debugging | buggy_01_load_data.R through buggy_04_plot.R; module07_debugging_starter.R; ai_workflow_practice.py | Reproduce defect; Python complete/missing mean4 and explicit all-missing guard; regression tests and minimal fix |
| 11 Capstone | module08_feature_export_starter.R or ai_workflow_practice.py; patient_survey_messy.csv | Reviewed CSV/HTML summary, restart/reproduction record and explicit limits |

CSV patient labels and values are fictional teaching fixtures, not participant
records. Bugs in buggy_* and the missing-value average are intentional; some R
starters need dplyr/tidyverse. Run each route's classroom acceptance separately.
Clean reference changes belong to the instructor; student solutions stay in their
own work repositories. No names, grading data or credentials belong in the source.