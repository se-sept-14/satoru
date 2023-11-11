from pydantic import BaseModel

class ReviewSchema(BaseModel):
  content: str
