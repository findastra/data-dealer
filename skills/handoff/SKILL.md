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
from: <model name and version>, <YYYY-MM-DD>
needs: <files to read>
---
## What I did
## Task
## Done when
## Return
Write results to <path>, set status: done, commit.
```

`## What I did` is required on every card you write, and you update it when you finish someone else's card. List it explicitly, so the next assistant does not have to dig through chat or git history:
- every repo, branch and commit you changed or pushed, and whether it is on `main`;
- every file you added or changed, and any file on Astra's PC you touched (write paths as `%USERPROFILE%\...`);
- commands that changed anything (build, publish, push) and what you tested;
- where things live now, including which version of the dashboard is live;
- what is **not** done, and what is waiting on Astra.

Same format as `findastra/astras-pet-os` (`skills/handoff/SKILL.md` there). Added by Claude Opus 5.5 (`claude-opus-5-5`), 2026-10-17.

## Rules
- One card, one deliverable. Name the files to read; don't paste secrets.
- The taker sets `status: taken by <who>` before starting and records which model did the work.
- Results go in the repo, not in chat, so the next assistant can see them.
