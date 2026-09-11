# Module 10: OS Automation

Automating operating system tasks, filesystem inspections, and user/group administration on Linux servers.

## 📄 Scripts Included

* **[`check_file.py`](./check_file.py)**: Inspects files and directories, checking path existence and file properties using Python's `os.path`.
* **[`ostasks.py`](./ostasks.py)**: System administration automation (creating directories, adding system users/groups, configuring file permissions via `os` and `subprocess`).

## 🚀 Execution
> [!NOTE]
> Scripts modifying system users or groups require administrative privileges on a Linux host or VM.

```bash
python3 check_file.py
sudo python3 ostasks.py
```
