https://kiali.io/documentation/latest/architecture/

## Prometheus
Prometheus is an open source monitoring system and time series database. You can use Prometheus with Istio to record metrics that track the health of Istio and of applications within the service mesh. You can visualize metrics using tools like Grafana and Kiali.

## Kiali - Observability
The metrics collected by Istio are scraped into Prometheus and visualized using Kiali.
What microservices are part of my Istio service mesh and how are they connected?

answers who is calling who, which version of a service has failures etc.

## Grafana – Metrics Visualization
Kiali has basic metric capabilities. It can show the default Istio metrics for workloads, apps and services. It allows to apply some groupings to the provided metrics and fetch metrics for different time ranges. However, Kiali doesn’t allow to customize the views nor customize the Prometheus queries. If you need these capabilities, you’ll want to install Grafana. 

## Jaeger - Distributed Tracing
One way to find a correlation between multiple HTTP requests is through the use of a correlation ID. This ID should be passed to all requests, so that the tracing platform knows which requests belong together.

For Istio to work properly, the following headers should be passed through:

x-request-id x-b3-traceid x-b3-spanid x-b3-parentspanid x-b3-sampled x-b3-flags x-ot-span-context

Istio supports a number of tracing backends, including Zipkin, Jaeger, Lightstep, and Datadog.

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


kubectl run fortio --image=istio/fortio -- load -t 5m -qps 5 http://10.101.94.93:8080/date

# Open up a browser (three tabs) and go to:
Kiali http://Exterternal IP:Node Port/kiali (username: admin, password: admin) <br>
Prometheus http://localhost:9090/ <br/>
Grafana http://Exterternal IP:Node Port/dashboard/db/istio-mesh-dashboard <br>
Jaeger http://Exterternal IP:Node Port <br>
