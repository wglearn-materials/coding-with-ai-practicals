---
name: check-output
description: Check hello_copilot.R against the bundled five-line greeting fixture. Use when asked to check greeting output.
---
1. Read [expected output](./expected-output.txt) and the attached hello_copilot.R.
   If either is missing or a different script is selected, stop and report NOT RUN.
2. Inspect the script before execution. Ask for approval to run exactly
   `Rscript hello_copilot.R` from /workspace/work; wait for the user's answer.
   Do not run other commands. If unsafe, unavailable or declined, report NOT RUN.
3. After approval, run that command once. Capture its actual exit status and stdout.
   PASS requires exit status 0 and the fixture's five lines in order, with no extra
   lines. Ignore only CRLF versus LF and a final newline. Otherwise report FAIL.
   If execution evidence is missing or incomplete, report NOT RUN, not a prediction.
4. Reply with status PASS / FAIL / NOT RUN, command, observed exit status and any
   output difference or reason not run. Do not edit code, data or the expected fixture.
