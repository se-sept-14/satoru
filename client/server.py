from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import HTTPException

app = FastAPI(docs_url = None, redoc_url = None)

@app.exception_handler(404)
async def angular_router_handler(request: Request, exc: HTTPException):
  return HTMLResponse(open(Path(__file__).parent / 'dist/index.html').read())

app.mount('/', StaticFiles(directory = Path(__file__).parent / 'dist'), name = 'dist')