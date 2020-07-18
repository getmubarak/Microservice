Canary testing 

A canary deployment is a strategy for safely rolling out a new version of a service. 
With Istio, you can use percentage-based traffic splitting to direct a small amount of traffic to the new version. 
Then you can run a canary analysis on v2, and finally direct more traffic at the new version until it's serving all traffic.



 A/B testing is primarily used to review the effectiveness of a change and how the market reacts to the change. The new features will be rolled out to a certain set of users. You can implement this with application-level switches (ie, smart logic that knows when to display certain UI controls), static switches (in the application), and also using Canary releases.
 
