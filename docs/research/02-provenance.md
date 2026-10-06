# How to preserve provenance — and is it just standard deviation?

*Research note for Data Dealer · Claude Opus 5.5 · 6 Oct 2026*

## Short answer
No. Standard deviation (and every other summary statistic) is a **fingerprint**, useful as evidence, but it cannot prove where data came from:

- **Not unique.** Infinitely many different datasets share the same mean and standard deviation. Two people can upload different data with identical statistics.
- **Forgeable.** Anyone can generate data matching a target mean and standard deviation in a few lines of code.
- **Fragile in the wrong way.** Legitimate cleaning (dedupe, scrubbing a name) changes the statistics; a malicious swap that preserves them doesn't.
- **Silent on rights.** Statistics say nothing about who made the data, what they consented to, or which license applies, and that is what buyers are being sued over.

"Exact" measurement of data is done with **cryptographic hashes**, not statistics: change one bit and a SHA-256 hash changes completely, and nobody can construct a different file with the same hash.

## What provenance actually needs: four layers
| Layer | Question it answers | Mechanism | What breaks without it |
| --- | --- | --- | --- |
| 1. Rights | Who made it, and what did they agree to? | ID-verified contributor, e-signed attestation of ownership, license grant, consent scope | You can prove the bytes but not that you were allowed to sell them |
| 2. Integrity | Are these the exact bytes? | SHA-256 per file and per row-chunk → Merkle root | Silent tampering or swaps |
| 3. Lineage | What happened to it? | W3C PROV graph: seed → prompt + model → generated rows → filters → judges → Deck | Synthetic data with no link to its seeds, no record of which models touched it |
| 4. Accountability | Can anyone rewrite history, including us? | Ed25519 signature over the canonical manifest + entry in an append-only transparency log | A signed manifest can be quietly replaced with another signed manifest |

### Layer 2 in practice: Merkle trees
Hash every file and every 10,000-row chunk. Pair hashes and hash the pairs, up to a single **Merkle root**. The root commits to every row. A buyer can verify the whole Deck by recomputing it, and you can prove one chunk belongs to a Deck by revealing only that chunk plus a short path of hashes, without exposing the rest.

### Layer 3 in practice: lineage standards
- **Croissant 1.1** (MLCommons) adds W3C PROV-O lineage and ODRL machine-readable usage rules to dataset metadata, so lineage and license terms travel inside `croissant.json`. [ODI](https://theodi.org/news-and-events/blog/croissant-11/)
- **Data Provenance Standard** v1.0 from the Data & Trust Alliance is being formalized at OASIS; it tags source, lineage, legal rights and collection metadata. [OASIS](https://groups.oasis-open.org/discussion/call-for-participation-data-provenance-standard-dps-tc)
- **C2PA** (v2.3, Dec 2025) signs provenance into images and video. Useful when contributors' photos already carry it, but platforms strip the metadata on upload, so we keep our own record and don't rely on it. [SoftwareSeni](https://softwareseni.com/c2pa-adoption-in-2026-hardware-platforms-and-verification-reality)

### Layer 4 in practice: sign and log
- **Signing:** AWS KMS has supported Ed25519 (EdDSA) keys since 7 Nov 2025, with 64-byte signatures. Only the Ledger's deterministic signer has `kms:Sign`. [AWS](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-kms-edwards-curve-digital-signature-algorithm/)
- **Logging:** a transparency log is an append-only, publicly auditable record of signatures. Sigstore's Rekor v2 (tile-based, cheaper to run) went GA on 10 Oct 2025; we can use the public instance pattern or self-host a tile log. [Sigstore](https://blog.sigstore.dev/rekor-v2-ga/)
- **Canonical JSON:** sign the RFC 8785 canonical form so whitespace or key order can't change the signature.

## Where statistics do help
| Use | How | Stage |
| --- | --- | --- |
| Synthetic fidelity | Compare distributions, correlations, embeddings of synthetic vs. seed | Forge scoring |
| Privacy | Distance to closest real record; membership-inference tests, so synthetic rows aren't near-copies of seeds | Forge filter |
| Near-duplicates and origin | MinHash for text, PDQ perceptual hashes for images, embedding search against the web and our own vault | Assay |
| Drift | Profile each new seed batch against the Deck it extends | Assay / Forge |
| Leak tracing | Unique canary rows per buyer copy | Shoe |
| Proving a model trained on your data | Data watermarks: publish one watermarked rephrasing, keep others secret, compare model likelihoods (STAMP, ICML 2025) | Post-sale enforcement |

STAMP detected datasets that appeared only once in training, under 0.001% of tokens. [PMLR](https://proceedings.mlr.press/v267/rastogi25a.html)

**Rule of thumb: cryptography proves, statistics suggest.** Use statistics to decide what to check; use hashes, signatures and logs to prove what you claim.

## Manifest contents (minimum)
```
deck_id, version, grade, tier
merkle_root, file hashes, chunk size
contributors[]: pseudonymous id, agreement version, license, consent scope, ID-check reference
assay[]: checks run, tool versions, results, reviewer (model id or person)
lineage: PROV graph (seeds → prompts + models → rows → filters → judges)
models[]: model id, version, provider, license, role, what it saw
judges[]: seat, model id, rows scored, error rate, 95% upper bound
usage_policy: ODRL terms
compliance_exports: AB 2013 categories, EU training-data summary fields
signature, log_entry_id, revoked (bool)
```

## Recall
Revocation is a new log entry pointing at the old one, never a deletion. The Floor desk triggers it; the Shoe notifies every buyer of that Deck; the Cage freezes held royalties.

## Erasure vs. immutability
Write-once storage and GDPR erasure conflict only if personal data is what's locked. Lock only scrubbed seeds and hashes. Keep raw uploads in quarantine under a per-file KMS key; destroying the key makes the file unreadable (crypto-shredding). For backups that can't be erased immediately, regulators accept data that is "put beyond use" until it expires. [Impossible Cloud](https://www.impossiblecloud.com/magazine/s3-object-lock-and-gdpr-navigating-compliance-in-2026-new)
