variable "project_name" {
  type        = string
}

variable "environment" {
  type        = string
}

variable "region" {
  type        = string
}

variable "cluster_name" {
  type        = string
}

variable "cidr_block" {
  description = "CIDR block for the VPC"
  type        = string
}

variable "eks_version" {
  type        = string
}

variable "desired_size" {
  description = "Desired number of nodes"
  type        = number
}

variable "max_size" {
  description = "Maximum number of nodes"
  type        = number
}

variable "min_size" {
  description = "Minimum number of nodes"
  type        = number
}

variable "instance_types" {
  description = "List of instance types for nodes"
  type        = list(string)
}

variable "tags" {
    type = map(string)
}

variable "k8s_secrets_config" {
  description = "List of Kubernetes secret configurations"
  type = list(object({
    namespace_name      = string
    k8s_secret_name     = string
    keys                = list(string) # Keys for each secret
  }))
}
variable "secret_id" {
  description = "AWS Secrets Manager Secret ID"
  type        = string
}