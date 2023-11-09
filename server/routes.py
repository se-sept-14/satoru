from peewee import fn
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException, Depends

from utils.env import CRYPTO
from models.db import db_connection, Tags, Users
from utils.crypto import pwd_context, oauth2_scheme
from models.api import UserRegistration, UserResponse, UserLogin

router = APIRouter()

@router.get("/")
async def root():
  return {
    "swagger": "/docs",
    "redoc": "/redoc"
  }

@router.get("/tags")
async def fetch_tags():
  rows = Tags.select()
  return {
    'data': [{ 'id': row.id, 'name': row.name } for row in rows]
  }

@router.post("/register", response_model = UserResponse)
async def register_user(user_data: UserRegistration):
  with db_connection.transaction():
    existing_user = Users.select().where(Users.email == user_data.email or Users.username == user_data.username).first()

    if existing_user:
      raise HTTPException(status_code = 400, detail = "Email or Username already in use")
    
    # Check if there is an admin user in the db or not
    is_admin = Users.select().where(Users.is_admin == 1).count()
    user_data.is_admin = 1 if not is_admin else 0

    hashed_pwd = pwd_context.hash(user_data.password)

    new_user = Users.create(
      email = user_data.email,
      password = hashed_pwd,
      is_admin = user_data.is_admin,
      profile = "{}" if not user_data.profile else user_data.profile,
      username = user_data.username
    )
  
  return new_user

def create_access_token(data: dict, expires_delta: timedelta = None):
  to_encode = data.copy()
  
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.utcnow() + timedelta(minutes = 15)
  

  to_encode.update({
    "exp": expire
  })
  encoded_jwt = jwt.encode(to_encode, CRYPTO['secret_key'], algorithm = CRYPTO['algorithm'])

  return encoded_jwt

@router.post("/login")
async def login_user(credentials: UserLogin):
  user = Users.get_or_none(Users.email == credentials.email)

  if user is None or not pwd_context.verify(credentials.password, user.password):
    raise HTTPException(status_code = 401, detail = "Incorrect email or password")
  
  access_token = create_access_token(data = {
    "id": user.id,
    "email": user.email,
    "is_admin": user.is_admin
  })

  return {
    "access_token": access_token,
    "token_type": "bearer"
  }

def decode_token(token: str = Depends(oauth2_scheme)):
  try:
    payload = jwt.decode(token, CRYPTO['secret_key'], algorithms = CRYPTO['algorithm'])
    user_id = payload.get("id")
    is_admin = payload.get("is_admin")

    if user_id is None or is_admin is None:
      raise HTTPException(status_code = 403, details = "Invalid credentials")
    
    return {
      "id": user_id,
      "is_admin": is_admin
    }
  except JWTError:
    raise HTTPException(status_code = 403, detail = "Invalid credentials")

# Test protected route
@router.get("/protected")
async def protected_route(current_user: dict = Depends(decode_token)):
  user_id = current_user["id"]
  is_admin = current_user["is_admin"]

  return {
    "message": "This is a protected endpoint",
    "id": user_id,
    "is_admin": is_admin
  }
