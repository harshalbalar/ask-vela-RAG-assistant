# Data Classification & Handling Policy

**Owner:** Security · **Last updated:** 2025-03-30 · **Doc ID:** IT-SEC-013

## Classification levels
- **Public** — marketing site, public docs. No restrictions.
- **Internal** — most company docs. Share only inside Vela Cloud.
- **Confidential** — customer data, financials, employee PII. Encrypt in transit and at rest.
- **Restricted** — secrets, encryption keys, security findings. Access on a strict need-to-know basis.

## Security incident reporting
A **security incident** (suspected breach, leaked credential, exposed customer data) must be
reported within **1 hour** to `#security-incident` and security@velacloud.example. Do not investigate
on your own. This is distinct from engineering outages (see ENG-INC-009).

## Customer data
Never copy customer (Confidential) data to a local machine or a personal account. Use approved,
access-controlled tooling only.
