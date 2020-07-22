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

1. Lets say the Kubernetes service is listening on port 80 <br/>
2. we have 3 K8s host nodes  <br/>
IPs 10.10.10.1, 10.10.10.2, 10.10.10.3 <br/>
3. the Nodeport picked at random was 31852. <br/>
4. With NodePort, Kubernetes Exposes the service on each Node’s 31852 .<br>
4. A client that exists outside of the cluster could visit <br/>
10.10.10.1:31852, 10.10.10.2:31852, or 10.10.10.3:31852 <br/>
5. Kubeproxy will forward the request to mynodeportservice's port 80 <br>
  
kubectl delete svc dateapi

kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab4/dateapi-service-nodeport.yaml

kubectl get svc

NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          
dateapi      NodePort    10.98.167.124   <none>        8080:30007/TCP 

### From within the cluster 
curl http://10.98.167.124:8080/date

### From outside the cluster

http://<public ip> :30007/date

How you get this address depends on how you set up your cluster. For example, if you are using Minikube, you can see the node address by running kubectl cluster-info.

kubectl cluster-info

note: you can also create a Service with NodePort using expose command
kubectl expose deployment dateapi-v1 --type=NodePort --name=dateapi

## Create a Service with load balancer
A single node is a single point of failure for the system. Once the node is down, clients can’t access the cluster any more. A service can be declared as LoadBalancer type to create a layer 4 load balancer in front of multiple nodes. As this layer 4 load balancer is outside of the Kubernetes network, a Cloud Provider Controller is needed for its provision. This Cloud Provider Controller watches the Kubernetes master for the addition and removal of Service resources and configures a layer 4 load balancer in the cloud provider network to proxy the NodePorts on multiple Kubernetes nodes.

kubectl delete svc dateapi

kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab4/dateapi-service-nodeport.yaml

kubectl get svc

NAME         TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          
dateapi      LoadBalancer   10.96.30.191   172.17.0.66   8080:32452/TCP

http://172.17.0.66:32452/date




