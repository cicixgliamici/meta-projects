# Continuous Integration vs. Continuous Delivery vs. Continuous Deployment

These three terms (often abbreviated as CI/CD) represent the progressive stages of an automated software release pipeline. While they sound similar, they mean very different things.

---

## 1. Continuous Integration (CI)

**Continuous Integration** is the practice of frequently merging developers' code changes into a central repository (e.g., the `main` branch) multiple times a day.

### The Problem it Solves
"Integration Hell" — When developers work on isolated branches for weeks and then attempt to merge them together, resulting in massive conflicts and broken builds.

### How it Works
Every time a developer pushes code or opens a Pull Request, an automated server (like GitHub Actions, GitLab CI, or Jenkins) takes over:
1. It builds the application from source.
2. It runs a suite of automated tests (Unit tests, Linter checks).
3. It reports success or failure.

**Goal:** Ensure the codebase is always in a healthy, buildable state.

---

## 2. Continuous Delivery (CD)

**Continuous Delivery** is an extension of CI. It ensures that every change that passes the CI tests is automatically built, packaged, and prepared for a release to production.

### How it Works
After the CI pipeline passes:
1. The code is compiled into a deployable artifact (e.g., a Docker Image, a `.jar` file, or a zip package).
2. The artifact is pushed to an Artifact Registry.
3. The artifact is automatically deployed to a **Staging** or **QA** environment for final human verification.

**The defining characteristic of Continuous Delivery is a manual approval step.** The code is *ready* to be deployed at any moment, but a human must press the "Deploy to Production" button.

---

## 3. Continuous Deployment (CD)

**Continuous Deployment** goes one step further than Continuous Delivery. 

### How it Works
Every change that passes all stages of the production pipeline is released to your customers **automatically, with no human intervention.**

**Goal:** Reduce the feedback loop with customers to the absolute minimum. A developer commits code, and minutes later, it is live in production.

### Requirements
Continuous Deployment requires an extremely mature engineering culture:
- Exceptional automated testing (if a bug passes the tests, it goes live).
- Real-time observability and alerting.
- Feature Flags (to deploy code to production but keep it turned off for users until marketing is ready).
- Automated rollback capabilities if error rates spike after a deployment.

---

## Summary

| Practice | Automation Level | Deployment to Production |
| :--- | :--- | :--- |
| **Continuous Integration** | Automated Build & Test | No deployment. |
| **Continuous Delivery** | Automated Release Preparation | Manual trigger required. |
| **Continuous Deployment** | Fully Automated Pipeline | Automatic trigger upon passing tests. |
