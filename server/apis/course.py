from utils.parser import parse_course
from utils.crypto import decode_token
from models.api import (
  SearchQuery,
  CourseEdit, CourseCreate
)
from models.db import (
  db_connection,
  Courses, Tags, CourseTagMap
)

from fastapi import (
  Depends,
  APIRouter,
  HTTPException
)
from playhouse.shortcuts import model_to_dict

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
@course_router.delete("/{id}")
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

@course_router.put("/{id}")
async def update_course(id: int, course_data: CourseEdit, current_user: dict = Depends(decode_token)):
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
                # Update course attributes based on the provided data
                for field, value in course_data.dict(exclude_unset=True).items():
                    setattr(course, field, value)

                # Save the changes to the database
                course.save()

                return {"message": f"Course with ID {id} updated successfully", "updated_course_id": id}
            else:
                raise HTTPException(status_code=404, detail=f"Course with ID {id} not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Something went wrong: {e}")

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
