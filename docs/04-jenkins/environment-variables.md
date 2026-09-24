# 🌐 Jenkins Environment Variables & Build Parameters

Jenkins automatically populates a rich collection of contextual environment variables during every build execution.

---

## 📋 1. Standard Built-in Environment Variables

To inspect all available variables on your Jenkins server, navigate to:
```text
http://<JENKINS-IP>:8080/env-vars.html
```

| Variable | Description | Example Real-World Value |
|---|---|---|
| **`$BUILD_NUMBER`** | Current sequential build integer | `1`, `2`, `25` |
| **`$BUILD_ID`** | Build execution timestamp identifier | `2026-09-24_20-30-00` |
| **`$BUILD_TAG`** | Unique string identifier for the build | `jenkins-vprofile-pipeline-25` |
| **`$BUILD_URL`** | Full HTTP URL linking directly to the build log | `http://44.202.22.36:8080/job/vprofile-pipeline/25/` |
| **`$JOB_NAME`** | The name of the Jenkins project | `vprofile-pipeline` |
| **`$WORKSPACE`** | Absolute filesystem path of the build directory | `/var/lib/jenkins/workspace/vprofile-pipeline` |
| **`$NODE_NAME`** | Name of the agent executing the job | `built-in` or `agent-linux-01` |
| **`$EXECUTOR_NUMBER`**| Slot number of the executor running this build | `0` or `1` |
| **`$JAVA_HOME`** | Active JDK installation directory | `/usr/lib/jvm/java-17-openjdk-amd64` |
| **`$JENKINS_URL`** | Root URL configured in system settings | `http://44.202.22.36:8080/` |

---

## 💻 2. Practical Examples: Using Variables in Pipelines

### In Shell Scripts (`Execute shell` or `sh '...'`):
```bash
# Versioning an artifact
mkdir -p versions
cp target/vprofile-v2.war versions/vpro$BUILD_NUMBER.war

# Logging context
echo "Running Build #$BUILD_NUMBER for Job $JOB_NAME in workspace $WORKSPACE"
```

### In Declarative Jenkinsfile:
```groovy
pipeline {
    agent any

    environment {
        APP_VERSION = "2.3.0-${env.BUILD_NUMBER}"
        DEPLOY_ENV  = 'staging'
    }

    stages {
        stage('Echo Metadata') {
            steps {
                echo "Deploying ${env.JOB_NAME} Build #${env.BUILD_NUMBER} to ${env.DEPLOY_ENV}"
            }
        }
    }
}
```

---

## 🎛️ 3. Parameterized Builds (`Build with Parameters`)

Allow engineers to supply runtime configuration:

```groovy
pipeline {
    agent any

    parameters {
        string(name: 'VERSION', defaultValue: '2.3.6', description: 'Application release tag')
        choice(name: 'TARGET_ENV', choices: ['dev', 'qa', 'staging', 'prod'], description: 'Deployment target')
        booleanParam(name: 'RUN_INTEGRATION_TESTS', defaultValue: false, description: 'Execute slow integration tests?')
    }

    stages {
        stage('Build') {
            steps {
                sh "cp target/vprofile-v2.war versions/vpro${params.VERSION}.war"
                echo "Targeting environment: ${params.TARGET_ENV}"
            }
        }
    }
}
```
