# 📖 Ansible Playbooks & Practical Automation

Playbooks are Ansible's configuration, deployment, and orchestration language. They describe the policy you want your remote systems to enforce.

---

## 📄 1. Production Playbook: Automating Jenkins Installation

File: `install_jenkins.yml`

```yaml
---
- name: Automate Jenkins Controller Installation on Ubuntu 24.04
  hosts: jenkins_servers
  become: yes
  vars:
    java_package: openjdk-17-jdk

  tasks:
    - name: Update apt package cache
      apt:
        update_cache: yes
        cache_valid_time: 3600

    - name: Install OpenJDK 17 Runtime
      apt:
        name: "{{ java_package }}"
        state: present

    - name: Download official Jenkins GPG keyring
      get_url:
        url: https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
        dest: /usr/share/keyrings/jenkins-keyring.asc
        mode: '0644'

    - name: Add Jenkins APT repository
      apt_repository:
        repo: "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/"
        state: present
        filename: jenkins

    - name: Install Jenkins package
      apt:
        name: jenkins
        state: latest
        update_cache: yes

    - name: Ensure Jenkins service is enabled and started
      systemd:
        name: jenkins
        state: started
        enabled: yes
```

---

## 📋 2. Inventory File (`inventory.ini`)

```ini
[jenkins_servers]
44.202.22.36 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/Jenkins-serverkey.pem
```

---

## 🏃 3. Execution Commands

```bash
# Check syntax of playbook
ansible-playbook -i inventory.ini install_jenkins.yml --syntax-check

# Dry-run (Check mode without applying modifications)
ansible-playbook -i inventory.ini install_jenkins.yml --check

# Execute playbook against target servers
ansible-playbook -i inventory.ini install_jenkins.yml
```
