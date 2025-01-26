locals {
  secrets_map = {
    for key, value in jsondecode(data.aws_secretsmanager_secret_version.secret.secret_string) :
    key => (value) 
  }
}


data "aws_secretsmanager_secret_version" "secret" {
  secret_id = var.secret_id
}

resource "kubernetes_namespace" "namespace" {
  for_each = toset([for ns in var.k8s_secrets_config : ns.namespace_name])

  metadata {
    name = each.key
  }

}

resource "kubernetes_secret" "emulator" {
  for_each = { for config in var.k8s_secrets_config : config.k8s_secret_name => config }

  metadata {
    name      = each.value.k8s_secret_name
    namespace = kubernetes_namespace.namespace[each.value.namespace_name].metadata[0].name
  }

  data = {
    for key in each.value.keys : key => local.secrets_map[key]
  }

  type = "Opaque"
  depends_on = [kubernetes_namespace.namespace]
}

