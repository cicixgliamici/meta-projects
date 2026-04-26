# Roadmap

## MVP 0 — Git, GitHub and CI

Status: current version.

Goals:

- explain the big picture of software delivery
- introduce Git fundamentals
- introduce GitHub/GitLab collaboration models
- provide a minimal Python API
- add unit tests
- add a GitHub Actions CI pipeline

Deliverables:

- `docs/00_big_picture`
- `docs/01_git`
- `docs/02_github_gitlab`
- `apps/hello-api-python`
- `.github/workflows/ci-python.yml`

---

## MVP 1 — Docker

Goals:

- explain containers
- add a Dockerfile for the Python API
- build the image locally
- run the application inside a container
- add a Docker build workflow

Planned files:

```text
docs/04_docker/
docker/python-api/Dockerfile
.github/workflows/docker-build.yml
cheatsheets/docker_commands.md
```

---

## MVP 2 — Docker Compose

Goals:

- explain multi-container local environments
- add an API + database example
- introduce volumes, networks and environment variables

Planned files:

```text
docs/05_docker_compose/
compose/python-api-postgres/docker-compose.yml
```

---

## MVP 3 — GitLab CI

Goals:

- compare GitHub Actions and GitLab CI
- add a GitLab CI example pipeline

Planned files:

```text
docs/03_ci_cd/gitlab_ci.md
gitlab/.gitlab-ci.example.yml
```

---

## MVP 4 — Kubernetes basics

Goals:

- explain Pods, Deployments and Services
- deploy the Python API locally using kind or minikube
- demonstrate rollout and rollback

Planned files:

```text
docs/06_kubernetes/
kubernetes/base/deployment.yaml
kubernetes/base/service.yaml
scripts/deploy_kind.sh
```

---

## MVP 5 — Production-like delivery

Goals:

- releases
- tags
- semantic versioning
- image registry
- deployment manifests
- basic observability
- security checks
