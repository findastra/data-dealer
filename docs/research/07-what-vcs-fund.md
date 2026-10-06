# What VCs fund, and how Data Dealer matches it

*Research note · Claude Opus 5.5 · 6 Oct 2026*

## What they say they want
- **Proprietary or rare data as the moat.** Over half of 20 VCs surveyed by TechCrunch named it as the differentiator, ahead of technology alone. Others stressed workflow stickiness, data quality and vertical depth. [TechCrunch](https://techcrunch.com/2025/01/10/vcs-say-ai-companies-need-proprietary-data-to-stand-out-from-the-pack)
- **Marketplace evidence.** a16z's 13 marketplace metrics: match rate, market depth, time to match, concentration, take rate, unit economics, multi-tenanting, switching costs, user and core-action retention cohorts, dollar retention, retention by geography, power-user curves. [a16z](https://a16z.com/2020/02/21/13-metrics-for-marketplace-companies)
- **Category proof.** a16z led Protege's $30M round in Jan 2026, and its partner framed the thesis as responsibly unlocking access to valuable data. [SiliconANGLE](https://siliconangle.com/2026/01/08/protege-raises-30m-grow-governed-marketplace-ai-training-data/)

## Qualities to build into the system (and where they live)
| What VCs look for | How Data Dealer has it | Where |
| --- | --- | --- |
| Proprietary data moat | Verified contributor network + provenance graph nobody else holds | Seed store, Attestation |
| Regulatory tailwind | Buyers owe AB 2013 and EU AI Act disclosures; our manifests export them | Verify & compliance API |
| Recurring revenue | Verify API subscription on top of transactional sales | Revenue stream 3 |
| Network effects | More seeds → more datasets → more buyers → more bounties → more contributors | Bounty loop |
| Improving margins | Repeat sales of a dataset carry no new compute | Money page |
| Defensibility via standards | Croissant 1.1, Data Provenance Standard, transparency log | Attestation |
| Risk discipline | Guardrails, human lane, recall drills | `docs/guardrails.md` |
| Measurable liquidity | Time-to-match, fill rate, repeat buyers on the dashboard | Growth role agent |
| Comparable exits | Gretel → NVIDIA, Human Native → Cloudflare | Market note |

## The metrics to show at a seed pitch
1. Paying pilots and revenue (even small), with logos or named personas.
2. Time from ticket to delivered dataset.
3. Verification pass rate and recall-drill time.
4. Gross margin on first sale vs. repeat sale.
5. Contributor time-to-first-payout and repeat-contribution rate.
6. Pipeline: letters of intent by vertical.

## Pitch deck structure
Standard practice is a short **teaser** (8–12 slides, read without you) that earns the meeting, then a longer **technical / diligence deck** for partners and their technical advisors. See `docs/pitch/`.
