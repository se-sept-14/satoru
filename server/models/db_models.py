from peewee import *

database = MySQLDatabase('recommender_system', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': '18.136.102.74', 'port': 3306, 'user': 'root', 'password': 'se-sept-14'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Courses(BaseModel):
    code = TextField()
    corerequisite = TextField()
    created_at = DateTimeField()
    credits = IntegerField()
    description = TextField()
    hours_per_week = TextField()
    instructor_name = TextField()
    instructor_picture = CharField()
    name = CharField()
    prerequisites = TextField()
    price = IntegerField()

    class Meta:
        table_name = 'courses'

class Tags(BaseModel):
    created_at = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    name = CharField(unique=True)

    class Meta:
        table_name = 'tags'

class CourseTagMap(BaseModel):
    course = ForeignKeyField(column_name='course_id', field='id', model=Courses)
    tag = ForeignKeyField(column_name='tag_id', field='id', model=Tags)

    class Meta:
        table_name = 'course_tag_map'

class Users(BaseModel):
    created_at = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    email = CharField(unique=True)
    is_admin = IntegerField()
    is_alumni = IntegerField()
    password = CharField()
    username = CharField(unique=True)

    class Meta:
        table_name = 'users'

class UserProfile(BaseModel):
    career_goals = TextField(null=True)
    completion_deadline = TextField(null=True)
    courses_willing_to_take = TextField(null=True)
    hours_per_week = IntegerField(null=True)
    learning_preferences = TextField(null=True)
    user = ForeignKeyField(column_name='user_id', field='id', model=Users, null=True, unique=True)

    class Meta:
        table_name = 'user_profile'

class FavoriteCoursesOrder(BaseModel):
    course = ForeignKeyField(column_name='course_id', field='id', model=Courses)
    order_index = IntegerField(null=True)
    user_profile = ForeignKeyField(column_name='user_profile_id', field='id', model=UserProfile)

    class Meta:
        table_name = 'favorite_courses_order'
        indexes = (
            (('user_profile', 'course'), True),
        )
        primary_key = CompositeKey('course', 'user_profile')

class Reviews(BaseModel):
    content = CharField()
    course = ForeignKeyField(column_name='course_id', field='id', model=Courses)
    created_at = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    is_flagged = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    ratings = IntegerField()
    user = ForeignKeyField(column_name='user_id', field='id', model=Users)

    class Meta:
        table_name = 'reviews'

class ReviewTagMap(BaseModel):
    review = ForeignKeyField(column_name='review_id', field='id', model=Reviews)
    tag = ForeignKeyField(column_name='tag_id', field='id', model=Tags)

    class Meta:
        table_name = 'review_tag_map'

class UsersCoursesMap(BaseModel):
    course = ForeignKeyField(column_name='course_id', field='id', model=Courses)
    user = ForeignKeyField(column_name='user_id', field='id', model=Users)

    class Meta:
        table_name = 'users_courses_map'

