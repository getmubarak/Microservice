Services can use multiple distributed resources in order to display the response to a user request. The Bulkhead Pattern compartmentalizes these calls so that poor performance of one service does not negatively impact the results of other services, and in the end, the user experience. The Bulkhead Pattern is based on a familiar concept implemented in ship designs. Ships are divided into watertight compartments in order to keep water from spreading from one compartment to other areas in the ship during a hull breach. Each of these compartments is called a “bulkhead.” This way if the ship’s hull is compromised the risk of the ship sinking is reduced.

A circuit breaker pattern is implemented on the caller side, to prevent overwhelming a service which may be struggling to handle calls. 
A bulkhead pattern is implemented on the service side, to prevent a failure during the handling of a single call from a caller affecting the handling of other incoming calls.

A bulkhead limits the number of parallel calls to another service; this prevents the calling service from using too many threads for the parallel calls, and from getting into trouble itself in the form of a full thread pool. Istio’s Circuit Breaker works by limiting the number of simultaneous calls it can make. If the number exceeds the threshold, the Circuit Breaker in the sidecar interrupts the call and acknowledges it with an error. Of course, the calling service should react to the interruption with a corresponding error message (HTTP Status Code 503 – Service Unavailable). Since the call from the service is routed through the sidecar to the called service, the Circuit Breaker acts like a bulkhead in this case, since it limits the number of parallel calls in the calling service and thus indirectly affects the calling service.

## apply throttling
kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab8/bulkhead/dateapi-virtual-service.yaml


## add circuit breaker
kubectl apply -f https://raw.githubusercontent.com/getmubarak/Microservice/master/lab8/circuitbreaker/destination-rule.yaml


## generate load
kubectl run fortio --image=istio/fortio -- load -t 5m -qps 5 http://<gateway ip>:80/date
