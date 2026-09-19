# 📝 Lecture Notes: CI Pipeline Flow (Jenkins + Git + Maven + SonarQube + Nexus)

## 📌 Summary of Concepts
The Continuous Integration pipeline automates the journey of code from developer commits through automated building, testing, code quality scanning, and artifact repository archiving.

```text
Developer ──> GitHub ──> Jenkins (Fetch) ──> Maven (Build & Unit Test) ──> SonarQube (Quality Gate) ──> Nexus (Upload Artifact)
```

---

## 1. Developer ➔ GitHub
- Developers write code and push commits upstream:
  ```bash
  git add .
  git commit -m "Implement feature"
  git push origin main
  ```
- GitHub serves as the central **Source Code Repository**.

---

## 2. GitHub ➔ Jenkins Triggers
- **Webhook:** GitHub actively sends an HTTP POST event to Jenkins immediately upon `git push`. Zero delay.
- **Poll SCM:** Jenkins polls GitHub on a schedule (e.g. `H/5 * * * *`). Higher latency and overhead.

---

## 3. Step 1 — Fetch Code (Git)
- Jenkins checks out code into the workspace: `/var/lib/jenkins/workspace/<job-name>/`.
- Isolates build execution per project.

---

## 4. Step 2 — Build Application (Maven)
- Tool: Apache Maven (`mvn clean package` or `mvn install`).
- Uses `pom.xml` (Project Object Model) to download dependencies and compile source code.
- Produces packaged artifact (e.g. `target/vprofile-v2.war`).

---

## 5. Step 3 — Unit Test (Fail-Fast)
- Command: `mvn test`.
- Executes unit test cases verifying business logic.
- **Fail-Fast:** If a test fails, Jenkins terminates the build immediately to prevent flawed logic from reaching downstream environments.

---

## 6. Step 4 — Code Analysis (SonarQube)
- Performs **Static Code Analysis** (evaluating code without runtime execution).
- Scans for:
  - **Bugs:** Coding mistakes likely to break runtime.
  - **Vulnerabilities:** Security flaws (SQL injection, hardcoded secrets).
  - **Code Smells:** Unmaintainable, convoluted code.
  - **Duplication:** Copy-pasted code blocks.
  - **Coverage:** Percentage of code exercised by tests.
- **Quality Gate:** Pass/Fail threshold. If failed, pipeline stops.

---

## 7. Step 5 — Upload Artifact (Nexus OSS)
- Nexus OSS is a dedicated **Artifact Repository** for storing compiled binaries (`.war`, `.jar`).
- Keeps versioned release archives (`vprofile-1.0.war`, `vprofile-1.1.war`).
- Decouples builds from deployment servers.

---

## 8. Critical Comparisons

### Unit Test vs SonarQube
- **Unit Test:** Verifies functional correctness (*"Does it calculate 10 + 20 = 30?"*).
- **SonarQube:** Verifies code health, maintainability, and security (*"Is the code clean, secure, and well-structured?"*).

### GitHub vs Nexus
- **GitHub:** Source code storage (`.java`, `.xml`, `.py`).
- **Nexus:** Binary artifact storage (`.war`, `.jar`, `.tar.gz`).

---

## 9. Memory Formula
**F ➔ B ➔ T ➔ A ➔ U**
- **F**etch (Git)
- **B**uild (Maven)
- **T**est (Maven Unit Test)
- **A**nalyze (SonarQube)
- **U**pload (Nexus)
