# Deploy Istio Service Mesh #
Time : 30 minutes

A service mesh ensures that communication among containerized and often ephemeral application infrastructure services is fast, reliable, and secure. The mesh provides critical capabilities including service discovery, load balancing, encryption, observability, traceability, authentication and authorization, and support for the circuit breaker pattern.

The service mesh is usually implemented by providing a proxy instance, called a sidecar, for each service instance. Sidecars handle interservice communications, monitoring, and security‑related concerns – indeed, anything that can be abstracted away from the individual services. This way, developers can handle development, support, and maintenance for the application code in the services; operations teams can maintain the service mesh and run the app.

Istio, backed by Google, IBM, and Lyft, is currently the best‑known service mesh architecture.

## download and extract the latest release
curl -L https://istio.io/downloadIstio | sh -

## Move to the Istio package directory
cd istio-1.6.5

## Add the istioctl client to your path
export PATH=$PWD/bin:$PATH

## Install Istio 
istioctl install --set profile=demo

Default — This is recommended for production deployments and configures the default settings of the IstioOperator API. That enforces most rules by default.

Demo — You can use it for playing around with Istio and learning, especially when you are using Minikube or a setup that has limited resources. 

Minimal — It contains a minimum amount of features just to support traffic management.

## check Istio status
istioctl proxy-status

## Label the namespaces on which you want to enable Istio to inject sidecar containers automatically. 
kubectl label namespace default istio-injection=enabled

## Ensure that there are no issues with the configuration:
istioctl analyze

kubectl get pod -n istio-system

## deploy microservice
kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab4/dateapi.yaml

kubectl get pods

We just deployed one container within the pod, but we are seeing two running in the pod. Istio is injecting sidecar containers automatically within the pod. 

kubectl get services

## make a request to the api.
curl http://10.106.138.233:8080/

## Create a ingress gateway 
Allocating a random port or external load balancer is easy to set in motion, but comes with unique challenges. Defining many NodePort services creates a tangle of random ports. Defining many Load Balancer services leads to paying for more cloud resources than desired. It’s not possible to avoid completely, but perhaps it could be reduced, contained, so that you would only need to allocate one random port or one load balancer to expose many internal services? The platform needed a new layer of abstraction, one that could consolidate many services behind a single entrypoint.
An Istio ingress gateway allows you to define entry points into the service mesh through which all incoming traffic flows. 

kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab6/mygateway.yaml

## check ingress gateway is running :

kubectl get gateway -A

kubectl get svc istio-ingressgateway -n istio-system

kubectl describe svc istio-ingressgateway -n istio-system |grep http2

<get port>
 
## create a virtual service :

kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab6/dateapi_virtualservice.yaml

## check virtual service is running :
kubectl get virtualservices.networking.istio.io

kubectl get virtualservice,gateway

curl http://10.100.172.29:80/date

<
In KataCoda to view the results on browser, click +
select port to view on Host1
Enter gateway port>

export INGRESS_HOST=$(sudo minikube ip)

export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].nodePort}')

curl http://$INGRESS_HOST:$INGRESS_PORT/date




