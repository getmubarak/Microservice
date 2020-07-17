Setup some tunnels to each of the services:
Open up three new shell windows and type in one line into each:

kubectl -n istio-system port-forward $(kubectl -n istio-system get pod -l app=grafana -o jsonpath='{.items[0].metadata.name}') 3000:3000

kubectl port-forward -n istio-system $(kubectl get pod -n istio-system -l app=jaeger -o jsonpath='{.items[0].metadata.name}') 16686:16686

kubectl -n istio-system port-forward $(kubectl -n istio-system get pod -l app=kiali -o jsonpath='{.items[0].metadata.name}') 20001:20001

Open up a browser (three tabs) and go to:
Kiali http://localhost:20001/kiali (username: admin, password: mysecret)
Grafana http://localhost:3000/dashboard/db/istio-dashboard
Jaeger http://localhost:16686
