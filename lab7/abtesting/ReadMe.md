


 A/B testing is primarily used to review the effectiveness of a change and how the market reacts to the change. The new features will be rolled out to a certain set of users. You can implement this with application-level switches (ie, smart logic that knows when to display certain UI controls), static switches (in the application), and also using Canary releases.
 

Canary releases can be used as a way to implement A/B testing due to similarities in the technical implementation. However, it is preferable to avoid conflating these two concerns: while canary releases are a good way to detect problems and regressions, A/B testing is a way to test a hypothesis using variant implementations. 
