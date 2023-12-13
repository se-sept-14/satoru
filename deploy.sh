#!/bin/bash

# Check if .env file exists
if [ ! -f ./server/.env ]; then
  echo "Error: .env file not found. Please create the .env file inside `server` directory before running this script."
  exit 1
fi
