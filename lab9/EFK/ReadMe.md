https://www.katacoda.com/javajon/courses/kubernetes-observability/efk

In traditional server environments, application logs are written to a file such as /var/log/app.log. 
These files are then viewed on each individual server or sent to a central repository for analysis and or retention.

This method of log collection is discouraged in Kubernetes due to the simple fact that pods can be numerous and short-lived. 
Kubernetes recommends letting the application output logs to the stdout and stderr. 

Each node has its own Kubelet running which will collect the segmented output logs and augment them into a singular log file.

