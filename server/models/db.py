import os
from datetime import datetime

from peewee import *
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path)
required_env_vars = [
  "MARIADB_HOST",
  "MARIADB_USER",
  "MARIADB_PORT",
  "MARIADB_PASSWORD",
  "MARIADB_DATABASE_NAME"
]
for var in required_env_vars:
  if not os.getenv(var):
    raise EnvironmentError(f"Missing required environment variable: {var}")


MARIADB = {
  "host": os.getenv("MARIADB_HOST"),
  "user": os.getenv("MARIADB_USER"),
  "port": int(os.getenv("MARIADB_PORT")),
  "password": os.getenv("MARIADB_PASSWORD"),
  "db_name": os.getenv("MARIADB_DATABASE_NAME")
}

db_connection = MySQLDatabase(
  MARIADB['db_name'],
  user = MARIADB['user'],
  host = MARIADB['host'],
  port = MARIADB['port'],
  password = MARIADB['password']
)

class Courses(Model):
  id: AutoField = AutoField(primary_key = True)
  name: CharField = CharField()
  code: TextField = TextField()
  price: IntegerField = IntegerField()
  credits: IntegerField = IntegerField()
  description: TextField = TextField()
  corerequisite: TextField = TextField()
  prerequisites: TextField = TextField()
  hours_per_week: TextField = TextField()
  instructor_name: TextField = TextField()
  instructor_picture: CharField = CharField()
  created_at: DateTimeField = DateTimeField(constraints = [SQL("DEFAULT current_timestamp()")])

  class Meta:
    database: MySQLDatabase = db_connection
    table_name: str = 'courses'

class Tags(Model):
  id: AutoField = AutoField(primary_key = True)
  name: CharField = CharField(unique = True)
  created_at: TimestampField = TimestampField(default = datetime.now)

  class Meta:
    database: MySQLDatabase = db_connection
    table_name: str = 'tags'

class CourseTagMap(Model):
  id: AutoField = AutoField(primary_key = True)
  course: ForeignKeyField = ForeignKeyField(column_name = 'course_id', field = 'id', model = Courses)
  tag: ForeignKeyField = ForeignKeyField(column_name = 'tag_id', field = 'id', model = Tags)

  class Meta:
    database: MySQLDatabase = db_connection
    table_name: str = 'course_tag_map'

class Users(Model):
  id: AutoField = AutoField(primary_key = True)
  password: CharField = CharField()
  is_admin: IntegerField = IntegerField()
  email: CharField = CharField(unique = True)
  username: CharField = CharField(unique = True)
  created_at: TimestampField = TimestampField(default = datetime.now)

  class Meta:
    database: MySQLDatabase = db_connection
    table_name: str = 'users'

class StudentProfile(Model):
  career_goals: TextField = TextField(null = True)
  completion_deadline: TextField = TextField(null = True)
  courses_willing_to_take: TextField = TextField(null = True)
  hours_per_week: IntegerField = IntegerField(null = True)
  learning_preferences: TextField = TextField(null = True)
  user: ForeignKeyField = ForeignKeyField(column_name = 'user_id', field = 'id', model = Users, null = True, unique = True)

  class Meta:
    database: MySQLDatabase = db_connection
    table_name: str = 'student_profile'

class FavoriteCoursesOrder(Model):
  course: ForeignKeyField = ForeignKeyField(column_name = 'course_id', field = 'id', model = Courses)
  order_index: IntegerField = IntegerField(null = True)
  user_profile: ForeignKeyField = ForeignKeyField(column_name = 'user_profile_id', field = 'id', model = StudentProfile)

  class Meta:
    database: MySQLDatabase = db_connection
    table_name: str = 'favorite_courses_order'
    indexes: tuple = (
      (('user_profile', 'course'), True),
    )
    primary_key: CompositeKey = CompositeKey('course', 'user_profile')

class Levels(Model):
  id: AutoField = AutoField(primary_key = True)
  name = TextField()

  class Meta:
    database: MySQLDatabase = db_connection
    table_name: str = 'levels'

class Reviews(Model):
  id: AutoField = AutoField(primary_key = True)
  content: CharField = CharField()
  course: ForeignKeyField = ForeignKeyField(column_name = 'course_id', field = 'id', model = Courses)
  ratings: IntegerField = IntegerField()
  created_at: DateTimeField = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
  user: ForeignKeyField = ForeignKeyField(column_name = 'user_id', field = 'id', model = Users)
  is_flagged: IntegerField = IntegerField(constraints=[SQL("DEFAULT 0")], null = True)

  class Meta:
    database: MySQLDatabase = db_connection
    table_name: str = 'reviews'

class ReviewTagMap(Model):
  id: AutoField = AutoField(primary_key = True)
  review: ForeignKeyField = ForeignKeyField(column_name = 'review_id', field = 'id', model = Reviews)
  tag: ForeignKeyField = ForeignKeyField(column_name = 'tag_id', field = 'id', model = Tags)

  class Meta:
    database: MySQLDatabase = db_connection
    table_name: str = 'review_tag_map'

class Students(Model):
  id: AutoField = AutoField(primary_key = True)
  category: TextField = TextField()
  dob: DateField = DateField()
  gender: TextField = TextField()
  name: TextField = TextField()
  profile_picture_url: CharField = CharField()
  pwd: IntegerField = IntegerField()  # Person-with-disability (not password)
  roll_no: CharField = CharField()
  student_email: TextField = TextField()
  user: ForeignKeyField = ForeignKeyField(column_name = 'user_id', field = 'id', model = Users)

  class Meta:
    database: MySQLDatabase = db_connection
    table_name: str = 'students'

class StudentAboutMe(Model):
  id: AutoField = AutoField(primary_key = True)
  address: TextField = TextField(null = True)
  contact_no: TextField = TextField(null = True)
  is_alumni: IntegerField = IntegerField(constraints=[SQL("DEFAULT 0")])
  level: ForeignKeyField = ForeignKeyField(column_name = 'level', field = 'id', model = Levels)
  user: ForeignKeyField = ForeignKeyField(column_name = 'user_id', field = 'id', model = Users)
  term = TextField()

  class Meta:
    database: MySQLDatabase = db_connection
    table_name: str = 'student_about_me'

class StudentCourseMap(Model):
  id: AutoField = AutoField(primary_key = True)
  course: ForeignKeyField = ForeignKeyField(column_name = 'course_id', field = 'id', model = Courses)
  user: ForeignKeyField = ForeignKeyField(column_name = 'user_id', field = 'id', model = Users)

  class Meta:
    database: MySQLDatabase = db_connection
    table_name: str = 'student_course_map'