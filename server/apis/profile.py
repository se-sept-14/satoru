from fastapi import APIRouter, HTTPException

from utils.crypto import hash_password
from models.api import UserProfileUpdate
from models.db import Users, UserProfile, FavoriteCoursesOrder

profile_router = APIRouter()

@profile_router.get("/{id}")
async def get_profile(id: int):
  user = Users.get_or_none(Users.id == id)
  if user is None:
    raise HTTPException(status_code = 404, detail = f"User with ID {id} not found")
  
  profile_data = {
    "id": user.id,
    "is_admin": user.is_admin,
    "username": user.username,
    "email": user.email,
    "created_at": user.created_at,
  }

  user_profile = UserProfile.get_or_none(UserProfile.user == user)
  if user_profile:
    profile_data.update({
      "career_goals": user_profile.career_goals,
      "hours_per_week": user_profile.hours_per_week,
      "completion_deadline": user_profile.completion_deadline,
      "learning_preferences": user_profile.learning_preferences,
      "courses_willing_to_take": user_profile.courses_willing_to_take,
    })

    # Fetch favourite courses (if they exist)
    favorite_courses = FavoriteCoursesOrder.select().where(
      FavoriteCoursesOrder.user_profile == user_profile
    )

    profile_data["favorite_courses"] = [
      {
        "course_id": order.course.id,
        "order_index": order.order_index
      } for order in favorite_courses
    ]
  
  return {
    "data": profile_data
  }

@profile_router.post("/{id}")
async def update_profile(id: int, user_data: UserProfileUpdate):
  user = Users.get_or_none(Users.id == id)
  if not user:
    return HTTPException(status_code = 404, detail = f"User with ID {id} not found")
  
  if user_data.username:
    user.username = user_data.username
  if user_data.email:
    user.email = user_data.email
  if user_data.password:
    user.password = hash_password(user_data.password)
  user.save()

  # Create or update UserProfile
  user_profile, created = UserProfile.get_or_create(user = user)

  # Update UserProfile fields
  if user_data.career_goals is not None:
    user_profile.career_goals = user_data.career_goals
  
  if user_data.hours_per_week is not None:
    user_profile.hours_per_week = user_data.hours_per_week
  if user_data.completion_deadline is not None:
    user_profile.completion_deadline = user_data.completion_deadline

  if user_data.learning_preferences is not None:
    user_profile.learning_preferences = user_data.learning_preferences

  if user_data.courses_willing_to_take is not None:
    user_profile.courses_willing_to_take = user_data.courses_willing_to_take

  user_profile.save()

  return {
    "message": "Profile updated successfully"
  }
