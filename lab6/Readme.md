
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

Istio comes bundled with a hello world example application. 
kubectl apply -f samples/helloworld/helloworld.yaml

kubectl get pods
We just deployed one container within the pod, but we are seeing two running in the pod. Istio is injecting sidecar containers automatically within the pod. 

kubectl get services

make cURL request to the helloworld application by running following command.
curl http://10.106.138.233:5000/hello

the service is doing round robin to two pods. 
 
To access the dashboard, you can use istioctl to open a proxy. use the default username admin and default password admin to log in
istioctl dashboard kiali

