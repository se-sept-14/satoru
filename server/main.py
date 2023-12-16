from pathlib import Path
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import HTTPException
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware

from apis.auth import auth_router
from apis.tags import tags_router
from models.db import db_connection
from apis.admin import admin_router
from apis.course import course_router
from apis.review import review_router
from apis.profile import profile_router

from utils.migrate import run_migrations
from utils.openapi import description, version, summary, title
from utils.cors import allowed_origins, allowed_credentials, allowed_methods, allowed_headers

# Lifecycle context (keep the DB connection alive till the FastAPI server is running)
@asynccontextmanager
async def lifecycle(app: FastAPI):
  try:
    db_connection.connect()
    run_migrations()
    yield
  finally:
    db_connection.close()

app = FastAPI(lifespan = lifecycle, redoc_url = None, summary = summary, version = version)
app.include_router(auth_router, prefix = "/api/auth")         # Auth endpoints
app.include_router(admin_router, prefix = "/api/admin")       # Admin endpoints
app.include_router(course_router, prefix = "/api/course")     # Course management endpoints
app.include_router(profile_router, prefix = "/api/profile")   # Profile management endpoints
app.include_router(review_router, prefix = "/api/review")     # Review management endpoints
app.include_router(tags_router, prefix = "/api/tags")         # Tag management endpoints

# Add a middleware to allow certain origins only (and credentials, methods and headers)
app.add_middleware(
  CORSMiddleware,
  allow_origins = allowed_origins,
  allow_methods = allowed_methods,
  allow_headers = allowed_headers,
  allow_credentials = allowed_credentials,
)

# Define a custom OpenAPI document
def custom_openapi():
  if app.openapi_schema:
    return app.openapi_schema

  openapi_schema = get_openapi(title = title, version = version, description = description, routes = app.routes)
  app.openapi_schema = openapi_schema
  return app.openapi_schema

app.openapi = custom_openapi