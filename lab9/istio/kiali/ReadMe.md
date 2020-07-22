# Kiali Dashboard
Time : 30 Mins

## Create a secret
KIALI_PASSPHRASE=$(read -sp 'Kiali Passphrase: ' pval && echo -n $pval | base64)

KIALI_USERNAME=$(read -p 'Kiali Username: ' uval && echo -n $uval | base64)

NAMESPACE=istio-system

cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Secret
metadata:
  name: kiali
  namespace: $NAMESPACE
  labels:
    app: kiali
type: Opaque
data:
  username: $KIALI_USERNAME
  passphrase: $KIALI_PASSPHRASE
EOF

## Install via istioctl
istioctl install --set values.kiali.enabled=true 

# Check Kiali service
kubectl -n istio-system get svc kiali

# Convert the Cluster-IP to LoadBalancer for remote access
kubectl patch service kiali --patch '{"spec":{"type":"LoadBalancer"}}' -n istio-system

# Using port forwarding for local access
kubectl -n istio-system port-forward svc/kiali  20001:20001

# get the IP address and port
kubectl -n istio-system get service kiali -o jsonpath='{.status.loadBalancer.ingress[0].ip}'

kubectl -n istio-system get service kiali -o jsonpath='{.spec.ports[?(@.name=="http-kiali")].port}'

# Navigate to the Kiali URL 
NAME    TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)           
kiali   LoadBalancer   10.97.34.213   172.17.0.20   20001:31948/TCP

(for example, http://172.17.0.20:31948/kiali/)
