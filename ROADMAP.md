# Software Delivery Lab

**From Git commits to production-like delivery.**

This repository is an educational lab about the practical lifecycle of software:

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
