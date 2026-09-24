# 🔒 Jenkins Security Hardening & Best Practices

Jenkins is a tier-1 mission-critical asset. A compromised Jenkins controller gives attackers read and write access to all source code repositories, cloud production credentials, and deployment environments.

---

## 🛡️ 1. The 10 Commandments of Jenkins Security

1. **Never Hardcode Secrets:**
   * Never place AWS keys, database passwords, or Nexus tokens into a `Jenkinsfile` or Git repository. Always use the encrypted Jenkins Credentials store.
2. **Never Grant Full Passwordless Sudo:**
   * Do not put `jenkins ALL=(ALL) NOPASSWD: ALL` into `/etc/sudoers`. If Jenkins is compromised, the host OS is immediately breached.
3. **Restrict Security Groups:**
   * Never open Port `22` (SSH) or Port `8080` (Jenkins) to `0.0.0.0/0`. Restrict administrative access to your specific IP or VPN.
4. **Use SG-to-SG Networking:**
   * Allow Nexus (:8081) and SonarQube (:9000) to accept traffic **only** from the Jenkins Security Group (`Jenkins-SG`).
5. **Enforce Role-Based Access Control (RBAC):**
   * Install the **Matrix-based security** or **Role-based Authorization Strategy** plugin. Give developers read/build permissions only on their designated project folders.
6. **Enable CSRF Protection:**
   * Cross-Site Request Forgery protection is enabled by default in modern Jenkins. Never disable it.
7. **Keep Groovy Sandbox Active:**
   * Always verify that **Use Groovy Sandbox** is checked on pipeline jobs to stop arbitrary Java execution.
8. **Audit & Rotate Credentials Regularly:**
   * Rotate GitHub PATs, Sonar tokens, and Nexus passwords quarterly.
9. **Isolate Builds on Worker Agents:**
   * Restrict executors on the controller to `0` or `1` for administrative tasks, and run all builds on isolated Linux/Docker worker nodes.
10. **Regular Configuration Backups:**
    * Schedule automated backups of `/var/lib/jenkins/*.xml`, `jobs/`, `users/`, and `secrets/` to a secure private S3 bucket.
