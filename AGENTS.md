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
| `.claude/agents/` | Agent definitions: pipeline agents and the six exec hats |
| `skills/` | Repeatable procedures (weekly brief, provenance manifest, handoffs) |
| `handoffs/` | Task cards for whichever assistant picks them up |
| `briefs/` | Weekly briefs |
| `dashboard/` | Source of the live process-flow dashboard |

## Rules for every assistant
1. Read `docs/guardrails.md` before changing anything that touches money, keys, personal data or contributor agreements.
2. Record your model name and version in any file you produce (front matter or footer). Every model counts toward the model roster.
3. Cite sources for any claim about the present (laws, companies, prices). Label guesses.
4. Never commit secrets, API keys, `.env` files or real personal data.
5. Public-facing credit is **Astra**.
