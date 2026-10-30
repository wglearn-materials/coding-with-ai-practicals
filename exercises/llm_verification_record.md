# Module 1: LLM verification record

Use only the invented examples below. This is an evidence record, not approval
to process participant data or adopt a missing-data method.

## Inputs and Task

Write or inspect Python/R code returning the mean of observed values and the
number missing. An all-missing input returns no numeric mean, never zero.
Use an approved assistant and runner if available; otherwise use the supplied
reference in Module 1, predict results and mark them as supplied, not executed.
No package installation or access to research files is needed.

## Expected Output

Complete predictions before inspecting the reference or generating code.

| Invented input | Expected mean | Expected missing | Observed result | Evidence status |
| --- | --- | --- | --- | --- |
| 2, 4, 6 | 4 | 0 | | not run / supplied / run by me |
| 2, missing, 6 | 4 | 1 | | not run / supplied / run by me |
| missing, missing | no numeric mean | 2 | | not run / supplied / run by me |

Python's supplied reference uses None; R uses NA. These are explicit missing
markers for this exercise, not a complete policy for every file/data type.

## Request and Boundaries

- Assistant/model/service and date, or supplied reference only:
- Exact request (no private content):
- Context supplied:
- Permitted tools and runner, or no execution:
- Stop condition: test these invented inputs; report evidence; do not read
  files, install packages, edit study code or choose a research method.

## Verification

- Code inspected (paste it here):
- Actual execution command and Python/R version, or not run:
- Expected versus observed results for all three cases:
- Separate generated claims from tool output or your own execution:
- One likely failure: division by total count, unhandled missing values or
  an all-missing input. Which test detects it?
- One correction made and re-tested, or none needed:

## Not established

- Three passing tests do not prove general correctness or scientific validity.
- Omitting missing observations still needs a justified research method.
- Local execution does not guarantee that assistant tool output remains local.
- This record does not authorize participant-data access or a model endpoint.

## Transfer to Module 2

What would change if these values belonged to participant P007?
Name what you would check before letting an assistant receive records or results:

Partner review: can another researcher distinguish prediction, supplied example,
actual execution and unresolved decisions from this record?