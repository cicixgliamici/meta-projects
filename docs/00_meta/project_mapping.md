# Project Mapping: Meta-Projects

This document provides a comprehensive mapping of the `meta-projects` repository, analyzing it from both a functional perspective (its purpose and value to the user) and a software perspective (its architecture and technical components).

## 1. Functional Perspective (What it does and what it is for)

From a functional standpoint, `meta-projects` is a **DevOps and Software Delivery Reference Laboratory**. It is designed to be an educational resource, a professional portfolio, and a personal knowledge base.

The project is structured around three main pillars:

*   **📚 Theory & Concepts (The Foundation):** Provides theoretical documentation (the "why") behind software engineering practices. It explains architectural concepts (Monolith vs Microservices), Git branching strategies, semantic versioning, and containerization fundamentals (Docker/Kubernetes).
*   **🧪 Practical Labs (The Implementation):** Translates theory into practice through real code examples. It allows the user (or a reviewer) to get hands-on experience with how an application is containerized, how multiple services interact, and how it is deployed to a cluster or cloud infrastructure.
*   **🎯 Interview Preparation (The Verification):** A Questions & Answers section aimed at preparing the user for technical interviews on DevOps, Git, CI/CD, and Cloud Native topics, validating the skills acquired in the first two pillars.

**Ultimate Goal:** To demonstrate mastery of the entire software lifecycle, from a Git commit all the way to production deployment, applying industry best practices.

## 2. Software Perspective (How it is built)

From a software standpoint, the repository acts as a **Polyglot Monorepo** that integrates application code, declarative infrastructure, and automation pipelines.

### Software Component Map

1.  **Core Applications (`apps/`)**
    *   **Python API (`apps/hello-api-python/`):** The main "dummy" application. A minimalist REST API (likely Flask/FastAPI) that serves as a guinea pig for CI/CD pipelines and containerization. It includes application logic, a `Dockerfile` for the build, and automated tests (`pytest`).

2.  **Local Infrastructure and Containerization**
    *   **Docker Compose (`docker-compose.yml`):** Orchestrates the local development environment. It allows launching the Python API along with any dependencies (e.g., a database) simulating a multi-container environment.

3.  **Automation and CI/CD (`.github/`, root)**
    *   **GitHub Actions (`.github/workflows/ci-python.yml`):** The primary Continuous Integration pipeline. It is responsible for linting, running the Python API tests, and validating the build on every push/pull request.
    *   **GitLab CI (`.gitlab-ci.example.yml`):** Provided as a benchmark to demonstrate flexibility in using different CI/CD tools.

4.  **Cloud Native Orchestration (`kubernetes/`)**
    *   **Kubernetes Manifests (`deployment.yaml`, `service.yaml`):** Translate the containerized application into resources managed by a K8s cluster, defining replication rules (Deployment) and network exposure (Service).

5.  **Infrastructure as Code (`terraform/`)**
    *   **HCL Configurations:** Defines the cloud infrastructure (e.g., AWS S3, Security Groups) declaratively, demonstrating automated provisioning skills separated from the application code.

6.  **Knowledge Base (`docs/`, `qa/`)**
    *   **Markdown:** The main engine of the project. All `.md` files form an interconnected hypertext of technical documentation, diagrams, and guides.

### Software Logical Flow (Pipeline)
The lifecycle implemented in the project is as follows:
`Code (apps/) -> Build/Test (GitHub Actions) -> Containerization (Dockerfile) -> Local Deployment (Compose) / Cloud Deployment (K8s/Terraform)`.
