# Data Dealer — Plan v2

Version 2 keeps the shape of the original process flow (`docs/process-flow.mmd`) and fixes what would have broken it: legally, financially or technically. The live diagram is the dashboard (`dashboard/`); the static chart is `diagrams/pipeline-v2.png`.

*Prepared for Astra. Model: Claude Opus 5.5, 6 Oct 2026. Not legal or financial advice.*

## One sentence
Data Dealer pays verified people for data they own, proves it is clean, expands it into synthetic data, and sells both with a signed, publicly checkable record of where every row came from and which AI models touched it.

## The flow
| Stage | Job | Key rule |
| --- | --- | --- |
| **Buyers** | AI teams (web) and AI agents (MCP / API) | Human teams first; agents are early |
| **The Table** | Search, manifests, tickets, orders | One front door; first purchase needs business verification, sanctions check, acceptable-use acceptance |
| **Dealer** (AI agent; proposed rename: Host) | Quote, preview, bounty | Preview labeled `SYNTHETIC PREVIEW`; posts a bounty only after the Cage confirms escrow; never touches money |
| **Contributors → The Source** | ID + 18+ check, e-signed agreement, payout account | Ownership attestation + license grant + indemnity |
| **Intake** | Quarantine, per-file key, hash, malware + CSAM hash scan | Nothing reaches a model before this |
| **The Assay** (AI agent) | Origin, forensics, personal-data scrub, quality, grade | Scrub before anything is locked; model sees reports, not raw files; other people's data inside an upload is scrubbed or rejected |
| **Seed vault** | Scrubbed seeds, write-once | Only scrubbed data is ever locked; real-data Decks (grade A/B) go straight to the Ledger |
| **The Forge** (AI job; proposed rename: Greenhouse) | Seed → synthetic, scored | Apache-2.0/MIT generators; synthetic mixed with real, never replacing it |
| **Pit Boss** (AI panel) | 3 judges, 3 model families | Pass if the 95% upper bound on error < 5%; max 3 retries |
| **The Ledger** (code) | Manifest, Merkle root, Ed25519 signature, log entry | No model holds a key |
| **Transparency log** | Append-only public record + verify page | Revocations are appended, never deleted |
| **The Deck** | Parquet + Croissant + manifest + datasheet + license | Graded and tiered |
| **The Cage** (code) | Payment, budget caps, 30-day holdback, splits | No model moves money |
| **The Shoe** (code) | Signed download / cloud share + canary rows | Each buyer's copy is traceable |
| **Shift Manager** (humans) | Disputes, takedowns, recalls, Exclusive deals, grade A spot-checks | The one human lane |

## Changes from v1
| v1 | v2 | Why |
| --- | --- | --- |
| Raw vault object-locked before the scrub | Quarantine with a per-file key → scrub → lock only scrubbed seeds | GDPR/CCPA erasure stays possible; destroying a key erases a file |
| No way to pull a Deck back | Shift Manager desk revokes in the log, notifies buyers, freezes royalties | Takedowns happen; recall is a selling point |
| Quote + 20-row sample before data exists | Price range + labeled synthetic preview | Don't imply real data you don't have |
| Forge ⇄ Pit Boss loop unbounded | Max 3 retries, then a human | No runaway compute |
| "Open-weight model" | Apache-2.0 / MIT only, license recorded per model | Clean rights chain |
| Grades and tiers undefined | Defined below | Buyers and contributors know what they get |
| Fully autonomous | Autonomous except the Shift Manager desk | Accountable people for disputes and big deals |
| "3 independent models" | 3 families, none from the generator's family; splits escalate | No shared blind spots |
| Error rate < 5% | 95% upper confidence bound < 5% | A small sample can't pass by luck |
| Agent buyers only | Human teams first, agents too | That's where money is today |
| Royalties at sale | 30-day holdback | Room to reverse fraud |
| — | CSAM hash scan at Intake | Legal duty (REPORT Act) |
| — | Every AI model recorded in the manifest | Buyers' disclosure laws ask for it |
| — | Transparency log + public verify | Proof nobody can quietly rewrite |
| — | Per-buyer canary rows | Trace leaks |
| — | Verify & compliance API | Recurring revenue |

## Design review, 6 Oct (before anything goes live)
| Problem found | Fix |
| --- | --- |
| The AI agent checked the buyer's budget before posting a bounty, so a model was making a money decision | The Cage checks the spending policy in code and escrows the money; the agent posts the bounty only after the Cage confirms |
| Real-data Decks could only reach buyers through the synthetic step | Seed vault → Ledger path for grade A/B Decks |
| Buyers weren't verified | Business verification, sanctions check and acceptable-use acceptance before the first purchase |
| Grade A needs a human spot-check, but the design said "autonomous except one desk" | Grade A spot-checks go to the Shift Manager desk |
| Uploads can contain other people's personal data | Contributor attests to third-party consent; the Assay flags it and scrubs or rejects |
| "Floor desk" had the casino hierarchy backwards (floorpersons report to the pit boss) | Renamed Shift Manager, who sits above the pit boss |
| Names that mislead | See `docs/metaphor-audit.md`; renames await Astra's approval |

## Go-live gate
Nothing goes live until every item is green on the dashboard: all design audits pass, names approved, first vertical chosen, partnership terms set, entity formed, lawyer-drafted contributor agreement and Deck license, buyer verification in place.

## Grades and tiers
| Grade | Meaning |
| --- | --- |
| **A** | Real data, ID-verified contributor, full consent chain, human spot-check passed at the Shift Manager desk |
| **B** | Real data, ID-verified contributor, automated checks only |
| **C** | Synthetic, generated from A/B seeds, Pit Boss passed; seeds named in lineage |

| Tier | License | Royalty rule |
| --- | --- | --- |
| Standard | Non-exclusive, internal training | Pool share on every sale |
| Limited | Non-exclusive, capped number of buyers | Pool share; price premium |
| Exclusive | One buyer, no resale, human sign-off | Higher one-time share |

## Revenue
1. **Deck sales** (core): platform keeps the share after royalties and costs.
2. **Bounties**: buyer-funded custom data, escrowed up front, platform fee.
3. **Verify & compliance API** (recurring): manifest checks and exports for California AB 2013's 12 categories and EU AI Act training-data summaries.
4. **Exclusive licenses** (premium).

Unit economics, self-funding rules and limits: `docs/research/08-economics.md` and `docs/guardrails.md`.

## Phases
| Phase | Goal | Done when |
| --- | --- | --- |
| 0 · Validate (now) | 10 buyer discovery calls in one vertical; founder agreement signed | 3 written letters of intent or pilot commitments |
| 1 · Manual pilot | Run the flow by hand for one Deck: real contributors, scripts instead of agents | One paid Deck with a signed manifest |
| 2 · Automate the spine | Intake, Assay, Ledger, Cage, Shoe as code; Dealer + Assayer as agents | 5 paid Decks, recall drill passed |
| 3 · Forge + Pit Boss | Synthetic Decks with the judge panel | Synthetic Deck sold twice |
| 4 · Agents buy | MCP server public, x402 option | First agent-initiated purchase |
| 5 · Raise | Seed round on pilot revenue and the provenance graph | Term sheet |

## Open decisions
Tracked in the weekly brief, by hat. The blocking three: first vertical, partnership terms, entity type.
