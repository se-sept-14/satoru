from fastapi import FastAPI
from contextlib import asynccontextmanager

from routes import router
from models.db import db_connection

# Lifecycle context
@asynccontextmanager
async def lifecycle(app: FastAPI):
  db_connection.connect()
  yield
  db_connection.close()

app = FastAPI(lifespan = lifecycle)
app.include_router(router, prefix = "/api")
