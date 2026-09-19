# 📝 Lecture Notes: Jenkins Plugins, Environment Variables & Artifact Versioning

## 📌 Summary of Concepts
Leveraging Jenkins plugins to interact with AWS S3, utilizing built-in environment variables, versioning deployable WAR/JAR files to prevent overwriting, and enabling instantaneous production rollbacks.

---

## 1. Jenkins Plugins
- Extends Jenkins with third-party tools (AWS, GitHub, Slack, S3).
- **Manage Plugins:** Updates, Available, Installed, Advanced, Download Progress.

### Key Plugins
- **Copy Artifact Plugin:** Transfers build output from one job to another.
- **S3 Publisher Plugin:** Uploads artifacts from Jenkins workspace to Amazon S3.
- **AWS SDK Plugin:** Required AWS API library.
- **SSH Server Plugin:** Secure execution on remote targets.
- **Build Timestamp Plugin:** Formats timestamp tags for builds.

---

## 2. Important Environment Variables
| Variable | Description |
|---|---|
| `$BUILD_NUMBER` | Sequential build count (1, 2, 3...) |
| `$BUILD_ID` | Timestamp of current run |
| `$JOB_NAME` | Name of the active job |
| `$WORKSPACE` | Absolute path of working directory |
| `$NODE_NAME` | Machine running build (`built-in`) |
| `$JAVA_HOME` | Assigned Java runtime directory |
| `$JENKINS_URL` | Base URL of controller |

---

## 3. Artifact Versioning Mechanism
### The Problem:
`target/vprofile-v2.war` gets overwritten every time a new build runs. If Build #3 is bad, Build #2 is already destroyed.

### The Solution:
Create a versioning script inside Jenkins Build Steps:
```bash
# Compile and build
mvn clean install

# Create storage directory
mkdir -p versions

# Copy with build number
cp target/vprofile-v2.war versions/vpro$BUILD_NUMBER.war
```

### Output:
```text
versions/
├── vpro1.war
├── vpro2.war  <== Stable Release
└── vpro3.war  <== Defective Release
```

---

## 4. `$BUILD_NUMBER` vs `$VERSION`
- `$BUILD_NUMBER`: Auto-generated incremental integer (`1`, `2`, `3`).
- `$VERSION`: Custom parameter configured by team for semantic versioning (`v2.3.6`).

---

## 5. Amazon S3 Storage & Rollback
- Jenkins uploads `versions/vpro$BUILD_NUMBER.war` to an AWS S3 bucket.
- **Why S3?**
  - Durable (11 9's) offsite storage.
  - Keeps Jenkins server disk light.
  - Allows deployment systems across regions to access binaries.
- **Rollback Process:**
  - If `vpro3.war` fails in production, deploy `vpro2.war` immediately from S3/Nexus without re-compiling code!

---

## 6. One-Minute Revision Formula
```text
CODE ──> BUILD ──> TEST ──> ARTIFACT ──> VERSION ──> S3 / NEXUS ──> ROLLBACK
```
