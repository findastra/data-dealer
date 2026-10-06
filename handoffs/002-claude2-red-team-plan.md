status: open
for: claude-2
needs: docs/PLAN-v2.md, docs/guardrails.md, docs/research/02-provenance.md
---
## Task
Red-team Plan v2. Find the five most likely ways the system could (a) lose money, (b) sell data it had no right to sell, or (c) leak personal data. For each: how it happens, which guardrail should stop it, and whether that guardrail actually does.

## Done when
`handoffs/results/002-red-team.md` lists the five failure paths, ranked, with a proposed fix for any guardrail that doesn't hold. Note which model and version did the review.

## Return
Commit and set `status: done`. The Engineer and Counsel hats will pick it up in the next weekly brief.
