# Docker Cheatsheet

A quick reference for the most common Docker commands used in day-to-day development.

## Images
*An image is a read-only template with instructions to create a container.*

- `docker pull <image>`: Download an image from Docker Hub (e.g., `docker pull ubuntu`).
- `docker build -t <name>:<tag> .`: Build an image from a Dockerfile in the current directory.
- `docker images`: List all local images.
- `docker rmi <image_id>`: Delete an image.

## Containers
*A container is a running instance of an image.*

- `docker run -d -p 8080:80 <image>`: Run a container in detached mode (`-d`), mapping port 8080 on the host to port 80 in the container.
- `docker ps`: List all running containers.
- `docker ps -a`: List all containers (running and stopped).
- `docker stop <container_id>`: Gracefully stop a container.
- `docker kill <container_id>`: Force kill a container.
- `docker rm <container_id>`: Delete a stopped container.

## Interacting with Containers
- `docker logs <container_id>`: View the output logs of a container.
- `docker logs -f <container_id>`: Follow the logs in real-time.
- `docker exec -it <container_id> /bin/bash` (or `sh`): Open an interactive shell inside a running container.

## Cleanup
- `docker system prune`: Remove all stopped containers, dangling images, and unused networks. (Use with caution!).
