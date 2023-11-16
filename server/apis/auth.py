from models.db import db_connection, Users
from models.api import UserRegistration, UserResponse
from utils.crypto import hash_password, verify_password, create_access_token

from typing_extensions import Annotated
from fastapi import Form, APIRouter, HTTPException

auth_router = APIRouter()


@auth_router.post("/register", response_model = UserResponse)
async def register_user(user_data: UserRegistration):
  with db_connection.transaction():
    existing_user = Users.select().where(Users.email == user_data.email or Users.username == user_data.username).first()

    if existing_user:
      raise HTTPException(status_code = 400, detail = "Email or Username already in use ⚠️")
    
    # Check if there is an admin user in the db or not
    is_admin = Users.select().where(Users.is_admin == 1).count()
    user_data.is_admin = 1 if not is_admin else 0

    hashed_pwd = hash_password(user_data.password)

    new_user = Users.create(
      email = user_data.email,
      password = hashed_pwd,
      is_admin = user_data.is_admin,
      username = user_data.username
    )
  
  return new_user


@auth_router.post("/login")
async def login_user(username: Annotated[str, Form()], password: Annotated[str, Form()]):
  try:
    user = Users.get_or_none(Users.username == username)

    if user is None or not verify_password(password, user.password):
      raise HTTPException(status_code = 401, detail = "Incorrect email or password 🚫")
    
    access_token = create_access_token(data = {
      "id": user.id,
      "email": user.email,
      "is_admin": user.is_admin
    })

    return {
      "access_token": access_token,
      "token_type": "Bearer"
    }
  except Exception as e:
    raise HTTPException(status_code = 500, detail = f"{str(e)}")