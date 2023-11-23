#!/bin/bash

# Stop running containers
echo "Stopping running containers ..."
docker compose down

# Delete old images
echo "Delete old docker image ..."
docker image rm server-api:latest

# Checkout the `main` branch
git checkout main

# Pull the changes from main
git pull

# Remove existing dist folder inside server
rm -rf dist

# Build vite application
echo "Building vite for prod ..."
cd ../client
npm install
npm run build
mv -f dist ../server
cd ../server

# Deploy the current version
echo "Building and deploying containers ..."
docker compose up -d
