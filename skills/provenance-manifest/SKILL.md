---
name: provenance-manifest
description: Build, sign, log and verify a Data Dealer dataset manifest. Use when packaging a dataset, checking a manifest a buyer sent back, or revoking one.
---

# Provenance manifest

A manifest is proof, in four layers. Each layer answers a different question; none replaces another.

| Layer | Question | Mechanism |
| --- | --- | --- |
| Rights | Who made it and what did they agree to? | Signed contributor attestation (ID-verified), license, consent scope |
| Integrity | Are these the exact bytes? | SHA-256 per file and per row-chunk → Merkle root |
| Lineage | What happened to it? | W3C PROV graph: seed → prompt + model → rows → filters → judges → dataset (Croissant 1.1 carries PROV-O) |
| Accountability | Can anyone rewrite history? | Ed25519 signature (AWS KMS) + entry in an append-only transparency log |

## Build
1. Hash every file and every 10k-row chunk (SHA-256). Build the Merkle tree; record the root.
2. Collect: contributor IDs (pseudonymous), agreement versions, licenses, Verification reports, Synthesis prompts and seeds, **every AI model that touched the data** (model ID, version, provider, license, role), judge verdicts, grade, tier.
3. Write `manifest.json` and the matching PROV/ODRL fields in `croissant.json`.
4. Export the buyer's compliance view: the 12 California AB 2013 categories and the EU training-data summary fields we can fill.

## Sign and log
1. Canonicalize JSON (RFC 8785), sign with Attestation's Ed25519 KMS key. Only the deterministic signer service holds `kms:Sign`; no model ever does.
2. Append `{deck_id, merkle_root, manifest_sha256, signature}` to the transparency log.
3. Publish the lookup at the public verify page.

## Verify (buyer side)
Recompute hashes → compare Merkle root → check signature with the published public key → confirm the log entry and that it is not revoked.

## Revoke
Review desk only. Append a revocation entry (never delete), mark the dataset withdrawn, notify every buyer of that dataset, freeze held royalties.

## What statistics are for
Distribution fingerprints (means, standard deviations, quantiles, correlations, embeddings) score synthetic fidelity, catch drift and near-duplicates, and support leak detection with canary rows. They are **evidence**, not **proof**: many different datasets share the same standard deviation, and anyone can forge one.
