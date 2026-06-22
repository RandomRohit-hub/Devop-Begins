import os

base_dir = "/home/roots/Desktop/ci branch/ci"

dirs = [
    "jenkins",
    "sonarqube",
    "nexus",
    "scripts",
    "notes",
    "diagrams",
    "examples",
    "templates"
]

for d in dirs:
    os.makedirs(os.path.join(base_dir, d), exist_ok=True)

files_content = {
    "README.md": """# CI Learning Architecture

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
""",

    "jenkins/installation-guide.md": """# Jenkins Installation Guide

1. Install Java (JDK 17 or 21 is recommended).
2. Add Jenkins repository key and source list to your package manager.
3. Install Jenkins (`sudo apt-get install jenkins`).
4. Start Jenkins service (`sudo systemctl start jenkins`).
5. Retrieve initial admin password from `/var/lib/jenkins/secrets/initialAdminPassword`.
6. Complete web setup wizard and install suggested plugins.
""",

    "jenkins/setup-guide.md": """# Jenkins Setup Guide

1. Go to **Manage Jenkins** > **Global Tool Configuration**.
2. Add JDK installations (e.g., JDK 17, JDK 21).
3. Add Maven installation.
4. Ensure environment variables are set correctly for these tools.
""",

    "jenkins/plugins-guide.md": """# Jenkins Plugins Guide

**Required Plugins:**
- Git Plugin: Connect Jenkins with GitHub
- Nexus Artifact Uploader: Publish artifacts
- SonarQube Scanner: Code Quality Analysis
- Pipeline Maven Integration: Pipeline support for Maven projects
- Pipeline Utility Steps: Extended tools
- Build Timestamp: Artifact versioning
""",

    "jenkins/credentials-guide.md": """# Jenkins Credentials Guide

1. Go to **Manage Jenkins** > **Manage Credentials**.
2. Add Global Credentials.
3. Examples:
   - GitHub Personal Access Token (Secret text or Username/Password).
   - Nexus Repository Credentials.
   - SonarQube Server Token.
""",

    "jenkins/freestyle-job-guide.md": """# Jenkins Freestyle Job Guide

1. Create a New Item > **Freestyle project**.
2. Under **Source Code Management**, select Git and provide repo URL.
3. In **Build Environment**, select 'Provide Node & npm bin/ folder to PATH' or necessary JDK.
4. Add **Build Step** (e.g., Invoke top-level Maven targets: `clean package`).
5. Add **Post-build Action** to archive artifacts (`**/*.jar`).
""",

    "jenkins/pipeline-job-guide.md": """# Jenkins Pipeline Job Guide

1. Create a New Item > **Pipeline**.
2. In the Pipeline section, choose 'Pipeline script from SCM'.
3. Provide the Git URL and specify the branch (`ci` or `main`).
4. Set the Script Path to `Jenkinsfile`.
""",

    "jenkins/Jenkinsfile": """pipeline {
    agent any

    tools {
        jdk 'JDK17'
        maven 'Maven3'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/RandomRohit-hub/Devop-Begins.git'
            }
        }

        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }

        stage('Unit Test') {
            steps {
                sh 'mvn test'
            }
        }

        stage('Checkstyle') {
            steps {
                sh 'mvn checkstyle:checkstyle'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                echo 'Run SonarQube Analysis'
            }
        }

        stage('Archive Artifact') {
            steps {
                archiveArtifacts artifacts: '**/*.jar'
            }
        }
    }
}
""",

    "examples/basic-Jenkinsfile": """pipeline {
    agent any
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World!'
            }
        }
    }
}""",

    "examples/maven-Jenkinsfile": """pipeline {
    agent any
    tools {
        maven 'Maven3'
        jdk 'JDK17'
    }
    stages {
        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }
    }
}""",

    "examples/sonarqube-Jenkinsfile": """pipeline {
    agent any
    stages {
        stage('SonarQube') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh 'mvn sonar:sonar'
                }
            }
        }
    }
}""",

    "examples/multistage-Jenkinsfile": """pipeline {
    agent any
    stages {
        stage('Build') { steps { echo 'Building...' } }
        stage('Test') { steps { echo 'Testing...' } }
        stage('Analysis') { steps { echo 'Analyzing...' } }
        stage('Deploy') { steps { echo 'Deploying...' } }
    }
}""",

    "sonarqube/installation-notes.md": """# SonarQube Installation

1. Can be installed via Docker: `docker run -d --name sonarqube -p 9000:9000 sonarqube:lts`
2. Access the dashboard at `http://localhost:9000`.
3. Default credentials: `admin` / `admin`.
""",

    "sonarqube/configuration-notes.md": """# SonarQube Configuration

1. Create a new project manually or wait for the first scan.
2. Generate a User Token for Jenkins integration.
3. Configure Quality Gates based on project requirements (e.g., Code coverage > 80%).
""",

    "sonarqube/jenkins-integration.md": """# Jenkins Integration with SonarQube

1. Install SonarQube Scanner plugin in Jenkins.
2. Add SonarQube server details and authentication token in Jenkins System configuration.
3. Configure the SonarQube Scanner tool under Global Tool Configuration.
4. Call `withSonarQubeEnv` in the pipeline.
""",

    "sonarqube/sonar-project.properties": """sonar.projectKey=devop-begins
sonar.projectName=Devop Begins Project
sonar.projectVersion=1.0
sonar.sources=src/main/java
sonar.java.binaries=target/classes
sonar.tests=src/test/java
""",

    "nexus/installation-guide.md": """# Nexus Installation Guide

1. Install via Docker: `docker run -d -p 8081:8081 --name nexus sonatype/nexus3`
2. Access at `http://localhost:8081`.
3. Get admin password from the container: `docker exec -it nexus cat /nexus-data/admin.password`.
""",

    "nexus/artifact-upload-guide.md": """# Nexus Artifact Upload

1. Create a `maven2` hosted repository in Nexus (e.g., `releases` or `snapshots`).
2. Use Jenkins `nexusArtifactUploader` step or Maven `deploy` phase to push artifacts.
""",

    "nexus/jenkins-integration.md": """# Jenkins Nexus Integration

1. Install Nexus Artifact Uploader Plugin.
2. Add Nexus credentials to Jenkins.
3. In pipeline, provide Nexus URL, repository name, credentials ID, and artifact details.
""",

    "notes/beginner-notes.md": """# Beginner Notes

- **Jenkins**: Automation server to orchestrate builds.
- **Pipeline**: Series of automated steps.
- **Maven**: Build tool for Java.
- **Git**: Version control system.
""",

    "notes/intermediate-notes.md": """# Intermediate Notes

- **Pipeline as Code**: Storing the pipeline definition alongside code (`Jenkinsfile`).
- **Code Quality**: Using SonarQube to catch bugs early.
- **Artifact Management**: Storing `.jar` files in a centralized repository (Nexus).
""",

    "notes/advanced-notes.md": """# Advanced Notes

- **Shared Libraries**: Reusable pipeline logic.
- **Multibranch Pipelines**: Automatically creating pipelines for every Git branch.
- **Quality Gates**: Blocking a build if code doesn't meet minimum standards.
""",

    "notes/interview-notes.md": """# Interview Notes

- **Q: Why use Pipeline as Code?**
  A: Version control, audit trail, easier collaboration, and reproducible builds.
- **Q: What is a Quality Gate?**
  A: A set of Boolean conditions (like coverage > 80%) that must be met before code can be promoted.
""",

    "notes/troubleshooting-notes.md": """# Troubleshooting Notes

- If Maven fails, check `JAVA_HOME` and tool configurations.
- If Git fails to clone, check credentials and branch names.
- If Jenkins server runs out of disk, check workspace cleanup policies and artifact retention.
""",

    "notes/lecture01-build-job.md": """# Jenkins Build Job

Steps:
1. Create Freestyle Project
2. Configure Git Repository
3. Configure JDK
4. Configure Maven Build
5. Build Project
6. Archive Artifact

Important:
- Public repo does not need credentials.
- Private repo requires GitHub PAT.
- JDK version selected under Build Environment.
""",

    "notes/lecture02-plugins.md": """# Jenkins Plugins

Required Plugins:
- Git Plugin: Connect Jenkins with GitHub
- Nexus Artifact Uploader: Publish artifacts
- SonarQube Scanner: Code Quality Analysis
- Pipeline Maven Integration: Pipeline support for Maven projects
- Pipeline Utility Steps: Extended tools
- Build Timestamp: Artifact versioning
""",

    "notes/lecture03-code-analysis.md": """# Code Analysis

- Analyzes code for code smells, bugs, and security vulnerabilities.
- Integrated into the CI pipeline right after unit tests.
- Tool: SonarQube.
""",

    "diagrams/ci-flow.md": """# CI Flow Diagram

Developer
    |
    v
GitHub Repository
    |
    v
Jenkins
    |
    +--> Checkout Code
    |
    +--> Build (Maven)
    |
    +--> Unit Test
    |
    +--> Checkstyle
    |
    +--> SonarQube Analysis
    |
    +--> Package Artifact
    |
    +--> Upload to Nexus
    |
    +--> Success
""",

    "scripts/install-jenkins.sh": """#!/bin/bash
echo "Installing Jenkins..."
# Placeholder script
""",

    "scripts/install-sonarqube.sh": """#!/bin/bash
echo "Installing SonarQube via Docker..."
docker run -d --name sonarqube -p 9000:9000 sonarqube:lts
""",

    "scripts/install-nexus.sh": """#!/bin/bash
echo "Installing Nexus via Docker..."
docker run -d -p 8081:8081 --name nexus sonatype/nexus3
"""
}

for filepath, content in files_content.items():
    full_path = os.path.join(base_dir, filepath)
    with open(full_path, "w") as f:
        f.write(content)

print(f"Generated {len(files_content)} files in {base_dir}")
