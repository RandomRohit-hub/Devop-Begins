# CI Learning Architecture

## Purpose
This branch (`ci`) serves as a dedicated learning and reference repository for Continuous Integration, Delivery, Pipeline-as-Code, and DevOps concepts. It is completely isolated from the application source code in `main`.

## Folder Explanations
* **`jenkins/`**: Guides for Jenkins installation, configuration, jobs, and plugins.
* **`sonarqube/`**: Notes on Code Quality analysis, configuration, and Jenkins integration.
* **`nexus/`**: Guides for storing and retrieving versioned artifacts.
* **`scripts/`**: Bash scripts for automated tool installations.
* **`notes/`**: Categorized course notes extracted from lectures.
* **`diagrams/`**: ASCII diagrams of CI workflows.
* **`examples/`**: Jenkinsfile examples for different scenarios.
* **`templates/`**: Reusable pipeline segments.

## Jenkins Workflow
1. Code Checkout from GitHub
2. Build code using Maven
3. Run Unit Tests & Checkstyle
4. SonarQube Quality Gate
5. Package Artifact (`.jar` or `.war`)
6. Upload to Nexus Repository

## SonarQube Workflow
1. Jenkins runs `sonar-scanner` or Maven Sonar plugin.
2. Code is analyzed for bugs, vulnerabilities, code smells.
3. Report is published to SonarQube server.
4. Quality Gate status is fed back to the Jenkins Pipeline.

## Nexus Workflow
1. Successful pipeline build packages the artifact.
2. Jenkins authenticates with Nexus.
3. Artifact is pushed to the appropriate repository (Release/Snapshot).

## Commands Reference
* `mvn clean package`: Clean previous build and package application
* `mvn test`: Execute unit tests
* `mvn checkstyle:checkstyle`: Run checkstyle analysis
* `git checkout -b ci`: Create new ci branch

## Common Troubleshooting
* **GitHub Access**: Ensure Personal Access Token (PAT) is correctly configured if repo is private.
* **Maven build fails**: Check JDK configuration matching the Maven requirement.
* **SonarQube fails**: Ensure the webhook is correctly set up if using Quality Gates.

## Learning Roadmap
1. Jenkins Freestyle Builds
2. GitHub Source Code Integration
3. Maven Builds & JDK Tool Configuration
4. Artifact Archiving
5. Nexus Integration
6. SonarQube Integration
7. Pipeline as Code (Jenkinsfile)
8. Code Quality Analysis & Build Versioning
9. Complete CI Workflow Architecture
