# Deployment & Release Process

**Owner:** Platform Team · **Last updated:** 2025-05-10 · **Doc ID:** ENG-REL-011

## CI/CD
All merges to `main` trigger a CI pipeline (GitHub Actions): lint, unit tests, integration tests,
container build. Green builds auto-deploy to `staging`.

## Promotion to production
Production deploys happen via a manual approval in the pipeline. Any engineer can deploy; a second
engineer must approve. We deploy multiple times per day.

## Deploy freeze
A **deploy freeze** applies on Fridays after 14:00 and during the end-of-quarter week, unless it is
a SEV1 fix approved by an engineering manager.

## Rollback
Use `velactl rollback <service> <version>` or revert the deploy in the pipeline. Target rollback
time is under 10 minutes. Feature flags (PROD-FLAG-020) are the preferred way to disable risky code.
