from playhouse.shortcuts import model_to_dict
from fastapi import APIRouter, Depends, HTTPException

from models.db import Users, StudentProfile, Students, StudentAboutMe, Levels, DoesNotExist
from utils.crypto import decode_token
from models.api import StudentProfileUpdate,StudentUpdate,StudentAboutMeUpdate,LevelUpdate

profile_router = APIRouter(tags = ["Profile 👤"])


@profile_router.get("/", summary = "Fetch profile of a user 🗣️")
async def profile(current_user: dict = Depends(decode_token)):
  try:
    user_profile = StudentProfile.get(StudentProfile.user == current_user["id"])
    about_me = StudentAboutMe.get(StudentAboutMe.id == current_user["id"])
    student_info = Students.get(Students.user == current_user["id"])

  except DoesNotExist:
    raise HTTPException(status_code = 404, detail = "User profile not found 🚫")

  return {
    "data": {
      "id": user_profile.user_id,
      "career_goals": user_profile.career_goals,
      "hours_per_week": user_profile.hours_per_week,
      "completion_deadline": user_profile.completion_deadline,
      "learning_preferences": user_profile.learning_preferences,
      "courses_willing_to_take": user_profile.courses_willing_to_take,

      "address": about_me.address,
      "contact_no": about_me.contact_no,
      "is_alumni": about_me.is_alumni,
      "level": about_me.level,
      "term": about_me.term,

      "category": student_info.category,
      "dob": student_info.dob,
      "email": student_info.email,
      "gender":student_info.gender,
      "name": student_info.name,
      "profile_picture_url": student_info.profile_picture_url,
      "pwd": student_info.pwd,
      "roll_no": student_info.roll_no,
      "student_email": student_info.student_email,
      
    }
  }



@profile_router.post("/", summary = "Create / Update profile of a user 👥")
async def profile(
  student_update: StudentUpdate,
  student_profile_update: StudentProfileUpdate,
  student_about_me_update: StudentAboutMeUpdate,
  current_user: dict = Depends(decode_token)
):
  user_id = current_user['id']

  # Either get the existing student, or create a new one
  student, created = Students.get_or_create(user = user_id)
  student.category = student_update.category if student_update.category else student.category
  student.dob = student_update.dob if student_update.dob else student.dob
  student.gender = student_update.gender if student_update.gender else student.gender
  student.name = student_update.name if student_update.name else student.name
  student.profile_picture_url = student_update.profile_picture_url if student_update.profile_picture_url else student.profile_picture_url
  student.pwd = student_update.pwd if student_update.pwd else student.pwd
  student.roll_no = student_update.roll_no if student_update.roll_no else student.roll_no
  student.student_email = f'{student_update.roll_no}@student.iitm' if student_update.roll_no else student.student_email
  student.save()

  # Either get the existing profile, or create a new one
  student_profile, created = StudentProfile.get_or_create(user = user_id)

  # If the profile exists, update the fields with non-None values from the update
  student_profile.career_goals = student_profile_update.career_goals if student_profile_update.career_goals else student_profile.career_goals
  student_profile.completion_deadline = student_profile_update.completion_deadline if student_profile_update.completion_deadline else student_profile.completion_deadline
  student_profile.courses_willing_to_take = student_profile_update.courses_willing_to_take if student_profile_update.courses_willing_to_take else student_profile.courses_willing_to_take
  student_profile.hours_per_week = student_profile_update.hours_per_week if student_profile_update.hours_per_week != 0 else student_profile.hours_per_week
  student_profile.learning_preferences = student_profile_update.learning_preferences if student_profile_update.learning_preferences else student_profile.learning_preferences
  student_profile.save()

  return {
    'data': model_to_dict(student_profile, exclude = [Users.password])
  }
    # try:
    #     user=current_user["id"]

    #     # Update or create student entry
    #     student,created = Students.get_or_create(
    #       category=student_update.category,
    #       dob=student_update.dob,
    #       email=student_update.email,
    #       gender=student_update.gender,
    #       name=student_update.name,
    #       profile_picture_url=student_update.profile_picture_url,
    #       pwd=student_update.pwd,
    #       roll_no=student_update.roll_no,
    #       student_email=student_update.student_email,
    #       user=user,
    #     )

    #     # Update or create student_about_me entry
    #     student_about_me,created = StudentAboutMe.get_or_create(
    #       address=student_about_me_update.address,
    #       contact_no=student_about_me_update.contact_no,
    #       is_alumni=student_about_me_update.is_alumni,
    #       level=level.id if level else None,  # use level.id instead of level
    #       student=student.id if student else None,  # use student.id instead of student
    #       term=student_about_me_update.term,
    #     )

    #     # Update or create student_profile entry
    #     student_profile = StudentProfile.get_or_create(
    #         career_goals=student_profile_update.career_goals,
    #         completion_deadline=student_profile_update.completion_deadline,
    #         courses_willing_to_take=student_profile_update.courses_willing_to_take,
    #         hours_per_week=student_profile_update.hours_per_week,
    #         learning_preferences=student_profile_update.learning_preferences,
    #         user=user,
    #     )
    # except IntegrityError:
    #     raise HTTPException(status_code=400, detail="Profile creation/update failed due to integrity error ⚠️")

    # return {
    #     "message": "Profile created or updated successfully ✔️"
    # }
