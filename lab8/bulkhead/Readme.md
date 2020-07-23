
Similar to compartments on a ship, bulkheads are intended to partition the functionality of software into sections that can fail individually without causing the overall application to become unresponsive. They prevent errors from cascading further, while the rest of the application stays functional.

it helps to contain failures, attacks or performance degradations from spreading to other portions of the system because they are essentially partitioned.

A bulkhead limits the number of parallel calls to another service; this prevents the calling service from using too many threads for the parallel calls, and from getting into trouble itself in the form of a full thread pool. Istio’s Circuit Breaker works by limiting the number of simultaneous calls it can make. If the number exceeds the threshold, the Circuit Breaker in the sidecar interrupts the call and acknowledges it with an error. Of course, the calling service should react to the interruption with a corresponding error message (HTTP Status Code 503 – Service Unavailable). Since the call from the service is routed through the sidecar to the called service, the Circuit Breaker acts like a bulkhead in this case, since it limits the number of parallel calls in the calling service and thus indirectly affects the calling service.



## generate load

kubectl run fortio --image=istio/fortio -- load -t 5m -qps 5 http://10.101.210.76:80/date
