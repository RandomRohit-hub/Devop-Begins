# 📝 Master Jenkinsfile Syntax & Declarative Architecture

A comprehensive breakdown of declarative `Jenkinsfile` syntax, structural keywords, and real-world pipeline templates.

---

## 🏗️ 1. The Core Declarative Pipeline Structure

Below is the foundational Jenkinsfile demonstrated throughout our laboratory modules:

```groovy
pipeline {
    agent any

    tools {
        maven "MAVEN3.9"
        jdk "JDK17"
    }

    stages {

        stage('Fetch code') {
            steps {
                git branch: 'atom',
                    url: 'https://github.com/hkhcoder/vprofile-project.git'
            }
        }

        stage('Unit Test') {
            steps {
                sh 'mvn test'
            }
        }

        stage('Build') {
            steps {
                sh 'mvn install -DskipTests'
            }

            post {
                success {
                    echo "Archiving artifact..."
                    archiveArtifacts artifacts: '**/*.war'
                }
            }
        }

    }
}
```

---

## 🔍 2. Keyword-by-Keyword Architectural Breakdown

| Directive | Purpose & Working Mechanism |
|---|---|
| **`pipeline { ... }`** | The mandatory root block declaring that this is a valid Jenkins Declarative Pipeline. |
| **`agent any`** | Instructs Jenkins to allocate the build to any available online worker agent or local controller executor slot. |
| **`tools { ... }`** | Prepares the runtime environment by injecting the configured `JAVA_HOME` and `MAVEN_HOME` paths. **The names `"MAVEN3.9"` and `"JDK17"` must exactly match the tool names configured in `Manage Jenkins ➔ Tools`!** |
| **`stages { ... }`** | Container holding one or more sequential `stage` blocks. |
| **`stage('Fetch code')`** | Visual block in the Jenkins UI. Clones the Git repository and switches to the specified branch into `$WORKSPACE`. |
| **`sh 'mvn test'`** | Invokes Maven Surefire plugin to execute automated unit tests. If any assertion fails, the step exits with a non-zero code, immediately failing the pipeline. |
| **`sh 'mvn install -DskipTests'`** | Packages the Java application into `target/vprofile-v2.war`. |
| **`post { ... }`** | Conditional execution block that runs after a stage completes. |
| **`archiveArtifacts`** | Associates the generated binary (`**/*.war`) with the build record so it can be downloaded directly from the Jenkins UI. |

---

## 💡 3. Why `mvn install -DskipTests` Follows `mvn test`

A very common interview question:
> **Question:** *"Why did the pipeline run `mvn test` in the Unit Test stage and then run `mvn install -DskipTests` in the Build stage?"*
> 
> **Answer:**
> By default, `mvn install` automatically runs the entire test suite again before packaging. Since the pipeline already dedicated an isolated `stage('Unit Test')` to execute and validate test assertions, running tests again during `mvn install` would double the build duration. `-DskipTests` tells Maven: *"Compile and package the WAR file now, because the code has already been tested and verified."*

---

## 🚀 4. Full Enterprise Multi-Stage Jenkinsfile (With Sonar & Nexus)

```groovy
pipeline {
    agent any

    tools {
        maven "MAVEN3.9"
        jdk "JDK17"
    }

    environment {
        NEXUS_URL = 'http://172.31.20.12:8081'
        SONAR_SERVER = 'SonarQube-Server'
    }

    stages {
        stage('Fetch Code') {
            steps {
                git branch: 'main', url: 'https://github.com/RandomRohit-hub/Devop-Begins.git'
            }
        }

        stage('Compile') {
            steps {
                sh 'mvn clean compile'
            }
        }

        stage('Unit Testing') {
            steps {
                sh 'mvn test'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv(SONAR_SERVER) {
                    sh 'mvn sonar:sonar'
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('Package & Version Artifact') {
            steps {
                sh '''
                    mvn install -DskipTests
                    mkdir -p versions
                    cp target/vprofile-v2.war versions/vpro$BUILD_NUMBER.war
                '''
            }
        }

        stage('Upload to Nexus') {
            steps {
                nexusArtifactUploader(
                    nexusVersion: 'nexus3',
                    protocol: 'http',
                    nexusUrl: '172.31.20.12:8081',
                    groupId: 'com.visualpathit',
                    version: "${BUILD_NUMBER}",
                    repository: 'vprofile-repo',
                    credentialsId: 'nexus-login-creds',
                    artifacts: [
                        [artifactId: 'vpro-app', classifier: '', file: "versions/vpro${BUILD_NUMBER}.war", type: 'war']
                    ]
                )
            }
        }
    }

    post {
        always {
            echo "Pipeline run completed. Cleaning temporary workspace caches..."
        }
        success {
            archiveArtifacts artifacts: 'versions/*.war'
            echo "Artifact successfully published to Nexus!"
        }
        failure {
            echo "Pipeline failed! Please check console logs for errors."
        }
    }
}
```
