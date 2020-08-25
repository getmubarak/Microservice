
# What we did
We split the services based on the smallest functionality from the beginning of the project in order to accommodate any scaling needs that may arise in the future (a hard initial requirement from the client). Our initial designs had changed quite a bit during development due to many things, including lack of clear insights into 3rd party integrations and limitations of certain parts of the systems that we had to build with. This resulted in a system that was difficult to update and required complex orchestration of deployment to ensure coupled services were deployed properly. In short, we tried to prematurely optimize the entire platform.

## Lesson learned
It’s an easy and common mistake to over-optimize when designing a system by modularizing everything. With microservices, these mistakes will lead to a lot of deployment issues (which is why there’s a deployment section coming up in this article), so ask yourself the following questions before you split a piece of code into two or more microservices:

If I update A, do I need to update B (coupling)?
Does every request to A go to B (dependency)?
If  A talks to B and B breaks, will it cause data inconsistency and would it break data integrity?
If the answer to any of these questions was yes, you probably should rethink the split.

# Documentation
## What we did
The decision for inter-service communication was to use a REST API, so Swagger (now OpenAPI spec 3.0) was a natural choice for documentation of each service. It provided a clear and concise way of describing the API and it allowed for great tooling, like generating client libraries.
We wrote the API contract using Swagger during a “design” phase, then went to code, and then higher level documentation (sequence diagrams, data flows, etc…)
This approach definitely slowed our progress during each iteration. Newer developers on the project had a difficult time getting up to speed with how the whole system worked. This might not be needed when you have large development teams, but for small teams and team leads you still need to be able to transfer the whole system’s knowledge quickly and efficiently, so this approach didn’t work so well.

## Lesson learned
In your typical agile environment, efficiently lazy developers preach that documentation is less of a priority. However, with microservices, it’s mission critical to document the architecture and component interaction among your microservices. That interaction is where all the complexity of your system lies. The whole reason for microservices is to simplify the logic of each component in order to allow for more control over scaling, resources, and faster iterations of said components, and while this is true, a complex system will remain complex. With Microservices Architecture, that complexity just moves up a level for the most part. It’s much easier to understand high-level concepts and then dive into details than the other way around (this will help in onboarding new developers on your team).
It is imperative to keep the documentation up to date, because the addition of any new service may exponentially grow the complexity of the system.

# Versioning Strategy
## What we did
To be honest, we didn’t “officially” version the services as we were building 1.0 for this project. We did keep a history of versions that were built, but we didn’t have an easy rollback mechanism until later in the development (see deployment, again). Not that big of a deal… until something breaks and the team scrambles to figure out the issue only to discover that it was due to a minor model update – the service receiving the request is now rejecting it because it’s expecting another ‘required’ parameter.

## Lesson Learned
Care should be taken when introducing new versions. Breaking changes can have a chain effect when working with a microsystem architecture, so avoid it as much as possible.
Newer versions should have at least the same data in the response: Avoid removing data from responses so that services that rely on that data don’t break.
Newer versions should have, at most, the same input strictness: Avoid introducing new required parameters. New parameters should be optional, so existing services that talk to the updated service don’t break.

# Authentication and Authorization
## What we did
Here we opted to use Kong both as a gateway and for authentication and authorization of this service, and it was a good choice because it has a straightforward API and is easily extensible.
When building a project such as this it’s recommended to have a separate service that handles the authentication and authorization as it will become easier to manage, can be extended as the project scales, and can be integrated with any existing authorization infrastructure the organization uses. Kong can do all of these things because of its flexible plugin system.

## Lesson Learned
Sometimes you make the right call from the beginning, which is great.Using Kong as the gateway for authentication and authorization has been (so far) the right call for this system that we built.
Since Kong supports two storage backends (Postgres and Cassandra), we opted to use Cassandra, but we probably could have also used Postgres and had a bit of an easier time with our deployments since Cassandra requires a lot of memory.

# Fail Frequently
## What we did
We had our services connected to a database cluster and every now and then the connection would die causing the service to stop responding and was unable to restart the connection on its own. We added all kinds of logic to the driver wrapper to help restart connectivity, but there was always a case where a manual restart of the service had to be done.

## Lesson learned
Containers and inter-node connectivity will always fail at some point. When that happens, log the necessary information and let the service crash. Your system should have other healthy containers that can take on the request when it is retried. This approach will help keep your system up while giving you time to debug the issue and react if it’s not related to a hardware failure.

# Common Code Sharing
## What we did
Antipattern Alert:
We started by creating some shared modules and clients for the existing services and put them all into a shareable module. This turned out to be one of the worst decisions we made, but it seemed like a great idea at the time. Soon enough though, we started seeing dependency issues where the service would require a certain version of a component in the shared library and a different version of a different component.

## Lesson learned
Code sharing can and will save a lot of time, every developer knows that. But when implementing some shared code within your system your shared libraries should be written with zero context of the system as a whole and should be service agnostic code (purely logical).
Shared libraries should be limited to a single functionality, or a group of related functionalities (ne library for logging, another for service A communication, another for service B communication, etc).
Note: If you’re sharing data models, then you should rethink the split. If not well thought out, this can easily become an antipattern.

# Logging
## What we did
We used ELK stack for our logging and pushed the logs to logstash. We also passed a “requested” as part of every message, which allowed us to track requests through the system.
If the service was logging something that was triggered by an external event (Like an http call to that service, for example) then it will use the requestId that was used by that service and that would get forwarded with any subsequent calls.
This worked well for the most part until one day everything stopped and we realized that the service that would authenticate logs crossing zones had broke and it was trying to log its own errors, which prevented it from recovering.

## Lesson learned
Logging is very important for a project like this as you need to be able to monitor a request lifecycle and how it flows through the system.
There are a few different ways to gather logs. You could have an agent on each container that collects logs from stdout/stderr and ships them to a log server, or you could send the logs directly to the log server. The disadvantage of the latter is that you would need to implement and configure the logging client for each service, whereas if you are using an agent that collects the logs from stdout/stderr, it will allow you to streamline the process.

# Testing
## What we did
We have an amazing QA team, but this was our first enterprise-level microservices project and we have had some challenges with testing.
The QA team was asked to test outages and components breaking, as well as the individual microservice behavior.
There was a lot of infrastructure context that needed to be transferred to the QA team in order to accomplish that and we were still not able to uncover all the critical issues. We desired better tools to make deployments and breaking certain parts of the system easier, and more streamlined. ( We didn’t find or build them, yet )

## Lesson learned
While it is well-known that unit-testing and integration testing are vital tactics for testing complex systems, there are several nuances with both of them in a microservices world:
Unit Testing: For the individual services, unit testing is crucial. You need to have the ability to mock the communication layer among the services and if the inter-service communication is happening by making synchronous calls
Integration Testing: Can be among 2 or more services. These tests validate that the related services can communicate with each other properly, and appropriate fallbacks happen when certain services are not available.
All of that testing can and should be done by the developers working on the service and QA should probably only be engaged to do exploratory testing (try to break the system from an end user’s point of view, malicious or not) if they are not well-equipped to do outage testing.

# Deployment
## What we did
Deployment orchestration is not trivial when dealing with microservices. Here we decided to use docker 1.11 with swarm. It turns out that swarm mode just came out and wasn’t stable or mature enough for us to start using. As a result, we had to resort to a lot, and I mean a lot, of custom scripts to manage this beast.
These are just some of the issues encountered:
Managing the scripts for 3 gateways when there are version changes for a service request that has to cross these 3 gateways.
Managing multiple versions and rollbacks with custom tooling around swarm
Keeping track of service dependencies to ensure a smooth update
Service discovery for multiple versions
“Encouraging” swarm nodes to reconnect to the swarm following an outage
Managing the swarm backend

## Lesson learned
Complex systems already have their own set of devops problems. Complex systems with a lot of inter-dependencies will add an exponential amount of work to devops.
Building less parts, less is more, holds true for those devops.
When using bleeding edge technologies, ensure you have an upgrade path. With the fast-changing world of devops, a lot can be gained with newer versions of the tools that aim to maximize automation. Even though our tools have long matured since then, and a lot has been automated, our devops team would still take the upgrade over maintaining those tools.
