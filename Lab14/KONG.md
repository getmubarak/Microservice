# Kong is a open-source API Gateway 

The main platform used to be substantially a monolithic Java codebase hosted on Tomcat and communicating with a single database for pretty much every operation.

First and foremost deployments became harder. Every small change required a full redeployment of the entire system and lots of team coordination, increasing our overhead and risks. 
When the codebase became increasingly hard to deploy, it made it harder to isolate failures, harder to onboard new contributors, and we knew something was fundamentally wrong. Slowly but surely these problems also affected the team performance and morale leading to an overall feeling of frustration. 


Transitioning a large legacy codebase is like opening a can of worms

## 
As we started to approach our transition it became evident that we couldn’t just allocate all of our resources to the project, and since our existing business was still running and growing on the monolith we had to split the team in two even smaller teams: one that would maintain the old codebase, while the other one would work on the new codebase. We underestimated resource allocation, and as a side effect this also created some morale friction across the two teams, since maintaining a large monolithic application is not as exciting as working on new technologies. This problem can be more easily dealt with in a larger team. In hindsight, we should have at least considered some sort of team members rotation, and the reason it wasn’t done was because we thought it would have slowed us down. 

##
The truth is that transitioning to microservices won’t happen overnight, no matter how hard we think about it and how much we plan for the transition, it’s just not going to happen quickly. And since the transition can sometimes be longer than the times it takes for a competitive market to move forward, the huge risk is leaving the business behind and damaging the company. Timing the transition is therefore as important as the transition itself



