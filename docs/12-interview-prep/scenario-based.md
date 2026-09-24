# 🎯 Real-World Scenario-Based DevOps Interview Questions

Scenario and situational questions designed to test practical debugging, incident response, and architectural judgment.

---

### Scenario 1: A production deployment introduced a critical bug. The team wants you to roll back immediately. What is your response and procedure?
> **Model Answer:**
> "I would **never re-compile an older Git commit from scratch during an active production outage**, as doing so re-introduces build compilation risks, missing dependencies, and delays while test suites run.
> 
> Because our CI/CD pipeline implements **Artifact Versioning** and stores deliverables in Sonatype Nexus / AWS S3, all prior tested builds are preserved as immutable binaries (`vpro2.war`, `vpro1.war`).
> 
> My procedure:
> 1. Identify the last verified healthy build version (e.g. `vpro2.war`).
> 2. Fetch `vpro2.war` directly from the Nexus repository or S3 bucket.
> 3. Deploy the binary to the application server (e.g. replace `ROOT.war` in Tomcat and restart the service).
> 4. Verify health checks pass (`HTTP 200 OK`). Service is restored in under 2 minutes.
> 5. Conduct a post-mortem to analyze why the defect passed the staging environment."

---

### Scenario 2: You ran a Jenkins build on an AWS EC2 instance, and the build crashed with `No space left on device`. You resized the EBS volume from 8 GB to 20 GB in the AWS console, but the build still fails with the exact same error. What happened and how do you fix it?
> **Model Answer:**
> "Resizing an EBS volume in the AWS console only increases the underlying virtual block hardware storage. It does **not automatically resize the Linux partition or filesystem inside the operating system**. The OS still sees the old 8 GB partition boundary.
> 
> To resolve this:
> 1. SSH into the instance and run `lsblk` to verify the disk `xvda` is 20 GB while partition `xvda1` is still 8 GB.
> 2. Grow the partition using `sudo growpart /dev/xvda 1`.
> 3. Check the filesystem type with `df -Th /`.
> 4. If ext4 (standard Ubuntu), expand the filesystem with `sudo resize2fs /dev/xvda1`. If XFS, run `sudo xfs_growfs -d /`.
> 5. Confirm with `df -h /` that 13+ GB of free space is now available. Re-run the Jenkins build."

---

### Scenario 3: Your SonarQube Quality Gate stage in Jenkins keeps timing out after 5 minutes, even though SonarQube server shows the analysis completed. What is the root cause?
> **Model Answer:**
> "`waitForQualityGate` relies on an **asynchronous webhook callback** sent from SonarQube back to Jenkins (`http://<jenkins-ip>:8080/sonarqube-webhook/`).
> 
> If it times out, the callback was either never configured or was blocked in transit.
> 
> Diagnostic Steps:
> 1. In SonarQube (**Administration ➔ Configuration ➔ Webhooks**), verify the webhook URL is registered with the correct Jenkins IP and port.
> 2. Verify the trailing slash is included: `/sonarqube-webhook/`.
> 3. Inspect the AWS Security Group for Jenkins: ensure it allows inbound traffic on port `8080` from the SonarQube instance's Security Group (`Sonar-SG`).
> 4. Inspect SonarQube's **Recent Deliveries** log for the webhook to verify if the HTTP request returned `200 OK`, `Connection Refused`, or `403 Forbidden`."
