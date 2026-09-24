# 🩺 AWS Troubleshooting & Diagnostics

A practical diagnostic runbook for solving cloud connectivity, authorization, and storage failures.

---

## 🚨 Incident 1: Connection Refused / Connection Timed Out

### Symptoms:
* Running `ssh -i key.pem ubuntu@<IP>` hangs indefinitely and throws:
  ```text
  ssh: connect to host <IP> port 22: Connection timed out
  ```
* Or web browser reports `ERR_CONNECTION_TIMED_OUT` when loading Jenkins (`:8080`).

### Systematic Diagnostic Checklist:
1. **Did the Public IP change?** If the EC2 instance was Stopped and Started, AWS dynamically assigns a brand-new Public IPv4 address. Verify the IP in the EC2 Console.
2. **Has your ISP changed your home IP?** If your Security Group rule restricts port 22/8080 to `My IP`, check your current public IP via `curl ifconfig.me`. If it changed, edit the Security Group rule.
3. **Is the Instance State 'Running'?** Check if instance status checks pass (`2/2 checks passed`).
4. **Is Route Table configured with an Internet Gateway?** Verify that the subnet route table has `0.0.0.0/0` targeted to `igw-xxxxxx`.

---

## 🚨 Incident 2: Host Key Verification Failed (EC2 Re-creation)

### Symptoms:
```text
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Host key for 44.202.22.36 has changed and you have requested strict checking.
```

### Cause:
You terminated an old instance and launched a new one that was allocated the same public IP address, but its host SSH fingerprint is different.

### Fix:
Remove the old cached host key from your local machine:
```bash
ssh-keygen -R 44.202.22.36
```
Then reconnect cleanly.

---

## 🚨 Incident 3: S3 Access Denied (`403 Forbidden`)

### Symptoms:
```text
upload failed: versions/vpro1.war to s3://vprofile-build-artifacts/vpro1.war: 
An error occurred (AccessDenied) when calling the PutObject operation: Access Denied
```

### Fix Checklist:
1. Verify the IAM Role is attached to the EC2 instance:
   * EC2 Console ➔ Select Instance ➔ Actions ➔ Security ➔ **Modify IAM role**.
2. Check the IAM policy resource ARN: ensure it includes both the bucket (`arn:aws:s3:::bucket`) and all nested keys (`arn:aws:s3:::bucket/*`).
3. If KMS encryption is enabled on the bucket, ensure the role has `kms:GenerateDataKey` and `kms:Decrypt` permissions.
