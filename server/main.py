from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from apis.auth import auth_router
from models.db import db_connection
from apis.admin import admin_router
from apis.course import course_router
from apis.review import review_router
from apis.profile import profile_router
from apis.tags import tags_router

# Lifecycle context
@asynccontextmanager
async def lifecycle(app: FastAPI):
  db_connection.connect()
  yield
  db_connection.close()

# Allowed origins
origins = ["*"]

app = FastAPI(lifespan = lifecycle)
app.include_router(auth_router, prefix = "/api/auth")
app.include_router(course_router, prefix = "/api/course")
app.include_router(review_router, prefix = "/api/review")
app.include_router(profile_router, prefix = "/api/profile")
app.include_router(admin_router, prefix = "/api/admin")
app.include_router(tags_router, prefix = "/api/tags")

app.mount("/", StaticFiles(directory = "dist", html = True))

app.add_middleware(
  CORSMiddleware,
  allow_origins = origins,
  allow_credentials = True,
  allow_methods = "*",
  allow_headers = "*"
)