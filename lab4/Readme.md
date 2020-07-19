# Deploy Microservice to Kubernetis  #
Time : 30 minutes

https://www.katacoda.com/courses/istio/connecting-controlling-microservices/deploying-canary-releases#



kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab4/dateapi.yaml

kubectl get deployments

kubectl get pods

kubectl get svc

curl http://10.102.109.133:8080




kubectl get deployments
kubectl expose deployment hello-world --type=NodePort --name=example-service
kubectl describe services example-service
<Make a note of the NodePort value for the service.>

How you get this address depends on how you set up your cluster. For example, if you are using Minikube, you can see the node address by running kubectl cluster-info.
kubectl cluster-info.

curl http://<public-node-ip>:<node-port>
  
  
kubectl delete deployment <name>

