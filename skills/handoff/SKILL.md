---
name: handoff
description: Write or pick up a task card in handoffs/ so work can move between Claude sessions, Astra's second Claude account, and Astra (OpenAI). Use when a task should be done by a different assistant or needs a second opinion.
---

# Handoff cards

Any assistant that can read this repo can take a card: this Claude, Astra's second Claude account, or Astra (OpenAI). The repo is the shared desk.

## Card format — `handoffs/NNN-short-name.md`
```
status: open | taken by <who> | done
for: astra-openai | claude-2 | any
needs: <files to read>
---
## Task
## Done when
## Return
Write results to <path>, set status: done, commit.
```

## Rules
- One card, one deliverable. Name the files to read; don't paste secrets.
- The taker sets `status: taken by <who>` before starting and records which model did the work.
- Results go in the repo, not in chat, so the next assistant can see them.
