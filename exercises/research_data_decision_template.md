# Research data decision worksheet

Use fictional examples for the course. For a real project, complete this within approved institutional storage; do not put participant values, keys, confidential protocols, or identifying examples in a public repository or unapproved chat. This record supports a discussion, not automated legal clearance.

Optional practice from Module 5 onward. Module 2 uses on-page questions, not this
worksheet. Complete one short activity below; the project checklist is optional.

## One invented example, four answers

Alex Morgan is an invented participant: P007, age 43, depression score 18. A protected key connects the code to Alex. The fictional study permits analysis in its approved university environment but forbids sending participant records to outside services.

Use Alex's example, or choose another invented table from Module 2. In pairs, take
about 10 minutes:

1. **Describe:** What needs protection? Which clue tells you that?
2. **Check:** What analysis and sharing are permitted? What evidence is missing?
3. **Trace:** What would the assistant receive through files, pasted text or tool results? Who receives each copy?
4. **Choose and test:** Give one permitted route and one invented code-help prompt with an expected result. State what the assistant cannot access, and a fallback if permission is unclear.

For invented scores 2, missing and 6, the observed-value mean should be 4 and the missing count 1. If all scores are missing, the code must flag that no valid mean is available. These tests check behavior, not whether omitting missing answers is appropriate for a real study.

Then change one condition: internal processing is no longer permitted. Which
real-data action must stop? Check your reasoning against the
[Module 2 questions](../data-before-ai.html#exercise).

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

## Expected output

One short decision record: what needs protection, what is permitted, what the
assistant would receive and your next action. Include an invented code-help
example and its expected result. Identify the records and outputs that must stay
outside assistant access. The checklist supports review; it is not legal clearance.

For a reminder of minimization versus invention, see
[Module 2's comparison](../data-before-ai.html#prepare-data). Do not transform
restricted records without permission. Invented tests check code, not scientific
conclusions or permission to release data.
