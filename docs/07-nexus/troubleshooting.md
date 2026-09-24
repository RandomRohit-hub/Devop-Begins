# 🩺 Nexus Troubleshooting & Diagnostics

A practical diagnostic runbook for resolving Sonatype Nexus service issues, HTTP errors during artifact upload, and permission failures.

---

## 🚨 1. Nexus Service Fails to Start (`systemctl status nexus` shows failed)

### Symptoms:
Running `sudo systemctl status nexus` shows service exited.
Inspecting `/opt/nexus/sonatype-work/nexus3/log/nexus.log`:
```text
java.io.FileNotFoundException: /opt/nexus/sonatype-work/nexus3/db (Permission denied)
```

### Root Cause:
The Nexus directory or subfiles are owned by `root` instead of the dedicated `nexus` user (often occurs when testing commands with `sudo`).

### Fix:
Restore ownership recursively:
```bash
sudo chown -R nexus:nexus /opt/nexus/
sudo systemctl restart nexus
```

---

## 🚨 2. HTTP 401 Unauthorized During Artifact Upload

### Symptoms:
Inside Jenkins build console:
```text
[ERROR] Failed to deploy artifacts: Could not transfer artifact ... 
Status code 401, Unauthorized
```

### Fix Checklist:
1. Verify the credentials configured in Jenkins (**Manage Jenkins ➔ Credentials**) match the active Nexus password.
2. In Nexus, verify the user account has the **`nx-repository-admin`** or **`nx-repository-view-*-*-add`** and **`edit`** privileges.

---

## 🚨 3. HTTP 400 Bad Request / Repository Read-Only

### Symptoms:
Jenkins fails with `HTTP 400 Repository is read only: maven-releases`.

### Root Cause:
You attempted to upload an artifact with the exact same version string (e.g. `2.3.0`) to a hosted repository configured with **Disable redeploy**.

### Fix:
1. In development, change the Nexus repository deployment policy to **Allow redeploy**.
2. In CI/CD, always use incrementing versions: `versions/vpro$BUILD_NUMBER.war`.
