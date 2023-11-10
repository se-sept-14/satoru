from models.api import CourseCreate
from utils.parser import parse_course
from utils.crypto import decode_token
from models.db import (
  db_connection,
  Courses, Tags, CourseTagMap
)

from fastapi import (
  Depends,
  APIRouter,
  HTTPException
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

@course_router.get("/")
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
    return HTTPException(status_code = 403, detail = f"You are not an admin")
  else:
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
          # Check if the tag already exists
          tag, created = Tags.get_or_create(name = tag_name)

          CourseTagMap.create(course = new_course, tag = tag)
    except Exception as e:
      return HTTPException(status_code = 500, detail = f"Something went wrong: {e}")

  return {
    "message": "Course added successfully",
    "data": {
      "id": new_course.id,
    }
  }
@course_router.delete("/delete/{id}")
async def delete_course(id: int, current_user: dict = Depends(decode_token)):
    # Check if the user is an admin
    is_admin = current_user["is_admin"]
    if not is_admin:
        raise HTTPException(status_code=403, detail="You are not an admin")

    try:
        with db_connection.atomic():
            # Retrieve the course by ID
            course = Courses.get_or_none(Courses.id == id)

            # If the course exists, delete it
            if course:
                course.delete_instance()
                return {"message": f"Course with ID {id} deleted successfully", "id": id}
            else:
                raise HTTPException(status_code=404, detail=f"Course with ID {id} not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Something went wrong: {e}")

@course_router.put("/edit/{id}")
async def edit_course(id: int, course_data: CourseCreate, current_user: dict = Depends(decode_token)):
    # Check if the user is an admin
    is_admin = current_user["is_admin"]
    if not is_admin:
        raise HTTPException(status_code=403, detail="You are not an admin")

    try:
        with db_connection.atomic():
            # Retrieve the course by ID
            course = Courses.get_or_none(Courses.id == id)

            # If the course exists, update its attributes
            if course:
                course.name = course_data.name
                course.code = course_data.code
                course.price = course_data.price
                course.credits = course_data.credits
                course.description = course_data.description
                course.corerequisite = course_data.corerequisite
                course.prerequisites = course_data.prerequisites
                course.hours_per_week = course_data.hours_per_week
                course.instructor_name = course_data.instructor_name
                course.instructor_picture = course_data.instructor_picture

                # Save the changes to the database
                course.save()

                # The course instance has now been updated in the database

                return {"message": f"Course with ID {id} updated successfully", "id": id}
            else:
                raise HTTPException(status_code=404, detail=f"Course with ID {id} not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Something went wrong: {e}")






