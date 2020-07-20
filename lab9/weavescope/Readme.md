
## To install Weave Scope on your Kubernetes cluster, run
kubectl create -f 'https://cloud.weave.works/launch/k8s/weavescope.yaml?k8s-service-type=NodePort'
 
k8s-service-type - can be either LoadBalancer or NodePort, by default this is unspecified (only internal access)

## get all services
kubectl get svc --all-namespaces

weave         weave-scope-app   NodePort    10.102.56.34   <none>        80:32111/TCP

## Open Scope in Your Browser

curl http://10.102.56.34:32111
