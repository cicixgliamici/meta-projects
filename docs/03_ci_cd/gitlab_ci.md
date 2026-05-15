# GitLab CI/CD

GitLab CI/CD is a built-in tool for software development using continuous methodologies. Unlike GitHub where actions are in `.github/workflows/`, GitLab relies on a single `.gitlab-ci.yml` file placed at the root of the repository.

## Core Concepts

1. **Pipelines**: The top-level component, comprising jobs and stages.
2. **Stages**: Define *when* to run the jobs (e.g., `build`, `test`, `deploy`). Jobs in the same stage run in parallel. Jobs in the next stage run after the previous stage completes successfully.
3. **Jobs**: Define *what* to do (e.g., compile code, run tests).
4. **GitLab Runners**: Applications that run jobs in a pipeline. You register runners to your GitLab instance. They can be shared or specific to a project.

## GitHub Actions vs. GitLab CI

| Feature | GitHub Actions | GitLab CI/CD |
| :--- | :--- | :--- |
| **Configuration Files** | Multiple YAML files in `.github/workflows/` | Single `.gitlab-ci.yml` file at the root. |
| **Ecosystem** | Uses "Actions" from the GitHub Marketplace. | Uses container images and scripts. |
| **Execution Context** | Runs directly on VMs (Runners) or inside containers. | Almost always runs entirely inside Docker containers (`image:` keyword). |
| **Artifacts** | Passed explicitly between jobs using actions. | Handled natively by keywords (`artifacts: paths:`). |
| **Stages** | Implicitly created by defining `needs:` between jobs. | Explicitly defined in an array (`stages: [build, test]`). |

## Basic `.gitlab-ci.yml` Example

```yaml
stages:
  - test
  - deploy

run_unit_tests:
  stage: test
  image: python:3.12-slim
  script:
    - pip install -r requirements.txt
    - pytest

deploy_to_staging:
  stage: deploy
  script:
    - echo "Deploying..."
  only:
    - main
```
