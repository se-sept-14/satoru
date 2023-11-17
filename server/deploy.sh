#!/bin/bash

# Stop running containers
echo "Stopping running containers ..."
docker compose down

# Delete old images
echo "Delete old docker image ..."
docker image rm server-api:latest

# Build vite application
echo "Building vite for prod ..."
cd ../client
npm install
npm run build
mv dist ../server
cd ../server

# Deploy the current version
echo "Building and deploying containers ..."
docker compose up -d