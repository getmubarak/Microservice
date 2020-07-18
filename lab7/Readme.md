Traffic Management

Routing




Serve different versions to different users -- Users on different plans or from a different regions may be served by separate environments
A/B testing.
Gradual rollouts.



A/B Testing is used when we have two versions of an application (usually those differ visually) that we are not 100% sure which will increase user interaction and so we try both versions at the same time and collect metrics.

kubctl delete virtual service

What if you want to pin your service to only v2? This can be done by specifying a subset in the VirtualService but we need to define those subsets first in a DestinationRules. A DestinationRule essentially maps labels to Istio subsets.

