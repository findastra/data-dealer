# Guardrails — what the system may never do

These are hard limits. The dashboard's design audits check the ones that can be checked against the system model; the weekly brief checks the rest. Changing this file requires a note in that week's brief.

## Never
1. **A model never moves money, holds a key, or signs a manifest.** Settlement, Attestation signer and Fulfillment are deterministic code with their own credentials.
2. **No unscrubbed data in write-once storage.** Raw uploads live in quarantine under a per-file key; only Verification's scrubbed output is locked.
3. **No excluded data:** health records, biometrics, minors' data, government ID images or numbers, financial account data, scraped data, or anything the contributor doesn't own.
4. **No file reaches a model or a person before the child-safety hash scan.** Matches go to the legal reporting path only.
5. **No Exclusive deal, takedown decision, recall, or refund above the threshold without a person at the Review desk.**
6. **No API-model output used as training rows.** Generation uses Apache-2.0 / MIT open-weight models; API models only judge and advise.
7. **No judge from the generator's model family.**
8. **No deletion of log entries.** Revocations are appended.
9. **No bounty before escrow.** Settlement checks the buyer's spending policy in code and holds the money; only then may the agent post a bounty.
10. **No purchase before buyer verification.** First purchase requires business verification, a sanctions check and acceptance of the acceptable-use policy.
11. **Nothing goes live until the go-live gate on the dashboard is all green.**

## Caps
| Cap | Value | Enforced by |
| --- | --- | --- |
| Synthesis retries per batch | 3, then Review desk | Dagster job |
| Eval panel pass bar | 95% upper bound on error < 5% | Eval runner |
| Contributor payout holdback | 30 days | Settlement |
| Buyer-agent spend | Daily and per-order cap set by the buyer | Settlement (OPA policy) |
| New contributor payouts | Capped until 3 accepted uploads | Settlement |
| Compute spend | ≤ 25% of trailing 90-day revenue once live | Treasury rule, CFO role agent |
| Open bounties | ≤ escrowed buyer money | Settlement |
| Runway floor | Below 6 months, new bounties pause | Treasury rule |

## Self-sustaining, growing, limited
- **Sustain:** royalties are paid only from collected cash; compute has a revenue-linked ceiling; repeat dataset sales carry no new compute cost.
- **Grow:** each dataset adds seeds and lineage to the provenance graph; the verify API grows with every buyer that has to file disclosures.
- **Limit:** the caps above, the excluded categories, and one human lane that can stop anything.
