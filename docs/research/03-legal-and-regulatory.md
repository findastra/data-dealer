# Legal and regulatory landscape

*Research note · Claude Opus 5.5 · 6 Oct 2026. Not legal advice; this is a briefing for a lawyer conversation.*

## Disclosure laws create our demand
**EU AI Act, general-purpose AI (Article 53).** Providers must keep technical documentation, publish a training-data summary, maintain a copyright-compliance policy and give downstream providers information. Obligations applied from 2 Aug 2025; the Commission's AI Office gained enforcement powers on 2 Aug 2026. Fines reach 3% of global turnover or €15M, whichever is higher. [CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-gpai-enforcement-20260509-csa-st/)

**California AB 2013** (in force 1 Jan 2026). Developers of public generative AI systems must post high-level summaries covering 12 categories: sources/owners, purpose fit, number of data points, data types, copyrighted/trademarked/patented/public-domain content, whether data was purchased or licensed, personal information, aggregate consumer information, cleaning/processing, collection period, first-use dates, and synthetic data generation. xAI has challenged it as an unconstitutional taking of trade secrets. [Goodwin](https://www.goodwinlaw.com/en/insights/publications/2026/01/alerts-otherindustries-californias-ab-2013-takes-effect)

**What this means for us:** every manifest should export those 12 categories and the EU summary fields. That export is the verify & compliance API.

## Copyright: sourcing is where liability lives
| Case | Where it stands |
| --- | --- |
| Bartz v. Anthropic | Training on lawfully acquired books held fair use (Jun 2025); pirated copies were not. $1.5B settlement, final approval 20 Jul 2026, about $3,000 per work. [Authors Guild](https://authorsguild.org/news/court-grants-final-approval-anthropic-copyright-settlement/) |
| Kadrey v. Meta | Summary judgment for Meta on training (Jun 2025), framed narrowly; appeal on piracy theories pending |
| Thomson Reuters v. Ross | Fair use rejected where the AI product competed directly (Feb 2025); on appeal |
| NYT v. Microsoft & OpenAI | Aug 2026: some claims dismissed; direct infringement, vicarious infringement and DMCA claims proceed |
| Getty v. Stability, music publishers v. Anthropic, Disney v. Midjourney | Ongoing |

Case statuses from a public tracker: [you.com](https://for.you.com/posts/ai-copyright-case-tracker-courts-split-as-suits-multiply-400ec211)

**Lesson:** courts have been more forgiving about *training* than about *how the data was obtained*. A provable acquisition chain is the product.

## Duties from hosting uploads
- **Child safety (REPORT Act, signed 7 May 2024):** providers with actual knowledge of apparent CSAM must report to NCMEC's CyberTipline, preserve the material for one year, and secure it per the NIST framework. First-violation fines up to $600K (≤100M monthly users). Hash-match scanning at Intake (Thorn Safer or PhotoDNA) before any person or model sees a file. [Wilson Sonsini](https://wsgr.com/en/insights/new-minor-safety-obligations-for-online-services-report-act-expands-child-sexual-exploitation-reporting-requirements.html)
- **Personal data (GDPR, CCPA):** right to erasure. Lock only scrubbed data; crypto-shred raw files. [Impossible Cloud](https://www.impossiblecloud.com/magazine/s3-object-lock-and-gdpr-navigating-compliance-in-2026-new)
- **DMCA:** register a designated agent; run takedowns through the Shift Manager desk.

## Contracts to have drafted
1. **Contributor agreement:** ownership attestation, license grant (including synthetic derivatives), consent scope, indemnity, royalty terms, holdback, termination and recall.
2. **Deck license:** permitted uses (ODRL terms mirror it), no resale, tier rules, audit rights, canary-row notice.
3. **Terms for agent buyers:** who is bound when an agent buys (the account owner), spending-policy responsibility.
4. **Founder agreement:** equity, vesting (4 years, 1-year cliff), IP assignment to the company, roles, decision rights, departure terms. Each founder should check their employer's invention-assignment and outside-activity policies first.

## Questions for a lawyer
- Does the contributor license cover synthetic derivatives and their resale?
- Which states/countries can contributors come from at launch?
- Is a royalty to contributors a securities, employment or tax-reporting issue at our scale?
- Exclusive license structure and liability caps.
