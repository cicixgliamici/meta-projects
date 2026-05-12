# Git & GitHub - Interview Q&A

### 1. What is the difference between `git merge` and `git rebase`?
**Answer:** 
Both integrate changes from one branch to another, but in different ways.
- `git merge` takes two divergent branches and creates a new "merge commit" tying them together. It preserves the exact chronological history of the commits, but it can make the log messy.
- `git rebase` "moves" the base of your current branch to the tip of the target branch (e.g., main), rewriting the project history to make it perfectly linear. It is cleaner, but dangerous on public/shared branches because it changes commit hashes.

### 2. What happens if I do a `git push --force`?
**Answer:** 
You destructively overwrite the remote branch history with your local history. If other developers had downloaded the remote branch and were working on commits that you removed, their work will be detached, causing huge problems. Only use it on personal branches (like your unmerged Pull Requests) after a `rebase` or a `commit --amend`.

### 3. How do you resolve a merge conflict?
**Answer:** 
1. I run `git pull` (or merge/rebase). Git stops and warns me of a conflict.
2. I open the conflicting files. Git will have inserted conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
3. I manually edit the file, choosing which code to keep (or use a visual tool in my IDE).
4. I save the file, stage it with `git add`, and complete the operation with `git commit` (or `git rebase --continue`).

### 4. What is a `git stash`?
**Answer:** 
It is a feature that allows you to temporarily save your local (uncommitted) changes by putting them "aside" on a stack, giving you a clean working directory. It is useful if you suddenly have to switch branches to fix an urgent bug. You can then restore your changes later using `git stash pop`.

### 5. What is the difference between a Fork and a Branch?
**Answer:** 
- A **Branch** is an independent line of development within the *same* repository.
- A **Fork** is a complete copy of the repository (often under another user's personal account). It is used in Open Source projects when you do not have write access to the original repository: you fork it, develop on your fork, and then open a Pull Request against the original repo.
