# 🐧 Linux Basics

Welcome to the **Linux Basics** module of DevOps Begins. This section covers Linux filesystem layout, administrative commands, service orchestration, package management, and quick recall cheat sheets.

---

## 📂 Directory Contents

* **[`linux-directories.md`](./linux-directories.md)**: Detailed breakdown of the Linux directory tree (`/`, `/etc`, `/var`, `/bin`, `/opt`, etc.) and their specific roles in server administration.
* **[`linux-commands.md`](./linux-commands.md)**: Comprehensive command reference including file operations, text processing (`grep`, `cat`), service controls (`systemctl`), and package management (`yum`/`rpm`).
* **[`reference/Linux_Recall_Sheet.pdf`](./reference/Linux_Recall_Sheet.pdf)**: Offline PDF reference and recall cheat sheet.

---

## 🚀 Quick Navigation

### 1. Filesystem Overview
In Linux, everything is treated as a file. The root of the entire hierarchy is `/`.

Key locations to remember:
* `/etc`: System configuration files (e.g. `/etc/hosts`, `/etc/passwd`).
* `/var/log`: System and application service log files.
* `/bin` & `/usr/bin`: Standard system executable binaries.
* `/opt`: Third-party software and standalone enterprise applications.

👉 See **[Linux Directory Structure](./linux-directories.md)** for full documentation.

### 2. Common Administrative Commands

```bash
# Check current directory
pwd

# List directory contents with details
ls -la

# Manage system services (e.g. Apache)
systemctl status httpd
sudo systemctl restart httpd

# Monitor resource consumption
free -m
df -h
top
```

👉 See **[Linux & Bash Commands Reference](./linux-commands.md)** for more examples and tables.
