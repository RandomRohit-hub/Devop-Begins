# Module 12: Infrastructure Files

Infrastructure as Code (IaC) configuration files provisioning local test nodes with Vagrant and automating configuration with Ansible.

## 📄 Files Included

* **[`Vagrantfile`](./Vagrantfile)**: Vagrant specification to launch a VirtualBox virtual machine running Ubuntu/CentOS with network port forwarding and shared sync folders.
* **[`playbook.yml`](./playbook.yml)**: Ansible playbook configuring dependencies, packages, and services automatically upon machine boot.

## 🚀 Execution
```bash
vagrant up
vagrant ssh
```
