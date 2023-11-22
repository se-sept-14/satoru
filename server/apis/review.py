import os
from utils.crypto import decode_token
from utils.parser import parse_review_inference
from models.api import ReviewsCreate, ReviewTagMapCreate
from models.db import Reviews, Tags, ReviewTagMap, DoesNotExist, db_connection

from detoxify import Detoxify
from fastapi import APIRouter, Depends, HTTPException

from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path)
required_env_vars = ["TOXICITY_THRESHOLD"]
for var in required_env_vars:
  if not os.getenv(var):
    raise EnvironmentError(f"Missing required environment variable: {var}")

review_router = APIRouter()


@review_router.post("/")
async def create_review(review: ReviewsCreate, current_user: dict = Depends(decode_token)):
  try:
    model = Detoxify("unbiased-small")
    flag = False

    toxicity = model.predict(review.content)
    inference = parse_review_inference(toxicity)
    for key in inference:
      if inference[key] >= float(os.getenv("TOXICITY_THRESHOLD")):
        flag = True

    review_instance = Reviews.create(
      content = review.content,
      course = review.course_id,
      ratings = review.ratings,
      user = current_user["id"],
      is_flagged = flag
    )

    return {
      "message": "Review created successfully ✔️",
      "data": {
        "id": review_instance.id,
        "profanity_check": inference
      }
    }
  except Exception as e:
    raise HTTPException(status_code = 500, detail = str(e))


@review_router.get("/all")
async def get_all_reviews(current_user: dict = Depends(decode_token)):
  try:
    reviews = Reviews.select().dicts()
    return {
      "reviews": list(reviews)
    }
  except Exception as e:
    raise HTTPException(status_code = 500, detail = str(e))


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
        if review_instance.user_id != current_user['id']:
            raise HTTPException(status_code=403, detail="Not authorized to edit this review")
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


@review_router.delete("/flagged/{review_id}")
async def delete_flagged_review(review_id: int, current_user: dict = Depends(decode_token)):
    try:
        print(type(current_user["is_admin"]))
        print(current_user["is_admin"] == 0)
        if current_user['is_admin'] == 0:
            raise HTTPException(status_code=403, detail="Not authorized to delete this review")
        
        with db_connection.atomic():
            review_instance = Reviews.get_by_id(review_id)
            if review_instance.is_flagged != 1:
                raise HTTPException(status_code=404, detail="Review not found or not flagged")
            db_connection.execute_sql(f"DELETE FROM reviews WHERE id={review_id}")

        return {"message": "Flagged review deleted successfully"}
    
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Review not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@review_router.post("/tag")
async def tag_review(review_tag: ReviewTagMapCreate, current_user: dict = Depends(decode_token)):
  try:
    is_admin = current_user["is_admin"]
    if not is_admin:
      return HTTPException(status_code = 403, detail = f"You are not an admin ⛔")
    
    review = Reviews.get(Reviews.id == review_tag.review_id)
    tag = Tags.get(Tags.id == review_tag.tag_id)

    if review and tag:
      review_tag_map = ReviewTagMap.create(review = review, tag = tag)
      review_tag_map.save()
    else:
      return HTTPException(
        status_code = 404,
        detail = f"Review ID {review_tag.review_id} or Tag ID {review_tag.tag_id} not found 🚫"
      )
    
    return {
      "message": "Review tagged successfully ✔️",
      "data": {
        "review_id": review_tag_map.review_id,
        "tag_id": review_tag_map.tag_id
      }
    }
  except DoesNotExist as dne:
    raise HTTPException(status_code = 404, detail = f"No such review or tag 🚫")
  except Exception as e:
    raise HTTPException(status_code = 500, detail = f"{str(e)}")