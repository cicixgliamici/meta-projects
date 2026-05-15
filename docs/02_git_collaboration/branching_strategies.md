# Branching Strategies

Choosing how a team uses Git branches is critical for a smooth software delivery pipeline. Here are the three most common branching strategies used in the industry.

## 1. Git Flow
Git Flow is a strict branching model designed for scheduled releases. It relies on two long-lived branches and several short-lived branches.

**Branches:**
- `main` (or `master`): Stores the official release history. Every commit is a tagged release.
- `develop`: Serves as an integration branch for features.
- `feature/*`: Short-lived branches created from `develop` for new features.
- `release/*`: Created from `develop` when preparing a new release, allowing for bug fixes and metadata updates before merging to `main` and `develop`.
- `hotfix/*`: Created directly from `main` to quickly patch production bugs, then merged back into both `main` and `develop`.

**Pros:** Strict control over releases, great for software that has multiple versions in production (e.g., desktop apps, mobile apps).
**Cons:** Can be slow and over-complicated for modern web applications that deploy multiple times a day.

## 2. GitHub Flow
A lightweight, branch-based workflow that supports teams and projects where deployments are made regularly.

**Workflow:**
1. Create a `feature` branch from `main`.
2. Commit changes to the feature branch.
3. Open a Pull Request against `main`.
4. Discuss and review the code.
5. Deploy from the feature branch (optional but recommended in some setups) to test in a staging environment.
6. Merge into `main` and deploy to production immediately.

**Pros:** Simple, fast, perfect for CI/CD and SaaS (Software as a Service) where there is only one "current" version in production.
**Cons:** Lack of dedicated release branches can make it difficult to maintain older versions of the software.

## 3. Trunk-Based Development (TBD)
A branching model where all developers commit code to a single branch (`trunk` or `main`) multiple times a day. This is the ultimate goal for mature Continuous Integration teams.

**Workflow:**
- Developers work on extremely short-lived feature branches (merged within hours) or directly on `main`.
- Features that are incomplete are hidden behind **Feature Flags** (Feature Toggles) so they don't break production.

**Pros:** Eliminates "merge hell", forces true Continuous Integration, highest deployment frequency.
**Cons:** Requires high discipline, extensive automated testing, and good feature flag management.
