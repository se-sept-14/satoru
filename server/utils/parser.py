from models.db import Courses

def parse_course(course: Courses):
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
  data['created_at'] = course.created_at

  return data
