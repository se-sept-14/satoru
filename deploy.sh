#!/bin/bash

# Checkout the `main` branch
git checkout main

# Pull the changes from main
git pull

# Run the deploy.sh script inside `server` directory
cd server/
sh deploy.sh