# CLAUDE.md

Read `AGENTS.md` first; everything there applies.

Claude-specific notes:
- Agent definitions live in `.claude/agents/` (pipeline: dealer, verifier, eval-judge; role agents: ceo, engineer, cfo, counsel, data-steward, growth).
- Procedures live in `skills/`; follow `skills/weekly-brief/SKILL.md` for the Monday brief and `skills/handoff/SKILL.md` for task cards.
- The dashboard source is `dashboard/src.html`; run `python3 dashboard/build.py` to embed the current agent and skill files, then republish the artifact.
- Commit messages: imperative, short. Public credit: Astra.
