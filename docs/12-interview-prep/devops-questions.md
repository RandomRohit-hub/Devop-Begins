# 🎯 Top DevOps & CI/CD Architectural Interview Questions

Architectural, conceptual, and pipeline lifecycle interview questions.

---

### Q1: What is the Golden Formula for Continuous Integration (CI)?
> **Answer:** **F ➔ B ➔ T ➔ A ➔ U**
> 1. **F**etch Code (Git Clone / Checkout)
> 2. **B**uild Application (Maven Compile / Package)
> 3. **T**est Units (Automated JUnit / Surefire test execution)
> 4. **A**nalyze Quality (SonarQube Scanner & Quality Gate evaluation)
> 5. **U**pload Artifact (Versioned package published to Nexus OSS or AWS S3)

---

### Q2: What is the exact difference between Continuous Delivery and Continuous Deployment?
> **Answer:**
> * **Continuous Delivery:** Every passing build produces a tested, deployable artifact that is automatically staged and verified in a pre-production environment. Promotion to Production requires **a manual business approval / button click** by a release manager.
> * **Continuous Deployment:** There is **zero human intervention**. Every code commit that passes automated linting, unit tests, integration tests, and security scans is automatically deployed directly into live production environments.

---

### Q3: What is a SonarQube Quality Gate and why is it critical in CI?
> **Answer:** A Quality Gate is a set of Boolean conditions that code must satisfy before it can be deemed production-ready (e.g. Code coverage >= 80%, 0 Critical vulnerabilities, 0 Blocker bugs, duplicated lines < 3%). It acts as the automated quality threshold. If a build fails the Quality Gate, Jenkins halts the pipeline, preventing vulnerable or low-quality code from being packaged into an artifact.

---

### Q4: Why do we store artifacts in Nexus or S3 instead of GitHub?
> **Answer:**
> * **GitHub (SCM):** Designed for human-readable text diffs (`.java`, `.py`, `.xml`). Checking large 100MB+ pre-compiled binaries into Git rapidly bloats the `.git` database, degrading clone and fetch speeds for all developers.
> * **Nexus / S3 (Artifact Store):** Purpose-built to store, index, and distribute large binary deliverables (`.war`, `.jar`, Docker images) with strict immutability, high throughput, and dependency proxy caching.

---

### Q5: What are the 4 Key DORA Metrics?
> **Answer:**
> 1. **Deployment Frequency (DF):** How often an organization deploys code to production.
> 2. **Lead Time for Changes (LTFC):** Time from code commit to running in production.
> 3. **Mean Time to Recovery (MTTR):** Time required to restore service after an outage.
> 4. **Change Failure Rate (CFR):** Percentage of production releases resulting in degraded service or rollbacks.
