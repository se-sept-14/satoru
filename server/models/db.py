from peewee import *
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
  metadata = TextField(null = True)
  name = CharField()

  class Meta:
    database = db_connection
    table_name = 'courses'

class Tags(Model):
  id = AutoField(primary_key = True)
  name = CharField(unique = True)

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
  email = CharField(unique = True)
  is_admin = IntegerField()
  password = CharField()
  profile = TextField(null = True)
  username = CharField(unique = True)

  class Meta:
    database = db_connection
    table_name = 'users'

class Reviews(Model):
  id = AutoField(primary_key = True)
  content = CharField()
  course = ForeignKeyField(
    column_name = 'course_id',
    field = 'id',
    model = Courses
  )
  ratings = IntegerField()
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
