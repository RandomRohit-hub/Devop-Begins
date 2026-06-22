#!/bin/bash
echo "Installing Nexus via Docker..."
docker run -d -p 8081:8081 --name nexus sonatype/nexus3
