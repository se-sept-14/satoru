#!/bin/bash
echo "Building docker image ..."
docker compose build

echo "Running the docker containers ..."
docker compose up -d