# 🩺 Maven Troubleshooting & Error Resolution

A practical reference for diagnosing and resolving Maven build failures in Jenkins pipelines.

---

## 🚨 1. `Could not resolve dependencies ... Failure to transfer`
* **Symptom:**
  ```text
  [ERROR] Failed to execute goal on project vprofile-project: Could not resolve dependencies:
  Failed to collect dependencies at org.springframework:spring-webmvc:jar:5.3.30
  ```
* **Root Cause:**
  1. The Jenkins server has no outbound internet connectivity to download from Maven Central.
  2. Or Nexus proxy is offline or blocked by Security Group.
* **Fix:** Test DNS and network reachability from Jenkins shell: `curl -I https://repo.maven.apache.org`. Check AWS Route Tables and Security Group outbound rules.

---

## 🚨 2. `Fatal error compiling: error: release version 17 not supported`
* **Symptom:**
  ```text
  [ERROR] Failed to execute goal org.apache.maven.plugins:maven-compiler-plugin:3.8.1:compile: 
  Fatal error compiling: error: invalid target release: 17
  ```
* **Root Cause:** Maven was executed using an older Java version (e.g. Java 8 or 11) while `pom.xml` targets Java 17.
* **Fix:** Ensure Jenkins pipeline explicitly references OpenJDK 17:
  ```groovy
  tools {
      jdk "JDK17"
      maven "MAVEN3.9"
  }
  ```

---

## 🚨 3. `java.lang.OutOfMemoryError: Java heap space`
* **Symptom:** Maven crashes during compilation or test runs with an OOM error.
* **Fix:** Increase the JVM heap allocated to the Maven process via `MAVEN_OPTS`:
  ```bash
  export MAVEN_OPTS="-Xmx1024m -XX:MaxMetaspaceSize=512m"
  ```
  Or inside the Jenkinsfile environment block:
  ```groovy
  environment {
      MAVEN_OPTS = '-Xmx1024m'
  }
  ```
