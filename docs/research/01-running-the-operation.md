# What it takes to run this operation, and how to learn it

*Research note for Data Dealer · Claude Opus 5.5 · 6 Oct 2026. Costs and time are rough planning assumptions, not quotes.*

## The jobs, and who (or what) does them
| Job | Early stage (2 founders) | Automated by | Human still needed for |
| --- | --- | --- | --- |
| Find buyers, sell pilots | Founder | Growth hat drafts lists and follow-ups | Calls, pricing, trust |
| Recruit contributors | Founder | Dealer posts bounties | Community, first 50 people |
| Contributor agreement, Deck license | Startup lawyer | — | Drafting and sign-off |
| Intake, Assay, Ledger, Cage, Shoe | Technical founder | Code + Assayer agent | Code review on money and keys |
| Forge + Pit Boss | Technical founder | Batch jobs + judge panel | Calibration, escalations |
| Disputes, takedowns, recalls | Both founders | Floor desk queue | Every decision |
| Books, taxes, payouts | Founder + bookkeeper | CFO hat, Stripe Connect | Filing, sign-off |
| Weekly direction | Both founders | Six hats write the brief | Answering the questions |

## What to learn, in order
Each step unlocks the next. Learn by building the manual pilot (Phase 1), not by studying first.

1. **Data basics:** CSV/JSON → Parquet, pandas or Polars, schema validation (pandera). *Practice:* turn one messy dataset into a clean Parquet file with a schema.
2. **Hashes and signatures:** SHA-256, Merkle trees, public/private keys, Ed25519. *Practice:* sign a manifest locally, verify it, then change one byte and watch verification fail.
3. **Postgres + SQL:** tickets, catalog, audit log. *Practice:* the catalog table and a "search Decks" query.
4. **Cloud essentials (AWS):** S3, IAM least privilege, KMS keys, Object Lock modes. *Practice:* quarantine bucket + per-file key + crypto-shred one file.
5. **Payments:** Stripe Billing, Stripe Connect (contributor payouts, tax forms), Stripe Identity. *Practice:* test-mode payment → 30-day hold → payout.
6. **Personal-data scrubbing:** Presidio analyzers and anonymizers. *Practice:* scrub a sample chat log; measure what it misses.
7. **Agents:** Claude Agent SDK and Managed Agents (agents, environments, sessions, permission policies, budgets), MCP servers. *Practice:* an MCP server with `search_decks` and `create_ticket`.
8. **Evals:** Inspect AI, judge rubrics, confidence intervals on error rates. *Practice:* score the judge calibration set from handoff 001.
9. **Synthetic data:** profiling (ydata-profiling), SDV/SDMetrics, distance-to-closest-record privacy checks. *Practice:* generate 1,000 rows from 100 seeds and score them.
10. **Law you must know well enough to brief a lawyer:** copyright and licensing for training data, GDPR/CCPA basics, California AB 2013, EU AI Act GPAI duties, DMCA, REPORT Act.

## First 90 days
| Weeks | Goal | Output |
| --- | --- | --- |
| 1–2 | Founder agreement, entity choice, one vertical picked | Signed agreement; one-page vertical thesis |
| 2–4 | 10 buyer discovery calls | Notes; 3 written pilot commitments |
| 3–6 | Lawyer drafts contributor agreement + Deck license | Two signed-off templates |
| 4–8 | Manual pilot: recruit 20 contributors, run checks with scripts, hand-build one Deck and manifest | Deck #1 with signed manifest |
| 8–12 | Sell Deck #1; automate Intake + Ledger + Cage | First revenue; recall drill passed |

## Credits and programs worth applying for
AWS Activate, Anthropic's startup program, and Stripe Atlas (if forming a Delaware C-corp). Check each program's current terms before applying.

## Biggest risks to running it
1. **Supply quality:** contributors uploading data they don't own. Mitigated by attestation, origin checks, holdback, and recall.
2. **Demand timing:** agent buyers are early. Sell to human teams first.
3. **One person holding everything:** keys, money and code review need two people from the start.
