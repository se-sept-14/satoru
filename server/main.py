import os

from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware

from apis.auth import auth_router
from apis.tags import tags_router
from models.db import db_connection
from apis.admin import admin_router
from apis.course import course_router
from apis.review import review_router
from apis.profile import profile_router

from utils.openapi import description

# Lifecycle context
@asynccontextmanager
async def lifecycle(app: FastAPI):
  try:
    db_connection.connect()
    yield
  finally:
    db_connection.close()

app = FastAPI(lifespan = lifecycle, redoc_url = None) # Disabled /redoc
app.include_router(admin_router, prefix = "/api/admin")
app.include_router(auth_router, prefix = "/api/auth")
app.include_router(course_router, prefix = "/api/course")
app.include_router(profile_router, prefix = "/api/profile")
app.include_router(review_router, prefix = "/api/review")
app.include_router(tags_router, prefix = "/api/tags")

app.add_middleware(
  CORSMiddleware,
  allow_origins = ["https://pickmycourse.vercel.app", "http://localhost:8000", "http://localhost:5000", "https://api.pickmycourse.online"],
  allow_credentials = "*",
  allow_methods = ["*"],
  allow_headers = ["*"]
)

def custom_openapi():
  if app.openapi_schema:
    return app.openapi_schema

  openapi_schema = get_openapi(
    title = "SE-Sept-14 Recommender System API 🚀", version = "1.2.1",
    description = description, routes = app.routes,
  )
  app.openapi_schema = openapi_schema
  return app.openapi_schema

app.openapi = custom_openapi