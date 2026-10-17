status: open (waiting on Astra: review and merge claude/dashboard-fixes-20261017; decide when Codex's dashboard shell goes live)
for: any
from: Claude Opus 5.5 (claude-opus-5-5), 2026-10-17
needs: AGENTS.md, dashboard/src.html, docs/chip-coin-20261014.md, astras-pet-os PET-PROGRAM-FRAMEWORK.md and docs/flash-audit-20261014.md
---
# Dashboard audit and fixes: handoff

## What I did

Astra asked a Claude chat (6-7 Oct) to audit the live ops dashboard for code errors, fix them and make the text slightly larger. On 17 Oct she asked for that chat's work to be put into the repo.

**Live dashboard** (https://claude.ai/artifact/CzBXnEWyRjq5Tui7o3oRS8)
- Published version 11 (eight fixes) and version 12 (larger text). Version 12 is live now. No other assistant has published since.
- Version 12 is `main`'s dashboard (`70d68bb`) plus the changes below. It does **not** include Codex's Chip coin, yellow phone or L3 activity work: those are only on the `codex/*` branches.
- Its declared capabilities (data store with the root rule read `view` / write `admin`, and Claude sampling) were carried forward unchanged.

**This repo, branch `claude/dashboard-fixes-20261017`** (from `main` at `70d68bb`; not on `main`):
- `dashboard/src.html`, the eight fixes:
  1. The weekly brief no longer goes blank after a brief with no role sections (`hatSel` clamped to 0 or more).
  2. Assignments with an unknown priority show under "Later" instead of disappearing from the Assignments page and Chip's goals (`priOf`).
  3. Chip shows the sleep face and "offline" until assignments load, instead of "all clear".
  4. Going to an assignment hidden by the Anywhere / At home filter switches the filter to All first (`focusAssign`).
  5. A living-layer audit run with no timestamp shows its title only, not "Invalid Date".
  6. Saving outside Claude says "Saving works when this dashboard is open in Claude."
  7. Pressing Enter while Chip is answering keeps the typed message.
  8. The markdown viewer hides table separator rows such as `|:--|--:|`.
- `dashboard/src.html`, larger text: root font size 110%, body 15.5px (was 14px), and sticky offsets 76px → 82px for the taller top bar.
- `dashboard/index.html` and `data-dealer-20261008.html` rebuilt with `python dashboard/build.py` and copied (the sync step in `docs/chip-coin-20261014.md`).
- `AGENTS.md`: a "Part of Astra's PetOS" section linking the hub's rules (PET-FILES.md requires it), and a built-with line.
- `skills/handoff/SKILL.md`: the card format now has `from:` and `## What I did`, the same as the hub's handoff skill.
- This file.

**findastra/astras-pet-os, branch `claude/chip-row-20261017`** (commit `f9f3cf5`; not on `main`): Chip's row in `INTELLIGENCE-LEVELS.md`. The stale "PC folder is not connected" error is removed. The row now lists the unmerged dashboard branches and Chip's chat on the live dashboard. `npm test`: 89 of 89 pass.

**Tested**
- Before the fixes: every page, Chip, the rail and the 16 design audits ran in a local copy with no script errors. Each bug was reproduced with mock data.
- After the fixes: the same mock tests passed, with no script errors. The data store and sampling calls were checked against the runtime type definitions (contract 0.2.69).
- Not tested: live data and Chip's Claude answers end to end, because the test browser was not signed in to claude.ai. Larger text was not viewed in a browser.
- The change applies cleanly to `dashboard/src.html` and `data-dealer-20261008.html` on `codex/l3-activity-20261016`: all 13 parts, with small line offsets. Merging this branch and Codex's stack should only need the rebuild. `AGENTS.md` edits stay above Codex's appended lines.

**Nothing on Astra's PC was changed** apart from temporary git worktrees under `%TEMP%`, removed after pushing. The working copy in the pet folder stayed on Codex's branch, untouched.

## Task
1. Astra reviews and merges `claude/dashboard-fixes-20261017` into `main`, so the repo matches the live dashboard.
2. When Codex's `codex/*` dashboard branches are reviewed: merge them on top, rebuild (`python dashboard/build.py`, copy `dashboard/index.html` to `data-dealer-20261008.html`). A Claude session then republishes the artifact to the same link. Only Astra decides when that shell goes live.
3. Astra reviews and merges `claude/chip-row-20261017` in the hub.

## Open, not from this work
- `findastra/data-dealer` is **public** on GitHub. The README says "Private working repo", and the hub registry says private (hub migration plan, decision 2).
- Flash Audit A18: no declared tool inventory for Data Dealer (hub card 015).
- The 12 Oct brief's roster warning: `.claude/agents/eval-judge.md` says `model: haiku` instead of a pinned model ID.

## Done when
Both branches are merged and the live dashboard matches `main`.

## Return
Update `## What I did`, set `status: done`, commit on a branch.
