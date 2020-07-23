
## install
istioctl install --set profile=demo --set values.tracing.enabled=true  --set values.kiali.enabled=true  --set addonComponents.grafana.enabled=true

## Kiali - Observability
What microservices are part of my Istio service mesh and how are they connected?

answers who is calling who, which version of a service has failures etc.

## Grafana – Metrics Visualization
The metrics collected by Istio are scraped into Prometheus and visualized using Grafana.

## Jaeger Tracer 
 Tracing requests throughout services.

Open up a browser (three tabs) and go to:
Kiali http://localhost:20001/kiali (username: admin, password: mysecret)
Grafana http://localhost:3000/dashboard/db/istio-dashboard
Jaeger http://localhost:16686
