from fastapi import APIRouter, HTTPException, Depends
from models.db import Users
from utils.crypto import decode_token

admin_router = APIRouter()

# Endpoint to fetch all students
@admin_router.get("/all_students")
async def get_all_students(current_user: dict = Depends(decode_token)):
    # Check if the current user is an admin
    is_admin = current_user["is_admin"]
    if not is_admin:
        raise HTTPException(status_code=403, detail="You are not an admin")

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
                # Add more fields as needed
            }
            for student in students
        ]

        return {"data": students_data}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Something went wrong: {e}")


# @admin_router.put("/alumni/{user_id}")
# async def make_alumni(user_id: int, current_user: dict = Depends(decode_token)):
#     is_admin = current_user["is_admin"]
#     if not is_admin:
#         raise HTTPException(status_code=403, detail="You are not an admin")
#     try:
#         student = Users.get_by_id(user_id)
#     except Users.DoesNotExist:
#         raise HTTPException(status_code=404, detail="User not found")
#     if student.is_admin == 1:
#         raise HTTPException(status_code=400, detail="Admin cannot be alumni")
#     # print(student)
#     student.is_alumni = 1 if student.is_alumni == 0 else 0
#     student.save()
#     return {"message": "Status of the student changed successfully"}

@admin_router.put("/alumni/{user_id}")
async def make_alumni(user_id: int, current_user: dict = Depends(decode_token)):
    is_admin = current_user["is_admin"]
    if not is_admin:
        raise HTTPException(status_code=403, detail="You are not an admin")
    try:
        student = Users.get_by_id(user_id)
    except Users.DoesNotExist:
        raise HTTPException(status_code=404, detail="User not found")
    if student.is_admin == 1:
        raise HTTPException(status_code=403, detail="Admin cannot be alumni")
    if student.is_alumni == 1:
        return {"message": "Student is already an alumni"}
    print(student)
    print(type(student.is_alumni))

    # student.is_alumni = 1 if student.is_alumni == 0 else 0
    student.is_alumni = 1 - student.is_alumni
    student.save()
    return {"message": "Status of the student changed successfully"}
