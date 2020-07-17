Resiliency

1. Timeouts

2. Retries

3. Circuit breakers
Enables fast failure rather than clients trying to connect to an overloaded or failing host. Once that limit has been reached the circuit breaker “trips” and stops further connections to that host.

4. Fault injection
There are two types of faults 
Delays — are timing failures. They mimic increased network latency or an overloaded upstream service.
Aborts — are crash failures. They mimic failures in upstream services. Aborts usually manifest in the form of HTTP error codes or TCP connection failures.
