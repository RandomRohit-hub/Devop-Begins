# 🔑 AWS IAM (Identity and Access Management) for CI/CD

AWS Identity and Access Management (IAM) enables you to manage access to AWS services and resources securely.

---

## 🚫 1. Anti-Pattern: Hardcoded AWS Access Keys

A critical security vulnerability occurs when engineers embed AWS Access Keys into scripts or Jenkinsfiles:

```groovy
// DANGEROUS DISASTER IN A JENKINSFILE:
environment {
    AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"       // ❌ NEVER DO THIS!
    AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
}
```

> [!CAUTION]
> **Why this is catastrophic:**
> If the repository is cloned, forked, or made public, automated threat actors scrape these keys within minutes, creating hundreds of GPU cryptocurrency-mining EC2 instances and leaving the account owner with thousands of dollars in debt.

---

## 🛡️ 2. The Enterprise Solution: IAM Roles & Instance Profiles

Instead of issuing static credentials, attach an **IAM Role (Instance Profile)** directly to the Jenkins EC2 instance!

```mermaid
flowchart LR
    subgraph EC2["Jenkins EC2 Instance"]
        APP["Jenkins Process / AWS CLI"]
        METADATA["Instance Metadata Service<br/>(IMDSv2)"]
        APP --> METADATA
    end

    subgraph AWS_IAM["AWS IAM"]
        ROLE["IAM Role:<br/>JenkinsS3ArtifactRole"]
        POLICY["IAM Policy:<br/>s3:PutObject on vprofile-artifacts"]
        ROLE --- POLICY
    end

    METADATA -- "Fetches Temporary Short-Lived STS Tokens" --> ROLE
    APP -- "Uploads vpro1.war with zero hardcoded keys" --> S3["Amazon S3 Bucket"]
```

### Benefits:
1. **Zero Static Secrets:** No secrets stored on disk, in Jenkins credentials, or in source code.
2. **Automatic Token Rotation:** AWS STS automatically rotates temporary security credentials every few hours.
3. **Granular Least Privilege:** Policies permit actions only on specified buckets.

---

## 📜 3. Minimal Least-Privilege IAM Policy for S3 Artifact Uploads

Attach this policy to the Jenkins EC2 IAM Role:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowJenkinsS3ArtifactUpload",
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::vprofile-build-artifacts-2026",
        "arn:aws:s3:::vprofile-build-artifacts-2026/*"
      ]
    }
  ]
}
```
