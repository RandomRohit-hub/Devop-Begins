# Linux Directory Structure

In Linux, everything is a file, and all files and directories start from the **root directory** represented by a single forward slash `/`.

![Linux File Structure](../assets/diagrams/file_structure.png)

---

## Directory Hierarchy & Explanations

Here is a summary of the standard directories found in Linux/CentOS and their purposes:

| Directory | Name/Meaning | Common Use Case / Purpose |
|:---|:---|:---|
| `/` | **Root** | The starting point of the directory tree. All folders branch from here. |
| `/bin` | **User Binaries** | Contains essential command binaries that must be available in single-user mode (e.g., `ls`, `cp`, `mv`, `cat`, `pwd`). |
| `/sbin` | **System Binaries** | Essential system binaries used mainly by the administrator (`root`) for system maintenance (e.g., `reboot`, `shutdown`, `fdisk`). |
| `/etc` | **Configuration** | Contains configuration files for the system and installed applications (e.g., `/etc/passwd`, `/etc/hosts`, `/etc/ssh/`). |
| `/home` | **User Home** | Home directories for personal storage of normal users (e.g., `/home/username`). |
| `/root` | **Root Home** | The home directory for the administrator (root user). |
| `/lib` / `/lib64` | **Shared Libraries** | Contains shared library files needed by the binaries in `/bin` and `/sbin`. |
| `/media` | **Removable Media** | Mount point for removable media like USBs, CD-ROMs, etc., which auto-mount here. |
| `/mnt` | **Temporary Mount** | A temporary mount point where system administrators can manually mount filesystems. |
| `/opt` | **Optional Add-ons** | Contains add-on/third-party software packages (e.g., Google Chrome, custom enterprise software). |
| `/proc` | **Process Info** | A virtual filesystem providing system/process info (e.g., `/proc/cpuinfo`, `/proc/meminfo`). |
| `/run` | **Runtime Data** | Stores temporary runtime data since the last boot (e.g., currently logged-in users, active daemons). |
| `/srv` | **Service Data** | Site-specific data served by this system, such as web server data or FTP files. |
| `/sys` | **System Virtual FS** | A modern virtual filesystem that exports information about devices and drivers in the kernel. |
| `/tmp` | **Temporary Files** | Temporary files created by applications. Often wiped on reboot. |
| `/usr` | **User Programs** | Contains binaries, libraries, documentation, and source code for user programs (e.g., `/usr/bin`, `/usr/local`). |
| `/var` | **Variable Data** | Stores files that change frequently in size, such as system logs (`/var/log`), mail queues, and web content (`/var/www`). |
| `/afs` | **Andrew File System** | Used for network shared filesystems across large-scale enterprise/academic environments. |
| `/vagrant` | **Vagrant Shared** | Shared folder between your host OS and the Vagrant virtual machine. |

---

## Essential Directories to Remember

*   **`/etc`** ➔ System and application configuration files
*   **`/home`** ➔ User personal files
*   **`/var`** ➔ Logs and dynamically changing data
*   **`/bin`** ➔ Basic commands
*   **`/dev`** ➔ Physical and virtual hardware device nodes
*   **`/proc`** ➔ Kernel and process statistics
*   **`/tmp`** ➔ Temporary files
*   **`/usr`** ➔ Installed user software and utilities

---

## Helpful Commands for Directory Navigation

```bash
# 1. Show all files in root directory
ls /

# 2. Show detailed directory listing with permissions and owners
ls -l /

# 3. Check disk space usage of a directory
du -sh /var

# 4. View mounted devices and partitions
mount
```
