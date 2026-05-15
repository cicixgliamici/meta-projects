# Commits, Branches, and Merges

A practical guide for team collaboration with Git.

## 1) Commits

Best practices:

- One commit = one logical change.
- Write clear commit messages.
- Avoid "WIP" commits on shared branches.

Examples:

```text
Add health endpoint
Fix /health test response
Update README with setup steps
```

## 2) Branches

Suggested naming pattern:

- `main`: stable production-ready branch
- `feature/<name>`: new features
- `fix/<name>`: bug fixes
- `docs/<name>`: documentation updates

## 3) Merges

Recommended approach:

1. Open small PRs that are easy to review.
2. Ensure CI checks pass before merging.
3. Merge only after review approval.

## 4) Pre-merge checklist

- [ ] `git status` is clean
- [ ] local tests pass
- [ ] PR description is updated
- [ ] no unresolved conflicts
