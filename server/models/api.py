from typing import Optional, List
from pydantic import BaseModel, EmailStr, constr

# Create user request schema
class UserRegistration(BaseModel):
  email: EmailStr
  username: constr(min_length = 4, max_length = 32)
  password: constr(min_length = 4, max_length = 32)

# Create user response schema
class UserResponse(BaseModel):
  id: int
  email: str
  is_admin: int
  username: str
  access_token: str
  token_type: str

# User's profile update request schema
class UserProfileUpdate(BaseModel):
  career_goals: Optional[str] = None
  hours_per_week: Optional[int] = None
  completion_deadline: Optional[str] = None
  learning_preferences: Optional[str] = None
  courses_willing_to_take: Optional[str] = None

# CREATE Course request schema
class CourseCreate(BaseModel):
  name: str
  code: str
  price: int
  credits: int
  description: str
  corerequisite: str
  prerequisites: str
  hours_per_week: str
  instructor_name: str
  instructor_picture: str
  tags: List[str]

# EDIT Course request schema
class CourseEdit(BaseModel):
  name: Optional[str] = None
  code: Optional[str] = None
  price: Optional[int] = None
  credits: Optional[int] = None
  description: Optional[str] = None
  corerequisite: Optional[str] = None
  prerequisites: Optional[str] = None
  hours_per_week: Optional[str] = None
  instructor_name: Optional[str] = None
  instructor_picture: Optional[str] = None

class ReviewsCreate(BaseModel):
  content: Optional[str]
  course_id: Optional[int]
  ratings: Optional[int]

class ReviewTagMapCreate(BaseModel):
  review_id: int
  tag_id: int

class SearchQuery(BaseModel):
  query: str