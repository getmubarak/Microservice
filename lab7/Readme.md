Traffic Management

Routing

Canary testing -- redirect a small percentage of user traffic to a new service version.
Serve different versions to different users -- Users on different plans or from a different regions may be served by separate environments
A/B testing.
Gradual rollouts.


kubctl delete virtual service

What if you want to pin your service to only v2? This can be done by specifying a subset in the VirtualService but we need to define those subsets first in a DestinationRules. A DestinationRule essentially maps labels to Istio subsets.

