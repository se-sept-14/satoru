from detoxify import Detoxify
from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager

from interfaces.reviews import ReviewSchema
from utils.parser import parse_review_inference

model: Detoxify = None

# Lifecycle context
@asynccontextmanager
async def lifecycle(app: FastAPI):
  global model
  try:
    model = Detoxify('original')
    yield
  finally:
    del model

app = FastAPI(lifespan = lifecycle)

@app.post("/inference/review")
async def classify_review(review: ReviewSchema):
  review_text = review.content
  
  if len(review_text) == 0:
    return HTTPException(status_code = 404, detail = f"Empty review text")
  
  results = model.predict(review_text)
  data = parse_review_inference(results)

  return {
    "data": data
  }
