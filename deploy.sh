#!/bin/bash

# Navigate to the directory wherever this script is located
cd "$(dirname "$0")"

# Checkout the `main` branch
git checkout main

# Pull the changes from main
git pull origin main

# Remove old vite build files
echo "Delete the existing vue build ..."
rm -fr ./client/dist/

# Build a fresh copy of vite for production
echo "Building production build of vue ..."
cd ./client/
npm install
npm run build
cd -

docker compose down -v
docker compose up --build -d