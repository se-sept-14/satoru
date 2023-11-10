from typing import Optional, List, Union
from pydantic import BaseModel, conint, constr

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

# User's profile update request schema
class UserProfileUpdate(BaseModel):
  username: Optional[str] = None
  email: Optional[str] = None
  password: Optional[str] = None
  career_goals: Optional[str] = None
  hours_per_week: Optional[int] = None
  completion_deadline: Optional[str] = None
  learning_preferences: Optional[str] = None
  courses_willing_to_take: Optional[str] = None
