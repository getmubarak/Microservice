
create a storage volume of 256 MB
wget https://raw.githubusercontent.com/getmubarak/Microservice/master/lab5/mongo-pv.yaml
kubectl create -f mongo-pv.yaml
kubectl get pv

claim/obtain the storage created and can be mounted on the mongo container. 
wget https://raw.githubusercontent.com/getmubarak/Microservice/master/lab5/mongo-pvc.yaml
kubectl create -f mongo-pvc.yaml
kubectl get pvc
kubectl get pv

wget https://raw.githubusercontent.com/getmubarak/Microservice/master/lab5/mongo.yaml
kubectl create -f mongo.yaml
kubectl get deployments

wget https://raw.githubusercontent.com/getmubarak/Microservice/master/lab5/mongo-svc.yaml
kubectl create -f mongo-svc.yaml
kubectl get svc mongo
curl 10.100.83.25:27017

wget https://raw.githubusercontent.com/getmubarak/Microservice/master/lab5/tasksapp.yaml
kubectl create -f tasksapp.yaml
kubectl get deployments

wget https://raw.githubusercontent.com/getmubarak/Microservice/master/lab5/tasksapp-svc.yaml
kubectl create -f tasksapp-svc.yaml
kubectl get svc tasksapp-svc

curl --header "Content-Type: application/json" --request POST --data '{"desc":"buy beer"}' http://10.110.170.73:8080/add
curl http://10.110.170.73:8080/get

kubectl scale deployment tasksapp --replicas=3

kubectl get pods
kubectl describe pods ${POD_NAME}
kubectl logs pod-crashloopbackoff-7f7c556bf5-9vc89

kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0-beta8/aio/deploy/recommended.yaml
kubectl proxy

