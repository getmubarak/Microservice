Blue-green deployment is a technique that reduces downtime and risk by running two identical production environments called Blue and Green. At any time, only one of the environments is live, with the live environment serving all production traffic. For this example, Blue is currently live and Green is idle.
Once you have deployed and fully tested the software in Green, you switch the router so all incoming requests now go to Green instead of Blue. Green is now live, and Blue is idle.

kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab7/bluegreen/virtual-service-v1.yaml


kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab7/bluegreen/virtual-service-v2.yaml
