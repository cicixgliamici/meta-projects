# Kubernetes Fundamentals

As applications grow to hundreds or thousands of containers, managing them manually (or with simple tools like Docker Compose) becomes impossible. **Kubernetes (K8s)** is a Container Orchestration platform designed to automate deploying, scaling, and operating application containers.

## Why Container Orchestration?
When running containers in production, you need answers to:
- What happens if a container crashes? (Self-healing)
- How do we handle sudden traffic spikes? (Auto-scaling)
- How do users access the application? (Load balancing and Service Discovery)
- How do we update an application without downtime? (Rolling updates)

Kubernetes handles all of this automatically based on a desired state you define.

## Architecture

Kubernetes clusters are composed of two main parts:
1. **Control Plane (Master Nodes)**: The brain of the cluster. It makes global decisions (scheduling, responding to cluster events). Key components include the API Server, Scheduler, and `etcd` (the database storing cluster state).
2. **Worker Nodes**: The machines that actually run the containerized applications. They contain the `kubelet` (an agent that communicates with the Control Plane) and a container runtime (like Docker or containerd).

## Core Concepts (Objects)

Kubernetes uses declarative configuration (YAML). You declare what you want, and K8s makes it happen using these core objects:

### 1. Pod
A Pod is the smallest deployable computing unit in Kubernetes. Unlike Docker, K8s doesn't run containers directly; it wraps them in a Pod. A Pod can contain one or multiple containers that share storage (Volumes) and the same IP address.

### 2. Deployment
You rarely create individual Pods. Instead, you create a Deployment. A Deployment instructs Kubernetes on how to create and update instances of your application. You can declare "I want 3 replicas of the frontend pod," and the Deployment controller will ensure exactly 3 are running at all times.

### 3. Service
Pods are mortal. They are born and they die, and their IP addresses change constantly. A **Service** provides a stable IP address and DNS name that load-balances traffic across a set of Pods. If the frontend needs to talk to the backend, it sends requests to the Backend Service, not the individual Backend Pods.

### 4. ConfigMaps and Secrets
Used to decouple configuration artifacts from image content to keep containerized applications portable. `ConfigMaps` store non-confidential data in key-value pairs, while `Secrets` store sensitive information like passwords, OAuth tokens, and SSH keys.
