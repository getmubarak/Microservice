Canary testing / Traffic Shifting

A canary deployment is a strategy for safely rolling out a new version of a service. 
With Istio, you can use percentage-based traffic splitting to direct a small amount of traffic to the new version. 
Then you can run a canary analysis on v2, and finally direct more traffic at the new version until it's serving all traffic.



kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab7/canary/virtual-service.yaml

kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab7/canary/destination-rule.yaml

