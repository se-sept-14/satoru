#!/bin/bash

# Check if .env file exists
if [ ! -f .env ]; then
  echo "Error: .env file not found. Please create the .env file before running this script."
  exit 1
fi

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

# Build vite app
cd ../client        # Move to vite directory
npm install         # Install the dependencies
npm run build       # Build the vue app
mv -f dist ../server   # Move it to fastapi server
cd -                # Go back to /server directory

# Deploy the current version
echo "Building and deploying containers ..."
docker compose up -d
