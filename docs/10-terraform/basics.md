# 🛠️ Terraform Basics, State & HCL Syntax

A practical guide to HashiCorp Configuration Language (HCL), resource definitions, variables, and state management.

---

## 📄 1. Practical HCL: Provisioning Jenkins EC2 & Security Group

File: `main.tf`

```hcl
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# 1. Security Group for Jenkins
resource "aws_security_group" "jenkins_sg" {
  name        = "jenkins-sg-terraform"
  description = "Allow SSH and Jenkins Web UI"

  ingress {
    description = "SSH from trusted IP"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.my_ip]
  }

  ingress {
    description = "Jenkins Web UI"
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = [var.my_ip]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# 2. EC2 Instance for Jenkins
resource "aws_instance" "jenkins_server" {
  ami                    = "ami-04a81a99f7ecacba0" # Ubuntu 24.04 in us-east-1
  instance_type          = "t2.small"
  vpc_security_group_ids = [aws_security_group.jenkins_sg.id]
  key_name               = "Jenkins-serverkey"

  root_block_device {
    volume_size = 20
    volume_type = "gp3"
  }

  tags = {
    Name        = "Jenkins-Controller"
    Environment = "DevOps-Laboratory"
  }
}
```

---

## 💾 2. The Critical Role of Terraform State (`terraform.tfstate`)

Terraform records the mapping between your declarative code and real-world AWS infrastructure in a JSON file called `terraform.tfstate`.

> [!CAUTION]
> **State Security Precautions:**
> 1. **Never commit `terraform.tfstate` to Git!** State files can contain unencrypted database passwords and cloud private keys.
> 2. **Use Remote State:** In enterprise teams, store state in an **Amazon S3 bucket with server-side encryption** and state locking via **DynamoDB**.
