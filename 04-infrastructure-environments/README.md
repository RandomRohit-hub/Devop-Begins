# Infrastructure Environments (Vagrant & AWS)

This directory houses infrastructure configurations for spawning development boxes locally using Vagrant and VirtualBox, as well as cloud references.

## Folder Overview

| Directory | Platform | Description |
|:---|:---|:---|
| **[`docker-environment/`](./docker-environment/)** | Vagrant / Ubuntu Focal | Spins up an Ubuntu VM and provisions it by automatically installing Docker. |
| **[`docker-compose-environment/`](./docker-compose-environment/)** | Vagrant / Ubuntu Focal | Spins up an Ubuntu VM and provisions it with both Docker and Docker Compose. |
| **[`vprofile-local/`](./vprofile-local/)** | Vagrant / Ubuntu Focal | Standard development environment setup for testing the Vprofile project locally. |
| **[`vprofile-aws-lift-and-shift/`](./vprofile-aws-lift-and-shift/)** | AWS Cloud | Contains reference links, instructions, and the Vprofile source archive (`vprofile-project-awsliftandshift.zip`) for cloud lift-and-shift migrations. |

---

## Getting Started with Vagrant

To provision any of the local environments, make sure you have [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/) installed, then:

```bash
# Navigate to the chosen environment directory
cd 04-infrastructure-environments/docker-environment

# Start and provision the virtual machine
vagrant up

# Access the shell of the virtual machine
vagrant ssh

# Turn off the VM when done
vagrant halt

# Destroy the VM and delete all associated files
vagrant destroy
```
