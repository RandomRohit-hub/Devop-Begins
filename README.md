# DevOps Begins — Reference Repository

Welcome to **DevOps Begins**, a structured repository documenting key foundational areas of DevOps, systems administration, scripting, and local environment orchestration.

This repository serves as a personal knowledge base, cheat sheet index, and practice script suite designed to help developers transition into infrastructure engineering.

---

## 📂 Repository Index & Structure

```text
Devop-Begins/
├── 01-linux-basics/                 # Linux directory structures, commands, and cheat sheets
│   ├── reference/
│   │   └── Linux_Recall_Sheet.pdf   # Linux commands & filesystem layout sheet
│   ├── linux-directories.md         # Detailed guide to Linux directory hierarchies
│   └── linux-commands.md            # Extensive commands index (systemctl, yum, etc.)
│
├── 02-git-and-github/               # Git version control commands and setup workflows
│   ├── reference/
│   │   └── Git_GitHub_CheatSheet.pdf # Offline PDF cheat sheet for Git/GitHub
│   └── README.md                    # Git basic workflow guide
│
├── 03-bash-scripting/               # Shell scripting tutorials, syntax, and active scripts
│   ├── practice/                    # Basic scripts (Variables, conditions, loops, user inputs)
│   ├── scripts/                     # Automated systems monitoring & site deployment scripts
│   └── README.md                    # Structured Bash script guide
│
├── 04-infrastructure-environments/  # Vagrant files & VMs for Docker, Docker-compose & local projects
│   ├── docker-environment/          # Ubuntu VM auto-provisioned with Docker
│   ├── docker-compose-environment/  # Ubuntu VM auto-provisioned with Docker & Compose
│   ├── vprofile-local/              # Multi-tier local application VM setup
│   ├── vprofile-aws-lift-and-shift/ # Cloud deployment references and source packages
│   └── README.md                    # Guide on spinning up environments
│
├── 05-load-balancing/               # AWS Elastic Load Balancing practice and configurations
│   ├── scripts/                     # Script assets to spin up backend HTTP servers
│   └── README.md                    # Elastic Load Balancing configuration walkthrough
│
├── 06-CI-and-Delivery-w-jenkins/    # Jenkins CI/CD pipeline automation & build verification
│   ├── jenkins.txt                  # Sample Jenkins workspace log and diagnostics
│   └── README.md                    # CI/CD architecture and vProfile reference guide
│
├── 07-PYthon/                       # Python for DevOps Automation course (13 structured modules)
│   ├── 01-Python-Basics/            # Data types, variables, slicing, and basics
│   ├── 02-Python-Syntax-vs-Bash/    # Syntax comparison between Bash and Python
│   ├── 03-Operators/                # Arithmetic, comparison, and logical operators
│   ├── 04-Conditions/               # If-else control flow
│   ├── 05-Loops/                    # For/while loops, nested loops, break/continue
│   ├── 06-Functions/                # Modular functions, *args, and **kwargs
│   ├── 07-Built-in-Methods/         # String, list, and dictionary manipulation methods
│   ├── 08-Exception-Handling/       # Defensive programming with try/except
│   ├── 09-JSON/                     # JSON data parsing and serialization
│   ├── 10-OS-Automation/            # System administration, users/groups, os/subprocess
│   ├── 11-Fabric-Automation/        # SSH-based remote multi-node automation
│   ├── 12-Infrastructure-Files/     # Local VM Vagrantfile & Ansible provisioning
│   ├── 13-IDE-File/                 # Python IDE starter script
│   └── readme.md                    # Full Python course roadmap and guides
│
└── assets/                          # Static media, architecture and cheat sheet diagrams
    └── diagrams/                    # System flowcharts, structures, and protocol maps
```

---

## 🛠️ Highlights of Key Areas

### 🐧 [01. Linux Basics](./01-linux-basics/)
*   Understand the **Standard Hierarchy** (such as `/etc`, `/var`, `/bin`, `/opt`).
*   Get quick-access lists of **System Commands** for managing services, checking resource usage (`free`, `df`), and administrative privilege elevations (`sudo -i`).

### 🐙 [02. Git & GitHub](./02-git-and-github/)
*   Foundational workflows: initializing repositories, creating commits, managing branches, and pushing upstream.
*   Cheat sheet referencing common command pairs for daily usage.

### 📜 [03. Bash Scripting](./03-bash-scripting/)
*   **Concepts Covered:** Variables, command substitution, command-line arguments, user prompts, conditionals, and loops.
*   **Production scripts:**
    *   [`02_websetup.sh`](./03-bash-scripting/scripts/02_websetup.sh): Auto-deploys full HTML templates on CentOS.
    *   [`11_service_monitoring.sh`](./03-bash-scripting/scripts/11_service_monitoring.sh): Robust monitoring script utilizing shebang configurations and error traps (`set -euo pipefail`).

### 🐳 [04. Infrastructure Environments](./04-infrastructure-environments/)
*   Leverage **Vagrant** and **VirtualBox** to create local sandbox VMs instantly.
*   Predefined configuration blocks to initialize Docker and Docker Compose environments automatically.

### ⚖️ [05. Load Balancing (ELB)](./05-load-balancing/)
*   Demonstrates how to set up active nodes behind an AWS Application/Classic load balancer.
*   Use [`multios_websetup.sh`](./05-load-balancing/scripts/multios_websetup.sh) to quickly bootstrap Apache web services on either RedHat/CentOS or Ubuntu/Debian targets automatically.

### 🏗️ [06. CI & Delivery with Jenkins](./06-CI-and-Delivery-w-jenkins/)
*   Continuous Integration and Continuous Delivery workflow fundamentals.
*   Console build log diagnostics and integration with the enterprise multi-tier [vprofile-project](https://github.com/hkhcoder/vprofile-project/tree/jdk11).

### 🐍 [07. Python for DevOps Automation](./07-PYthon/)
*   Complete 13-module structured roadmap from Python syntax basics to production infrastructure automation.
*   Covers OS system administration (`os`, `subprocess`), remote SSH execution (`fabric`), JSON serialization, and Ansible integration.

---

## ⚡ Quick Start

To spin up a local VM with Docker pre-installed, simply run:

```bash
# Navigate to the environment
cd 04-infrastructure-environments/docker-environment

# Launch VM
vagrant up

# Enter VM Shell
vagrant ssh
```
