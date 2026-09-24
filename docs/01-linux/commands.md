# ⌨️ Essential Linux Commands for DevOps

A comprehensive reference for day-to-day operations, server administration, log debugging, and pipeline automation.

---

## 🧭 1. Navigation, Inspection & User Identity

```bash
# Print current working directory
pwd
# Example output in Jenkins job: /var/lib/jenkins/workspace/FirstJob

# Identify active user identity and UID/GID
whoami
# Output: jenkins

id
# Output: uid=111(jenkins) gid=113(jenkins) groups=113(jenkins)

# Check system uptime, logged-in users, and 1, 5, 15 min load averages
uptime
w

# List files with detailed permissions, ownership, and hidden dotfiles
ls -la /var/lib/jenkins/

# Create nested directory trees without failing if they already exist
mkdir -p versions
mkdir -p /opt/nexus /tmp/nexus
```

---

## 💾 2. Disk & Storage Management (Crucial for CI Builds)

Jenkins workspaces and Maven repositories rapidly consume disk space. Mastering storage inspection commands is vital.

```bash
# Inspect disk usage across mounted filesystems in human-readable GB/MB
df -h

# Check filesystem type (ext4, xfs)
df -Th

# List all block storage devices, partitions, and mount points
lsblk

# Display detailed partition table and sector layouts
sudo fdisk -l

# Calculate disk usage of specific directories (sorted by largest first)
du -sh /var/lib/jenkins/* | sort -hr | head -n 10
du -sh /var/lib/jenkins/.m2/repository/
```

---

## 🌐 3. Networking & Port Inspection

Verify whether local daemons are actively listening and accepting traffic:

```bash
# Display all listening TCP ports with process IDs and program names
sudo ss -lntp

# Filter for specific CI/CD ports:
sudo ss -lntp | grep 8080   # Jenkins
sudo ss -lntp | grep 8081   # Nexus
sudo ss -lntp | grep 9000   # SonarQube
sudo ss -lntp | grep 5432   # PostgreSQL
sudo ss -lntp | grep 80     # Nginx Reverse Proxy

# Probe local HTTP headers without opening a browser
curl -I http://localhost:8080
curl -I http://localhost:8081
curl -I http://localhost:9000

# Test network reachability and latency to a remote host
ping -c 4 github.com

# Test TCP socket connectivity to a specific port
nc -zv 172.31.20.15 8081
```

---

## 📜 4. Process Monitoring & System Health

```bash
# Real-time interactive process viewer
top
htop

# Search for running processes by name
ps aux | grep jenkins
ps aux | grep java
ps aux | grep nexus

# Gracefully terminate a process by PID
kill <PID>

# Force terminate an unresponsive process
kill -9 <PID>

# Inspect memory usage (RAM and Swap) in megabytes
free -m
free -h
```

---

## 🔍 5. Text Processing & Log Analysis

```bash
# Display the end of a log file in real time
tail -f /var/log/nginx/sonar.error.log
journalctl -u jenkins -f

# Search for case-insensitive error strings in files
grep -in "error" /opt/sonarqube/logs/sonar.log
grep -rn "BUILD FAILURE" /var/lib/jenkins/jobs/*/builds/

# Extract specific columns (e.g. print usernames and shells)
cut -d: -f1,7 /etc/passwd

# Replace text inline inside configuration files
sed -i 's/8080/8082/g' /etc/default/jenkins
```

---

## 📦 6. Package Management (Ubuntu/Debian vs Amazon Linux/RHEL)

| Action | Ubuntu / Debian (`apt`) | Amazon Linux / RHEL / CentOS (`yum` / `dnf`) |
|---|---|---|
| **Update repo index** | `sudo apt update` | `sudo yum check-update` |
| **Install package** | `sudo apt install openjdk-17-jdk -y` | `sudo yum install java-17-amazon-corretto-devel -y` |
| **Remove package** | `sudo apt remove nginx -y` | `sudo yum remove nginx -y` |
| **Search package** | `apt search postgresql` | `yum search postgresql` |
