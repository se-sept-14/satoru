#!/bin/bash

# Stop existing (and running continers)
echo "Stopping existing containers ..."
docker compose down

# Check if .env file exists
if [ ! -f ./server/.env ]; then
  echo "Error: .env file not found. Please create the .env file inside `server` directory before running this script."
  exit 1
fi

# Run the docker compose service
echo "Deploying ..."
docker compose up --build -d