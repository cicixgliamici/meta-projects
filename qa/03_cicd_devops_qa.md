# CI/CD & DevOps - Interview Q&A

### 1. What exactly do CI, CD, and CD stand for?
**Answer:** 
- **Continuous Integration (CI):** The practice of merging all developers' code into a shared branch frequently. It involves automatic builds and tests on every commit to prevent regressions ("Integration Hell").
- **Continuous Delivery (CD):** Extends CI by ensuring the application is *always ready* to be released. It requires a manual human click to deploy to production.
- **Continuous Deployment (CD):** The final level where, if the CI pipeline passes all tests, the application is deployed directly to production in a fully automated way without human intervention.

### 2. What is Infrastructure as Code (IaC) and what are its benefits?
**Answer:** 
IaC is the practice of managing and configuring IT infrastructure through code (declarative text files) rather than manual processes (clicking on a dashboard). 
Benefits include: infrastructure versioning, immediate reproducibility, elimination of human errors, and the ability to use CI/CD for infrastructure releases.

### 3. What does it mean when Terraform (or an IaC tool) is "Declarative" and "Idempotent"?
**Answer:** 
- **Declarative:** You declare the *end result* you want to achieve (e.g., "I want 3 servers"), without writing step-by-step imperative instructions to get there. The tool calculates the difference and applies the changes.
- **Idempotent:** No matter how many times you run the script, if the desired end state has already been reached, the tool will perform no operations.

### 4. How do you handle passwords, tokens, or API keys in your DevOps scripts or code?
**Answer:** 
You should never hardcode secrets in source code or repositories (like Git). You must use Secret Management systems. In a CI pipeline, you use "Repository Secrets" (e.g., GitHub Secrets); in Kubernetes, you use `Secrets`; or at an enterprise level, tools like HashiCorp Vault inject them as environment variables at runtime.

### 5. What is "Shift-Left Security" (DevSecOps)?
**Answer:** 
Traditionally, security was tested at the end of the development cycle (on the "right" of the timeline). "Shift-Left" means moving security checks as early as possible (to the "left"), integrating them directly into the CI pipeline (static code analysis, Docker image vulnerability scanning) to block issues before they reach production.
