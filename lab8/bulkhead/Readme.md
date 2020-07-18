it helps to contain failures, attacks or performance degradations from spreading to other portions of the system because they are essentially partitioned.


Istio configuration that limits a web service to issue no more than 500 requests per second against a users service and a search service to issue no more than 200 requests per second. 

Two Perspectives on the Bulkhead
Bulkheads can be implemented in a way that focuses on either the concerns of developers or the concerns of operations teams. The key difference between these two implementations is that developers are more concerned with whether or not their application will run as designed, while the operations team is more concerned with whether or not they can effectively secure and scale the services when they begin to interact with additional services in an organic manner.
