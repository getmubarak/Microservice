1,  deploy dashboard serive on master node:
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.3/aio/deploy/recommended.yaml

2, start proxy: 
kubectl proxy&

3, create your own secret and obtain the token:
kubectl create serviceaccount <account name>
kubectl create clusterrolebinding dashboard-admin --clusterrole=cluster-admin --serviceaccount=default:<account name>
kubectl get secret
kubectl describe secret <secret name>
  
4, create ssh tunnel from a remote host outside of the cluster where you would access dashboard:
ssh -L 9999:127.0.0.1:8001 -N -f -l <user name> <k8s master host name or ip>
"-L" local port forwarding
"9999" is a local host port. it can be any available port. It can also be 8001
"127.0.0.1:8001" is where the proxy runs on k8s master host
Password may be required for the <user name> on the master host to create a tunnel
This command forwards any local request on port 9999 to"127.0.0.1:8001" on the master host
  
5, open a browser with the following api:
http://localhost:9999/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/

Then select "token" and past the token to log in the dashboard.

Setup some tunnels to each of the services:
Open up three new shell windows and type in one line into each:

kubectl -n istio-system port-forward $(kubectl -n istio-system get pod -l app=grafana -o jsonpath='{.items[0].metadata.name}') 3000:3000

kubectl port-forward -n istio-system $(kubectl get pod -n istio-system -l app=jaeger -o jsonpath='{.items[0].metadata.name}') 16686:16686

kubectl -n istio-system port-forward $(kubectl -n istio-system get pod -l app=kiali -o jsonpath='{.items[0].metadata.name}') 20001:20001

Open up a browser (three tabs) and go to:
Kiali http://localhost:20001/kiali (username: admin, password: mysecret)
Grafana http://localhost:3000/dashboard/db/istio-dashboard
Jaeger http://localhost:16686
