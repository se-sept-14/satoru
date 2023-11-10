#!/bin/bash

# Generate a timestamp (YYYYMMDDHHMMSS format)
timestamp=$(date +"%Y%m%d%H%M%S")

# Build the docker image
sh docker-build.sh "$timestamp"

docker run -d --name satoru-api -p 5000:5000 "satoru-api:$timestamp"