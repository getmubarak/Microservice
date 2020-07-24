## Centralize Configuration

A ConfigMap is an API object used to store non-confidential data in key-value pairs. Use a ConfigMap for setting configuration data separately from application code.

There are four different ways that you can use a ConfigMap to configure a container inside a Pod:
Command line arguments to the entrypoint of a container <br/>
Environment variables for a container <br/>
Add a file in read-only volume, for the application to read <br/>
Write code to run inside the Pod that uses the Kubernetes API to read a ConfigMap <br/>

## 
kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab11/config.yaml

##
kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab5/mongo-pv.yaml<br/>
kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab5/mongo-pvc.yaml<br/>
kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab5/mongo.yaml<br/>
kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab5/mongo-svc.yaml<br/>
kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab5/tasksapp-svc.yaml<br/>

##
kubectl apply -f  https://raw.githubusercontent.com/getmubarak/Microservice/master/lab11/tasksapp.yaml


##
kubectl get svc

curl --header "Content-Type: application/json" --request POST --data '{"desc":"buy beer"}' http://10.110.170.73:8080/add

curl http://10.110.170.73:8080/get

