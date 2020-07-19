# Deploy Istio Service Mesh #
Time : 30 minutes

start a Kubernetes cluster
https://www.katacoda.com/courses/kubernetes/installing-weave-scope-on-kubernetes

download and extract the latest release
curl -L https://istio.io/downloadIstio | sh -

Move to the Istio package directory
cd istio-1.6.5

Add the istioctl client to your path
export PATH=$PWD/bin:$PATH

Install Istio 
istioctl install --set profile=demo

Default — This is recommended for production deployments and configures the default settings of the IstioOperator API. That enforces most rules by default, and you can customise the configuration according to your requirements.
Demo — You can use it for playing around with Istio and learning, especially when you are using Minikube or a setup that has limited resources. For running the sample application, this is the most suitable profile, and we are going to use it for the demo.
Minimal — It contains a minimum amount of features just to support traffic management.

Label the namespaces on which you want to enable Istio to inject sidecar containers automatically. 
kubectl label namespace default istio-injection=enabled

Ensure that there are no issues with the configuration:
istioctl analyze
kubectl get pod -n istio-system

deploy
kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab4/dateapi.yaml

kubectl get pods
We just deployed one container within the pod, but we are seeing two running in the pod. Istio is injecting sidecar containers automatically within the pod. 

kubectl get services

make cURL request to the helloworld application by running following command.
curl http://10.106.138.233:8080/

An Istio ingress gateway allows you to define entry points into the service mesh through which all incoming traffic flows. 
kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab6/mygateway.yaml

You can see the ingress gateway is running using:
kubectl get gateway -A
kubectl get svc istio-ingressgateway -n istio-system
kubectl describe svc istio-ingressgateway -n istio-system |grep http2
<get port>
 
kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab6/dateapi_virtualservice.yaml

You can see the virtual service is running using:
kubectl get virtualservices.networking.istio.io
kubectl get virtualservice,gateway

curl http://10.100.172.29:80

<
In KataCoda to view the results on browser, click +
select port to view on Host1
Enter gateway port>

export INGRESS_HOST=$(sudo minikube ip)
export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].nodePort}')
curl http://$INGRESS_HOST:$INGRESS_PORT

To access the dashboard, you can use istioctl to open a proxy. use the default username admin and default password admin to log in
istioctl dashboard kiali

