# Synthetic data: what makes it worth buying

*Research note · Claude Opus 5.5 · 6 Oct 2026*

## Model collapse, and how to avoid it
Training generative models on their own outputs degrades them when synthetic data **replaces** real data generation after generation. When synthetic data **accumulates alongside** the original real data, test error stays bounded and collapse is avoided. The result held across language models, diffusion models and VAEs, with a proof for linear models. [Gerstgrasser et al., 2024](https://arxiv.org/abs/2404.01413v2)

**Design consequences**
- Every synthetic Deck names its real seeds in its lineage, so buyers can keep real data in the mix.
- Sell seed + synthetic bundles, not synthetic alone, for training use.
- Track generation depth: never generate from synthetic rows (depth stays 1).

## Scoring a Forge batch
| Dimension | Question | Typical method |
| --- | --- | --- |
| Fidelity | Does it look like the seeds statistically? | Column distributions, correlations (SDMetrics) |
| Diversity | Is it more than reworded copies? | Embedding spread, n-gram novelty |
| Privacy | Is any row too close to a real person's record? | Distance to closest record vs. a holdout baseline; membership-inference test |
| Usefulness | Does a model trained on it do well on real data? | Train on synthetic, test on held-out real |
| Correctness | Are the facts right? | Pit Boss judge panel on a random sample |

## Generator licensing
API providers' terms can restrict using outputs to train other models, so generation uses Apache-2.0 or MIT open-weight models. Llama-family licenses add naming and attribution duties; Apache-2.0 and MIT releases (many Qwen, Mistral and gpt-oss releases) impose minimal restrictions. Confirm the license on each model card before use and record it in the manifest. [License comparison](https://wz-it.com/en/knowledge/ki/open-llm-licenses-commercial-use/)

## Judge independence
A judge from the same family as the generator shares its blind spots and tends to approve its style. Rule: three judge families, none matching the generator. Escalate to a human when families disagree on more than 10% of rows.

## Pass bar
Score at least 300 sampled rows per batch and pass only if the **95% upper confidence bound** on the error rate is below 5% (upper end of the two-sided 95% Clopper–Pearson interval). With 300 rows and 6 errors (2%), the upper bound is 4.3%, a pass; with 10 errors (3.3%), it is 6.0%, a fail.
