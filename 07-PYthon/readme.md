
# Python Installation on Linux (Bash)

This guide covers installing Python on Linux, creating your first Python script, and running it from the Bash terminal.

---

## Check Existing Python Installation

Check the default Python version:

```bash
python --version
```

Check the Python 3 version:

```bash
python3 --version
```

---

## Install Python

### CentOS / RHEL

Update the system:

```bash
sudo yum update -y
```

Search available Python packages:

```bash
yum search python3
```

Install Python 3:

```bash
sudo yum install python3 -y
```

Verify the installation:

```bash
python3 --version
```

---

### Ubuntu / Debian

Update package information:

```bash
sudo apt update
```

Install Python 3:

```bash
sudo apt install python3 -y
```

Verify the installation:

```bash
python3 --version
```

---

## Install Vim

### CentOS / RHEL

```bash
sudo yum install vim -y
```

### Ubuntu / Debian

```bash
sudo apt install vim -y
```

---

## Create a Python Script

Create a new file using Vim:

```bash
vim hello.py
```

Or use Nano:

```bash
nano hello.py
```

---

## Add a Shebang

If you want to execute the script directly, add the following line at the top of the file.

```python
#!/usr/bin/python3
```

---

## Example

```python
#!/usr/bin/python3

print("Hello, World!")
```

---

## Make the Script Executable

```bash
chmod +x hello.py
```

---

## Run the Script

Using the Python interpreter:

```bash
python3 hello.py
```

Or execute it directly:

```bash
./hello.py
```

---

## Useful Commands

| Command | Purpose |
|----------|---------|
| `python --version` | Check Python version |
| `python3 --version` | Check Python 3 version |
| `yum search python3` | Search available Python packages |
| `sudo yum install python3 -y` | Install Python 3 (CentOS/RHEL) |
| `sudo apt install python3 -y` | Install Python 3 (Ubuntu/Debian) |
| `vim hello.py` | Create or edit a Python file |
| `nano hello.py` | Edit a Python file with Nano |
| `chmod +x hello.py` | Make the script executable |
| `python3 hello.py` | Run the script using Python |
| `./hello.py` | Run the executable script |

---

## Python Interactive Shell (REPL)

Start Python:

```bash
python3
```

Exit the interpreter:

```python
exit()
```

or press:

```text
Ctrl + D
```

---

## Python 2 vs Python 3

Python 2:

```python
print "Hello"
```

Python 3:

```python
print("Hello")
```

---

## Notes

- Use Python 3 for all new development.
- Most modern Linux distributions include Python 3 by default.
- Use `python3` if `python` points to Python 2.
- Add a shebang only if you intend to execute the script directly.
- Remember to make the script executable with `chmod +x`.

---

## Quick Reference

```bash
python3 --version

sudo yum update -y
sudo yum install python3 -y
sudo yum install vim -y

sudo apt update
sudo apt install python3 -y

vim hello.py

chmod +x hello.py

python3 hello.py
./hello.py
```

---

## Workflow

```text
Install Python
        │
        ▼
Create hello.py
        │
        ▼
Write Python code
        │
        ▼
chmod +x hello.py
        │
        ▼
python3 hello.py
        │
        └── or ──► ./hello.py
```
