# Meta Projects

A practical repository of notes and labs about Git, GitHub, and software delivery, written as **GitHub-ready Markdown**.

## Current status

This is an initial content cleanup pass focused on readability and consistency.

## 📚 1. Theory & Concepts (docs/)

A collection of theoretical guides to understand the "why" before the "how".

- **Architecture & Ecosystem**
  - [microservices_vs_monolith.md](docs/01_architecture/microservices_vs_monolith.md) — Architectural paradigms
  - [from_code_to_production.md](docs/01_architecture/from_code_to_production.md) — Delivery pipeline overview
  - [build_systems.md](docs/01_architecture/build_systems.md) — How code is compiled (Make, Maven, Cargo, Lake)
  - [language_servers_protocol.md](docs/01_architecture/language_servers_protocol.md) — How IDEs understand code (LSP)
  - [design_by_contract.md](docs/01_architecture/design_by_contract.md) — Formal specifications (JML, Frama-C, deal)
  - [project_mapping.md](docs/00_meta/project_mapping.md) — Functional and software repository mapping
  - [development_history.md](docs/00_meta/development_history.md) — Past roadmap and development history
  - [review_readiness_plan.md](docs/00_meta/review_readiness_plan.md) — Future goals and roadmap to bulletproof the repository
  - [GLOSSARY.md](docs/00_meta/GLOSSARY.md) — Key terms and definitions
- **Git & Collaboration**
  - [branching_strategies.md](docs/02_git_collaboration/branching_strategies.md) — Git Flow vs GitHub Flow vs Trunk-Based
  - [pull_requests_vs_merge_requests.md](docs/02_git_collaboration/pull_requests_vs_merge_requests.md) — Terminology differences
  - [semantic_versioning.md](docs/02_git_collaboration/semantic_versioning.md) — SemVer rules and release tags
  - [commits_branches_merges.md](docs/02_git_collaboration/commits_branches_merges.md) — Git fundamentals
  - [git_commands.md](docs/02_git_collaboration/git_commands.md) — Essential Git CLI reference
  - [github_workflow.md](docs/02_git_collaboration/github_workflow.md) — Step-by-step collaborative workflow
  - [github_projects.md](docs/02_git_collaboration/github_projects.md) — Agile tracking using GitHub Projects
- **CI/CD & DevOps**
  - [ci_vs_cd.md](docs/03_ci_cd/ci_vs_cd.md) — Differences between Continuous Integration, Delivery, and Deployment
  - [software_testing_fundamentals.md](docs/03_ci_cd/software_testing_fundamentals.md) — Test Suites, Unit Tests vs Integration Tests
  - [github_actions.md](docs/03_ci_cd/github_actions.md) — CI/CD concepts specific to GitHub Actions
  - [gitlab_ci.md](docs/03_ci_cd/gitlab_ci.md) — CI/CD concepts specific to GitLab CI
  - [software_delivery_pipeline.md](docs/03_ci_cd/software_delivery_pipeline.md) — CI/CD overview diagram
- **Infrastructure & Containerization**
  - [docker_fundamentals.md](docs/04_infrastructure/docker_fundamentals.md) — Containers, images, layers, volumes
  - [docker_cheatsheet.md](docs/04_infrastructure/docker_cheatsheet.md) — Essential commands
  - [kubernetes_fundamentals.md](docs/04_infrastructure/kubernetes_fundamentals.md) — K8s core concepts (Pods, Deployments, Services)
  - [infrastructure_as_code.md](docs/04_infrastructure/infrastructure_as_code.md) — IaC theory, declarative vs imperative
  - [observability_and_monitoring.md](docs/04_infrastructure/observability_and_monitoring.md) — Logs, Metrics, Tracing (Prometheus/Grafana)

## 🧪 2. Laboratories & Code

Practical implementations to get your hands dirty.

- **Lab 1: Python API + CI/CD**
  - `apps/hello-api-python/` — Minimal Python Flask API with tests
  - `.github/workflows/ci-python.yml` — Live GitHub Actions pipeline
  - `.gitlab-ci.example.yml` — Example GitLab pipeline for comparison
- **Lab 2: Local Docker**
  - `docker-compose.yml` — Multi-container development environment
  - [docker_cheatsheet.md](docs/docker_cheatsheet.md) — Essential commands
- **Lab 3: Kubernetes Deployment**
  - `kubernetes/` — Contains `deployment.yaml` and `service.yaml`
- **Lab 4: Infrastructure as Code**
  - `terraform/` — AWS S3 and Security Group provisioning example
- **Lab 7: Software Testing**
  - `labs/lab-07-software-testing/` — Practical examples of Unit Tests, Mocks, and Integration Tests using Python and Pytest.

## 🎯 3. Interview & Exam Q&A (qa/)

A curated list of classic interview questions and answers for DevOps and Software Engineering roles.

- [01_git_github_qa.md](qa/01_git_github_qa.md) — Rebase vs Merge, Merge Conflicts, Stash, Forks.
- [02_docker_k8s_qa.md](qa/02_docker_k8s_qa.md) — VMs vs Containers, Pods vs Containers, Volumes.
- [03_cicd_devops_qa.md](qa/03_cicd_devops_qa.md) — Idempotency, Shift-Left Security, Secret Management.
