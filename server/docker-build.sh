#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo "Image built at $0 <timestamp>"
  exit 1
fi

timestamp="$1"
docker build -t "satoru-api:$timestamp" .