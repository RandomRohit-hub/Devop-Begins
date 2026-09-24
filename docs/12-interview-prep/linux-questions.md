# 🎯 Top Linux Interview Questions for DevOps Engineers

Real-world Linux systems administration and troubleshooting interview questions.

---

### Q1: What is the difference between hard links and soft (symbolic) links?
> **Answer:**
> * **Hard Link:** Points directly to the file's underlying **inode** on the disk filesystem. Deleting the original file does not delete the data as long as at least one hard link exists. Cannot span across different filesystems or link to directories.
> * **Soft Link (Symlink):** A special pointer file containing the pathname of the target file. If the target file is moved or deleted, the symlink becomes broken (dangling). Can cross filesystems and point to directories.

---

### Q2: How do you identify which process is consuming Port 8080 and kill it?
> **Answer:**
> ```bash
> # 1. Identify listening process and its PID:
> sudo ss -lntp | grep 8080
> # Or using lsof:
> sudo lsof -i :8080
> 
> # 2. Terminate gracefully:
> sudo kill <PID>
> 
> # 3. Force kill if unresponsive:
> sudo kill -9 <PID>
> ```

---

### Q3: What is the Linux Out-Of-Memory (OOM) Killer?
> **Answer:** The OOM Killer is a Linux kernel mechanism that activates when available system memory (RAM + Swap) drops dangerously close to zero. The kernel computes a heuristic "badness score" based on memory footprint and runtime priority and forcefully sends `SIGKILL` to sacrifice the highest-scoring process to prevent the entire operating system kernel from panicking and freezing.

---

### Q4: Explain the difference between `fork()` and `exec()`.
> **Answer:**
> * **`fork()`:** Creates an exact duplicate child process that inherits memory, file descriptors, and registers from the calling parent process.
> * **`exec()`:** Replaces the current process memory space, code, and execution context with a completely new executable binary program (e.g. running a shell script or Maven command).

---

### Q5: How do you check memory and disk usage in human-readable format?
> **Answer:**
> * Disk filesystem capacity: `df -h`
> * Specific directory size: `du -sh /var/lib/jenkins/* | sort -hr | head -n 10`
> * Memory and Swap usage: `free -m` or `free -h`
> * Real-time processes: `top` or `htop`
