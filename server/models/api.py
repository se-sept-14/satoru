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
  profile: Optional[str] = None

class LearningPreference(BaseModel):
  content: Optional[str]
  is_selected: Optional[bool]

class FavouriteSubjects(BaseModel):
  Q: Optional[str]
  A: Optional[List[conint(ge = 1)]]

class HouseDevoted(BaseModel):
  Q: Optional[str]
  A: Optional[conint(ge = 15, le = 45)]

class CoursesWillingToTake(BaseModel):
  value: Optional[int]
  is_selected: Optional[bool]

class IntendToComplete(BaseModel):
  value: Optional[str]
  date_time: Optional[str]
  is_selected: Optional[bool]
