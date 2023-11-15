from fastapi import APIRouter, Depends, HTTPException, Form
from fastapi.security import OAuth2PasswordBearer
from models.db import Users, Reviews, db_connection
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
        reviews = Reviews.select().dicts()
        return {"reviews": list(reviews)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


    
@review_router.post("/flag/{review_id}")
async def flag_review(review_id: int, current_user: dict = Depends(decode_token)):
    try:
        review = Reviews.get_by_id(review_id)
        # Toggle the value of is_flagged
        review.is_flagged = 1 if review.is_flagged == 0 else 0
        review.save()
        return {"message": "Review flag toggled successfully"}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Review not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@review_router.put("/{review_id}")
async def edit_review(review_id: int, review: ReviewsCreate, current_user: dict = Depends(decode_token)):
    try:
        review_instance = Reviews.get_by_id(review_id)
        review_instance.content = review.content
        review_instance.ratings = review.ratings
        review_instance.save()
        return {"message": "Review updated successfully"}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Review not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@review_router.delete("/{review_id}")
async def delete_review(review_id: int, current_user: dict = Depends(decode_token)):
    try:
        with db_connection.atomic():
            review_instance = Reviews.get_by_id(review_id)
            if review_instance.user_id != current_user['id']:
                raise HTTPException(status_code=403, detail="Not authorized to delete this review")
            db_connection.execute_sql(f"DELETE FROM reviews WHERE id={review_id}")
        return {"message": "Review deleted successfully"}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Review not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

