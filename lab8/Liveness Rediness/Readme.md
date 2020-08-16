
Liveness probe checks the container health as we tell it do, and if for some reason the liveness probe fails, it restarts the container. 


In some cases we would like our application to be alive, but not serve traffic unless some conditions are met e.g, populating a dataset, waiting for some other service to be alive etc. In such cases we use readiness probe. If the condition inside readiness probe passes, only then our application can serve traffic.
