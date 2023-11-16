from models.db import Users
from utils.crypto import decode_token

from fastapi import APIRouter, HTTPException, Depends

admin_router = APIRouter()


@admin_router.get("/all-students")
async def get_all_students(current_user: dict = Depends(decode_token)):
  # Check if the current user is an admin
  is_admin = current_user["is_admin"]
  if not is_admin:
    raise HTTPException(status_code = 403, detail = "You are not an admin ⛔")

  try:
    # Fetch all users who are not admins
    students = Users.select().where(Users.is_admin == 0)

    # Construct a list of student data
    students_data = [
      {
        "id": student.id,
        "username": student.username,
        "email": student.email,
        "created_at": student.created_at,
      } for student in students
    ]

    return { "data": students_data }

  except Exception as e:
    raise HTTPException(status_code = 500, detail = f"{e}")


@admin_router.get("/alumni/{user_id}")
async def make_alumni(user_id: int, current_user: dict = Depends(decode_token)):
  is_admin = current_user["is_admin"]
  if not is_admin:
    raise HTTPException(status_code = 403, detail = "You are not an admin ⛔")
  
  try:
    student = Users.get_or_none(Users.id == user_id)
    if not student:
      return HTTPException(status_code = 404, detail = f"User with ID {user_id} does not exist ❌")
    
    if student.is_alumni:
      return HTTPException(status_code = 419, detail = f"Student is already an alumni 🎓")
    
    query = Users.update(is_alumni = True).where(Users.id == user_id)
    query.execute()
  except Exception as e:
    raise HTTPException(status_code = 500, detail = f"{str(e)}")

  return {
    "data": { "id": user_id },
    "message": "Student is now an alumni 🎓"
  }