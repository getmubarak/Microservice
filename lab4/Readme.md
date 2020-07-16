# Deploy Microservice to Kubernetis  #
Time : 30 minutes

https://www.katacoda.com/courses/istio/connecting-controlling-microservices/deploying-canary-releases#



kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab4/dateapi.yaml

kubectl get deployments

kubectl get pods

kubectl get svc

curl http://10.102.109.133:8080

kubectl delete deployment <name>

