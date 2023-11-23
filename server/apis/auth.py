from models.db import db_connection, Users, DoesNotExist
from models.api import UserRegistration, UserResponse, UserLogin
from utils.crypto import hash_password, verify_password, create_access_token, decode_token, JWTError

from typing_extensions import Annotated
from fastapi import Form, APIRouter, HTTPException, Depends

auth_router = APIRouter(tags = ["Auth 🔐"])


@auth_router.post("/register", response_model = UserResponse, summary = "Register a new user 👤")
async def register_user(user_data: UserRegistration) -> UserResponse:
  with db_connection.transaction():
    existing_user = Users.get_or_none((Users.email == user_data.email) | (Users.username == user_data.username))

    if existing_user:
      raise HTTPException(status_code = 400, detail = "Email or Username already in use ⚠️")
    
    # Check if there is an admin user in the db or not
    is_admin = 1 if not Users.select().where(Users.is_admin == 1).count() else 0

    hashed_pwd = hash_password(user_data.password)

    new_user = Users.create(
      email = user_data.email,
      password = hashed_pwd,
      is_admin = is_admin,
      username = user_data.username
    )

    # Log in the user after successful registration
    access_token = create_access_token(
      data = {
        "id": new_user.id,
        "email": new_user.email,
        "is_admin": new_user.is_admin,
      }
    )

  return {
    "id": new_user.id,
    "email": new_user.email,
    "is_admin": new_user.is_admin,
    "username": new_user.username,
    "access_token": access_token,
    "token_type": "Bearer",
  }


@auth_router.post("/login", response_model = UserLogin, summary = "Login a user 🔑")
async def login_user(username: Annotated[str, Form()], password: Annotated[str, Form()]):
  if not username or not password:
    raise HTTPException(status_code = 400, detail = "Username and Password are required ⚠️")

  user = Users.get_or_none(Users.username == username)
  if user is None:
    raise HTTPException(status_code = 404, detail = "User not found 👀")
  
  if not verify_password(password, user.password):
    raise HTTPException(status_code = 401, detail = "Incorrect email and password 🚫")

  access_token = create_access_token(data = {
    "id": user.id,
    "email": user.email,
    "is_admin": user.is_admin
  })

  return {
    "access_token": access_token,
    "token_type": "Bearer"
  }


@auth_router.post("/change-password", summary = "Change password of current user 🔓")
async def change_password(
  current_password: str = Form(..., description = "Current Password"),
  new_password: str = Form(..., description = "New Password"),
  current_user: dict = Depends(decode_token)
):
  credentials_exception = HTTPException(status_code = 401, detail = "Failed to validate credentials")

  try:
    user_id: int = current_user["id"]

    if user_id is None:
      raise credentials_exception
  except HTTPException as exc:
    raise exc
  except JWTError:
    raise credentials_exception
  
  user = Users.get_or_none(Users.id == user_id)
  if user is None:
    raise HTTPException(status_code = 401, detail = "User not found or invalid credentials")
  
  if not verify_password(current_password, user.password):
    raise HTTPException(status_code = 401, detail = "Incorrect current password 🚫")
  
  if verify_password(current_password, user.password):
    raise HTTPException(status_code = 400, detail = "New password cannot be the same as old password")
  
  new_hashed_password = hash_password(new_password)

  with db_connection.transaction():
    user.password = new_hashed_password
    user.save()
  
  return { "message": "Password changed successfully" }