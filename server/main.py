from fastapi import FastAPI
from contextlib import asynccontextmanager

from models.db import db_connection
from apis.auth import auth_router
from apis.profile import profile_router
from apis.course import course_router
from apis.review import review_router

# Lifecycle context
@asynccontextmanager
async def lifecycle(app: FastAPI):
  db_connection.connect()
  yield
  db_connection.close()

app = FastAPI(lifespan = lifecycle)
app.include_router(auth_router, prefix = "/api/auth")
app.include_router(profile_router, prefix = "/api/profile")
app.include_router(course_router, prefix = "/api/course")
app.include_router(review_router, prefix = "/api/review")