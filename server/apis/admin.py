from models.db import Users
from utils.crypto import decode_token
from models.api import StudentData, AllStudentData, AlumniResponse

from fastapi import APIRouter, HTTPException, Depends

admin_router = APIRouter(tags = ["Admin 🤵"])


@admin_router.get("/all-students", summary = "Fetch a list of all students 🧑‍🤝‍🧑", response_model = AllStudentData)
async def get_all_students(current_user: dict = Depends(decode_token)):
  is_admin = current_user["is_admin"] # Check if the current user is an admin
  if not is_admin:
    raise HTTPException(status_code = 403, detail = "You are not an admin ⛔")

  try:
    # Fetch all users who are not admin
    students = Users.select().where(Users.is_admin == 0)

    # Construct a list of student data
    students_data = [
      {
        "id": student.id,
        "email": student.email,
        "username": student.username,
        "is_alumni": student.is_alumni,
        "created_at": str(student.created_at)
      } for student in students
    ]
    return { "data": students_data }
  except Exception as e:
    raise HTTPException(status_code = 500, detail = f"{e}")


@admin_router.get("/alumni/{user_id}", summary = "Make a student alumni 🎓", response_model = AlumniResponse)
async def make_alumni(user_id: int, current_user: dict = Depends(decode_token)):
  is_admin = current_user["is_admin"]
  if not is_admin:
    raise HTTPException(status_code = 403, detail = "You are not an admin ⛔")
  
  try:
    student = Users.get_or_none(Users.id == user_id)
    if not student:
      raise HTTPException(status_code = 404, detail = f"User with ID {user_id} does not exist ❌")
    
    if student.is_alumni:
      raise HTTPException(status_code = 419, detail = f"Student is already an alumni 🎓")
    
    query = Users.update(is_alumni = True).where(Users.id == user_id)
    query.execute()
  except HTTPException as e:
    raise e
  except Exception as e:
    raise HTTPException(status_code = 500, detail = f"{str(e)}")

  return { "data": { "id": user_id }, "message": "Student is now an alumni 🎓" }
