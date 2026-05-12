# GitHub Actions

GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline directly within GitHub.

## Core Concepts

1. **Workflows**: A configurable automated process that will run one or more jobs. Workflows are defined by a YAML file checked into your repository (`.github/workflows/`).
2. **Events**: A specific activity in a repository that triggers a workflow run (e.g., `push` to main, opening a `pull_request`, or a `schedule` via cron).
3. **Jobs**: A set of steps in a workflow that execute on the same runner. By default, jobs in a workflow run in parallel, but you can configure them to run sequentially by defining dependencies.
4. **Steps**: An individual task that can run commands in a job. A step can be an *action* or a shell command.
5. **Actions**: Custom applications for the GitHub Actions platform that perform a complex but frequently repeated task (e.g., `actions/checkout@v4` checks out your repo).
6. **Runners**: A server that runs your workflows. GitHub provides Ubuntu Linux, Microsoft Windows, and macOS runners, but you can also host your own.

## Example Workflow Structure

```yaml
name: Example CI
on: [push] # The Event

jobs:
  build: # The Job
    runs-on: ubuntu-latest # The Runner
    steps: # The Steps
      - uses: actions/checkout@v4 # An Action
      - name: Run a script
        run: echo "Hello World" # A Shell command
```
