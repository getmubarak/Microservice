## Microservice Authentication
In microservice scenarios, authentication is handled centrally. If you're using an API Gateway, the gateway is a good place to authenticate. A user starts by sending his credentials to the API gateway which will forward the credentials to the Authorization Server (AS) or the OAuth Server. The AS will generate a JASON Web Token (JWT) and will return it back to the user.

 Whenever the user wants to access a certain resource, he’ll request it from the API Gateway and will send the JWT along with his request. The API Gateway will forward the request with the JWT to the microservice that owns this resource. 

# Microservice Authorization #

The microservice will decide to either grant the user the resource (if the user has the required permissions) or not. Based on the implementation, the microservice can make this decision by itself (if it knows the permissions of this user over this resource) or simply forward the request to one of the Authorization Servers within the environment to determine the user’s permissions.

As we move from monoliths to microservices, we needed to centralize our authorization effort by creating an authorization service.  

## Code Authorization

When a user makes a request to the api gateway, the request passes through the authorization middleware which extracts the jwt(from cookie or header), verifies that it’s valid and retrieves the permissions claim from the jwt. Afterwards, the Authorize endpoint of the authorization service is called with the permissions as well as the url and http verb of the called endpoint. The authorize endpoint essentially returns true if any of the user’s permission has access to the endpoint.

## Data Authorization

There are some situations where different users have access to the same endpoint but the content they see are different i.e some users can see extra properties in the returned result. In this kind of scenario, authorization still happens as usual via the authorization service, however the microservice being called will still receive the users permissions as metadata and it will return specific fields based on the user’s permission.

## RequestAuthentication policy that validates incoming tokens
kubectl apply -f  https://raw.githubusercontent.com/getmubarak/Microservice/master/lab10/RequestAuthentication.yaml


## AuthorizationPolicy, which ensures that all requests have a JWT - and rejects requests that do not, returning a 403 error.
kubectl apply -f  https://raw.githubusercontent.com/getmubarak/Microservice/master/lab10/AuthorizationPolicy.yaml


## use the script gen-jwt.py to generate new tokens 
wget https://raw.githubusercontent.com/istio/istio/release-1.6/security/tools/jwt/samples/gen-jwt.py <br/>
chmod +x gen-jwt.py

## You also need the key.pem file:
wget https://raw.githubusercontent.com/istio/istio/release-1.6/security/tools/jwt/samples/key.pem

##  install jwcrypto library
pip2 install jwcrypto

##  creates a token that expires in 25 seconds
TOKEN=$(./gen-jwt.py ./key.pem --expire 25)

##  curl the Istio ingress gateway without a JWT
the AuthorizationPolicy wil reject our request because we did not supply a token:

curl http://{INGRESS_IP}:{port}

## curl with an invalid JWT.
We will receive an authentication error:

curl --header "Authorization: Bearer JingleBell"  http://{INGRESS_IP}:{port}

## if we curl with a valid JWT, we can successfully reach the frontend via the IngressGateway:
curl --header "Authorization: Bearer $TOKEN" http://{INGRESS_IP}:{port}
