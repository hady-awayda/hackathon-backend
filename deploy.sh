#!/bin/bash

# Create network if it doesn't exist
docker network create hackathon-network || true

# Stop existing containers and remove images
# docker compose -f docker-compose.app.yml down --rmi local

# Prune unused Docker resources
docker system prune -f

# Check if MySQL container exists
if [ ! "$(docker ps -q -f name=hackathon-mysql-dev)" ]; then
    if [ "$(docker ps -aq -f status=exited -f name=hackathon-mysql-dev)" ]; then
        # cleanup
        docker rm hackathon-mysql-dev
    fi
    # run your container
    docker compose -f docker-compose.db.yml up -d
fi

# Always run the app container
docker compose -f docker-compose.app.yml up -d --build

# Cleanup images
docker image prune -f