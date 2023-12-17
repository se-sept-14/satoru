#!/bin/bash

# Stop existing (and running continers)
echo "Stopping existing containers ..."
docker compose down

# Check if .env file exists in 'server' directory
if [ ! -f ./server/.env ]; then
  echo "Error: .env file not found. Please create the .env file inside \`server\` directory before running this script. Check the README"
  exit 1
fi

# Check if .env file exists in 'client' directory
if [ ! -f ./client/.env ]; then
  echo "Error: .env file not found. Please create the .env file inside \`client\` directory before running this script. Check the README"
  exit 1
fi

# Run the docker compose service
echo "Deploying ..."
docker compose up --build -d