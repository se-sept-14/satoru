from utils.crypto import decode_token
from models.db import Users, Students, StudentAboutMe

from playhouse.shortcuts import model_to_dict
from fastapi import APIRouter, HTTPException, Depends

admin_router = APIRouter(tags = ["Admin 🤵"])


@admin_router.get("/all-students", summary = "Fetch a list of all students 🧑‍🤝‍🧑")
async def get_all_students(current_user: dict = Depends(decode_token)):
  is_admin = current_user["is_admin"] # Check if the current user is an admin
  if not is_admin:
    raise HTTPException(status_code = 403, detail = "You are not an admin ⛔")

  try:
    # Fetch all users who are not admin
    users = Users.select().where(Users.is_admin == 0)

    students = []
    for user in users:
      user_dict = model_to_dict(user)
      student = Students.get_or_none(Students.user_id == user.id)
      student_dict = model_to_dict(student, exclude = [Users.password]) if student is not None else {}
      students.append({ **student_dict })

    return { "data": students }
  except Exception as e:
    raise HTTPException(status_code = 500, detail = f"{e}")


@admin_router.get("/alumni/{user_id}", summary = "Make a student alumni 🎓")
async def make_alumni(user_id: int, current_user: dict = Depends(decode_token)):
  is_admin = current_user["is_admin"]
  if not is_admin:
    raise HTTPException(status_code = 403, detail = "You are not an admin ⛔")
  
  try:
    user = Users.get_or_none(Users.id == user_id)
    if not user:
      raise HTTPException(status_code = 404, detail = f"User with ID {user_id} does not exist ❌")
    
    student = StudentAboutMe.get_or_none(StudentAboutMe.user_id == user.id)
    if student is None:
      raise HTTPException(status_code = 404, detail = "Student has not completed the profile 🧑‍🎓")
    
    query = StudentAboutMe.update(is_alumni = True).where(StudentAboutMe.user_id == user.id)
    query.execute()
  except HTTPException as e:
    raise e
  except Exception as e:
    raise HTTPException(status_code = 500, detail = f"{str(e)}")

  return { "data": { "id": user_id }, "message": "Student is now an alumni 🎓" }
