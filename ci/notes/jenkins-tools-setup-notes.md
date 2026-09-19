# 📝 Lecture Notes: Jenkins Installation & Tool Configuration

## 📌 Summary of Concepts
Configuring build runtimes (Java/JDK, Maven, Git, NodeJS) under **Manage Jenkins → Tools** to ensure reproducible builds across diverse project requirements.

---

## 1. Jenkins Installation Basics
- Commonly hosted on Ubuntu Linux EC2 instances.
- **Default Port:** `8080` (requires AWS Security Group inbound TCP 8080 allow rule).
- Access URL: `http://<SERVER-IP>:8080`.

---

## 2. SSH Connection to EC2
```bash
# Connect with EC2 private key
ssh -i Downloads/Jenkins-serverkey.pem ubuntu@44.202.22.36

# Elevate privileges
sudo -i
```

---

## 3. Jenkins Filesystem Layout
- **Root Home Directory:** `/var/lib/jenkins/`
- Key subdirectories:
  - `jobs/`: Build configurations and console histories.
  - `plugins/`: Installed plugin binaries (`.jpi`).
  - `secrets/`: Cryptographic keys and passwords.
  - `workspace/`: Job execution working directory.

---

## 4. Initial Admin Password
```bash
cat /var/lib/jenkins/secrets/initialAdminPassword
```
Use this one-time token to complete web UI setup.

---

## 5. Manage Jenkins ➔ Tools
Tells Jenkins where development compilers and tools are installed.

### Option 1: Install Automatically
- Check *Install automatically*. Jenkins downloads and unpacks binaries into agent workspaces on first build.

### Option 2: Manual Installation (Preferred for Production JDKs)
- Install on the server via `apt`:
  ```bash
  apt update && apt install openjdk-17-jdk -y
  ```
- Find exact installation path:
  ```bash
  ls -la /usr/lib/jvm/
  # Example: /usr/lib/jvm/java-17-openjdk-amd64
  ```
- In Jenkins Tools:
  - Name: `JDK17`
  - JAVA_HOME: `/usr/lib/jvm/java-17-openjdk-amd64`

> [!WARNING]
> Do NOT use `/usr/local/jvm` or `/usr/bin/java`. `JAVA_HOME` must point to the directory containing `bin/`, `lib/`, and standard libraries!

---

## 6. Maven Configuration
- Add Maven in Tools with Name: `Maven3.9`.
- Check *Install automatically* from Apache or point to `/usr/share/maven`.
- In Jenkins jobs, select `Maven3.9` from the dropdown.

---

## 7. Memory Command List
```bash
ssh -i <key.pem> ubuntu@<IP>
sudo -i
ls /var/lib/jenkins/
cat /var/lib/jenkins/secrets/initialAdminPassword
apt install openjdk-17-jdk -y
java -version
ls /usr/lib/jvm/
git --version
```
