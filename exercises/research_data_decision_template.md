# Research data decision worksheet — before AI assistance

Use fictional examples for the course. For a real project, complete this within approved institutional storage; do not put participant values, keys, confidential protocols, or identifying examples in a public repository or unapproved chat. This record supports a discussion, not automated legal clearance.

## Classroom route: one case, four answers

Alex Morgan is an invented participant: P007, age 43, depression score 18. A protected key connects the code to Alex. The fictional study permits analysis in its approved university environment but forbids sending participant records to outside services.

Choose Alex's case B, or a different fictional case in the lesson. In pairs, take 10 minutes:

1. **Describe:** What needs protection? Which clue tells you that?
2. **Check:** What analysis and sharing are permitted? What evidence is missing?
3. **Trace:** What would the assistant receive through files, pasted text or tool results? Who receives each copy?
4. **Choose and test:** Give one permitted route and one invented code-help prompt with an expected result. State what the assistant cannot access, and a fallback if permission is unclear.

For invented scores 2, missing and 6, the observed-value mean should be 4 and the missing count 1. If all scores are missing, the code must flag that no valid mean is available. These tests check behavior, not whether omitting missing answers is appropriate for a real study.

Then change one condition: internal processing is no longer permitted. Which real-data action must stop? Compare with the worked decision in [Module 2](../data-before-ai.html#exercise).

The detailed fields below are an optional project-review checklist, not additional required classroom questions.

## 1. What information do I have?

- Dataset/project reference (non-sensitive description):
- Source, data steward, and origin:
- People involved or linkable? Direct identifiers:
- Indirect identifiers / rare combinations / external linkage:
- Personal / pseudonymized / assessed anonymous / synthetic / non-personal:
- Health, genetics, beliefs, biometrics, or other protected attributes:
- Confidentiality, embargo, intellectual-property, and license restrictions:
- Free text, image/audio metadata, logs, derived outputs, or small cells needing review:
- Evidence for classification; uncertainties:

Labels overlap. Removing names, hashing IDs, aggregation, or synthetic generation from real data does not alone establish anonymity.

## 2. What use is authorized?

Processing includes reading, calculating, changing and disclosing data. Check internal analysis and external disclosure separately because permission for one need not cover the other.

- Research question and exact proposed processing:
- Applicable framework(s) and institution's confirmation of scope:
- Purpose/authority: consent or other applicable authorization, legal basis/condition where required:
- Ethics protocol / amendment or applicability decision:
- Data access/use agreement and permitted recipients:
- License/confidentiality restrictions:
- Permission to analyze internally:
- Separately: permission to disclose this material to the proposed service/tools:
- Evidence reference, approving role, date, and limits (no copied personal information):

## 3. What would be exposed?

- Provider / institutional account / plan:
- Model service, endpoint (address/interface used to reach the model), and approved features:
- Information path, including branches (for example: local file → R prints a row → assistant includes the row in a request → remote model service receives it; possible logs or other recipients):
- For each connection: what information moves, which component sends it, and which person or organization receives it:
- Prompt, code/comments, schema, actual rows, filenames, errors, plots, outputs:
- Automatic context/retrieval and file/tool permissions:
- Third-party tools / embedding endpoint / subprocessors:
- Processing/storage/backup/support locations and transfer arrangements:
- Retention/deletion, training use, telemetry, human access:
- Contract / processor arrangement / business associate agreement (BAA, when HIPAA applies):
- Configuration evidence and date verified:

“Local execution,” “no training,” “Swiss-hosted,” and “private repository” answer different questions; none alone establishes full permission.

## 4. How can I continue productively?

- Decision: proceed within verified scope / use lower-exposure alternative / clarify before sharing.
- Restriction: external disclosure forbidden / processing itself forbidden / permission unclear; evidence:
- Selected solution: generic code-only assistance / independent synthetic examples / assessed anonymous extract or aggregate / institution-approved hosted AI / approved local or on-premises AI / request authorization or keep AI out of the data step.
- Why this solution fits all applicable data labels and restrictions:
- Fallback that does not require access to or disclosure of restricted records:
- Minimum information needed for the AI task:
- Invented example or generic code-only prompt:
- Files/data/tool outputs that must remain inaccessible to the assistant:
- What may cross from the example workspace into the study environment (reviewed code), and what must not return automatically (real rows, logs, results):
- How the generated code will be run and verified in an authorized environment:
- For direct AI analysis of real data: required approval, responsible office, and configuration evidence:
- Pending question and responsible contact (principal investigator/data steward, data-protection officer/legal office, IT/security, ethics office):
- Approval scope and recheck trigger (new data, model, connector, purpose, terms):

Lower exposure does not grant authorization. If processing itself is forbidden, do not access or transform the real records to anonymize them or generate synthetic data. Use unrelated fictional examples while permission is clarified.

## Course practice — fictional cases B, F, H

Start with case B from [Data Before AI](../data-before-ai.html#examples): Alex Morgan, P007, age 43, depression score 18, with a protected participant key. Give the classification clues, permitted use, possible exposure, selected solution and fallback. Cases F and H are optional comparisons. Distinguish forbidden external disclosure from a lack of authority to process the records at all. Compare with the worked decision on the lesson page.

Expected output: one short decision record for your chosen case, with an invented code-help prompt, the files/outputs the assistant must not access, and a test of the generated code. For example, mean(x, na.rm = TRUE) on invented x <- c(2, NA, 6) should return 4; count the one missing answer separately. All-missing input gives NaN in this R expression; the pipeline must flag that no valid mean is available. This checks code, not whether omitting missing values is appropriate for the real study.

Add one counterfactual per decision: change either the permission (internal processing is no longer authorized) or the information flow (an agent sends real printed rows to a remote model). State which part of your route must change and why. Record your prediction before revealing the lesson's case reasoning; do not treat the interactive feedback as institutional clearance.

## 5. Practical preparation — fictional data only

Open the [Module 2 preparation mini-lesson](../data-before-ai.html#prepare-data). Keep real records, linkage keys, private schemas and confidential methods out of the AI workspace.

Preparation methods are choices, not a required six-stage anonymisation procedure. For code help, start with independently invented values and the minimum shareable schema (columns and their types); do not transform real records without permission.

- Task the AI actually needs to help with; minimum shareable columns and types:
- Fictional before/after transformation: pseudonymisation / generalisation / aggregation / reviewed redaction; why this technique helps:
- What it does **not** remove: linkage, rare combinations, free text, small cells/differencing, metadata, logs or confidentiality restrictions:
- If a key exists, where it stays separate and who may access it (no actual key or identifier):
- Independently invented synthetic example: schema, types, a missing value and an edge case; confirm it was not fitted to or copied from restricted data:
- Predicted versus actual code result and utility check; what research question the transformation can no longer answer:
- If using the optional Python or R demonstration, chosen route and observed evidence; label unexecuted code as unexecuted:
- Real-data processing permission versus disclosure permission; intended recipient/configuration and approval evidence still missing:
- Proceed within authorised scope / keep AI on invented examples / hold and ask the data steward; reason:

Removing names, using a code, suppressing a toy small cell or inventing records is not a release certificate. Synthetic teaching values test code, not scientific conclusions. If the schema or protocol is confidential too, use an unrelated generic example. When processing itself is not permitted, do not transform the restricted records.
