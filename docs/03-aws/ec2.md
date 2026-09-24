# 🖥️ Amazon EC2 (Elastic Compute Cloud)

Amazon Elastic Compute Cloud (Amazon EC2) provides scalable computing capacity in the cloud. It eliminates your need to invest in hardware up front, allowing rapid deployment and configuration of servers.

---

## 🏗️ 1. EC2 Instance Configuration for CI/CD Tools

In our DevOps laboratory, three independent EC2 instances are provisioned to isolate tool workloads:

| Server Name | Operating System (AMI) | Instance Type | vCPU / RAM | Storage (EBS) | Default Public Port |
|---|---|---|---|---|---|
| **Jenkins-Server** | Ubuntu Server 24.04 LTS | `t2.small` | 1 vCPU / 2 GB RAM | 20 GB gp3 | `8080` (HTTP) |
| **SonarQube-Server**| Ubuntu Server 24.04 LTS | `t2.medium` | 2 vCPU / 4 GB RAM | 20 GB gp3 | `9000` / `80` (HTTP) |
| **Nexus-Server** | Amazon Linux 2023 | `t2.medium` | 2 vCPU / 4 GB RAM | 25 GB gp3 | `8081` (HTTP) |

---

## 🔑 2. SSH Key Pair Access & Best Practices

When launching an EC2 instance, AWS generates or accepts a public/private cryptographic key pair (`.pem` format):

```bash
# Set strict permissions (SSH client will reject keys with open permissions)
chmod 400 Jenkins-serverkey.pem

# Connect to Ubuntu-based instances (Jenkins, SonarQube)
ssh -i Jenkins-serverkey.pem ubuntu@<PUBLIC-IP>

# Connect to Amazon Linux / RHEL instances (Nexus)
ssh -i Jenkins-serverkey.pem ec2-user@<PUBLIC-IP>

# Switch to superuser after login
sudo -i
```

### SSH Security Precautions:
* **Never commit `.pem` private keys to Git.** Add `*.pem` to your `.gitignore` immediately.
* If a private key is ever exposed or leaked, terminate the instance or remove the corresponding public key from `~/.ssh/authorized_keys` immediately.

---

## 📊 3. Sizing Guidelines: Why Separate EC2 Instances?

1. **Memory Isolation:**
   * SonarQube embeds **Elasticsearch**, which reserves at least 1.5–2 GB RAM for search indexes, plus another 1 GB for the web service and PostgreSQL.
   * Nexus runs on a JVM that dynamically allocates 2–3 GB RAM for caching proxy dependencies and indexing binaries.
   * If Jenkins, SonarQube, and Nexus share a single small instance, **the Linux OOM (Out Of Memory) Killer** will terminate processes indiscriminately during heavy builds.
2. **Blast Radius Reduction:**
   * If a developer runs an intensive, buggy Maven build that hogs 100% CPU on Jenkins, the Nexus artifact repository and SonarQube quality database remain completely unaffected.
3. **Independent Maintenance & Upgrades:**
   * You can reboot or update SonarQube without terminating running Jenkins pipelines.
