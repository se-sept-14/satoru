from fastapi import APIRouter

from models.db import db_connection, Users

profile_router = APIRouter()

@profile_router.get("/{id}")
async def get_profile(id: int):
  data = {}
  profile = Users.get_or_none(Users.id == id)
  data['id'] = profile.id
  data['is_admin'] = profile.is_admin
  data['username'] = profile.username
  data['email'] = profile.email
  data['created_at'] = profile.created_at

  return {
    "data": data
  }
