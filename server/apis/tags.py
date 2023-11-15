from fastapi import APIRouter, Depends
from utils.crypto import decode_token
from playhouse.shortcuts import model_to_dict

from models.api import (
  SearchQuery,
)
from models.db import (
  Tags
)

tags_router = APIRouter()

@tags_router.post("/search")
async def search_tags(search_query: SearchQuery, current_user: dict = Depends(decode_token)):
    results = []
    tags = Tags.select().where(
        Tags.name ** f"%{search_query.query}%"
    )
    for tag in tags:
        results.append(model_to_dict(tag))
    return {
        "data": results
    }


