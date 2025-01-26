
# Infrastructure as Code (IAC)

This repository contains Infrastructure as Code (IAC) configurations, organized to manage and provision resources using Kubernetes, Helm, and Terraform.

## Features
- Kubernetes manifests for deploying workloads and services.
- Helm charts for managing application deployments.
- Terraform modules for provisioning cloud infrastructure.

## Components

### Kubernetes
- Contains YAML files for:
  - Workloads (e.g., API and frontend deployments).
  - Services (e.g., API service, ingress configurations).
  - Secrets and configurations.

### Helm
- Helm charts and templates for deploying applications.

### Terraform
- Modules and configurations to provision cloud infrastructure like VPCs, EKS clusters, and node groups.

## Prerequisites
To use the configurations in this repository, ensure you have the following tools installed:

1. [Kubectl](https://kubernetes.io/docs/tasks/tools/)
2. [Helm](https://helm.sh/)
3. [Terraform](https://www.terraform.io/)

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

