# Linux & Bash Commands Reference

This document serves as a quick cheat sheet for commonly used Linux commands, system administration, and shell scripting basics.

---

## 1. Directory Navigation & File Operations

| Command | Action / Purpose |
|:---|:---|
| `pwd` | Show current working directory path |
| `cd /` | Change directory to the root |
| `ls` | List files and folders in the current directory |
| `ls /` | List files and folders in the root directory |
| `mkdir <name>` | Create a new directory |
| `rm <file>` | Remove a file |
| `rm -r <folder>` | Remove a directory recursively |
| `clear` | Clear the terminal screen |

---

## 2. File Viewing & Manipulation

| Command | Action / Purpose |
|:---|:---|
| `cat <file>` | Display full contents of a file |
| `grep <pattern> <file>` | Search for a specific text pattern inside a file |
| `cat /var/run/httpd/httpd.pid` | Show Apache HTTPD Process ID (PID) |

---

## 3. Service Management (`systemctl`)

These commands are used to manage system services (such as Apache `httpd`).

```bash
# Start a service
systemctl start httpd

# Stop a service
systemctl stop httpd

# Restart a service
systemctl restart httpd

# Check the status of a service
systemctl status httpd

# Enable a service to start automatically on system boot
systemctl enable httpd

# Check if a service is actively running (returns quiet exit code)
systemctl is-active httpd
```

---

## 4. Package Management (`yum` / `rpm`)

Used for installing and managing software packages on CentOS/RHEL.

```bash
# Install a package (e.g., Apache HTTPD) automatically accepting prompts
yum install httpd -y

# Find running processes matching a name
ps -ef | grep httpd

# Check if a package is installed via RPM query
rpm -qa | grep httpd
```

---

## 5. Shell Scripting Basics

### General Setup & Inputs
*   `#!/bin/bash` ➔ The Shebang. Place this at the absolute top of scripts to specify the Bash interpreter.
*   `chmod +x script.sh` ➔ Make the script executable.
*   `./script.sh` ➔ Execute the script in the current directory.
*   `echo $?` ➔ Show the exit status of the previously executed command (0 = success, non-zero = failure).
*   `date` ➔ Print the current date and time.
*   `sleep 3` ➔ Pause execution for 3 seconds.
*   `read VAR` ➔ Accept user input and store it in `$VAR`.
*   `read -p "Prompt Message: " VAR` ➔ Accept user input with a custom prompt message.

### Conditions & Comparisons
```bash
if [ condition ]
then
    # executed if condition is true
else
    # executed if condition is false
fi
```

*   `-eq` ➔ Equal to comparison (numeric)
*   `-gt` ➔ Greater than comparison (numeric)

---

## 6. Access & Remote Administration
*   `sudo -i` ➔ Switch to the root user with administrative privileges.
*   `vagrant ssh scriptbox` ➔ Connect to the Vagrant virtual machine named `scriptbox` via SSH.
