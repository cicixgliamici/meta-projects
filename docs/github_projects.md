# GitHub Projects & Issue Tracking

While Git tracks code, delivering software successfully requires tracking work, bugs, and requirements. GitHub provides a native project management tool called **GitHub Projects**.

## Key Components

### 1. Issues
Issues are the fundamental tracking unit. They can represent bugs, feature requests, or user stories.
- **Labels**: Used to categorize issues (e.g., `bug`, `enhancement`, `good first issue`).
- **Assignees**: Shows who is actively working on the task.
- **Milestones**: Used to track progress on groups of issues or pull requests (e.g., "v1.0.0 Release").

### 2. Pull Requests (PRs) linked to Issues
A best practice in GitHub is to link a PR to the issue it resolves. If you write `Fixes #12` or `Closes #12` in your PR description, GitHub will automatically close Issue #12 when the PR is merged into `main`.

### 3. Projects (Kanban Boards)
GitHub Projects allows you to visualize your issues and pull requests as cards on a board. 
- **Classic Kanban**: Columns like `To Do`, `In Progress`, `In Review`, `Done`.
- **Automation**: You can set up workflows so that when a developer creates a PR linked to an issue, the issue card automatically moves to the `In Review` column.

## Agile Workflow Example

1. **Planning**: The Product Owner writes user stories as **Issues** and assigns them to the upcoming **Milestone**.
2. **Prioritization**: Issues are placed in the `To Do` column of the **Project** board.
3. **Development**: A developer assigns the issue to themselves, moves it to `In Progress`, and creates a local branch.
4. **Review**: The developer opens a **Pull Request** (linking the issue). The card auto-moves to `In Review`.
5. **Delivery**: The PR is approved and merged. The issue automatically closes and moves to `Done`.
