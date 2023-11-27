from playhouse.shortcuts import model_to_dict
from fastapi import APIRouter, Depends, HTTPException

from models.db import Tags
from models.api import SearchQuery
from utils.crypto import decode_token

tags_router = APIRouter(tags = ["Tags 🔖"])

@tags_router.post("/search", summary = "Search for tags 🔎")
async def search_tags(search_query: SearchQuery, current_user: dict = Depends(decode_token)):
  if not search_query.query:
    raise HTTPException(status_code = 400, detail = "Search query empty 🗅")

  results = []
  try:
    query = search_query.query.strip()
    tags = Tags.select().where(Tags.name ** f"%{query}%")
    for tag in tags:
      results.append(model_to_dict(tag))
  except Exception as e:
    raise HTTPException(status_code = 500, detail = f"{str(e)}")
  
  return { "data": results }


@tags_router.post("/create", summary = "Create a new tag 📑")
async def create_tag(name: str, current_user: dict = Depends(decode_token)):
  is_admin = current_user["is_admin"]
  if not is_admin:
    raise HTTPException(status_code = 403, detail = "You are not an admin ❌")
  
  try:
    new_tag, created = Tags.get_or_create(name = name.strip())
    if created:
      return { "message": f"{new_tag.name} tag created successfully ✅", "data": model_to_dict(new_tag) }
    else:
      return { "message": f"{name.strip()} tag already exists 😵‍💫" }
  except Exception as e:
    raise HTTPException(status_code = 500, detail = str(e))
