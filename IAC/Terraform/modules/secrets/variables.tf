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