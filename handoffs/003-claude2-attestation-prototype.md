status: open
for: claude-2
needs: skills/provenance-manifest/SKILL.md, docs/research/02-provenance.md, docs/guardrails.md
---
## Task
Build the first runnable piece of the system: a local Attestation prototype in `prototype/attestation/` (Python, standard library + `cryptography`).
1. `manifest.py build <folder>`: SHA-256 every file and every 10,000-row chunk of any CSV/Parquet, build a Merkle root, write `manifest.json` with the fields listed in the provenance skill (use placeholder contributor and model entries).
2. `manifest.py sign`: canonical JSON (RFC 8785 style: sorted keys, no whitespace), Ed25519 signature with a local key file (never committed; `.gitignore` it).
3. `manifest.py verify <folder>`: recompute hashes, check the root and the signature; exit non-zero on any mismatch.
4. A test that changes one byte and proves verification fails.

## Done when
`python -m pytest prototype/attestation` passes, and the README in that folder shows the three commands. Record your model name and version in the README.

## Return
Branch `claude-2/003`, pull request to main, set this card to `status: done` in the PR.
