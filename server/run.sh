#!/bin/bash

# Check if .env file exists
if [ ! -f .env ]; then
  echo "Error: .env file not found. Please create the .env file before running this script.\n'cp .env.example. env' and change the values in '.env'"
  exit 1
fi

uvicorn main:app --reload