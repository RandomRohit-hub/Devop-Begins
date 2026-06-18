# Bash Scripting

This folder contains exercises, practice files, and deployment scripts for learning and automating Linux administration tasks using Bash.

## Directory Structure

*   **[`practice/`](./practice/)**: Contains scripts explaining foundational concepts of Bash scripting.
*   **[`scripts/`](./scripts/)**: Contains production-like administration, installation, and system-monitoring scripts.

---

## Script Highlights

### 1. Basic Concepts (`practice/`)
*   **[`01_first_script.sh`](./practice/01_first_script.sh)**: Introductory script displaying system uptime, RAM usage, and disk space.
*   **[`02_variables.sh`](./practice/02_variables.sh)**: Declaring and using environment and local variables.
*   **[`03_command_substitution.sh`](./practice/03_command_substitution.sh)**: Capturing execution output of CLI commands into script variables.
*   **[`04_command_line_arguments.sh`](./practice/04_command_line_arguments.sh)**: Accepting positional parameters (`$1`, `$2`, etc.) inside a script.
*   **[`05_user_input.sh`](./practice/05_user_input.sh)**: Reading interactive values and passwords securely.
*   **[`06_if_else.sh`](./practice/06_if_else.sh)**: Conditional flow control.
*   **[`07_while_loop.sh`](./practice/07_while_loop.sh)** & **[`08_for_loop.sh`](./practice/08_for_loop.sh)**: Executing repetitive actions.
*   **[`09_script_for_monitoring.sh`](./practice/09_script_for_monitoring.sh)**: Checking if Apache is running, and launching it if inactive.
*   **[`10_autorun_script.sh`](./practice/10_autorun_script.sh)**: Cron job string showing how to run scripts periodically.

### 2. Practical Administration (`scripts/`)
*   **[`01_system_info.sh`](./scripts/01_system_info.sh)**: System resources check.
*   **[`02_websetup.sh`](./scripts/02_websetup.sh)**: Automatic download, installation, configuration, and deployment of a multi-package web template on CentOS/RHEL.
*   **[`07_user_input.sh`](./scripts/07_user_input.sh)**: Validates user input and processes credentials safely.
*   **[`11_service_monitoring.sh`](./scripts/11_service_monitoring.sh)**: Production-grade service monitoring with shell trap cleanups and safe defaults (`set -euo pipefail`).
