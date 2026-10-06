# Agents and payments: the harness and the rails

*Research note · Claude Opus 5.5 · 6 Oct 2026*

## Agent harness: Claude Managed Agents
A pre-built, configurable agent harness running in managed infrastructure (beta; header `managed-agents-2026-04-01`). Four concepts: **agent** (model, system prompt, tools, MCP servers, skills), **environment** (Anthropic cloud sandbox or self-hosted sandbox on your infrastructure), **session** (a running instance), **events** (messages in and out, streamed). Also: permission policies, session budgets, multi-agent orchestration, scheduled deployments, webhooks. [Claude docs](https://platform.claude.com/docs/en/managed-agents/overview)

**Constraint that shaped our design:** Managed Agents is stateful and not currently eligible for Zero Data Retention or HIPAA BAA coverage. So the Assayer runs in a self-hosted sandbox, tools process raw files on our servers, and the model receives reports and scrubbed samples only.

| Agent | Harness | Why |
| --- | --- | --- |
| Dealer | Managed Agents, cloud sandbox | No raw data; needs long-running sessions and budgets |
| Assayer | Managed Agents, self-hosted sandbox | Raw files stay in our account |
| Forge | Dagster + vLLM batch jobs | A generation job, not an autonomous agent |
| Pit Boss judges | Inspect AI eval runner | Reproducible scoring, logged per run |
| Exec hats | Scheduled Claude sessions now; Managed Agents scheduled deployments later | Weekly cadence |

## MCP
Anthropic donated the Model Context Protocol to the new Agentic AI Foundation (a directed fund under the Linux Foundation) on 9 Dec 2025, co-founded with Block and OpenAI, supported by Google, Microsoft, AWS, Cloudflare and Bloomberg. An MCP server is how agent buyers reach The Table. [Anthropic](https://anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)

## x402 (agent payments)
HTTP 402 turned into a payment handshake: server returns price details, agent signs a gasless stablecoin authorization, a facilitator settles on-chain (mostly USDC on Base), server delivers. Coinbase published it in May 2025; the x402 Foundation (Coinbase + Cloudflare) followed in Sep 2025, and the Linux Foundation adopted it in Apr 2026 with members including Visa, Mastercard, Google, AWS, Circle, Stripe and Shopify. [Spark](https://www.spark.money/research/x402-protocol-ai-agent-payments)

| Pros | Cons |
| --- | --- |
| Agents pay without accounts or cards | No chargebacks or disputes in the protocol |
| Seconds to settle, tiny fees | Agents need KYC'd stablecoin balances |
| Backed by major payment companies | ~Half of early volume was tests and bots (165M transactions, ~$50M by Apr 2026) |

**Our use:** offer x402 alongside Stripe and AWS Marketplace, enforce budgets and allowlists ourselves at the Cage, and plan revenue on invoices and cards first.
