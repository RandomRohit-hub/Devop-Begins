# ⌨️ Essential Docker Commands Reference

A practical command reference for image lifecycle, container operations, networking, volumes, and troubleshooting.

---

## 🏗️ 1. Image Management

```bash
# Build an image from a Dockerfile in current directory
docker build -t vprofile-app:1.0 .

# List local images with sizes and image IDs
docker images

# Tag an image for a remote registry
docker tag vprofile-app:1.0 myregistry.azurecr.io/vprofile-app:1.0

# Push image to registry
docker push myregistry.azurecr.io/vprofile-app:1.0

# Pull an image from Docker Hub
docker pull sonarqube:lts
docker pull sonatype/nexus3

# Remove an unused local image
docker rmi vprofile-app:1.0
```

---

## 🏃 2. Container Execution & Lifecycle

```bash
# Run a container detached in background with port forwarding
docker run -d --name nexus-server -p 8081:8081 sonatype/nexus3
docker run -d --name sonar-server -p 9000:9000 sonarqube:lts

# List actively running containers
docker ps

# List all containers (including stopped/exited)
docker ps -a

# Stop, start, and restart a container
docker stop nexus-server
docker start nexus-server
docker restart nexus-server

# Force kill and remove a container
docker rm -f nexus-server

# Open an interactive bash shell inside a running container
docker exec -it nexus-server /bin/bash

# View live container log streams
docker logs -f sonar-server
```

---

## 💾 3. Volumes & System Cleanup

```bash
# Create a persistent named volume
docker volume create nexus-data

# Run container mounting persistent volume
docker run -d -p 8081:8081 -v nexus-data:/nexus-data sonatype/nexus3

# Clean up dangling images, stopped containers, and unused networks
docker system prune -a --volumes
```
