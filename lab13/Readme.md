# Microservice Authorization #

The microservice will decide to either grant the user the resource (if the user has the required permissions) or not. Based on the implementation, the microservice can make this decision by itself (if it knows the permissions of this user over this resource) or simply forward the request to one of the Authorization Servers within the environment to determine the user’s permissions.

As we move from monoliths to microservices, we needed to centralize our authorization effort by creating an authorization service.  

## Code Authorization

When a user makes a request to the api gateway, the request passes through the authorization middleware which extracts the jwt(from cookie or header), verifies that it’s valid and retrieves the permissions claim from the jwt. Afterwards, the Authorize endpoint of the authorization service is called with the permissions as well as the url and http verb of the called endpoint. The authorize endpoint essentially returns true if any of the user’s permission has access to the endpoint.

## Data Authorization

There are some situations where different users have access to the same endpoint but the content they see are different i.e some users can see extra properties in the returned result. In this kind of scenario, authorization still happens as usual via the authorization service, however the microservice being called will still receive the users permissions as metadata and it will return specific fields based on the user’s permission.
