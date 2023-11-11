from peewee import IntegrityError
from fastapi import APIRouter, Depends, HTTPException, Form
from fastapi.security import OAuth2PasswordBearer
from models.db import Users, UserProfile
from models.api import UserProfileUpdate
from utils.crypto import hash_password, decode_token
from peewee import DoesNotExist

profile_router = APIRouter()

# OAuth2PasswordBearer for token-based authentication

@profile_router.get("/")
async def profile(current_user: dict = Depends(decode_token)):
    try:
        # Retrieve the user profile based on the user_id from the token
        user_profile = UserProfile.get(UserProfile.user == current_user["id"])

    except DoesNotExist:
        raise HTTPException(status_code=404, detail="User profile not found")

    return {
        "user_id": user_profile.user_id,
        "hours_per_week": user_profile.hours_per_week,
        "learning_preferences": user_profile.learning_preferences,
        "courses_willing_to_take": user_profile.courses_willing_to_take,
        "career_goals": user_profile.career_goals,
        "completion_deadline": user_profile.completion_deadline,
    }
@profile_router.post("/")
async def profile(
    profile_update: UserProfileUpdate,
    current_user: dict = Depends(decode_token)
):
    print(f"Decoded Token: {current_user}")
    print(f"Profile Update: {profile_update}")

    try:
        # Try to get the existing user profile, or create a new one if it doesn't exist
        user_profile, created = UserProfile.get_or_create(
            user=current_user["id"],
            defaults={
                'hours_per_week': profile_update.hours_per_week,
                'learning_preferences': profile_update.learning_preferences,
                'courses_willing_to_take': profile_update.courses_willing_to_take,
                'career_goals': profile_update.career_goals,
                'completion_deadline': profile_update.completion_deadline,
            }
        )

        if not created:
            # If the profile already exists, update the values
            user_profile.hours_per_week = profile_update.hours_per_week
            user_profile.learning_preferences = profile_update.learning_preferences
            user_profile.courses_willing_to_take = profile_update.courses_willing_to_take
            user_profile.career_goals = profile_update.career_goals
            user_profile.completion_deadline = profile_update.completion_deadline
            user_profile.save()

    except IntegrityError:
        raise HTTPException(status_code=400, detail="User profile creation failed due to integrity error")

    return {"message": "User profile created or updated successfully"}


