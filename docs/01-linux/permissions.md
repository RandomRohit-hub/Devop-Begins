# 🔐 Linux Permissions, Ownership & Sudo Management

Understanding Linux permissions and privilege escalation models is essential for securing build agents and orchestrators.

---

## 🧮 1. Permission Architecture (rwx & Octal Notation)

Every file and directory in Linux has permissions assigned to three target classes:
1. **User (Owner):** The account that owns the file.
2. **Group:** The group associated with the file.
3. **Others (World):** Any user who is neither the owner nor a member of the group.

```text
-  r w x  r - x  r - -    1  jenkins  jenkins  4096  Sep 24 20:30  run_build.sh
│  └──┬─┘  └──┬─┘  └──┬─┘
│     │       │       └── Others: Read only (4)
│     │       └────────── Group: Read + Execute (5)
│     └────────────────── Owner: Read + Write + Execute (7)
└── File Type (- = Regular file, d = Directory, l = Symlink)
```

### Octal Value Table:
* **Read (`r`):** `4`
* **Write (`w`):** `2`
* **Execute (`x`):** `1`
* **None (`-`):** `0`

### Common Octal Combinations:
* `755` (`rwxr-xr-x`): Standard for executable scripts and directories (Owner has full rights, everyone else can read and execute).
* `644` (`rw-r--r--`): Standard for configuration files and documents (Owner writes, everyone else reads).
* `600` (`rw-------`): Standard for sensitive keys and certificates (e.g. `chmod 600 id_rsa` or AWS `.pem` key).
* `700` (`rwx------`): Directory accessible only to the owner (`~/.ssh`).

```bash
# Set secure permissions on AWS EC2 SSH key
chmod 400 my-key.pem

# Grant execution rights to a shell build script
chmod +x build.sh

# Change ownership of Nexus installation recursively
sudo chown -R nexus:nexus /opt/nexus/
sudo chown -R sonar:sonar /opt/sonarqube/
```

---

## ⚠️ 2. Why `sudo apt update` Fails Inside Jenkins Jobs

A common real-world issue occurs when a beginner adds administrative commands inside a Jenkins **Execute shell** step:

```bash
# Build Step inside Jenkins:
sudo apt update
```

### The Result:
The build fails immediately with an error resembling:
```text
sudo: a terminal is required to read the password; either use the -S option to grant it via standard input, or configure an askpass helper
Finished: FAILURE
```

### Technical Root Cause:
1. **Non-Interactive Execution:** Jenkins executes shell steps as the system user `jenkins` via a non-interactive subshell (`/bin/sh -xe /tmp/jenkins...sh`).
2. **Interactive TTY Requirement:** When `sudo` is called, it demands a password on `stdin`. Because no human terminal (TTY) is attached, `sudo` terminates the command with exit code `1`.
3. **Jenkins Abort:** Under `-e` (exit on error), Jenkins immediately stops the build.

---

## 🛡️ 3. Safe Sudo Solutions vs Dangerous Anti-Patterns

### ❌ Dangerous Anti-Pattern: Full Passwordless Root
Many tutorials suggest adding this to `/etc/sudoers`:
```text
# DANGEROUS SECURITY HAZARD:
jenkins ALL=(ALL) NOPASSWD: ALL
```
> [!CAUTION]
> **Why this is disastrous:**
> If any developer, collaborator, or attacker injects malicious shell commands or an unreviewed Jenkinsfile into a pipeline (e.g. `sudo rm -rf /` or downloading a crypto miner), they gain unrestricted root privileges on the host server.

### ✅ Enterprise Solutions:

#### 1. Pre-Provision Tools in Infrastructure (Recommended)
Build runners should be pre-configured with JDK, Maven, Git, and Docker during AMI creation or via UserData scripts. Pipelines should only execute application build commands, never operating-system package managers.

#### 2. Granular Least-Privilege Sudoers Rule
If Jenkins must restart a specific daemon (e.g. Tomcat), grant permission **only** for that exact binary:
```bash
# Run: sudo visudo -f /etc/sudoers.d/jenkins

# Grant access ONLY to restart tomcat without password:
jenkins ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart tomcat9
```

---

## 👤 4. Service Account Provisioning Commands

When deploying enterprise DevOps tools, create dedicated service accounts without shell login:

```bash
# Create system user for Nexus with home directory /opt/nexus
sudo useradd -r -d /opt/nexus -s /bin/false nexus

# Create dedicated group and user for SonarQube
sudo groupadd sonar
sudo useradd -c "SonarQube - User" -d /opt/sonarqube/ -g sonar -s /bin/bash sonar

# Secure permissions on home directory
sudo chown -R sonar:sonar /opt/sonarqube/
```
