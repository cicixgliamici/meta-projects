# Infrastructure as Code (IaC)

In traditional operations, administrators manually configured servers, databases, and networks via command-line interfaces or web dashboards ("ClickOps"). This approach is slow, error-prone, and impossible to reproduce reliably.

**Infrastructure as Code (IaC)** is the practice of managing and provisioning computing infrastructure through machine-readable definition files, rather than physical hardware configuration or interactive configuration tools.

## Core Benefits

1. **Version Control**: Infrastructure is written as code (YAML, JSON, HCL). It can be stored in Git, allowing for code reviews (Pull Requests), history tracking, and easy rollbacks.
2. **Repeatability**: You can destroy an entire environment and spin it back up from scratch in minutes. 
3. **Consistency**: Eliminates "Configuration Drift" (where the development environment slowly diverges from staging and production).
4. **Automation**: Integrates perfectly into CI/CD pipelines.

## Declarative vs. Imperative

There are two main approaches to IaC:

- **Imperative**: You specify the exact commands needed to achieve the desired state (e.g., "1. Spin up an EC2 instance, 2. Run this bash script, 3. Open port 80"). This is often done via custom scripts.
- **Declarative**: You specify the *desired end state*, and the tool figures out how to get there (e.g., "I want 3 EC2 instances running behind a Load Balancer"). If you change the state from 3 to 5, the tool calculates the difference and spins up 2 more. This is the industry standard.

## Types of IaC Tools

IaC tools generally fall into two categories:

### 1. Provisioning Tools
These tools are used to provision the hardware/cloud resources themselves (Servers, VPCs, Subnets, Managed Databases).
- **Terraform**: The industry standard. Uses a declarative language (HCL) and works with almost any cloud provider.
- **AWS CloudFormation / Azure ARM**: Cloud-specific declarative tools.
- **Pulumi**: Allows you to define infrastructure using familiar programming languages (Python, TypeScript, Go).

### 2. Configuration Management Tools
Once the server is provisioned, these tools log into the server and configure the software (installing packages, setting up users, starting services).
- **Ansible**: Procedural/Declarative mix, agentless (connects via SSH).
- **Chef / Puppet**: Older, declarative, typically require an agent running on the target machine.

*Note: In modern containerized workflows (Docker/Kubernetes), Configuration Management tools are used less frequently, as the environment configuration is baked directly into the Docker image.*
