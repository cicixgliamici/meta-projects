# Meta Projects

A practical repository of notes and labs about Git, GitHub, and software delivery, written as **GitHub-ready Markdown**.

## Current status

This is an initial content cleanup pass focused on readability and consistency.

## 📚 1. Theory & Concepts (docs/)

A collection of theoretical guides to understand the "why" before the "how".

- **Architecture & Ecosystem**
  - [microservices_vs_monolith.md](docs/microservices_vs_monolith.md) — Architectural paradigms
  - [from_code_to_production.md](docs/from_code_to_production.md) — Delivery pipeline overview
  - [build_systems.md](docs/build_systems.md) — How code is compiled (Make, Maven, Cargo, Lake)
  - [GLOSSARY.md](docs/GLOSSARY.md) — Key terms and definitions
- **Git & Collaboration**
  - [branching_strategies.md](docs/branching_strategies.md) — Git Flow vs GitHub Flow vs Trunk-Based
  - [pull_requests_vs_merge_requests.md](docs/pull_requests_vs_merge_requests.md) — Terminology differences
  - [semantic_versioning.md](docs/semantic_versioning.md) — SemVer rules and release tags
- **CI/CD & DevOps**
  - [ci_vs_cd.md](docs/ci_vs_cd.md) — Differences between Continuous Integration, Delivery, and Deployment
  - [github_actions.md](docs/github_actions.md) — CI/CD concepts specific to GitHub Actions
  - [gitlab_ci.md](docs/gitlab_ci.md) — CI/CD concepts specific to GitLab CI
- **Infrastructure & Containerization**
  - [docker_fundamentals.md](docs/docker_fundamentals.md) — Containers, images, layers, volumes
  - [kubernetes_fundamentals.md](docs/kubernetes_fundamentals.md) — K8s core concepts (Pods, Deployments, Services)
  - [infrastructure_as_code.md](docs/infrastructure_as_code.md) — IaC theory, declarative vs imperative
  - [observability_and_monitoring.md](docs/observability_and_monitoring.md) — Logs, Metrics, Tracing (Prometheus/Grafana)

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

## 🎯 3. Interview & Exam Q&A (qa/)

A curated list of classic interview questions and answers for DevOps and Software Engineering roles.

- [01_git_github_qa.md](qa/01_git_github_qa.md) — Rebase vs Merge, Merge Conflicts, Stash, Forks.
- [02_docker_k8s_qa.md](qa/02_docker_k8s_qa.md) — VMs vs Containers, Pods vs Containers, Volumes.
- [03_cicd_devops_qa.md](qa/03_cicd_devops_qa.md) — Idempotency, Shift-Left Security, Secret Management.
