
## Kiali - Observability
What microservices are part of my Istio service mesh and how are they connected?

answers who is calling who, which version of a service has failures etc.

## Grafana – Metrics Visualization
The metrics collected by Istio are scraped into Prometheus and visualized using Grafana.

## Jaeger Tracer 
 Tracing requests throughout services. It is used for monitoring and troubleshooting microservices-based distributed systems, including:

Distributed context propagation <br/>
Distributed transaction monitoring <br/>
Root cause analysis <br/>
Service dependency analysis <br/>
Performance / latency optimization <br/>

## install
istioctl install --set profile=demo --set values.tracing.enabled=true  --set values.kiali.enabled=true  --set addonComponents.grafana.enabled=true

## check the services 
kubectl -n istio-system get svc

## verify that the prometheus service is running in your cluster.
kubectl -n istio-system get svc prometheus

## Convert the Cluster-IP to LoadBalancer for remote access
kubectl patch service grafana --patch '{"spec":{"type":"LoadBalancer"}}' -n istio-system

kubectl patch service kiali --patch '{"spec":{"type":"LoadBalancer"}}' -n istio-system

kubectl patch service jaeger-query --patch '{"spec":{"type":"LoadBalancer"}}' -n istio-system

## Using port forwarding for local access
kubectl -n istio-system port-forward svc/grafana 20001:20001


## check the externel IP and Node port  
kubectl -n istio-system get svc

## To view tracing information for each HTTP request, create some traffic by running the following commands at the command line:

while true; do <br>
  curl -s http://10.104.52.29:8080/date > /dev/null <br>
  echo -n .; <br>
  sleep 0.2 <br>
done <br>

# Open up a browser (three tabs) and go to:
Kiali http://Exterternal IP:Node Port/kiali (username: admin, password: mysecret) <br>
Grafana http://Exterternal IP:Node Port/dashboard/db/istio-dashboard <br>
Jaeger http://Exterternal IP:Node Port <br>
