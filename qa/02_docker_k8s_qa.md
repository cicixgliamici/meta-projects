# Docker & Kubernetes - Interview Q&A

### 1. What is the difference between a Container and a Virtual Machine (VM)?
**Answer:** 
- A **VM** emulates the entire hardware and requires its own Operating System (Guest OS). It is heavy and slow to boot.
- A **Container** only virtualizes at the OS level, sharing the Host machine's Kernel. It contains only the application and its dependencies. It is extremely lightweight (megabytes vs gigabytes) and starts in fractions of a second.

### 2. How do you persist data in Docker?
**Answer:** 
Since containers are ephemeral (data written inside them is lost when they are destroyed), we use **Volumes** or **Bind Mounts**. Volumes are portions of the host machine's filesystem directly managed by Docker and mounted inside the container.

### 3. What is Kubernetes and why isn't Docker enough?
**Answer:** 
Docker is used to create and run containers. But when you need to run hundreds of containers across different servers, manually managing load balancing, auto-scaling, and restarts upon crashes becomes impossible. **Kubernetes** is the orchestrator that automates all these operations to maintain the infrastructure in the desired state.

### 4. What is the difference between a Pod and a Container in K8s?
**Answer:** 
In Kubernetes, containers are never run directly. They are always encapsulated in a **Pod**, which is the smallest unit of deployment. A Pod can contain one or more containers that share the same IP address, network namespace, and storage volumes.

### 5. What is a Deployment in K8s?
**Answer:** 
A Deployment is a K8s object that defines the desired state of your application. It allows you to declare how many "replicas" (Pods) of your application you want running. The Deployment Controller will constantly ensure that this number is met and will handle update logic (e.g., Rolling Updates) with zero downtime.
