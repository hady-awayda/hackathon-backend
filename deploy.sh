#!/bin/bash

# Stop existing containers and remove images
echo "Stopping running containers"
docker compose -f docker-compose.app.yml down

# Prune unused Docker resources
echo "Pruning unused Docker resources"
docker system prune -f

# Create network if it doesn't exist
echo "Creating network if it doesn't exist"
docker network create hackathon-network 2>/dev/null || true

# Check if MySQL container exists
if [ ! "$(docker ps -q -f name=hackathon-mysql-dev)" ]; then
    if [ "$(docker ps -aq -f status=exited -f name=hackathon-mysql-dev)" ]; then
        # cleanup
        docker rm hackathon-mysql-dev
    fi
    # run your container
    echo "Starting MySQL container"
    docker compose -f docker-compose.db.yml up -d
else
    echo "MySQL container is already running"
fi

# Always run the app container
echo "Rebuilding and restarting app container"
docker compose -f docker-compose.app.yml up -d --build

# Cleanup images
docker image prune -f

echo "Deployment completed"