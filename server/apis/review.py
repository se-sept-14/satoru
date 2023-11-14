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

@router.get("/reviews")
async def get_all_reviews():
    try:
        # Assuming Reviews is a SQLAlchemy model
        reviews = Reviews.select().dicts()
        return {"reviews": list(reviews)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/delete/{review_id}")
async def delete_review(review_id: int, current_user: dict = Depends(decode_token)):
    try:
        # Assuming Reviews is a SQLAlchemy model
        review = Reviews.get(id=review_id)

        # Check if the user trying to delete the review is the owner
        if review.user != current_user["id"]:
            raise HTTPException(status_code=403, detail="You don't have permission to delete this review")

        # Delete the review
        review.delete_instance()

        return {"message": "Review deleted successfully"}
    except Reviews.DoesNotExist:
        raise HTTPException(status_code=404, detail="Review not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))