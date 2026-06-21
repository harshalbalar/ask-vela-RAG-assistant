# Feature Flag Policy

**Owner:** Product Engineering · **Last updated:** 2025-04-28 · **Doc ID:** PROD-FLAG-020

Vela Cloud uses **LaunchDarkly** for feature flags. Flags are the preferred mechanism for shipping
risky changes and for gradual rollouts.

## Naming & ownership
Flag keys use `team.feature-name`. Every flag must have an owner and a description. Unowned flags are
flagged in the monthly audit.

## Rollout
Roll out new features progressively: internal → 5% of tenants → 25% → 100%. Monitor error rates and
VelaQL query latency at each stage before increasing.

## Cleanup
**Temporary flags must be removed within 60 days** of reaching 100%. Stale flags are technical debt and
are tracked in the quarterly cleanup. Permanent operational flags (kill switches) are exempt but must be labeled `permanent`.
