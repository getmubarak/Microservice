Traffic Management

Routing

Canary testing -- redirect a small percentage of user traffic to a new service version.
Serve different versions to different users -- Users on different plans or from a different regions may be served by separate environments
A/B testing.
Gradual rollouts.

Blue-green deployment is a technique that reduces downtime and risk by running two identical production environments called Blue and Green. At any time, only one of the environments is live, with the live environment serving all production traffic. For this example, Blue is currently live and Green is idle.
Once you have deployed and fully tested the software in Green, you switch the router so all incoming requests now go to Green instead of Blue. Green is now live, and Blue is idle.

A/B Testing is used when we have two versions of an application (usually those differ visually) that we are not 100% sure which will increase user interaction and so we try both versions at the same time and collect metrics.

kubctl delete virtual service

What if you want to pin your service to only v2? This can be done by specifying a subset in the VirtualService but we need to define those subsets first in a DestinationRules. A DestinationRule essentially maps labels to Istio subsets.

