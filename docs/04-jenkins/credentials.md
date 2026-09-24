# 🔐 Jenkins Credentials Management & Secrets Security

Storing passwords, API tokens, and private SSH keys securely is mandatory for any production CI/CD pipeline. Jenkins provides a dedicated encrypted credentials store.

---

## 🚫 1. The Anti-Pattern: Hardcoded Secrets

```groovy
// DANGEROUS DISASTER IN A PIPELINE:
stage('Upload to Nexus') {
    steps {
        sh 'curl -u admin:admin123 --upload-file target/vprofile-v2.war http://172.31.20.12:8081/...'
    }
}
```

### Why this is disastrous:
1. The plaintext password is committed to GitHub history.
2. The password is printed directly in the **Console Output** for all Jenkins viewers to see.
3. If the password changes, you must edit and commit every pipeline that used it.

---

## 🛡️ 2. Jenkins Credential Types

Navigate to:
```text
Jenkins Dashboard ──> Manage Jenkins ──> Credentials ──> System ──> Global credentials
```

| Credential Type | Common Use Case | Real-World Example |
|---|---|---|
| **Secret text** | Single API tokens and webhooks | GitHub Personal Access Token (PAT), SonarQube User Token |
| **Username with password** | Standard HTTP basic authentication | Nexus administrator login (`nexus-login-creds`), Docker Hub login |
| **SSH Username with private key** | SSH authentication to worker nodes/servers | AWS EC2 private key (`.pem` file contents) |
| **Secret file** | Encrypted config files and keystores | Android signing keystores, Kubernetes `kubeconfig` |
| **Certificate** | PKCS#12 SSL/TLS certificates | Mutual TLS web service connections |

---

## 💻 3. Using Credentials Safely in a Jenkinsfile

Jenkins automatically masks credentials in console output with `****`:

### Example A: Username & Password Binding
```groovy
stage('Deploy to Server') {
    steps {
        withCredentials([usernamePassword(
            credentialsId: 'nexus-login-creds',
            usernameVariable: 'NEXUS_USER',
            passwordVariable: 'NEXUS_PASS'
        )]) {
            sh '''
                echo "Authenticating as $NEXUS_USER..."
                curl -u "$NEXUS_USER:$NEXUS_PASS" --upload-file target/app.war http://nexus:8081/repository/releases/
            '''
        }
    }
}
```

### Example B: Secret Token for SonarQube
```groovy
environment {
    SONAR_TOKEN = credentials('sonarqube-api-token')
}

stage('SonarQube Quality Scan') {
    steps {
        sh "mvn sonar:sonar -Dsonar.login=$SONAR_TOKEN"
    }
}
```
