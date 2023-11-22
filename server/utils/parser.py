from typing import Any, Dict
from models.db import Courses

def parse_course(course: Courses) -> Dict[str, Any]:
  if course is None:
    raise ValueError("Input 'course' cannot be None")

  data = {}
  
  data['id'] = course.id
  data['name'] = course.name
  data['code'] = course.code
  data['price'] = course.price
  data['credits'] = course.credits
  data['description'] = course.description
  data['corerequisite'] = course.corerequisite
  data['prerequisites'] = course.prerequisites
  data['hours_per_week'] = course.hours_per_week
  data['instructor_name'] = course.instructor_name
  data['instructor_picture'] = course.instructor_picture
  data['created_at'] = str(course.created_at)

  return data

def parse_review_inference(inference):
  data = {}

  data['toxicity'] = float(inference['toxicity'])
  data['severe_toxicity'] = float(inference['severe_toxicity'])
  data['obscene'] = float(inference['obscene'])
  data['threat'] = float(inference['threat'])
  data['insult'] = float(inference['insult'])
  data['identity_attack'] = float(inference['identity_attack'])

  return data