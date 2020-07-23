# Fault injection 

There are two types of faults 

## Delays — are timing failures.
They mimic increased network latency or an overloaded upstream service. 

kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab8/faultinjection/delay.yaml

## Aborts — are crash failures. 
They mimic failures in upstream services. Aborts usually manifest in the form of HTTP error codes or TCP connection failures.

kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab8/faultinjection/abort.yaml
