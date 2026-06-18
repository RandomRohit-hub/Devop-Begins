# Vprofile Project AWS Lift and Shift Reference

This directory contains resources and configurations for setting up the Vprofile Project using the AWS Lift and Shift strategy.

---

## 1. Project Reference Links

*   **Vprofile Prerequisite Documentation:** [vprofile-project/Prereqs_doc.md](https://github.com/hkhcoder/vprofile-project/blob/prereqs/Prereqs_doc.md)
*   **Source Git Repository (CentOS-compatible):** [vprofile-project.git](https://github.com/natrajwadhai13/vprofile-project.git)

---

## 2. Useful SSH & Network Commands

Below are standard commands used during the infrastructure setup:

### Checking IP Configuration
```bash
# Display IP addresses assigned to network interfaces
ip addr show
```

### SSH Connection to CentOS Local VM
```bash
# Connect to CentOS local server using Git Bash
ssh centos@192.168.1.47
```

### SSH Connection to Ubuntu Local VM
```bash
# Connect to Ubuntu local server
ssh ubuntu@192.168.1.48
```

### SSH Connection to AWS EC2 Instance
```bash
# Connect to AWS EC2 instance using a PEM key file
ssh -i key.pem ec2-user@<public-ip-address>
```
