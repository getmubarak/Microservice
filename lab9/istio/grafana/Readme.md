# Grafana Dashboard
Time : 30 Mins

## Verify that the prometheus service is running in your cluster.
kubectl -n istio-system get svc prometheus

## Install via istioctl
istioctl install --set addonComponents.grafana.enabled=true

## Verify that the Grafana service is running in your cluster.
kubectl -n istio-system get svc grafana

# Convert the Cluster-IP to LoadBalancer for remote access
kubectl patch service grafana --patch '{"spec":{"type":"LoadBalancer"}}' -n istio-system

# Using port forwarding for local access
kubectl -n istio-system port-forward svc/grafana  20001:20001

# get the IP address and port
kubectl -n istio-system get service grafana -o jsonpath='{.status.loadBalancer.ingress[0].ip}'

kubectl -n istio-system get service grafana -o jsonpath='{.spec.ports[?(@.name=="http-grafana")].port}'

# Navigate to the grafana URL 
NAME    TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)           
grafana   LoadBalancer   10.97.34.213   172.17.0.20   20001:31948/TCP

(for example, http://172.17.0.20:31948/dashboard/db/istio-mesh-dashboard )
