from utils.crypto import decode_token
from models.api import SearchQuery, CourseEdit, CourseCreate
from models.db import (
  Courses, Tags, CourseTagMap, StudentCourseMap,
  db_connection, fn, DoesNotExist
)

from playhouse.shortcuts import model_to_dict
from fastapi import (
  Depends, Path,
  APIRouter, HTTPException
)

course_router = APIRouter(tags = ["Course 📚"])


@course_router.get("/id/{id}", summary = "Fetch a course by ID 🪪")
async def get_course(id: int, current_user: dict = Depends(decode_token)):
  course = Courses.get_or_none(Courses.id == id)
  if course is None:
    raise HTTPException(status_code = 404, detail = f"No course with id {id} 🧊")

  data = model_to_dict(course) if course is not None else {}

  if course:
    tags = Tags.select().join(CourseTagMap).where(CourseTagMap.course == course)
    data["tags"] = [
      tag.name for tag in tags
    ] if tags else []

  return {
    "data": data
  }


@course_router.get("/all", summary = "Fetch all the courses 📚")
async def get_all_courses(current_user: dict = Depends(decode_token)):
  data = []
  courses = Courses.select()

  for course in courses:
    course_data = model_to_dict(course) if course is not None else {}
    tags = Tags.select().join(CourseTagMap).where(CourseTagMap.course == course)
    course_data["tags"] = [
      tag.name for tag in tags
    ] if tags else []

    data.append(course_data)
  
  return {
    "data": data
  }


@course_router.post("/", summary = "Add a new course 📖")
async def create_course(course_data: CourseCreate, current_user: dict = Depends(decode_token)):
  is_admin = current_user["is_admin"]
  if not is_admin:
    raise HTTPException(status_code = 403, detail = f"You are not an admin ⛔")

  try:
    with db_connection.atomic():
      new_course = Courses.create(
        name = course_data.name,
        code = course_data.code,
        price = course_data.price,
        credits = course_data.credits,
        description = course_data.description,
        corequisite = course_data.corequisite,
        prerequisites = course_data.prerequisites,
        hours_per_week = course_data.hours_per_week,
        instructor_name = course_data.instructor_name,
        instructor_picture = course_data.instructor_picture
      )

      for tag_name in course_data.tags:
        tag, created = Tags.get_or_create(name = tag_name.strip())
        CourseTagMap.create(course = new_course, tag = tag)
  except Exception as e:
    raise HTTPException(status_code = 500, detail = f"{e}")

  return {
    "message": "Course added successfully ✔️",
    "data": model_to_dict(new_course)
  }


@course_router.delete("/{id}", summary = "Delete a course 🗑️")
async def delete_course(id: int, current_user: dict = Depends(decode_token)):
  is_admin = current_user["is_admin"]
  if not is_admin:
    raise HTTPException(status_code = 403, detail = "You are not an admin ⛔")

  with db_connection.atomic():
    try:
      course = Courses.get(Courses.id == id)
      course_dict = model_to_dict(course)
      course.delete_instance()

      return {
        "data": course_dict,
        "message": f"Course with ID {id} deleted successfully 🗑️"
      }
    except DoesNotExist:
      raise HTTPException(status_code = 404, detail = f"Course with ID {id} not found 🚫")
    except Exception as e:
      raise HTTPException(status_code = 500, detail = str(e))


@course_router.put("/{id}", summary = "Modify an existing course 📝")
async def update_course(id: int, course_data: CourseEdit, current_user: dict = Depends(decode_token)):
  is_admin = current_user["is_admin"]
  if not is_admin:
    raise HTTPException(status_code = 403, detail = "You are not an admin ⛔")

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


@course_router.post("/search", summary = "Search for a course 🔍")
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

  return { "data": results }


@course_router.get("/recommend/{num_courses}", summary = "Get recommended courses ⚙️")
async def recommend_course(num_courses: int = Path(..., gt = 0, le = 4), current_user: dict = Depends(decode_token)):
  try:
    recommended_courses = Courses.select().order_by(fn.Rand()).limit(num_courses)
    data = []

    for course in recommended_courses:
      course_data = model_to_dict(course)
      data.append(course_data)
    return {
      "data": data
    }
  
  except Exception as e:
    raise HTTPException(status_code = 500, detail = f"{str(e)}")


@course_router.post('/student-course-map/{course_id}')
async def map_student_course(course_id, current_user: dict = Depends(decode_token)):
    try:
        course = Courses.get_by_id(course_id)
        student_course_map = StudentCourseMap.create(
            course=course,
            user=current_user["id"]
        )
        return {"message": "Course mapped successfully"}

    except Courses.DoesNotExist:
        raise HTTPException(status_code=404, detail="Course not found")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@course_router.get('/student-course')
async def get_student_courses(current_user: dict = Depends(decode_token)):
    try:
        course_ids = StudentCourseMap.select(StudentCourseMap.course_id).where(StudentCourseMap.user_id == current_user["id"])
        courses = Courses.select().where(Courses.id.in_(course_ids))
        data = []

        for course in courses:
            course_data = model_to_dict(course) if course is not None else {}
            tags = Tags.select().join(CourseTagMap).where(CourseTagMap.course == course)
            course_data["tags"] = [
              tag.name for tag in tags
            ] if tags else []
            data.append(course_data)

        return {
            "data": data
          }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@course_router.get('/courses-by-student/{student_id}')
async def cousese_by_student(student_id, current_user: dict = Depends(decode_token), ):
  try:
    if current_user['is_admin'] == 0:
      raise HTTPException(status_code=403, detail="Not an admin")
    
    course_ids = StudentCourseMap.select(StudentCourseMap.course_id).where(StudentCourseMap.user_id == student_id)
    courses = Courses.select().where(Courses.id.in_(course_ids))
    data = []

    for course in courses:
            course_data = model_to_dict(course) if course is not None else {}
            tags = Tags.select().join(CourseTagMap).where(CourseTagMap.course == course)
            course_data["tags"] = [
              tag.name for tag in tags
            ] if tags else []
            data.append(course_data)

    return {
        "data": data
      }
  
  except Exception as e:
      raise HTTPException(status_code=500, detail=str(e))