# Lab 02 — Branching Strategy

## Goal

Create a feature branch and merge it into `main`.

## Steps

```bash
git init branching-demo
cd branching-demo

echo "# Branching Demo" > README.md
git add README.md
git commit -m "Initial commit"

git switch -c feature/add-notes

echo "Some notes about branching." > notes.md
git add notes.md
git commit -m "Add branching notes"

git switch main
git merge feature/add-notes

git log --oneline --graph --all
```

## Expected result

The `main` branch should contain `notes.md`.

## Questions

1. Why are feature branches useful?
2. What is the difference between committing and merging?
3. What could go wrong if everyone pushed directly to `main`?
