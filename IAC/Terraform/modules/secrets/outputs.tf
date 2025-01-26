# output "kubernetes_secrets" {
#   value = {
#     for name, secret in kubernetes_secret.emulator :
#     name => {
#       secret_name = secret.metadata[0].name
#       namespace   = secret.metadata[0].namespace
#     }
#   }
# }