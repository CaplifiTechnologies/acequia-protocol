# Contributing to Ditch AI

Ditch AI is a commons standards body for governed infrastructure under AI.
Contributions are welcome from anyone with a legitimate interest in governed
commons infrastructure, civic computing, environmental stewardship, or
related fields.

## Before you start

Read the [Participation Agreement](contract-desk/drafts/ditch-ai-participation-agreement.md)
(draft). By submitting a contribution you agree to its terms, including the
IP provisions in Section 5.

## What you can contribute to

| Area | Path | License | Notes |
|------|------|---------|-------|
| **Primitives** | `app/acequia.py` | Apache 2.0 | The 9 inference primitives |
| **Headgate** | `app/headgate.py` | Apache 2.0 | Composable governance gate |
| **Tests** | `tests/` | Apache 2.0 | Always welcome |
| **Specs** | `specs/` | CC-BY-4.0 | Standards documents — proposals, drafts, reviews |
| **Docs** | `docs/` | CC-BY-4.0 | Guides, tutorials, examples |

### Fenced areas

The following require steward review and may involve held IP. PRs touching
these paths will not merge without explicit steward approval:

- `app/mayordomo.py` — origami fold engine integration (IP held)
- `app/tuner.py` — agent tuning system
- `founding/` — governance documents
- `brand/` — brand and identity
- `LICENSE`, `LICENSE-SPECS` — licensing terms

## How to contribute

1. **Fork** the repository.
2. **Branch** from `main`. Name your branch `<type>/<short-description>`
   (e.g., `fix/weir-edge-case`, `spec/resilience-gate-review`, `test/antenna-scan`).
3. **Write tests** for code changes. Every primitive change needs a test.
   Every headgate change needs a conformance test.
4. **Run the gate checks** locally before pushing:
   ```bash
   ./scripts/ci-gate.sh
   ```
5. **Sign off** every commit with the Developer Certificate of Origin:
   ```bash
   git commit -s -m "your message"
   ```
   This adds `Signed-off-by: Your Name <your@email.com>` to the commit.
6. **Open a PR** against `main`. Describe what changes and why.

## Commit messages

```
<type>: <short summary>

<optional body — what changed and why>

Signed-off-by: Your Name <your@email.com>
```

Types: `feat`, `fix`, `spec`, `test`, `docs`, `refactor`, `ci`.

## Code standards

- Python 3.11+. No external dependencies in the core primitives.
- The five forbidden check types in the headgate (`identity`, `worthiness`,
  `political_alignment`, `ability_to_pay_premium`, `end_use_value`) are
  load-bearing. A PR that weakens or removes a forbidden check will not merge.
- Headgate defaults protect whoever has least leverage. A PR that changes a
  default to favor the gate operator will not merge.
- Append-only ledgers are append-only. A PR that adds delete or overwrite
  to a ledger will not merge.
- The weir proportions; it does not block. A PR that turns a weir into a
  binary gate will not merge.

## Review process

- Every PR requires at least one review from a non-author.
- The steward (CODEOWNERS) reviews all PRs during the formation period.
- Specs follow the standards lifecycle: Proposal → Draft → Review →
  Candidate → Ratified. A PR to advance a spec's stage requires the voting
  threshold from the Participation Agreement.

## CI gate checks

The CI pipeline runs these automated checks on every PR:

1. **IP fence** — no held IP markers cross into the public package
2. **House path scan** — no references to private infrastructure paths
3. **Secret scan** — no API keys, tokens, private keys, or credentials
4. **Test suite** — all tests must pass
5. **DCO** — every commit must be signed off

If a gate check fails, the PR cannot merge. Fix the issue and push again.

## Reporting issues

Open an issue. Label it:
- `bug` — something broken
- `spec-proposal` — a new standard or amendment
- `question` — clarification about the protocol
- `security` — report privately (see SECURITY.md when published)

## No self-attestation

Per Section 4.3 of the Participation Agreement: the Founding Steward and
any vendor offering products built on Acequia Protocol standards may not
self-attest compliance. Compliance attestation requires review by at least
one independent participant.

## License

Code contributions are licensed under Apache 2.0 (see LICENSE).
Spec contributions are licensed under CC-BY-4.0 (see LICENSE-SPECS).
