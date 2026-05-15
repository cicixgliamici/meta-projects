# Development History & Past Roadmap

This file serves as a local history of activities, decisions made, and lessons learned, useful for avoiding repeated mistakes (ignored in `.gitignore`).

## Session [2026-05-12] - Initial Restructuring and DevOps Setup
- **Initial Analysis:** The repository was a "flat directory" with unstructured files. We noticed errors such as `README (4).md` containing actual Python code, `test_app.py` containing a YAML workflow for GitHub Actions, and `app.py` containing a markdown Git cheatsheet.
- **Actions Taken:**
  - Created the `docs/` folder and moved all theoretical markdowns (e.g., git guides, CI/CD pipelines, glossary).
  - Renamed `download` to `docs/GLOSSARY.md`.
  - Created `apps/hello-api-python/` where we extracted the Python code (`app.py`), configured `requirements.txt`, and added real unit tests with `pytest` in `test_app.py`.
  - The YAML workflow was correctly placed in `.github/workflows/ci-python.yml`.
  - Containerized the API by creating a `Dockerfile` and a `docker-compose.yml` in the root.
  - Updated `README.md` to point to the correct directories and resources.
  - Created git-ignored tracking files: `LOCAL_ROADMAP.md` and this file `LOCAL_HISTORY.md`.

## Things to Remember:
- **Do not confuse file extensions with contents**: In the past, there was a lot of confusion (e.g., `test_app.py` with YAML code). We maintain a strict separation between folders: `docs/` for theory, `apps/` for code, `.github/` for infrastructure.
- **Local Isolation**: Anything that is a "draft" or only for our local reference must be placed in `.gitignore` (as we did for this file and the local Roadmap).

## Session [2026-05-12] (Part 2) - Theoretical Documentation Expansion
- **Action**: The user requested more focus on the theoretical/documentation part of the project, temporarily pausing the laboratory part.
- **Created Files**:
  - `docs/branching_strategies.md`: Added theory for Git Flow, GitHub Flow, and Trunk-Based Development.
  - `docs/docker_fundamentals.md`: Fundamental explanation of Containers, Images, Volumes, and core concepts vs Virtual Machines.
  - `docs/semantic_versioning.md`: Explanation of SemVer rules (Major.Minor.Patch), essential for release management in CI/CD.
  - `docs/kubernetes_fundamentals.md`: Explanation of Container Orchestration, Control Plane vs Worker Nodes, and core objects (Pods, Deployments, Services).
  - `docs/infrastructure_as_code.md`: Fundamental IaC concepts, declarative vs imperative approach, and tool overview (Terraform, Ansible).
  - `docs/ci_vs_cd.md`: Definitive distinction between Continuous Integration, Continuous Delivery, and Continuous Deployment.
- **Update**: Indexed the new files in `README.md`.

## Session [2026-05-12] (Part 3) - Tooling Systematization (GitHub, GitLab, Docker)
- **Action**: Systematization of theory and labs for the specific requested tools.
- **Created Files**:
  - `docs/github_actions.md`: Theory on Workflows, Events, Jobs, and Runners.
  - `docs/gitlab_ci.md`: Theory on GitLab CI, Pipelines, Stages, and a direct comparison table with GitHub Actions.
  - `.gitlab-ci.example.yml`: Example file in root to demonstrate the equivalent of the Python pipeline we have on GitHub Actions.
  - `docs/github_projects.md`: Explanation of Agile methodology (Issues, linked PRs, Kanban Boards) integrated into GitHub.
  - `docs/docker_cheatsheet.md`: A quick reference for the most used Docker commands to complement `docker_fundamentals.md`.
- **Update**: All cross-references added to `README.md`.

## Session [2026-05-12] (Part 4) - 3-Pillar Restructuring (Theory, Labs, Q&A)
- **Action**: The user asked for advice on how to proceed. I proposed permanently structuring the repo into Theory, Practical Labs, and an Interview Q&A section.
- **Added Theory**: Created `docs/microservices_vs_monolith.md` (Architecture) and `docs/observability_and_monitoring.md` (Logs, Metrics, Traces).
- **Added Labs**: 
  - Created `kubernetes/` with YAML for Deployment and Service of the Python API.
  - Created `terraform/` with an example `main.tf` for AWS provisioning (S3 and Security Group).
- **Added Q&A**: Created the `qa/` folder with three crucial documents (`01_git_github_qa.md`, `02_docker_k8s_qa.md`, `03_cicd_devops_qa.md`) containing classic and trick DevOps interview questions.
- **Restructured README**: The `README.md` was completely redesigned to act as a landing page categorized into the 3 pillars.

## Session [2026-05-12] (Part 5) - Ecosystems and Build Systems
- **Action**: Added theoretical documentation on Build Systems and the compilation cycle for various languages.
- **Created Files**: `docs/build_systems.md` (Explains the role of build systems and provides practical examples like Make, CMake, Maven, Gradle, SBT, Lake for Lean 4, Cargo for Rust, and tools for Python/JS).
- **Update**: Inserted under "Architecture & Ecosystem" in `README.md`.

## Session [2026-05-12] (Part 6) - Code Commenting and Finalization
- **Action**: Heavily commented all code/configuration files in English to make the repository highly instructive.
- **Files Modified**: 
  - `terraform/main.tf` and `variables.tf` (Explained provider, resources, variables).
  - `kubernetes/deployment.yaml` and `service.yaml` (Explained replicas, selectors, NodePort, liveness probes).
  - `apps/hello-api-python/Dockerfile` and `docker-compose.yml` (Explained caching layers, exposed ports, volume mounts).
  - `.github/workflows/ci-python.yml` and `.gitlab-ci.example.yml` (Explained actions vs runners vs images).
  - `apps/hello-api-python/app.py` and `test_app.py` (Explained health endpoints and pytest fixtures).
- **Update**: Updated `LOCAL_ROADMAP.md` with future architectural suggestions.
