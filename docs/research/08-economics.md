# Economics: sustain, grow, limit

*Research note · Claude Opus 5.5 · 6 Oct 2026. All figures are illustrative assumptions to replace with pilot data.*

## Where cash comes from (green on the dashboard)
| Stream | Who pays | Timing | Character |
| --- | --- | --- | --- |
| Deck sales | Buyer | At order | Transactional, high margin on repeats |
| Bounties | Buyer, escrowed up front | Before work starts | Funds its own supply |
| Verify & compliance API | Buyers and their auditors | Monthly | Recurring |
| Exclusive licenses | One buyer | At signing | Lumpy, premium |

## Where cash goes
Contributor royalties (after a 30-day hold), payment fees, compute (Forge + judges), model APIs, cloud, legal, team.

## One $10,000 Deck sale (illustrative)
| Line | Assumption | Amount |
| --- | --- | --- |
| Buyer pays | Standard tier, grade B | $10,000 |
| Contributor royalty pool | 30% | −$3,000 |
| Payment processing | ~3% card | −$300 |
| Forge + judges compute | First build of this Deck | −$800 |
| **Gross profit** | **59%** | **$5,900** |

Second sale of the same Deck: no compute line → about 67% gross margin.

## Self-funding rules
1. Royalties are paid only from collected cash, after the holdback.
2. Compute ≤ 25% of trailing 90-day revenue once live; before revenue, a fixed monthly ceiling set by the founders.
3. Open bounties never exceed escrowed buyer money.
4. Under 6 months of runway, new bounties pause.

## Growth loop
Buyer ticket → bounty → contributors paid → verified seeds → Deck sold → repeat sales → more catalog → more buyers find a fit without a ticket (faster match, higher margin).

## Limits
See `docs/guardrails.md`. The system grows only inside those caps; the Shift Manager desk can stop anything.
