Circuit Breaker With Outlier Detection

Downstream clients need to be protected from excessive slowness of upstream services. 
Upstream services, in turn, must be protected from being overloaded by a backlog of requests. 

Circuit breakers Enables fast failure rather than clients trying to connect to an overloaded or failing host. Once that limit has been reached the circuit breaker “trips” and stops further connections to that host.

Ejection/eviction implies that the host is identified as unhealthy and won't be used to cater to user requests as part of the load balancing process for a specified duration. 

circuit breaker policies you set in the DestinationRule. There are two fields under TrafficPolicy which are relevant to circuit breaking: ConnectionPoolSettings and OutlierDetection.

ConnectionPoolSettings controls the maximum number of requests, pending requests, retries or timeouts, while OutlierDetection controls the number of errors before a service is ejected from the connection pool.

With these settings in the ConnectionPoolSettings field, only one connection can be made to the notifications service within a given time frame: one pending request with a maximum of one request per connection. If a threshold is reached, the circuit breaker will start tripping requests.

The OutlierDetection section is set so that it checks whether there is an error calling the service every second. If there is, the service is ejected from the load balancing pool for at least three minutes.

baseEjectionTime: 
 If the request is forwarded to a certain instance and it fails , Istio will eject this instance from the pool for a certain sleep window. In our example, the sleep window is configured to be 3s. This increases the overall availability by making sure that only healthy pods participate in the pool of instances.
 
ConsecutiveErrors - Number of errors before a host is ejected from the connection pool. In the example, if you have 1 consecutive errors while interacting with a service, Istio will mark the pod as unhealthy. 
 
Interval - The time interval for ejection analysis. For example, the service dependencies are verified every 10 seconds.

MaxEjectionPercent - The max percent of hosts that can be ejected from the load balanced pool. For example, the 100% maximum ejection percent indicates that all services can be ejected from the pool at the same time, if necessary.
