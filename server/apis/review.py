from fastapi import APIRouter, Depends, HTTPException

from utils.crypto import decode_token
from models.api import ReviewsCreate, ReviewTagMapCreate
from models.db import Reviews, Tags, ReviewTagMap, DoesNotExist

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

@review_router.post("/tag")
async def tag_review(review_tag: ReviewTagMapCreate, current_user: dict = Depends(decode_token)):
  try:
    is_admin = current_user["is_admin"]
    if not is_admin:
      return HTTPException(status_code = 403, detail = f"You are not an admin")
    
    review = Reviews.get(Reviews.id == review_tag.review_id)
    tag = Tags.get(Tags.id == review_tag.tag_id)

    if review and tag:
      review_tag_map = ReviewTagMap.create(review = review, tag = tag)
      review_tag_map.save()
    else:
      return HTTPException(status_code = 404, detail = f"Review ID {review_tag.review_id} or Tag ID {review_tag.tag_id} not found")
    
    return {
      "message": "Review tagged successfully",
      "data": {
        "review_id": review_tag_map.review_id,
        "tag_id": review_tag_map.tag_id
      }
    }
  except DoesNotExist as dne:
    raise HTTPException(status_code = 404, detail = f"No such review or tag")
  except Exception as e:
    raise HTTPException(status_code = 500, detail = f"{str(e)}")
