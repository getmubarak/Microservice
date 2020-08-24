## Microservice Authentication
In microservice scenarios, authentication is handled centrally. If you're using an API Gateway, the gateway is a good place to authenticate. A user starts by sending his credentials to the API gateway which will forward the credentials to the Authorization Server (AS) or the OAuth Server. The AS will generate a JASON Web Token (JWT) and will return it back to the user.

 Whenever the user wants to access a certain resource, he’ll request it from the API Gateway and will send the JWT along with his request. The API Gateway will forward the request with the JWT to the microservice that owns this resource. 
 
 
Time 30 mins

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
