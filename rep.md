**Key Observations:**

#### **Pipes:**

* **Resource Usage**:
  * **CPU**: The container is using minimal CPU (0.13%).
  * **Memory**: 56.44 MiB of memory is in use, representing only 0.58% of the total available memory.
  * **Processes (PIDS)**: The container runs with 9 active processes.

#### **Services:**

* **Resource Usage**:
  * **CPU**: Most services are idle or consuming negligible CPU, with a maximum of 0.22% usage by `services-rabbit-1`.
  * **Memory**: The memory usage is distributed across multiple containers:
    * `rest_api_service`: 42.27 MiB (0.43%)
    * `services-rabbit-1`: 142.3 MiB (1.46%)
    * Other services (e.g., `publish_service`, `screaming_service`, `filter_service`): Around 14-16 MiB each (\~0.15%)..

### **Differences Between `Pipes` and `Services`:**

1. **Resource Utilization**:

   * **Pipes** consumes more memory in a single container (56.44 MiB) than individual services.
   * **Services** spread the resource usage across multiple containers, with the RabbitMQ service being the most resource-intensive (142.3 MiB).
2. **Flexibility and Scalability**:

   * **Pipes** is tightly coupled and harder to update or scale specific parts without affecting the whole system.
   * **Services** allows independent scaling and updates, making it better suited for dynamic workloads.

### **Advantages of `Services` Architecture:**

1. **Modularity**:
   * Each service can be developed, deployed, and scaled independently.
   * Easier to debug and maintain specific parts of the application.
2. **Scalability**:
   * Individual services (e.g., `filter_service` or `rest_api_service`) can be scaled horizontally based on workload.
3. **Fault Isolation**:
   * Failures in one service are isolated and do not affect the others, unlike in a monolithic `pipes` architecture.
4. **Flexibility**:
   * Technologies can vary across services, allowing developers to choose the best tool for each job.

### **Performance Testing Note**:

As you mentioned:

> We cannot check the speed of one request because on localhost with `curl` it always was 0 on my testing.

This is expected due to:

1. **Localhost Optimization**: On localhost, the network stack is extremely optimized, making the request latency nearly negligible.
2. **Testing Tools**: `curl` is not a reliable benchmarking tool for measuring service latencies.

Instead, consider using load testing tools like:

* **[wrk](https://github.com/wg/wrk)**: Simulates high-concurrency requests and provides detailed latency statistics.
* **Apache Bench (ab)**: Useful for simple throughput and latency tests.
