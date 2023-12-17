#!/bin/bash

cd server
if [ ! -f .env ]; then
  echo "[ERROR] .env file not found"
  exit 1
fi

pm2 delete fastapi
pip install --no-cache-dir --upgrade -r requirements.txt
pm2 start "uvicorn main:app --host 0.0.0.0 --port 80" -n fastapi
cd -