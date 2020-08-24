# Microservice design

## Step 1: Start with a monolith. <br>

* A word of caution though as building a monolith can quickly lead to complicated code that will be hard to break down in smaller pieces. Try as much as you can to have clear modules identified so that you can extract them later out of the monolith. You can also start by separating the logic from your web UI and make sure that it interacts with your backend via a RESTful API over HTTP. This will make the transition to microservices easier in the future when you start moving some of the API resources to different services.

## Step 2: Organise your teams the right way

* Developers often conclude that technology is the answer to everything, but people and processes are prerequisites to using technology effectively, especially software development.

* Creating microservices is more about team organization and approach than it is about technology.

* you should create smaller teams that have all the competencies required to develop and maintain the services they're in charge of. 

## Step 3 :Embrace Devops Culture 

* continous delivery
* testing
* monitoring
* alerting

## step 4 : Build your microservices using a microservice chassis framework, which handles cross-cutting concerns

* service mesh
* api gateway
* traffic management
* Resilence

## Step 5 :Split the monolith to build a microservices architecture

* Go Macro First, then Micro. Start with larger services around a logical domain concept, and break the service down into multiple services when the teams are operationally ready.

* Start With Just One Service, Not With a Few in Parallel

* Start With Services That Bring Business Value

* The goal when identifying model boundaries and size for each microservice isn't to get to the most granular separation possible, although you should tend toward small microservices if possible. Instead, your goal should be to get to the most meaningful separation guided by your domain knowledge. The emphasis isn't on the size, but instead on business capabilities. 
Some people, such as Fred George, claim services should be small, maybe between 100-1000 lines of code (LoC). However, LoC is a poor metric for measuring software in general and even more so for determining the scope of a Microservice. 

* The (better) alternative to a complete rebuild is to slowly and systematically take over the old application. As you create new, independent services, you 
kill off the old corresponding services. This realizes benefits more quickly while reducing risk. This was dubbed the “Strangler Pattern” by Martin Fowler. 

* Our aim is to design Microservices that are autonomous, ie. have a low coupling with other services, have well defined interfaces, and implement a single business capability, ie. have high cohesion.

* words often have different meanings in different contexts. To overcome this hurdle, language should have a strict applicability context. This context is called a Bounded Context. It defines a boundary, inside of which a word can be used freely. Outside of it, the language’s terms may have different meanings.
A Microservice is a Bounded Context, but not vice versa. Not every Bounded Context is a Microservice. A Bounded Context defines the boundaries of the biggest services possible: services that won’t have any conflicting models inside of them.


