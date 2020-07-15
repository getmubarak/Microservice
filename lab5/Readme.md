
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

