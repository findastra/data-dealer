# AGENTS.md — read this first (any AI assistant)

This repo is the shared desk for every assistant working on **Data Dealer**: Claude sessions, Astra's second Claude account, and Astra (OpenAI). Founder: Astra.

## What this is
A marketplace that pays people for real data, verifies it, expands it into synthetic data, and sells it with signed provenance to AI teams and AI agents. Start with `docs/PLAN-v2.md`.

## Where things are
| Path | What |
| --- | --- |
| `docs/PLAN-v2.md` | The pipeline, with every change from v1 and why |
| `docs/guardrails.md` | Hard limits: what the system may never do |
| `docs/models.md` | Every AI model in the system, its job, and what data it touches |
| `docs/research/` | Research notes with sources |
| `docs/pitch/` | Pitch narrative (mini deck → technical deck) |
| `.claude/agents/` | Agent definitions: pipeline agents and the six role agents |
| `skills/` | Repeatable procedures (weekly brief, provenance manifest, handoffs) |
| `handoffs/` | Task cards for whichever assistant picks them up |
| `docs/team.md` | Who does what across Claude 1, Claude 2 and Astra |
| `briefs/` | Weekly briefs |
| `dashboard/` | Source of the live ops dashboard, published at https://claude.ai/artifact/CzBXnEWyRjq5Tui7o3oRS8 (assignments, audits, go-live gate) |

## Rules for every assistant
1. Read `docs/guardrails.md` before changing anything that touches money, keys, personal data or contributor agreements.
2. Record your model name and version in any file you produce (front matter or footer). Every model counts toward the model roster.
3. Cite sources for any claim about the present (laws, companies, prices). Label guesses.
4. Never commit secrets, API keys, `.env` files or real personal data.
5. Public-facing credit is **Astra**.

## Part of Astra's PetOS
Data Dealer is pet program #3 (pet: **Chip**) in [findastra/astras-pet-os](https://github.com/findastra/astras-pet-os). Before working here, also read that repo's `AGENTS.md` "Before any work" list, its [PET-FILES.md](https://github.com/findastra/astras-pet-os/blob/main/PET-FILES.md) and [PET-PROGRAM-FRAMEWORK.md](https://github.com/findastra/astras-pet-os/blob/main/PET-PROGRAM-FRAMEWORK.md). Changes to Chip's name, job, status, bubble lines, mood lines or audit are submitted to the Friendly Farmer through `cage.submit` in `pet.json`, with the date. Work on a branch named for your assistant and the date; `main` changes only with Astra's OK.

Dashboard audit, eight fixes and larger text by Claude Opus 5.5 (`claude-opus-5-5`), 2026-10-07; recorded in `docs/handoff-claude-20261017.md`.

Desktop appearance revision by OpenAI Codex (GPT-6), 2026-10-11. See desktop-pet-20261011.json; runtime behavior is in astras-pet-apps.
