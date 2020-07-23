https://www.katacoda.com/courses/kubernetes/kubernetes-observability-efk-by-javajon

In traditional server environments, application logs are written to a file such as /var/log/app.log. 
These files are then viewed on each individual server or sent to a central repository for analysis and or retention.

This method of log collection is discouraged in Kubernetes due to the simple fact that pods can be numerous and short-lived. 
Kubernetes recommends letting the application output logs to the stdout and stderr. 

Each node has its own Kubelet running which will collect the segmented output logs and augment them into a singular log file.

kubectl get pods
kubectl logs pod logging-app-pod

A small binary, Kubetail runs kubectl logs-f on multiple pods and combines the results into a single data stream. Many of the same commands found in kubectl logs-g are found in Kubetail.

Numerous tools and solutions are available for centrally connecting pod logs. One of the most notable being fluentd. Fluentd collects and parses logs from numerous sources, then ships them to one or multiple repositories. 


mkdir -p /mnt/data/efk-master && kubectl create -f pv-master.yaml
mkdir -p /mnt/data/efk-data && kubectl create -f pv-data.yaml
kubectl create namespace logs

helm init

helm repo update

helm install stable/elasticsearch  \
 --name elasticsearch  \
--namespace=logs \
--set client.replicas=1 \
--set master.replicas=1 \
--set cluster.env.MINIMUM_MASTER_NODES=1 \
--set cluster.env.RECOVER_AFTER_MASTER_NODES=1 \
--set cluster.env.EXPECTED_MASTER_NODES=1 \
--set data.replicas=1 \
--set data.heapSize=300m \
--set master.persistence.storageClass=elasticsearch-master \
--set master.persistence.size=5Gi \
--set data.persistence.storageClass=elasticsearch-data \
--set data.persistence.size=5Gi

helm install stable/fluent-bit --name fluent-bit  --namespace=logs --set backend.type=es --set backend.es.host=elasticsearch-client

helm install  stable/kibana --name=kibana --namespace=logs --set env.ELASTICSEARCH_HOSTS=http://elasticsearch-client:9200 --set service.type=NodePort --set service.nodePort=31000

watch kubectl get deployments,pods,services --namespace=logs



