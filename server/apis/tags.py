from fastapi import APIRouter, Depends
from playhouse.shortcuts import model_to_dict

from models.db import Tags
from models.api import SearchQuery
from utils.crypto import decode_token

tags_router = APIRouter()


@tags_router.post("/search")
async def search_tags(search_query: SearchQuery, current_user: dict = Depends(decode_token)):
  results = []
  tags = Tags.select().where(Tags.name ** f"%{search_query.query}%")

  for tag in tags:
    results.append(model_to_dict(tag))
  
  return {
    "data": results
  }