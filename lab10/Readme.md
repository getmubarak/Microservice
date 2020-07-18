Distributed tracing

One way to find a correlation between multiple HTTP requests is through the use of a correlation ID. This ID should be passed to all requests, so that the tracing platform knows which requests belong together.

For Istio to work properly, the following headers should be passed through:

x-request-id
x-b3-traceid
x-b3-spanid
x-b3-parentspanid
x-b3-sampled
x-b3-flags
x-ot-span-context

Istio supports a number of tracing backends, including Zipkin, Jaeger, Lightstep, and Datadog. 
