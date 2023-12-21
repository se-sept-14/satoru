#!/bin/bash

# Navigate to the directory wherever this script is located
cd "$(dirname "$0")"

# Checkout the `main` branch
git checkout main

# Pull the changes from main
git pull

# Run the deploy.sh script inside `server` directory
cd server/
sh deploy.sh
