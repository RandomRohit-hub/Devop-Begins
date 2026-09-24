# 🎯 Top AWS Interview Questions for DevOps Engineers

Cloud infrastructure, networking, security, and storage interview questions.

---

### Q1: What is the difference between an AWS Security Group and a Network Access Control List (NACL)?
> **Answer:**
> * **Security Group:** Operates at the **instance/ENI level**. It is **stateful** (inbound traffic automatically allows response outbound traffic). It supports **allow rules only** (implicit deny).
> * **NACL:** Operates at the **subnet boundary level**. It is **stateless** (inbound and outbound rules must be explicitly defined). It supports both **allow and deny rules** evaluated sequentially in numerical order.

---

### Q2: What is an IAM Role and why should Jenkins use an IAM Instance Profile instead of IAM User Access Keys?
> **Answer:** An IAM Role provides temporary, automatically rotated security credentials via AWS STS (Security Token Service). When an IAM Instance Profile is attached to an EC2 instance, SDKs and the AWS CLI automatically retrieve short-lived credentials from the Instance Metadata Service (IMDS). This completely eliminates the dangerous risk of hardcoding static `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` credentials in Jenkinsfiles or on server disks.

---

### Q3: What is the difference between EBS and S3?
> **Answer:**
> * **Amazon EBS (Block Storage):** Low-latency, high-performance block storage volume attached to a single EC2 instance in the same Availability Zone. Formatted with a filesystem (ext4, XFS) to run OS boot disks, databases, and Jenkins homes.
> * **Amazon S3 (Object Storage):** Scalable, distributed object storage accessed via HTTP REST APIs (`s3://bucket/object`). Offers 99.999999999% durability, unlimited storage, global accessibility, and lifecycle policies. Ideal for long-term build artifact retention.

---

### Q4: Why is it dangerous to open Port 22 or Port 8080 to `0.0.0.0/0`?
> **Answer:** `0.0.0.0/0` allows inbound connections from every internet-connected IP address globally. Port 22 is subjected to continuous automated SSH dictionary and brute-force bot attacks. Port 8080 exposes administrative Jenkins interfaces, potentially revealing source code, build logs, and configuration secrets to external scanners. Administrative ports should strictly be restricted to trusted IP addresses (`My IP/32`) or private VPN CIDRs.

---

### Q5: What is a Security Group to Security Group (SG-to-SG) reference?
> **Answer:** Instead of whitelisting an IP address or subnet range in an inbound rule, you reference another Security Group ID (e.g. `sg-0a1b2c3d`). This allows only network traffic originating from instances assigned to that specific security group. It is resilient to dynamic IP changes across reboots and keeps internal services (Nexus on 8081, SonarQube on 9000) completely hidden from the public internet.
