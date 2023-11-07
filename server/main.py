from models.db import connection, Tags

from fastapi import FastAPI
from contextlib import asynccontextmanager

# Lifecycle context
@asynccontextmanager
async def lifecycle(app: FastAPI):
  connection.connect()
  yield
  connection.close()

app = FastAPI()

@app.get("/")
async def root():
  return {
    "swagger": "/docs",
    "redoc": "/redoc"
  }

@app.get("/api/tags")
async def fetch_tags():
  rows = Tags.select()
  print(rows)

  return {
    'data': [row.name for row in rows]
  }
