# 📊 Learning Progress Tracker & Practical Milestones

Use this interactive tracking document to monitor your mastery across each DevOps discipline, hands-on lab, and pipeline milestone.

---

## 🎯 Current Status Summary

* **Active Learning Phase:** Continuous Integration, Pipeline as Code & Artifact Lifecycle
* **Active Working Branch:** `Continuous-Integration-and-Delivery-with-Jenkins`
* **Overall Completion:** ~60% of End-to-End DevOps Master Curriculum

---

## 📋 Comprehensive Skills Checklist

### 1. Linux & Systems Administration
- [x] Filesystem Hierarchy Standard (FHS) understanding
- [x] Basic navigation and inspection (`pwd`, `ls -la`, `whoami`, `id`, `uptime`)
- [x] Permissions and ownership (`chmod`, `chown`, octal notation `755`, `644`, `600`)
- [x] Service management with Systemd (`systemctl start/stop/restart/enable/status`)
- [x] Service debugging with `journalctl` (`-u <service> -f`)
- [x] Port inspection with `ss -lntp` and HTTP testing with `curl -I`
- [x] Storage diagnostics (`df -h`, `lsblk`, `fdisk -l`, `du -sh`)
- [x] Partition resizing (`growpart`, `resize2fs`, `xfs_growfs`)
- [x] Understanding why non-interactive `sudo` fails inside Jenkins jobs

### 2. Version Control with Git & GitHub
- [x] Git architecture (Working directory, Staging area, Local repo, Remote)
- [x] Daily commands (`git status`, `git add`, `git commit`, `git push`, `git pull`)
- [x] Branching and switching (`git checkout -b`, `git switch -c`)
- [x] Remote upstream tracking (`git push -u origin <branch>`)
- [x] Safe branch naming rules (prohibition of spaces in ref names)
- [x] Conflict resolution and merge markers (`<<<<<<<`, `=======`, `>>>>>>>`)
- [x] Discarding changes and stashing (`git restore`, `git stash`)

### 3. Amazon Web Services (AWS) Cloud
- [x] EC2 instance provisioning and sizing (`t2.small` for Jenkins, `t2.medium` for Sonar/Nexus)
- [x] SSH key pair access (`chmod 400`, `ssh -i <key.pem> ubuntu@<ip>`)
- [x] Stateful Security Groups (Inbound vs Outbound traffic)
- [x] Restricting administrative ports (SSH 22, Jenkins 8080) to `My IP`
- [x] Setting up Security Group to Security Group (SG-to-SG) rules
- [x] EBS volume modification in AWS Console (8 GB ➔ 20 GB)
- [x] IAM Roles & Instance Profiles vs dangerous hardcoded access keys
- [x] AWS Cost management (stopping unused instances, setting billing alerts)

### 4. Build Automation with Apache Maven
- [x] Maven convention over configuration (`src/main/java`, `src/test/java`, `target/`)
- [x] Project Object Model (`pom.xml`) and GAV coordinates (GroupId, ArtifactId, Version)
- [x] Managing dependencies and scopes (`compile`, `test`, `provided`, `runtime`)
- [x] Default lifecycle phases (`validate`, `compile`, `test`, `package`, `install`, `deploy`)
- [x] Executing unit tests via `mvn test`
- [x] Skipping redundant tests via `mvn install -DskipTests`
- [x] Maven repository hierarchy (Local `~/.m2`, Central, Internal Nexus mirror)

### 5. Jenkins Automation Server
- [x] Jenkins installation on Ubuntu 24.04 via official Debian keyring
- [x] Unlocking Jenkins via `/var/lib/jenkins/secrets/initialAdminPassword`
- [x] Inspecting `/var/lib/jenkins` filesystem hierarchy (`jobs/`, `plugins/`, `workspace/`)
- [x] Configuring Global Tools: OpenJDK 17 (`JAVA_HOME`) and Maven 3.9
- [x] Resolving `JAVA_HOME` configuration traps (`/usr/bin/java` vs root JDK folder)
- [x] Creating and configuring Freestyle jobs (all 6 sections)
- [x] Using built-in variables (`$BUILD_NUMBER`, `$JOB_NAME`, `$WORKSPACE`)
- [x] Implementing Parameterized Builds (`VERSION` string parameter)
- [x] Artifact versioning strategy (`mkdir -p versions && cp target/*.war versions/vpro$BUILD_NUMBER.war`)
- [x] Understanding zero-rebuild rollback mechanism
- [x] Writing Declarative Pipelines (`Jenkinsfile`) with `pipeline`, `agent`, `tools`, `stages`, `post`
- [x] Securing credentials with Jenkins Credentials store and masking (`****`)

### 6. Code Quality Analysis with SonarQube
- [x] Static code analysis vs dynamic unit testing
- [x] The 4 inspection categories: Bugs, Vulnerabilities, Security Hotspots, Code Smells
- [x] Linux host tuning (`vm.max_map_count=262144`, `fs.file-max=65536`, `nofile=65536`)
- [x] PostgreSQL database setup and dedicated `sonar` user provisioning
- [x] Nginx reverse proxy configuration on port 80 forwarding to `127.0.0.1:9000`
- [x] Quality Gate configuration and "Clean as You Code" methodology
- [x] Integrating SonarQube Scanner in Jenkins (`withSonarQubeEnv`)
- [x] Configuring SonarQube webhook callback to `http://<jenkins>:8080/sonarqube-webhook/`
- [x] Enforcing Quality Gate checks in pipelines (`waitForQualityGate abortPipeline: true`)

### 7. Artifact Management with Sonatype Nexus OSS
- [x] Purpose of artifact repositories in enterprise software delivery
- [x] Nexus installation on Amazon Linux 2023 with Corretto 17
- [x] Retrieving admin password from `/opt/nexus/sonatype-work/nexus3/admin.password`
- [x] Configuring repository types: Hosted (`maven-releases`), Proxy (`maven-central`), Group (`maven-public`)
- [x] Anonymous access security precautions
- [x] Integrating Nexus with Jenkins via `nexusArtifactUploader` step

### 8. Containerization with Docker
- [x] Container vs Virtual Machine architectural comparison
- [x] Basic container operations (`docker run`, `docker ps`, `docker exec`, `docker logs`)
- [x] Writing optimized multi-stage Dockerfiles
- [ ] Pushing images to Amazon ECR / Nexus Docker Registry
- [ ] Multi-container orchestration with Docker Compose

### 9. Container Orchestration with Kubernetes
- [x] Kubernetes cluster architecture (Control plane vs Worker nodes)
- [x] Core objects: Pods, Deployments, Services, ConfigMaps, Secrets
- [ ] Deploying microservices on minikube / Amazon EKS
- [ ] Ingress controllers and TLS cert-manager
- [ ] Helm packaging and templating

### 10. Infrastructure as Code & Config Management
- [x] Terraform architecture, HCL syntax, provider plugins
- [x] Terraform state management precautions (`terraform.tfstate`)
- [x] Ansible agentless architecture, YAML playbooks, idempotency
- [ ] Terraform AWS VPC and multi-tier provisioning modules
- [ ] Ansible roles and dynamic cloud inventories
