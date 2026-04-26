# Software Delivery Lab

**From Git commits to production-like delivery.**

This repository is an educational lab about the practical lifecycle of software:

```text
local code
  ↓
Git history
  ↓
GitHub / GitLab collaboration
  ↓
automated testing
  ↓
CI pipeline
  ↓
future: Docker, Compose, Kubernetes, deployment
```

The goal is not only to write code, but to understand how code becomes reliable, reviewable, testable, and deployable software.

---

## What this MVP contains

This is **MVP 0** of the repository.

It covers:

- the big picture of software delivery
- Git fundamentals
- GitHub/GitLab collaboration concepts
- a minimal Python API
- unit tests
- a GitHub Actions CI workflow

Future versions will add:

- Docker
- Docker Compose
- GitLab CI
- Kubernetes
- deployment examples
- observability and security basics

---

## Repository structure

```text
software-delivery-lab/
├── README.md
├── ROADMAP.md
├── GLOSSARY.md
├── docs/
│   ├── 00_big_picture/
│   ├── 01_git/
│   └── 02_github_gitlab/
├── apps/
│   └── hello-api-python/
├── labs/
│   ├── lab_01_git_basics/
│   ├── lab_02_branching_strategy/
│   └── lab_03_github_pull_request/
├── cheatsheets/
│   └── git_commands.md
└── .github/
    └── workflows/
        └── ci-python.yml
```

---

## Learning path

1. Understand the software delivery pipeline.
2. Learn Git as a local version-control system.
3. Learn GitHub/GitLab as collaboration platforms.
4. Run a small application locally.
5. Test the application.
6. Let GitHub Actions run tests automatically.

---

## Run the Python example locally

From the repository root:

```bash
cd apps/hello-api-python
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows PowerShell

pip install -r requirements.txt
python app.py
```

Then open:

```text
http://127.0.0.1:8000
```

Run tests:

```bash
pytest
```

---

## Educational philosophy

Each topic should have:

- a short conceptual explanation
- one or more practical commands
- a small lab
- expected outcomes
- common mistakes

This repository is designed to be useful for students, junior software engineers, and anyone who wants to understand the path from code to deployment.
