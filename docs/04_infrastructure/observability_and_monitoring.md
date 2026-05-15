# Observability and Monitoring

In a modern, distributed architecture (microservices), when a user reports "the system is slow," traditional debugging no longer works. You need **Observability**: the ability to understand the internal state of a system based entirely on its external outputs.

Monitoring tells you *if* a system is broken. Observability tells you *why* it is broken.

## The Three Pillars of Observability

### 1. Logs
Logs are discrete, timestamped records of events that happened over time (e.g., "User X logged in at 10:00 AM").
- **Tools**: ELK Stack (Elasticsearch, Logstash, Kibana), Fluentd, Datadog.
- **Best Practice**: Use structured logging (JSON format) so logs can be easily parsed and queried by machines.

### 2. Metrics
Metrics are numerical values measured over intervals of time (e.g., CPU usage is 80%, Memory is 2GB, Error Rate is 5%). They are excellent for triggering alerts.
- **Tools**: Prometheus (data collection) + Grafana (visualization).
- **Golden Signals**: The four metrics you must always monitor:
  1. **Latency**: How long it takes to serve a request.
  2. **Traffic**: How much demand is being placed on your system (e.g., requests per second).
  3. **Errors**: The rate of requests that fail.
  4. **Saturation**: How "full" your system is (e.g., CPU/Memory utilization).

### 3. Distributed Tracing
In a microservices architecture, a single user request might travel through 5 different services. Tracing tracks the progression of a single request as it moves through the entire system.
- **Tools**: Jaeger, OpenTelemetry, Zipkin.
- **How it works**: A unique `Trace ID` is generated when a request enters the system and is passed along in the HTTP headers to every subsequent service. This allows you to visualize exactly where a bottleneck is occurring.

## The DevOps Goal
The goal of implementing observability is to reduce MTTR (Mean Time To Recovery). When an alert fires (Metrics), an engineer uses Traces to isolate the specific service causing the issue, and then looks at the Logs of that service to find the exact line of code that failed.
