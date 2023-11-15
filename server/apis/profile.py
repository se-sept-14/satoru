from peewee import IntegrityError, DoesNotExist
from fastapi import APIRouter, Depends, HTTPException

from models.db import UserProfile
from utils.crypto import decode_token
from models.api import UserProfileUpdate

profile_router = APIRouter()


@profile_router.get("/")
async def profile(current_user: dict = Depends(decode_token)):
  try:
    user_profile = UserProfile.get(UserProfile.user == current_user["id"])

  except DoesNotExist:
    raise HTTPException(status_code = 404, detail = "User profile not found 🚫")

  return {
    "id": user_profile.user_id,
    "career_goals": user_profile.career_goals,
    "hours_per_week": user_profile.hours_per_week,
    "completion_deadline": user_profile.completion_deadline,
    "learning_preferences": user_profile.learning_preferences,
    "courses_willing_to_take": user_profile.courses_willing_to_take
  }


@profile_router.post("/")
async def profile(profile_update: UserProfileUpdate, current_user: dict = Depends(decode_token)):
  try:
    user_profile, created = UserProfile.get_or_create(
      user = current_user["id"],
      defaults = {
        'hours_per_week': profile_update.hours_per_week,
        'learning_preferences': profile_update.learning_preferences,
        'courses_willing_to_take': profile_update.courses_willing_to_take,
        'career_goals': profile_update.career_goals,
        'completion_deadline': profile_update.completion_deadline,
      }
    )

    if not created:
      user_profile.hours_per_week = profile_update.hours_per_week
      user_profile.learning_preferences = profile_update.learning_preferences
      user_profile.courses_willing_to_take = profile_update.courses_willing_to_take
      user_profile.career_goals = profile_update.career_goals
      user_profile.completion_deadline = profile_update.completion_deadline

      user_profile.save()
  except IntegrityError:
    raise HTTPException(status_code = 400, detail = "User profile creation failed due to integrity error ⚠️")

  return {
    "message": "User profile created or updated successfully ✔️"
  }