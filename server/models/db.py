from peewee import *
from datetime import datetime
from utils.env import MARIADB

db_connection = MySQLDatabase(
  MARIADB['db_name'],
  user = MARIADB['user'],
  password = MARIADB['password'],
  host = MARIADB['host'],
  port = MARIADB['port']
)

class Courses(Model):
  id = AutoField(primary_key = True)
  name = CharField()
  code = TextField()
  price = IntegerField()
  credits = IntegerField()
  description = TextField()
  corerequisite = TextField()
  prerequisites = TextField()
  hours_per_week = TextField()
  instructor_name = TextField()
  instructor_picture = CharField()
  created_at = DateTimeField(constraints = [SQL("DEFAULT current_timestamp()")])

  class Meta:
    database = db_connection
    table_name = 'courses'

class Tags(Model):
  id = AutoField(primary_key = True)
  name = CharField(unique = True)
  created_at = TimestampField(default = datetime.now)

  class Meta:
    database = db_connection
    table_name = 'tags'

class CourseTagMap(Model):
  id = AutoField(primary_key = True)
  course = ForeignKeyField(
    column_name = 'course_id',
    field = 'id',
    model = Courses
  )
  tag = ForeignKeyField(
    column_name = 'tag_id',
    field = 'id',
    model = Tags
  )

  class Meta:
    database = db_connection
    table_name = 'course_tag_map'

class Users(Model):
  id = AutoField(primary_key = True)
  password = CharField()
  is_admin = IntegerField()
  email = CharField(unique = True)
  username = CharField(unique = True)
  created_at = TimestampField(default = datetime.now)

  class Meta:
    database = db_connection
    table_name = 'users'

class UserProfile(Model):
  id = AutoField(primary_key = True)
  career_goals = TextField(null = True)
  hours_per_week = IntegerField(null = True)
  completion_deadline = TextField(null = True)
  learning_preferences = TextField(null = True)
  courses_willing_to_take = TextField(null = True)
  user = ForeignKeyField(
    column_name = 'user_id',
    field = 'id',
    model = Users,
    null = True
  )
  class Meta:
    database = db_connection
    table_name = 'user_profile'
  
class FavoriteCoursesOrder(Model):
  course = ForeignKeyField(
    column_name = 'course_id',
    field = 'id',
    model = Courses
  )
  order_index = IntegerField(null = True)
  user_profile = ForeignKeyField(
    column_name = 'user_profile_id',
    field = 'id',
    model = UserProfile
  )

  class Meta:
    database = db_connection
    table_name = 'favorite_courses_order'
    indexes = (
      (('user_profile', 'course'), True),
    )
    primary_key = CompositeKey('course', 'user_profile')

class Reviews(Model):
  id = AutoField(primary_key = True)
  content = CharField()
  course = ForeignKeyField(
    column_name = 'course_id',
    field = 'id',
    model = Courses
  )
  ratings = IntegerField()
  created_at = TimestampField(default = datetime.now)
  user = ForeignKeyField(
    column_name = 'user_id',
    field = 'id',
    model = Users
  )

  class Meta:
    database = db_connection
    table_name = 'reviews'

class ReviewTagMap(Model):
  id = AutoField(primary_key = True)
  review = ForeignKeyField(
    column_name = 'review_id',
    field = 'id',
    model = Reviews
  )
  tag = ForeignKeyField(
    column_name = 'tag_id',
    field = 'id',
    model = Tags
  )

  class Meta:
    database = db_connection
    table_name = 'review_tag_map'

class UsersCoursesMap(Model):
  id = AutoField(primary_key = True)
  course = ForeignKeyField(
    column_name = 'course_id',
    field = 'id',
    model = Courses
  )
  user = ForeignKeyField(
    column_name = 'user_id',
    field = 'id',
    model = Users
  )

  class Meta:
    database = db_connection
    table_name = 'users_courses_map'
