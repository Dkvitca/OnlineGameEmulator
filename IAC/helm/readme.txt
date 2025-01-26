steps to initiate the project:

helm install argocd argo/argo-cd -n argocd --create-namespace

helm install cert-manager cert-manager/cert-manager -n cert-manager --create-namespace --version 1.16.2

helm install ingress-nginx ingress-nginx/ingress-nginx -n ingress-nginx --create-namespace --version 4.12.0

sudo nano /etc/hosts -> and set a dns name for the ingress-nginx loadbalancer ip address

apply ingress.yaml for the argocd

### get the initial password for the argocd admin user
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo

kubectl create namespace demo -> for the app deployment


##### secrets with sealed secrets ####
the installation of sealed secrets is threw the charts. its namespace is in a default one called kube-system

to actually get a secret working we need to do the following:

1. create a secret with this imperative command:
    kubectl create secret generic mongodb-secret --dry-run=client -o yaml --from-literal=USER=dan --from-literal=PASSWORD=dan > secret.yaml
     
    note: for now as far as i know after creation we cannot change any of the values. 
        this means that the name is set, the namespace as well.
2. create a sealed secret with the following command:
    
    kubeseal --controller-name sealed-secrets --controller-namespace kube-system --format yaml --namespace demo < secret.yaml > sealed-mongo-secret.yaml

    note: after this we recive an encrypted secret. none of the values can be modified.
    note: we must use the flags --controller-name and --controller-namespace to specify the controller that will be used to decrypt the secret.
