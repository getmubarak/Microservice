
# Types of Communication
We can split communications into the following types:
* A request for data (Query)
* A request to carry out a task (Command)
* A notification that something happened (Event)

# Inter Service Communication
* Shared Database / File system.
* API Centric using synchronous HTTP calls/ grpc calls.
* Self-Contained Services using asynchronous messaging.

## Shared Database Drawbacks
* The shared database pattern can cause a few headaches:
* Applications can affect each other's performance.
* Changes to a single table might require coordination between multiple teams and coordinated deployments.
* Some schema changes that would be beneficial for one service are not made because of a negative impact on other services.
* The data is not really optimised for any application. It is probably the full data set and fully normalised. Some applications have to write mega queries to get the data they need.
* Complexity grows and grows as we try to create the one true data model that represents the entire system
