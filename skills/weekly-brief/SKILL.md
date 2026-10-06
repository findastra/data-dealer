---
name: weekly-brief
description: Produce the Data Dealer weekly brief. Use every Monday (scheduled) or when Astra asks for "the brief". Reads the repo and the week's news, writes one section per exec hat, posts audits to the dashboard and notifies Astra.
---

# Weekly brief

## Inputs
- This repo (`findastra/data-dealer`): `docs/PLAN-v2.md`, `docs/guardrails.md`, `docs/models.md`, last brief in `briefs/`, commits since last brief.
- The web: news from the last 7 days on the topics each hat watches (see `.claude/agents/*.md`).
- The dashboard's audit store (`audits` collection) for anything the living layer logged.

## Steps
1. `git log --since="8 days ago"`; list what changed.
2. Run the repo audits (below). Each one is a row: `{check, result: pass|warn|fail, detail, stage}`.
3. For each hat in this order — CEO, Engineer, CFO, Counsel, Data Steward, Growth — write:
   - **Pay attention:** at most 3 bullets, each with a source link and one line on why it matters to us.
   - **Questions for Astra:** the standing questions from the hat's agent file that are still unanswered, plus any new one this week raised. Drop a question once Astra answers it in the repo or chat.
4. Write `briefs/YYYY-MM-DD.md`, commit and push.
5. Write the brief to the dashboard (`briefs/<YYYY-MM-DD>` doc) and the audit rows (`audits/<YYYY-MM-DD>` doc, rows in an array).
6. Send Astra a short notification: the top 3 things across all hats, how many audits failed, and the number of open questions.

## Repo audits
| Check | Pass when |
| --- | --- |
| Secrets | No keys, tokens or `.env` files committed |
| Model roster | Every model named in code or agent files is listed in `docs/models.md` |
| Judge independence | No Pit Boss seat shares a family with the Forge generator |
| Guardrails current | `docs/guardrails.md` changed only with a note in the brief |
| Sources fresh | Research docs cite sources dated within 12 months for anything about the present |

## Style
Plain sentences. Lead with what changed. No filler. Facts carry a source; guesses are labeled as guesses.
