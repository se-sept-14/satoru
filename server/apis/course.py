from models.db import Courses
from models.api import CourseCreate
from utils.parser import parse_course
from utils.crypto import decode_token

from fastapi import (
  Depends,
  APIRouter,
  HTTPException
)

course_router = APIRouter()

@course_router.get("/id/{id}")
async def get_course(id: int, current_user: dict = Depends(decode_token)):
  course = Courses.get_or_none(Courses.id == id)
  data = parse_course(course) if course is not None else {};

  return {
    "data": data
  }

@course_router.get("/")
async def get_all_courses(current_user: dict = Depends(decode_token)):
  data = []
  courses = Courses.select()
  for course in courses:
    data.append(parse_course(course) if course is not None else {})
  
  return {
    "data": data
  }

@course_router.post("/")
async def create_course(course_data: CourseCreate, current_user: dict = Depends(decode_token)):
  is_admin = current_user["is_admin"]

  if not is_admin:
    return HTTPException(status_code = 403, detail = f"You are not an admin")
  else:
    try:
      new_course = Courses.create(
      name = course_data.name,
      code = course_data.code,
      price = course_data.price,
      credits = course_data.credits,
      description = course_data.description,
      corerequisite = course_data.corerequisite,
      prerequisites = course_data.prerequisites,
      hours_per_week = course_data.hours_per_week,
      instructor_name = course_data.instructor_name,
      instructor_picture = course_data.instructor_picture
    )
    except Exception as e:
      return HTTPException(status_code = 500, detail = f"Something went wrong: {e}")

  return {
    "message": "Course added successfully",
    "data": {
      "id": new_course.id,
    }
  }
