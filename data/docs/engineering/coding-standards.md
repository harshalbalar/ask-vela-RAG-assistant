# Coding Standards

**Owner:** Engineering · **Last updated:** 2025-02-28 · **Doc ID:** ENG-STD-012

## General
Code must pass automated linting and formatting before review. We use `gofmt` (Go), `rustfmt` (Rust),
and Prettier + ESLint (TypeScript).

## Pull requests
Keep PRs under ~400 lines where possible. Every PR needs at least **one approving review** and a
green CI run before merge. PR descriptions must link the relevant ticket.

## Testing
New features require unit tests. Bug fixes require a regression test reproducing the bug. We target
**>80% line coverage** on core services.

## Documentation
Public functions and APIs must have doc comments. Update the relevant wiki page in the same PR as a behavior change.
