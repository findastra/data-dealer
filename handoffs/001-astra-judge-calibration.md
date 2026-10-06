status: open
for: astra-openai
needs: .claude/agents/pit-boss-judge.md, docs/PLAN-v2.md
---
## Task
Act as Pit Boss judge seat 2. Read the judge rubric and the grade definitions. Write 20 example rows for a tabular "customer-support Q&A" Deck: 15 correct, 5 with realistic defects (wrong answer, leaked personal detail, duplicate, off-spec format, hallucinated fact). Then score all 20 yourself using the rubric.

## Done when
`handoffs/results/001-judge-calibration.json` holds the 20 rows, the true labels, your verdicts, and your model name and version.

## Return
Commit the file and set `status: done`. These rows become the calibration set every judge must pass before it joins the panel.
