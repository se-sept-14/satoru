from fastapi import APIRouter, Depends, HTTPException, Form
from fastapi.security import OAuth2PasswordBearer
from models.db import Users, Reviews
from models.api import ReviewsCreate
from utils.crypto import hash_password, decode_token
from peewee import DoesNotExist

review_router = APIRouter()

@review_router.post("/")
async def create_review(review: ReviewsCreate, current_user: dict = Depends(decode_token)):
    try:
        # Create a review instance using the Pydantic model
        review_instance = Reviews.create(
            content=review.content,
            course=review.course_id,
            ratings=review.ratings,
            user=current_user["id"]
        )
        return {"message": "Review created successfully", "review_id": review_instance.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@review_router.get("/all")
async def get_all_reviews():
    try:
        # Assuming Reviews is a SQLAlchemy model
        reviews = Reviews.select().dicts()
        return {"reviews": list(reviews)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


