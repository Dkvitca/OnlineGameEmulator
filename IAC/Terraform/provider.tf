terraform {
  backend "s3" {
    bucket = "dan-terraform-s3"
    key    = "terraform/emulator/terraform.tfstate"
    region = "ap-south-1"
    dynamodb_table = "dan-terraform-lock-table"
    encrypt        = true
  }
}

provider "aws" {
  region = var.region

  default_tags {
    tags = {
      owner           = "dan.kvitca"
      bootcamp        = "BC22"
      expiration_date = "03-03-2025"
    }
  }
}

provider "kubernetes" {
  host                   = module.eks_cluster.eks_cluster_endpoint
  cluster_ca_certificate = base64decode(module.eks_cluster.eks_cluster_certificate)
  token                  = data.aws_eks_cluster_auth.emulator-eks-cluster.token
}

data "aws_eks_cluster_auth" "emulator-eks-cluster" {
  name = var.cluster_name
}

provider "tls" {}