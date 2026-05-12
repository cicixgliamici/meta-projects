# Git Commands Cheatsheet

A compact list of commonly used Git commands.

## Setup

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Create a repository

```bash
git init
```

## Check status

```bash
git status
```

## Stage files

```bash
git add file.txt
git add .
```

## Commit

```bash
git commit -m "Meaningful message"
```

## View history

```bash
git log
git log --oneline
git log --oneline --graph --all
```

## Branching

```bash
git branch
git switch -c feature/my-feature
git switch main
```

## Merge

```bash
git merge feature/my-feature
```

## Remote

```bash
git remote -v
git remote add origin git@github.com:user/repo.git
```

## Push and pull

```bash
git push
git push -u origin feature/my-feature
git pull
```

## Useful undo commands

```bash
git restore file.txt
git restore --staged file.txt
git commit --amend
```
