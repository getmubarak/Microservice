# Deploy Microservice to Kubernetis  #
Time : 30 minutes

## Create a deployment
A deployment is a supervisor for pods giving you fine-grained control over how and when a new pod version is rolled out as well as rolled back to a previous state. <br/>

kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab4/dateapi-deployment-v1.yaml

kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab4/dateapi-deployment-v2.yaml

kubectl get deployments

kubectl get pods

## Create a Service with Cluster IP
A Service is bound to a ClusterIP, which is a virtual IP address, and no matter what happens to the backend Pods, the ClusterIP never changes, so a client can always send requests to the ClusterIP of the Service. 

kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab4/dateapi-service.yaml

kubectl get svc

kubectl describe services dateapi

curl http://10.102.109.133:8080


## Create a Service with node port
ClusterIP is only reachable inside a Kubernetes cluster, but what if we need to access some services from outside of the cluster?
With NodePort, Kubernetes creates a port for a Service on the host, which allows access to the service from the node network. 

kubectl delete svc dateapi

kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab4/dateapi-service-nodeport.yaml

kubectl get svc

NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          
dateapi      NodePort    10.98.167.124   <none>        8080:30007/TCP 

## From within the cluster 
curl http://10.98.167.124:8080/date

## From outside the cluster

curl http://<public ip> :30007/date

How you get this address depends on how you set up your cluster. For example, if you are using Minikube, you can see the node address by running kubectl cluster-info.

kubectl cluster-info

note: you can also create a Service with NodePort using expose command
kubectl expose deployment dateapi-v1 --type=NodePort --name=dateapi

