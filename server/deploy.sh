#!/bin/bash

# Generate a timestamp (YYYYMMDDHHMMSS format)
timestamp=$(date +"%Y%m%d%H%M%S")

# Build the docker image
docker build -t "satoru-api_$timestamp" .

# Run the docker container
docker run -d --name satoru-api_$timestamp -p 5000:5000 "satoru-api_$timestamp"