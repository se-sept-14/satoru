from playhouse.shortcuts import model_to_dict
from fastapi import APIRouter, Depends, HTTPException

from models.db import Tags
from models.api import SearchQuery
from utils.crypto import decode_token

tags_router = APIRouter(tags = ["Tags 🔖"])

@tags_router.post("/search", summary = "Search for tags 🔎")
async def search_tags(search_query: SearchQuery, current_user: dict = Depends(decode_token)):
  if not search_query.query:
    raise HTTPException(status_code = 400, detail = "Search query empty")

  results = []
  try:
    tags = Tags.select().where(Tags.name ** f"%{search_query.query}%")
    for tag in tags:
      results.append(model_to_dict(tag))
  except Exception as e:
    raise HTTPException(status_code = 500, detail = f"{str(e)}")
  
  return { "data": results }