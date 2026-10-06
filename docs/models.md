# Model roster — every AI model in the system

Any model that touches dataset data is written into that dataset's signed manifest: model ID, version, provider, license, role, and what it saw. Add a row here **before** a model enters the system; the weekly brief fails the roster audit otherwise.

| Model | Provider | Family | License / terms | Job | Sees | In manifest |
| --- | --- | --- | --- | --- | --- | --- |
| Claude Opus 5.5 (`claude-opus-5-5`) | Anthropic API | Claude | Anthropic commercial terms | Sourcing agent; CEO, Engineer, Counsel role agents; built the dashboard | Buyer specs, catalog metadata, repo, news | No dataset data |
| Claude Sonnet 5.5 (`claude-sonnet-5-5`) | Anthropic API, tools in self-hosted sandbox | Claude | Anthropic commercial terms | Verifier; CFO, Data Steward, Growth role agents | Tool reports and scrubbed samples, never raw files | Yes |
| spaCy `en_core_web_lg` (inside Presidio) | Self-hosted | spaCy | MIT | Finds personal data | Raw uploads, on our servers only | Yes |
| `all-MiniLM-L6-v2` embeddings | Self-hosted | sentence-transformers | Apache-2.0 | Near-duplicate and origin search | Scrubbed text | Yes |
| Qwen, Apache-2.0 release (confirm per model card) | Self-hosted vLLM | Qwen | Apache-2.0 | Synthesis generator | Scrubbed seeds | Yes |
| Claude Haiku 4.5 (`claude-haiku-4-5`) | Anthropic API | Claude | Anthropic commercial terms | Eval panel judge 1 | Sampled rows + seed spec | Yes |
| Astra (OpenAI GPT; GPT-6 per Astra's setup) | OpenAI API | OpenAI | OpenAI terms; verdicts only, never training rows | Eval panel judge 2; second opinion on the weekly brief | Sampled rows + seed spec | Yes |
| Mistral, Apache-2.0 release | Self-hosted vLLM | Mistral | Apache-2.0 | Eval panel judge 3 | Sampled rows + seed spec | Yes |
| Claude on Astra's second account | Claude app, human-driven | Claude | Consumer subscription | Red-team reviews from `handoffs/` | Repo docs only | No dataset data |

## Not AI (listed so nobody mistakes them for models)
SHA-256, Merkle trees, MinHash, PDQ perceptual hashing, Ed25519 signatures, OPA policies, SciPy confidence bounds.

## Rules
- **Independence:** three judge families, none matching the generator's. Today: generator = Qwen; judges = Claude, OpenAI, Mistral.
- **Rights chain:** API providers' terms can restrict using outputs to train other models, so only Apache-2.0 / MIT open-weight models generate rows.
- **Data location:** raw files are processed by self-hosted tools only. Claude Managed Agents is not currently eligible for Zero Data Retention or HIPAA BAA coverage, so hosted agents get reports and scrubbed samples, not raw uploads.
- **Production access:** judges and agents run on API keys under a company account, not on personal chat subscriptions.
