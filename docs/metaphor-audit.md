# Name and metaphor audit

*6 Oct 2026 · Claude Opus 5.5. Casino roles checked against published descriptions of casino staff (sources at the end).*

## Who is the dealer?
Two things were called "dealer": the company (Data Dealer) and the AI agent at The Table. In a casino, the **house** owns the games and the **dealer** is the house's employee who runs one table. So: **Data Dealer, the company, is the house.** The agent is the employee at the table who takes buyers' requests.

The catch: a real dealer also handles chips and pays out bets. Our agent is deliberately never allowed to touch money. That makes "Dealer" a partly wrong name for it. **Proposed:** rename the agent **Host**. A casino host looks after players' requests and arranges special treatment, and doesn't handle chips. That matches the agent's job exactly and leaves "Dealer" meaning only the company.

## Verdicts
| Name | What it means in real life | Our job | Verdict | Action |
| --- | --- | --- | --- | --- |
| Data Dealer (company) | The house that deals | Sells verified data | Works, with risk | Plain-English tagline next to it; ask a lawyer whether the name invites "data broker" treatment (several states regulate data brokers); test with 3–5 buyers |
| The Table | Where players and the house do business | API + MCP server | Accurate | Keep |
| Dealer (agent) | Runs a table **and handles chips** | Quotes, previews, bounties; never money | Partly wrong | **Proposed: rename to Host** |
| The Cage | Casino cashier | Payments, escrow, payouts | Accurate | Keep |
| The Shoe | Box that deals cards one at a time | Delivery | Accurate | Keep |
| The Deck | A set of cards, shuffled and dealt | Packaged dataset product | Fair | Keep; call the pitch materials "teaser" and "diligence slides" so "deck" means one thing |
| Pit Boss | Supervises the tables, catches errors and cheating, can stop play | Three-judge quality panel | Accurate | Keep. (Real pit bosses settle serious disputes themselves; ours escalates.) |
| Floor desk | Floorpersons work **under** the pit boss | Human escalations above the Pit Boss | **Wrong** (backwards) | **Fixed: renamed Shift Manager.** The shift manager sits above pit bosses and makes the calls they can't |
| Bounty | Reward for delivering something specific | Paid data request | Accurate | Keep |
| The Source | Where something comes from | Contributor sign-up | Accurate | Keep |
| Intake / quarantine | Isolate until checked | Encrypt, hash, scan uploads | Accurate | Keep |
| The Assay | Testing ore for purity before paying | Verification | Accurate | Keep |
| Seed vault | Bank of original seeds | Store of verified real data | Accurate | Keep; in code say "seed rows" so nobody confuses it with a random seed |
| The Forge | Shapes metal into goods, **but "forge" also means fake** (forgery) | Seed → synthetic | **Risky** for an authenticity business | **Proposed: rename to Greenhouse** (grows new plants from seeds; every plant traces to its seed, matching the logo). Alternative: Mint |
| The Ledger | Book of record | Manifest + signature | Accurate | Keep; say "not a blockchain" to investors |
| Transparency log | Technical term | Public append-only record | Accurate | Keep |
| Canary rows | Canary in a coal mine; "canary tokens" in security | Leak tracing | Accurate | Keep |
| Treasury | Where the money is kept | Platform share | Accurate | Keep |
| Living layer, exec hats | Plain phrases | Backend agents; role agents | Fine | Keep |

## Mixed metaphors
Two families are in use: casino and mining/farming. Rule that keeps it clear: **casino names for the front of house** (where buyers and money are: Table, Host, Cage, Shoe, Deck, Pit Boss, Shift Manager), **production names for the back of house** (Source, Intake, Assay, Seed vault, Greenhouse, Ledger).

## The casino frame itself
Casinos imply chance and "the house always wins". That's fun inside the company and in the brand voice, but it sends a mixed message to contributors who want a fair cut and to buyers' legal teams buying certainty. Use plain names in contracts, buyer documentation and the public verify page.

## Decisions for Astra
Approve or reject on the dashboard (Assignments):
1. Rename the agent Dealer → Host.
2. Rename The Forge → Greenhouse (or Mint).
3. Plain names in contracts and buyer docs; casino names inside.

Sources: [Dummies: the casino's cast of characters](https://www.dummies.com/article/home-auto-hobbies/games/betting/meeting-the-casinos-cast-of-characters-200979) · [Truest: casino shift manager](https://www.truest.me/careers/casino-shift-manager)
