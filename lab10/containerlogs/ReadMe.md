https://medium.com/@chris_linguine/how-to-monitor-distributed-logs-in-kubernetes-with-the-efk-stack-1218a565ce0c
https://www.digitalocean.com/community/tutorials/how-to-set-up-an-elasticsearch-fluentd-and-kibana-efk-logging-stack-on-kubernetes


In traditional server environments, application logs are written to a file such as /var/log/app.log. 
These files are then viewed on each individual server or sent to a central repository for analysis and or retention.

This method of log collection is discouraged in Kubernetes due to the simple fact that pods can be numerous and short-lived. 
Kubernetes recommends letting the application output logs to the stdout and stderr. 
Each node has its own Kubelet running which will collect the segmented output logs and augment them into a singular log file.

kubectl get pods
kubectl logs pod logging-app-pod

By default in Kubernetes, Docker is configured to write a container's stdout and stderr to a file under /var/log/containers on the host system. 

We can verify our logs by ssh-ing into the minikube virtual machine and looking at this file.
minikube ssh
cd /var/log/containers
ls | grep logging-app

sudo head -n7 logging-app-pod_default_logging-app-CONTAINER-ID.log

A small binary, Kubetail runs kubectl logs-f on multiple pods and combines the results into a single data stream. Many of the same commands found in kubectl logs-g are found in Kubetail.

Numerous tools and solutions are available for centrally connecting pod logs. One of the most notable being fluentd. Fluentd collects and parses logs from numerous sources, then ships them to one or multiple repositories. 

You can implement cluster-level logging by including a node-level logging agent on each node. The logging agent is a dedicated tool that exposes logs or pushes logs to a backend. Commonly, the logging agent is a container that has access to a directory with log files from all of the application containers on that node.
Using a node-level logging agent is the most common and encouraged approach for a Kubernetes cluster, because it creates only one agent per node, and it doesn't require any changes to the applications running on the node. 
