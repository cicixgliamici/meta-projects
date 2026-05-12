# Lab 01 — Git Basics

## Goal

Create a local Git repository and make your first commits.

## Steps

```bash
mkdir git-basics-demo
cd git-basics-demo

git init

echo "# Git Basics Demo" > README.md

git status
git add README.md
git commit -m "Add README"

echo "This is my first Git lab." >> README.md

git diff
git add README.md
git commit -m "Update README with description"

git log --oneline
```

## Expected result

You should see two commits in the history.

Example:

```text
abc1234 Update README with description
def5678 Add README
```

## Questions

1. What is the difference between `git status` and `git log`?
2. What does `git add` do?
3. Why should commit messages be meaningful?
