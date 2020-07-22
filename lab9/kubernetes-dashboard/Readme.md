
## 1,  deploy dashboard serive on master node:
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.3/aio/deploy/recommended.yaml

## 2. (cloud)  change service “type” from ClusterIP to NodePort:
kubectl  edit service kubernetes-dashboard -n kubernetes-dashboard <br/>
... <br/>
type: NodePort                   ### clusterIP to NodePort <br/>

## 3. Following command will give us mapped port to dash-board service
kubectl get services -n kubernetes-dashboard

## 4. Get token
Retrieve an authentication token for the eks-admin service account. Copy the <authentication_token> value from the output. You use this token to connect to the dashboard.

kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep eks-admin | awk '{print $1}')

## 5, open a browser with the following api:
http://node port ip address: port

## 6. paste token
Then select "token" and past the token to log in the dashboard.

