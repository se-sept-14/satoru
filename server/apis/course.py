from utils.crypto import decode_token
from utils.parser import parse_course
from models.api import SearchQuery, CourseEdit, CourseCreate
from models.db import (
  db_connection, fn,
  Courses, Tags, CourseTagMap
)

from playhouse.shortcuts import model_to_dict
from fastapi import (
  Depends, Path,
  APIRouter, HTTPException
)

course_router = APIRouter()


@course_router.get("/id/{id}")
async def get_course(id: int, current_user: dict = Depends(decode_token)):
  course = Courses.get_or_none(Courses.id == id)
  data = parse_course(course) if course is not None else {}

  if course:
    tags = Tags.select().join(CourseTagMap).where(CourseTagMap.course == course)
    data["tags"] = [
      tag.name for tag in tags
    ] if tags else []

  return {
    "data": data
  }


@course_router.get("/all")
async def get_all_courses(current_user: dict = Depends(decode_token)):
  data = []
  courses = Courses.select()

  for course in courses:
    course_data = parse_course(course) if course is not None else {}
    tags = Tags.select().join(CourseTagMap).where(CourseTagMap.course == course)
    course_data["tags"] = [
      tag.name for tag in tags
    ] if tags else []

    data.append(course_data)
  
  return {
    "data": data
  }


@course_router.post("/")
async def create_course(course_data: CourseCreate, current_user: dict = Depends(decode_token)):
  is_admin = current_user["is_admin"]
  if not is_admin:
    return HTTPException(status_code = 403, detail = f"You are not an admin ⛔")

  try:
    with db_connection.atomic():
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

      for tag_name in course_data.tags:
        tag, created = Tags.get_or_create(name = tag_name)
        CourseTagMap.create(course = new_course, tag = tag)
  except Exception as e:
    return HTTPException(status_code = 500, detail = f"{e}")

  return {
    "message": "Course added successfully ✔️",
    "data": {
      "id": new_course.id,
    }
  }


@course_router.delete("/{id}")
async def delete_course(id: int, current_user: dict = Depends(decode_token)):
  is_admin = current_user["is_admin"]
  if not is_admin:
    raise HTTPException(status_code = 403, detail = "You are not an admin ⛔")

  try:
    with db_connection.atomic():
      course = Courses.get_or_none(Courses.id == id)

      if course:
        course.delete_instance()
        return {
          "data": { "id": id },
          "message": f"Course with ID {id} deleted successfully 🗑️"
        }
      else:
        raise HTTPException(status_code = 404, detail = f"Course with ID {id} not found 🚫")
  except Exception as e:
    raise HTTPException(status_code = 500, detail = f"{e}")


@course_router.put("/{id}")
async def update_course(id: int, course_data: CourseEdit, current_user: dict = Depends(decode_token)):
  is_admin = current_user["is_admin"]
  if not is_admin:
    raise HTTPException(status_code = 403, detail = "You are not an admin ⛔")

  try:
    with db_connection.atomic():
      course = Courses.get_or_none(Courses.id == id)

      if course:
        for field, value in course_data.dict(exclude_unset = True).items():
          setattr(course, field, value)

        course.save()
        return {
          "data": { "id": id },
          "message": f"Course with ID {id} updated successfully ✔️"
        }
      else:
        raise HTTPException(status_code = 404, detail = f"Course with ID {id} not found 🚫")
  except Exception as e:
    raise HTTPException(status_code = 500, detail = f"{e}")


@course_router.post("/search")
async def search_course(search_query: SearchQuery, current_user: dict = Depends(decode_token)):
  results = []
  unique_course_ids = set() # Set to keep track of duplicate entries

  courses = Courses.select().where(
    Courses.name ** f"%{search_query.query}%" | Courses.description ** f"%{search_query.query}%"
  )

  tags = Tags.select().where(
    Tags.name ** f"%{search_query.query}%"
  )

  for course in courses:
    unique_course_ids.add(course.id)
    results.append(model_to_dict(course))

  for tag in tags:
    course_tag_maps = CourseTagMap.select().where(CourseTagMap.tag_id == tag.id).prefetch(Courses)
    for ctm in course_tag_maps:
      if ctm.course.id not in unique_course_ids:
        unique_course_ids.add(ctm.course.id)
        results.append(model_to_dict(ctm.course))

  return {
    "data": results
  }


@course_router.get("/recommend/{num_courses}")
async def recommend_course(
  num_courses: int = Path(..., title = "Number of courses", lt = 5),
  current_user: dict = Depends(decode_token)
):
  num_courses = max(1, min(4, num_courses))
  try:
    recommended_courses = Courses.select().order_by(fn.Rand()).limit(num_courses)
    data = []

    for course in recommended_courses:
      course_data = parse_course(course)
      data.append(course_data)

    return {
      "data": data
    }
  except Exception as e:
    raise HTTPException(status_code = 500, detail = f"{str(e)}")