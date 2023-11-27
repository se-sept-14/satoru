from playhouse.shortcuts import model_to_dict
from fastapi import APIRouter, Depends, HTTPException

from utils.crypto import decode_token
from models.api import (
  StudentUpdate,
  StudentAboutMeUpdate,
  StudentProfileUpdate
)
from models.db import (
  DoesNotExist,
  Users, Students, Levels,
  StudentProfile, StudentAboutMe
)

profile_router = APIRouter(tags = ["Profile 👤"])


@profile_router.get("/", summary="Fetch profile of a user 🗣️")
async def profile(current_user: dict = Depends(decode_token)):
  user_id = current_user['id']
  if user_id is None:
    raise HTTPException(status_code = 401, detail = 'Not user found ❌')

  try:
    user_profile = StudentProfile.get(StudentProfile.user == user_id)       # Fetching user profile details
    student_about_me = StudentAboutMe.get(StudentAboutMe.user == user_id)   # Fetching student about me details
    student_info = Students.get(Students.user == user_id)                   # Fetching student information
  except DoesNotExist:
    raise HTTPException(status_code = 404, detail = "User profile not found 🚫")

  student_info_dict = model_to_dict(student_info, exclude = [Users.password])
  user_profile_dict = model_to_dict(user_profile, exclude = [StudentProfile.user])
  student_about_me_dict = model_to_dict(student_about_me, exclude = [StudentAboutMe.user])

  return {
    'data': {
      **user_profile_dict,
      **student_info_dict,
      **student_about_me_dict,
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

  if student_about_me_update.level != 0:
    level = Levels.get_or_none(Levels.id == student_about_me_update.level)
    if level is None:
      raise HTTPException(status_code = 404, detail = f'No level with id: {student_about_me_update.level}')

  student_about_me = StudentAboutMe.get_or_none(StudentAboutMe.user == user_id)

  if student_about_me is None:
    # If no existing record, create a new one
    student_about_me = StudentAboutMe.create(
      user = user_id,
      address = student_about_me_update.address,
      contact_no = student_about_me_update.contact_no,
      level = level.id if level else None,
      term = student_about_me_update.term,
    )
  else:
    # If record exists, update the fields with non-None values from the update
    student_about_me.address = student_about_me_update.address if student_about_me_update.address else student_about_me.address
    student_about_me.contact_no = student_about_me_update.contact_no if student_about_me_update.contact_no else student_about_me.contact_no
    student_about_me.level = level.id if level else None
    student_about_me.term = student_about_me_update.term if student_about_me_update.term else student_about_me.term
    student_about_me.save()

  data = {
    'student': model_to_dict(student, exclude = [Users.password]),
    'profile': model_to_dict(student_profile, exclude = [StudentProfile.user]),
    'about_me': model_to_dict(student_about_me, exclude = [StudentAboutMe.user])
  }

  return {
    'data': data
  }
