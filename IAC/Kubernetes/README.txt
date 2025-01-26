steps for deploying a kubernetes cluster:

install mongodb and pass it like this:
    helm install mongodb bitnami/mongodb -f <relative path to the values.yaml file> -n myapp

helm install ingress-nginx ingress-nginx/ingress-nginx -n ingress-nginx


then deploy the app one after the other.