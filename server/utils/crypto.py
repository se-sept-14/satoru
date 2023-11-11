import os
from dotenv import load_dotenv
from jose import JWTError, jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path)

CRYPTO = {
  "algorithm": os.getenv("CRYPTO_ALGORITHM"),
  "secret_key": os.getenv("CRYPTO_SECRET_KEY"),
  "access_token_expire_minutes": int(os.getenv("CRYPTO_ACCESS_TOKEN_EXPIRE_MINUTES"))
}

pwd_context = CryptContext(
  schemes = ["bcrypt"],
  deprecated = "auto"
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "login")

def hash_password(password: str):
  return pwd_context.hash(password)

def verify_password(incoming_password: str, original_password: str):
  return pwd_context.verify(incoming_password, original_password)

def create_access_token(data: dict, expires_delta: timedelta = None):
  to_encode = data.copy()
  
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.utcnow() + timedelta(minutes = CRYPTO['access_token_expire_minutes'])
  

  to_encode.update({
    "exp": expire
  })
  encoded_jwt = jwt.encode(to_encode, CRYPTO['secret_key'], algorithm = CRYPTO['algorithm'])

  return encoded_jwt

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
