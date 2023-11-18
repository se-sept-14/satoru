#!/bin/bash

# Stop running containers
echo "Stopping running containers ..."
docker compose down

# Deploy the current version
echo "Building and deploying containers ..."
docker compose up -d