# 🐍 Python for DevOps Automation Course

Welcome to the Python module of the DevOps Automation course! This folder has been restructured into **13 logical modules** designed to take you from a complete beginner in Python syntax to building OS automation, SSH tasks, infrastructure orchestration, and API-oriented workflows.

---

## 📚 Course Modules & Directory Structure

| Module | Directory Name | Topics Taught | Main Scripts |
| :--- | :--- | :--- | :--- |
| **Module 1** | `01-Python-Basics` | Variables, types, quotes, string indexing/slicing | `first_script.py`, `variables.py`, `datatypes.py`, `slicing.py` |
| **Module 2** | `02-Python-Syntax-vs-Bash` | Comparing indentation, block rules, block-closing syntax | `bash_syntax.sh`, `python_syntax.py` |
| **Module 3** | `03-Operators` | Arithmetic, comparison, logical, membership, identity operators | `operators.py` |
| **Module 4** | `04-Conditions` | Control flow, `if`, `elif`, `else`, collection checks | `conditions.py`, `condition_vars.py` |
| **Module 5** | `05-Loops` | Iterating lists/tuples, `while` loops, nested loops, `break`/`continue` | `loops.py`, `loops_nested.py`, `break_example.py` |
| **Module 6** | `06-Functions` | Reusable code blocks, `*args`, `**kwargs`, modules, importing | `functions.py`, `kwargs.py`, `modern.py`, `call_modern.py` |
| **Module 7** | `07-Built-in-Methods` | Text manipulation, lists (append, extend, pop), dictionary methods | `built_in_methods.py` |
| **Module 8** | `08-Exception-Handling` | Safe execution progression: `try`, `except`, `else`, multi-exceptions | `try1.py` through `try4.py` |
| **Module 9** | `09-JSON` | JSON syntax, lists, nested objects, parsing JSON files in Python | `learn_json.json`, `parse_json.py` |
| **Module 10** | `10-OS-Automation` | Linux system administration, adding users/groups, file system queries | `ostasks.py`, `check_file.py` |
| **Module 11** | `11-Fabric-Automation` | Remote SSH execution, deploying local packages to target machines | `fabfile.py` |
| **Module 12** | `12-Infrastructure-Files`| Local development VM configuration & Ansible provisioning | `playbook.yml`, `Vagrantfile` |
| **Module 13** | `13-IDE-File` | Standard IDE template file | `main.py` |

---

## 🧠 Recommended Learning Progression

For the best learning experience, follow this step-by-step workflow:

```text
1. Python Basics (01-Python-Basics)
      ↓
2. Compare with Bash (02-Python-Syntax-vs-Bash)
      ↓
3. Mathematical/Logical Operators (03-Operators)
      ↓
4. Decision Making (04-Conditions)
      ↓
5. Control Loops (05-Loops)
      ↓
6. Modular Functions (06-Functions)
      ↓
7. String & Collection Methods (07-Built-in-Methods)
      ↓
8. Crash-proofing Scripts (08-Exception-Handling)
      ↓
9. API Data Serialization (09-JSON)
      ↓
10. Linux Administration (10-OS-Automation)
      ↓
11. Multi-Node Automation (11-Fabric-Automation)
      ↓
12. Infrastructure as Code (12-Infrastructure-Files)
```

---

## 🛠 Running the Scripts

Most basic scripts can be executed using the python interpreter directly:

```bash
# Example: Run slicing demonstration
python3 01-Python-Basics/slicing.py

# Example: Run JSON parsing demonstration
python3 09-JSON/parse_json.py
```

### OS Automation (Module 10)

The scripts in `10-OS-Automation` use administrative Linux commands like `useradd`, `groupadd`, and permissions configurations. Make sure to run them inside a Linux environment (e.g., your Vagrant Virtual Machine) with `sudo` permissions:

```bash
sudo python3 10-OS-Automation/ostasks.py
```

---

## 💡 Best Practices Implemented
1. **Clean Code & Comments**: Every script contains structured block comments explaining what each command does and why it's useful in a DevOps environment.
2. **Fixed Syntax Bugs**: Restructured `python_syntax.py` indentation, removed syntax-breaking trailing dots in `built_in_methods.py`, and resolved NameError hazards inside the exception exercises.
3. **Valid Formats**: Renamed all files with spaces or capitalization discrepancies to clean `snake_case` naming conventions for smooth terminal execution. Corrected `learn_json.json` to be a valid, parseable JSON file.
