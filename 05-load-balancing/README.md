# Load Balancing Practice (ELB)

This directory focuses on setting up backend target servers for load balancing, simulating production traffic routing using AWS Elastic Load Balancers (ELBs).

## Setup Scripts

*   **[`gymso_websetup.sh`](./scripts/gymso_websetup.sh)**: A simple CentOS-based shell script that downloads, unzips, and configures the Gymso Fitness web template under Apache.
*   **[`multios_websetup.sh`](./scripts/multios_websetup.sh)**: An advanced, OS-agnostic script that auto-detects whether the target server is CentOS or Ubuntu, installs dependencies (`httpd` vs `apache2`), pulls the Health template, configures files, and starts the service. Excellent for provisioning diverse targets behind a load balancer.

---

## Load Balancing Workflow

1.  Provision two or more target virtual machines or instances.
2.  Deploy the web content on each instance using the scripts inside the `scripts/` directory.
3.  Configure an Elastic Load Balancer (ELB) in AWS.
4.  Register the instances as targets in the ELB target group.
5.  Access the ELB DNS Endpoint to verify traffic routing and distribution.
