To test the timeout functionality you can inject a delay of say 10 seconds between your services. You can verify that when you invoke the service endpoint there is a delay of 10 seconds to get a response.

kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab8/timeouts/virtual-service.yaml
