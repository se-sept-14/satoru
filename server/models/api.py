from datetime import date
from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr, constr

"""Pydantic models for admin endpoints"""
# /all-students Student data object
class StudentData(BaseModel):
  id: int
  email: str
  username: str
  is_alumni: bool
  created_at: str

# List of Student data object
class AllStudentData(BaseModel):
  data: List[StudentData]

# /alumni/{id} User id object
class UserId(BaseModel):
  id: int

# /alumni/{id} response object
class AlumniResponse(BaseModel):
  data: UserId
  message: str

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

# Login user schema
class UserLogin(BaseModel):
  access_token: str
  token_type: str

class StudentUpdate(BaseModel):
  category: Optional[str] = None
  dob: Optional[date] = None
  gender: Optional[str] = None
  name: Optional[str] = None
  profile_picture_url: Optional[str] = None
  pwd: Optional[int] = None
  roll_no: Optional[str] = None

class StudentAboutMeUpdate(BaseModel):
  address: Optional[str] = None
  contact_no: Optional[str] = None
  level: Optional[int] = None
  term: Optional[str] = None

# User's profile update request schema
class StudentProfileUpdate(BaseModel):
  career_goals: Optional[str] = None
  completion_deadline: Optional[str] = None
  courses_willing_to_take: Optional[str] = None
  hours_per_week: Optional[int] = None
  learning_preferences: Optional[str] = None

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
  content: str
  course_id: int
  ratings: int = Field(..., gt = 0, le = 1) # Rating should be in the range 1-10

class ReviewTagMapCreate(BaseModel):
  review_id: int
  tag_id: int

class SearchQuery(BaseModel):
  query: str