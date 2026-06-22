# Nexus Installation Guide

1. Install via Docker: `docker run -d -p 8081:8081 --name nexus sonatype/nexus3`
2. Access at `http://localhost:8081`.
3. Get admin password from the container: `docker exec -it nexus cat /nexus-data/admin.password`.
