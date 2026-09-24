# 🛠️ Jenkins Installation, Service Setup & Tool Configuration

A complete installation guide for running Jenkins on Ubuntu Linux (AWS EC2), configuring systemd, and setting up development tools under **Manage Jenkins ➔ Tools**.

---

## 🚀 1. Step-by-Step Installation on Ubuntu 24.04 LTS

### Step 1: System Update & OpenJDK 17 Installation
Jenkins requires a Java runtime. Install OpenJDK 17:
```bash
sudo apt update
sudo apt install openjdk-17-jdk -y

# Verify Java runtime
java -version
```

### Step 2: Add Official Jenkins Debian Repository Keyring
```bash
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
```

### Step 3: Register Jenkins Apt Repository
```bash
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
https://pkg.jenkins.io/debian-stable binary/" | sudo tee \
/etc/apt/sources.list.d/jenkins.list > /dev/null
```

### Step 4: Install Jenkins Package
```bash
sudo apt update
sudo apt install jenkins -y
```

### Step 5: Start & Enable Systemd Service
```bash
sudo systemctl daemon-reload
sudo systemctl start jenkins
sudo systemctl enable jenkins
sudo systemctl status jenkins
```

---

## 🔑 2. Initial Setup Wizard & Administrator Password

1. Open your browser and navigate to:
   ```text
   http://<YOUR_EC2_PUBLIC_IP>:8080
   ```
2. Retrieve the initial admin password from the EC2 shell:
   ```bash
   sudo cat /var/lib/jenkins/secrets/initialAdminPassword
   ```
   *Example:* `ff05cfd8de5a45a6bb7c870a92302d7d`
3. Paste the password into the Unlock Jenkins field.
4. Select **Install suggested plugins**.
5. Create your primary administrative user account and finalize the Jenkins URL.

---

## ⚙️ 3. Configuring Global Tools (`Manage Jenkins ➔ Tools`)

Jenkins jobs require explicit paths to compilers and build tools to avoid relying on unpredictable system PATH defaults.

```text
Jenkins Dashboard ──> Manage Jenkins ──> Tools
```

### A. Configuring OpenJDK 17 (`JAVA_HOME`)
1. In the **JDK installations** section, click **Add JDK**.
2. **Name:** `JDK17` (This exact string is referenced in Jenkinsfiles).
3. **Uncheck** *Install automatically*.
4. **JAVA_HOME:** `/usr/lib/jvm/java-17-openjdk-amd64`

#### Finding Your Real JDK Directory on Linux:
```bash
# List JVM directories
ls -la /usr/lib/jvm/

# Identify symlink target
readlink -f $(which java)
# Output: /usr/lib/jvm/java-17-openjdk-amd64/bin/java
# Root directory is everything before /bin/java
```

> [!WARNING]
> **Common Trap / Error:**
> Setting `JAVA_HOME=/usr/bin/java` or `/usr/local/jvm`.
> Jenkins will display: **`"/usr/bin/java doesn't look like a JDK directory"`**.
> `JAVA_HOME` must always point to the directory containing the `bin/`, `lib/`, and `include/` subfolders!

---

### B. Configuring Apache Maven (`MAVEN3.9`)
1. In the **Maven installations** section, click **Add Maven**.
2. **Name:** `MAVEN3.9`
3. **Option A (Automatic):** Keep *Install automatically* checked ➔ Select **Install from Apache** ➔ Version `3.9.6` (or latest 3.9.x).
4. **Option B (Manual):** Install via shell (`sudo apt install maven -y`) and set `MAVEN_HOME` to `/usr/share/maven`.
5. Click **Save**.
