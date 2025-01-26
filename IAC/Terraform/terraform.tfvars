secret_id = "dan-emulator-secrets"

k8s_secrets_config = [
  {
    namespace_name      = "myapp"
    k8s_secret_name     = "mongodb-credentials"
    keys                = ["mongodb-root-password", "mongodb-passwords", "mongodb-replica-set-key"]
  },
  {
    namespace_name      = "myapp"
    k8s_secret_name     = "database-credentials"
    keys                = ["USER", "PASSWORD"]
  },
  {
    namespace_name      = "myapp"
    k8s_secret_name     = "aws-credentials"
    keys                = ["aws_access_key_id", "aws_secret_access_key", "aws_s3_bucket"]
  }
]
cluster_name = "dan-emulator-cluster"
cidr_block   = "10.0.0.0/16"
eks_version  = "1.31"
desired_size = 3
max_size     = 3
min_size     = 2
instance_types = ["t3.medium"]

tags = {
  environment = "dev"
  terraform  = "true"
  kubernetes = "dan-eks-cluster"
}



project_name = "emulator"
environment  = "dev"
region = "ap-south-1"