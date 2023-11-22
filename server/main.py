import os

from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.utils import get_openapi

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

app = FastAPI(lifespan = lifecycle)
app.include_router(auth_router, prefix = "/api/auth")
app.include_router(tags_router, prefix = "/api/tags")
app.include_router(admin_router, prefix = "/api/admin")
app.include_router(course_router, prefix = "/api/course")
app.include_router(review_router, prefix = "/api/review")
app.include_router(profile_router, prefix = "/api/profile")

if os.path.exists("dist"):
  app.mount("/", StaticFiles(directory = "dist", html = True))

def custom_openapi():
  if app.openapi_schema:
    return app.openapi_schema

  openapi_schema = get_openapi(
    title = "SE-Sept-14 Recommender System API 🚀",
    version = "1.0.1",
    description = description,
    routes = app.routes,
  )
  openapi_schema["info"]["x-logo"] = {
    "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
  }
  app.openapi_schema = openapi_schema

  return app.openapi_schema

app.openapi = custom_openapi