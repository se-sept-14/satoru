from fastapi import APIRouter, HTTPException

from models.db import Users
from utils.crypto import hash_password
from models.api import UserProfileUpdate

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

@profile_router.post("/{id}")
async def update_profile(id: int, user_data: UserProfileUpdate):
  user = Users.get_or_none(Users.id == id)
  if not user:
    raise HTTPException(status_code = 404, detail = 'User not found')
  
  if user_data.username:
    user.username = user_data.username
  
  if user_data.email:
    user.email = user_data.email
  
  if user_data.password:
    user.password = hash_password(user_data.password)
    

  return {}
