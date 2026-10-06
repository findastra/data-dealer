# Naming

*6 Oct 2026 · Claude Opus 5.5. Replaces the casino names and the earlier metaphor audit.*

No metaphors. Every part is named with words engineers, auditors and buyers' lawyers already use, from two real vocabularies:

- **Data plane — supply-chain vocabulary.** Data moves like goods through a supply chain with security controls: onboarding, quarantine, verification, synthesis, evaluation, attestation, catalog, settlement, fulfillment, recall. Provenance borrows directly from software supply-chain security (signed attestations, transparency logs, manifests), which is the discipline the design actually uses.
- **Control plane — agentic-systems vocabulary.** Agents, harnesses, tools, permission policies, evals and judges, human-in-the-loop review, role agents. Code that holds keys or moves money is called a *service*, never an agent. The control plane is what Astra calls the living layer.

| Now | Was | Why this name |
| --- | --- | --- |
| **Gateway** | The Table | API gateway + MCP server: the one front door that authenticates and routes buyers |
| **Sourcing agent** | Dealer | Procurement: turns a requirement into a spec, a quote and a sourcing request (the bounty) |
| **Settlement** | The Cage | Finance: completing payment, escrow and payouts |
| **Fulfillment** | The Shoe | Supply chain: delivering a paid order |
| **Catalog** / **dataset** | The Deck | The product shelf; each item is a versioned dataset |
| **Review desk** | Floor desk / Shift Manager | Human-in-the-loop review for what the system must not decide alone |
| **Onboarding** | The Source | Identity checks (KYC) and agreements before someone can supply |
| **Quarantine** | Intake | Hold uploads apart until they pass inspection |
| **Verification** (Verifier agent) | The Assay | Confirm origin, ownership and quality against evidence |
| **Seed store** | Seed vault | "Seed data" is the term of art for the real data synthetic data is generated from; in code say "seed rows" |
| **Synthesis** | The Forge | Data synthesis: generating new records from a model of real ones |
| **Eval panel** | Pit Boss | Evals with a panel of LLM judges, used as a pass/fail step |
| **Attestation** | The Ledger | Software supply-chain security (in-toto, SLSA): a signed statement of how an artifact was made |
| **Control plane** | Living layer | Agentic systems: the layer that runs agents, enforces policy and watches everything |
| **Role agents** | Exec hats | Six agents, one per job: CEO, Engineer, CFO, Counsel, Data Steward, Growth |

Unchanged because they were already literal: Buyers, Contributors, Treasury, Transparency log, Bounty, Canary rows, Grades, Tiers, Go-live gate.

**Company name.** Data Dealer is separate from the system names and stays Astra's call. Without the casino theme, "dealer" reads as "trader". A lawyer should still check whether the name invites "data broker" treatment.

**Files renamed:** `.claude/agents/dealer.md` → `sourcing-agent.md`, `assayer.md` → `verifier.md`, `pit-boss-judge.md` → `eval-judge.md`. The v1 diagram in `docs/process-flow.*` keeps the old names as history.
