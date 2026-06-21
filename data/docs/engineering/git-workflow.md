# Git Workflow

**Owner:** Engineering · **Last updated:** 2025-03-15 · **Doc ID:** ENG-GIT-015

## Branching
We use trunk-based development. Branch off `main`, name branches `<type>/<ticket>-<short-desc>`
(e.g. `feat/VEL-1234-add-rerank`). Keep branches short-lived (< 3 days).

## Commits
Use Conventional Commits: `feat:`, `fix:`, `chore:`, `docs:`, `refactor:`. Squash-merge into `main`.

## Code review
Request review via GitHub. Reviewers respond within **1 business day**. Do not merge your own PR
without an approval, even for trivial changes.

## Hotfixes
For urgent production fixes, branch `hotfix/<ticket>`, get expedited review, and deploy following ENG-REL-011.
