# 🏗️ Continuous Integration & Delivery with Jenkins

This module focuses on **Continuous Integration and Continuous Delivery (CI/CD)** concepts using Jenkins, automated builds, environment verification, and multi-tier application deployments.

---

## 📂 Module Contents

* **[`jenkins.txt`](./jenkins.txt)**: Sample Jenkins console output illustrating build execution, workspace context (`/var/lib/jenkins/workspace/first_job`), user permissions (`uid=111(jenkins)`), and system diagnostics inside a Linux agent.
* **Reference Repository**: [vprofile-project (jdk11 branch)](https://github.com/hkhcoder/vprofile-project/tree/jdk11) — An enterprise Java web application with multi-tier architecture (Tomcat, MySQL, Memcached, RabbitMQ, Nginx) used for CI/CD automation and deployment pipelines.

---

## 🛠️ Key Concepts Covered

### 1. Jenkins Architecture & Workspace
- **Jenkins Master / Controller**: Manages the schedule, dispatching jobs, recording metrics, and monitoring agents.
- **Jenkins Agent / Executor**: Executes the shell scripts or pipeline steps inside isolated workspaces.
- **Workspace Location**: Standard default workspace path on Ubuntu/Debian is `/var/lib/jenkins/workspace/<job-name>`.

### 2. Sample Job Verification (`jenkins.txt`)
The included execution log demonstrates a simple shell build step running diagnostics:
```bash
# Workspace inspection
whoami     # Checks Jenkins service user (jenkins)
pwd        # Outputs active job directory
w          # Displays system load averages and logged in users
id         # Prints user and group IDs (uid/gid)
```

### 3. CI/CD Workflow with vProfile
1. **Source Code Management (SCM)**: Polling or webhook triggers from GitHub (`vprofile-project:jdk11`).
2. **Build Automation**: Compiling Java code and generating `.war` artifacts with Maven (`mvn clean install`).
3. **Code Quality Analysis**: SonarQube integration for static code analysis.
4. **Artifact Storage**: Archiving built artifacts to Nexus or AWS S3.
5. **Continuous Deployment**: Deploying application artifacts to staging/production server clusters.
