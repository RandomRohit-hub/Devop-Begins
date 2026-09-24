# 🌐 AWS Networking Fundamentals for DevOps

A clear understanding of VPC, Subnets, Routing, and Internet Gateways is required to connect distributed DevOps components.

---

## 🏛️ 1. VPC Architecture Diagram

```mermaid
flowchart TD
    subgraph VPC["AWS Virtual Private Cloud (172.31.0.0/16)"]
        IGW["🌐 Internet Gateway (IGW)"]
        RT["Route Table (0.0.0.0/0 -> IGW)"]
        IGW --- RT

        subgraph SUBNET["Public Subnet (172.31.16.0/20)"]
            RT --- JNK["Jenkins EC2<br/>Private: 172.31.20.10<br/>Public: 44.202.22.36"]
            RT --- SON["SonarQube EC2<br/>Private: 172.31.20.11<br/>Public: 54.180.12.14"]
            RT --- NEX["Nexus EC2<br/>Private: 172.31.20.12<br/>Public: 3.85.110.22"]
        end
    end

    INTERNET["🌍 Public Internet / Developer Laptop"] <--> IGW
```

---

## 🔍 2. Public IP vs Private IP vs Elastic IP

| IP Type | Persistence Across Reboot | Persistence Across Stop/Start | Incurs Cost? | Use Case |
|---|---|---|---|---|
| **Public IPv4** | Retained | **Lost / Changes to new IP** | Included with running EC2 | Direct internet access for lab testing. |
| **Private IPv4** | Retained | **Retained** | Free | Internal communication (Jenkins to Nexus/Sonar). |
| **Elastic IP (EIP)**| Retained | **Retained permanently** | Free if attached to running EC2; billed if unattached | Production web entry points and fixed webhook URLs. |

> [!TIP]
> **Internal Service Communication Tip:**
> When configuring the Nexus or SonarQube URL inside Jenkins, use their **Private IP** (`http://172.31.20.12:8081`), not their public IP! Private IP traffic stays on AWS internal fiber, provides lower latency, and incurs zero data transfer costs.
