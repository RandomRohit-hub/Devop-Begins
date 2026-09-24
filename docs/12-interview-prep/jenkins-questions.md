# 🎯 Top Jenkins Interview Questions & In-Depth Technical Answers

A curated collection of real-world Jenkins technical interview questions asked by hiring managers and senior DevOps architects.

---

### Q1: What is Jenkins and what is its primary role in DevOps?
> **Answer:** Jenkins is an open-source automation server designed to orchestrate Continuous Integration and Continuous Delivery (CI/CD) workflows. Crucially, Jenkins is an **orchestrator**, not a compiler or artifact repository. It coordinates tools: fetching code via Git, executing compilation and testing via Maven, invoking code quality analysis via SonarQube, and pushing packaged deliverables to Nexus or AWS S3.

---

### Q2: What is the difference between a Freestyle Project and Pipeline as Code?
> **Answer:**
> * **Freestyle Project:** Configured primarily through web UI form fields. Good for simple tasks and beginner experimentation, but configuration is stored in internal XML files (`/var/lib/jenkins/jobs/<job>/config.xml`), making version control, peer reviews, and disaster recovery difficult.
> * **Pipeline as Code (Jenkinsfile):** The entire pipeline workflow is written as Groovy-based code stored directly inside the application's Git repository. It provides full version control, code review traceability, audit history, branch-specific execution, and seamless reproducibility across controllers.

---

### Q3: Why did `sudo apt update` fail inside a Jenkins build step?
> **Answer:** Jenkins executes build steps non-interactively as the unprivileged system user `jenkins` via `/bin/sh -xe`. When `sudo` is called, it requires an interactive terminal (TTY) to prompt for a password. Because no terminal is attached, `sudo` terminates with exit code 1, immediately aborting the build. The correct solution is never to run OS updates in CI builds, or use targeted least-privilege rules in `/etc/sudoers.d/jenkins`.

---

### Q4: Why run `mvn install -DskipTests` in the Build stage when `mvn test` was already executed?
> **Answer:** The pipeline dedicated an isolated `stage('Unit Test')` to execute tests via `mvn test`, ensuring fast feedback and clear build status. By default, Maven's `install` phase re-executes all unit tests before packaging. Running tests twice doubles build execution time without providing additional verification. `-DskipTests` instructs Maven to compile and package the binary immediately while skipping redundant test runs.

---

### Q5: What is the difference between `$BUILD_NUMBER` and a custom `$VERSION` parameter?
> **Answer:**
> * **`$BUILD_NUMBER`:** An automatically incrementing integer managed internally by Jenkins (`1`, `2`, `3`). It is unique to that specific job and is ideal for CI tracking and build-level traceability.
> * **`$VERSION`:** A user-defined string (e.g. `2.3.6`, `v1.0.0-rc`) supplied dynamically via Parameterized Builds (`Build with Parameters`). It reflects the formal Semantic Versioning release tag of the product.

---

### Q6: How does artifact versioning enable instant production rollback?
> **Answer:** If every build outputs the static filename `target/vprofile-v2.war`, each build overwrites the previous binary. If a bug is found in production, rolling back requires checking out older Git commits and re-compiling—a slow and risky process. By versioning artifacts (`versions/vpro$BUILD_NUMBER.war`) and storing them in Nexus or S3, previous known-good binaries are permanently preserved. Rollback is accomplished in seconds by simply re-deploying the prior stable binary (`vpro2.war`) with **zero code rebuilds**.

---

### Q7: What is `JAVA_HOME` and what is the most common configuration error in Jenkins?
> **Answer:** `JAVA_HOME` is an environment variable pointing to the root directory where the Java Development Kit (JDK) is installed. The most common mistake is pointing `JAVA_HOME` to `/usr/bin/java` (the executable binary) or `/usr/local/jvm`. Jenkins will reject this with: *"`/usr/bin/java doesn't look like a JDK directory`"*. `JAVA_HOME` must point to the directory containing the `bin/`, `lib/`, and `include/` subfolders (e.g. `/usr/lib/jvm/java-17-openjdk-amd64`).

---

### Q8: What caused the "No space left on device" error during the Maven build?
> **Answer:** The default 8 GiB root EBS volume attached to the EC2 server was exhausted. Repeated builds downloaded hundreds of megabytes of third-party libraries into the Maven local cache (`/var/lib/jenkins/.m2/repository/`) while retaining workspaces and build logs, consuming 94%+ disk space until Maven could no longer write the output WAR.

---

### Q9: Does expanding an AWS EBS volume immediately resize the Linux filesystem?
> **Answer:** **No.** Modifying the EBS volume in the AWS Console (e.g. from 8 GB to 20 GB) only expands the underlying virtual block hardware. The operating system partition table and filesystem still reflect the old size. The administrator must explicitly extend the partition using `growpart /dev/xvda 1` and grow the filesystem using `resize2fs /dev/xvda1` (for ext4) or `xfs_growfs` (for XFS).

---

### Q10: Why should you avoid installing too many Jenkins plugins?
> **Answer:**
> 1. **Security Vulnerabilities:** Many Jenkins CVEs originate in outdated third-party plugins.
> 2. **Memory Exhaustion:** Each loaded plugin consumes Java heap on the controller JVM.
> 3. **Dependency Conflicts:** Upgrading Jenkins core can break unmaintained plugins, leading to boot failure.
> 4. Only install essential, actively maintained plugins.
