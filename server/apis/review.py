import os
from utils.crypto import decode_token
from models.api import ReviewsCreate, ReviewTagMapCreate
from models.db import Users, Reviews, Tags, Courses, ReviewTagMap, DoesNotExist, db_connection

from playhouse.shortcuts import model_to_dict
from fastapi import APIRouter, Depends, HTTPException

review_router = APIRouter(tags = ["Review ✨"])


@review_router.post("/", summary = "Create a review ⭐")
async def create_review(review: ReviewsCreate, current_user: dict = Depends(decode_token)):
  if review.content is None or len(review.content) == 0:
    raise HTTPException(status_code = 401, detail = "Missing review content 🌚")

  try:
    flag = False
    
    course = Courses.get_or_none(Courses.id == review.course_id)
    print(course)
    if course is None:
      print(f"No such course ${review.course_id}")
      raise HTTPException(status_code=404, detail = f"No such course with id {review.course_id}")

    review_instance = Reviews.create(
      content = review.content,
      course = course,
      ratings = review.ratings,
      user = current_user["id"],
      is_flagged = flag
    )

    return {
      "message": "Review created successfully ✔️",
      "data": {
        "id": review_instance.id
      }
    }
  except HTTPException as http_exc:
    print(f"HTTPException caught: {http_exc}")
    raise  # Reraise the exception for FastAPI to handle

  except Exception as e:
      print(f"Unexpected exception: {e}")
      raise HTTPException(status_code=500, detail=str(e))


@review_router.get("/all", summary = "Fetch a list of all review 🚀")
async def get_all_reviews(current_user: dict = Depends(decode_token)):
  try:
    reviews = Reviews.select().dicts()
    return {
      "reviews": list(reviews)
    }
  except Exception as e:
    raise HTTPException(status_code = 500, detail = str(e))


@review_router.get("/course-id/{id}", summary = "Fetch the reviews for a particular course 🧾")
async def get_review_by_course_id(id: int, current_user: dict = Depends(decode_token)):
  course = Courses.get_or_none(Courses.id == id)
  if course is None:
    raise HTTPException(status_code = 404, detail = f"No such course with id {id} 🙈")
  
  data = []
  reviews = Reviews.select().where(Reviews.course_id == course.id)

  if reviews is None:
    return { "data": data }
  else:
    for review in reviews:
      data.append(model_to_dict(review, exclude = [Reviews.user]))
  
  return { "data": data }


@review_router.post("/flag/{review_id}", summary = "Flag a review 🏳️")
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


@review_router.put("/{review_id}", summary = "Edit a review 📝")
async def edit_review(review_id: int, review: ReviewsCreate, current_user: dict = Depends(decode_token)):
  try:
    review_instance = Reviews.get_by_id(review_id)
    if review_instance.user_id != current_user['id']:
      raise HTTPException(status_code = 403, detail = "Not authorized to edit this review ❌")
    review_instance.content = review.content
    review_instance.ratings = review.ratings
    review_instance.course_id = review.course_id
    review_instance.save()
    return {"message": "Review updated successfully"}
  except DoesNotExist:
    raise HTTPException(status_code = 404, detail = "Review not found")
  except Exception as e:
    raise HTTPException(status_code = 500, detail = str(e))


@review_router.delete("/{review_id}", summary = "Delete a review 🗑️")
async def delete_review(review_id: int, current_user: dict = Depends(decode_token)):
  with db_connection.atomic():
    review_instance = Reviews.get_by_id(review_id)
    print(review_instance.user_id != current_user['id'])

    if review_instance.user_id != current_user['id']:
        raise HTTPException(status_code = 403, detail = "Not authorized to delete this review 👤")
    
    db_connection.execute_sql(f"DELETE FROM reviews WHERE id={review_id}")
    
  return {"message": "Review deleted successfully"}


@review_router.delete("/flagged/{review_id}", summary = "Delete a flagged review 🚮")
async def delete_flagged_review(review_id: int, current_user: dict = Depends(decode_token)):
  try:
    if current_user['is_admin'] == 0:
      raise HTTPException(status_code=403, detail="Not authorized to delete this review")
      
    with db_connection.atomic():
      review_instance = Reviews.get_by_id(review_id)
      if review_instance.is_flagged != 1:
        raise HTTPException(status_code = 404, detail = "Review not found or not flagged ❌")
      db_connection.execute_sql(f"DELETE FROM reviews WHERE id={review_id}")

    return {"message": "Flagged review deleted successfully"}
  except DoesNotExist:
    raise HTTPException(status_code = 404, detail = "Review not found ❌")
  except Exception as e:
    raise HTTPException(status_code = 500, detail = str(e))


@review_router.post("/tag", summary = "Add tag to a review 🏷️")
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
