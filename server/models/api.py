from typing import Optional
from pydantic import BaseModel

# User's registration request schema
class UserRegistration(BaseModel):
  email: str
  password: str
  is_admin: Optional[int] = None
  profile: Optional[str] = None
  username: str

# User's registration response schema
class UserResponse(BaseModel):
  id: int
  email: str
  is_admin: int
  profile: str
  username: str
  
# User's login request schema
class UserLogin(BaseModel):
  email: str
  password: str
