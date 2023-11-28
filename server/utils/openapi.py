description = """
## **Components of this app** 🌠

👉 [FastAPI](https://fastapi.tiangolo.com) for RESTful API endpoints 🌐
    
👉 [MariaDB](https://mariadb.org) as the Relational SQL Database 📝
    
👉 [Peewee ORM](https://github.com/coleifer/peewee) for Database models, connection and queries 🖇
    
👉 [Docker](https://www.docker.com) for deployment 🖥

### 👇 **Courses table schema** 📚
| **Name** 👥          | **Type** 🔑 | **Constraints** 🔒                            |
| -------------------- | ----------- | --------------------------------------------- |
| `id`                 | *Integer*   | Primary Key, Auto Increment, Not Null, Unique |
| `name`               | *Text*      | Not Null                                      |
| `code`               | *Text*      | Not Null                                      |
| `price`              | *Integer*   | Not Null                                      |
| `credits`            | *Integer*   | Not Null                                      |
| `description`        | *Text*      | Not Null                                      |
| `corequisite`        | *Text*      | Not Null                                      |
| `hours_per_week`     | *Text*      | Not Null                                      |
| `prerequisites`      | *Text*      | Not Null                                      |
| `instructor_name`    | *Text*      | Not Null                                      |
| `instructor_picture` | *Text*      | Not Null                                      |
| `created_at`         | *Timestamp* | Not Null, DEFAULT `current_timestamp()`       |

### 👇 **Tags table schema** 🔖
| **Name** 👥  | **Type** 🔑 | **Constraints** 🔒                            |
| ------------ | ----------- | --------------------------------------------- |
| `id`         | *Integer*   | Primary Key, Auto Increment, Not Null, Unique |
| `name`       | *Text*      | Not Null                                      |
| `created_at` | *Timestamp* | Not Null, DEFAULT `current_timestamp()`       |

### 👇 **Course Tag Map table schema** 📖🔖
| **Name** 👥 | **Type** 🔑 | **Constraints** 🔒                            |
| ----------- | ----------- | --------------------------------------------- |
| `id`        | *Integer*   | Primary Key, Auto Increment, Not Null, Unique |
| `course_id` | *Integer*   | Not Null, Foreign Key (Courses.id)            |
| `tag_id`    | *Integer*   | Not Null, Foreign Key (Tags.id)               |

### 👇 **Users table schema** 👤
| **Name** 👥  | **Type** 🔑 | **Constraints** 🔒                            |
| ------------ | ----------- | --------------------------------------------- |
| `id`         | *Integer*   | Primary Key, Auto Increment, Not Null, Unique |
| `password`   | *Text*      | Not Null                                      |
| `is_admin`   | *Boolean*   | Not Null, DEFAULT `false`                     |
| `email`      | *Text*      | Not Null, Unique                              |
| `username`   | *Text*      | Not Null, Unique                              |
| `created_at` | *Timestamp* | Not Null, DEFAULT `current_timestamp()`       |

### 👇 **Student profile table schema** 👤📝
| **Name** 👥               | **Type** 🔑 | **Constraints** 🔒               |
| ------------------------- | ----------- | -------------------------------- |
| `career_goals`            | *Text*      |                                  |
| `completion_deadline`     | *Text*      |                                  |
| `courses_willing_to_take` | *Text*      |                                  |
| `hours_per_week`          | *Integer*   |                                  |
| `learning_preferences`    | *Text*      |                                  |
| `user`                    | *Integer*   | Not Null, Foreign Key (Users.id) |

### 👇 **Favorite Courses Order table schema** ⭐📖
| **Name** 👥       | **Type** 🔑 | **Constraints** 🔒                     |
| ----------------- | ----------- | -------------------------------------- |
| `course_id`       | *Integer*   | Not Null, Foreign Key (Courses.id)     |
| `order_index`     | *Integer*   |                                        |
| `user_profile_id` | *Text*      | Not Null, Foreign Key (UserProfile.id) |

### 👇 **Levels table schema** 👟
| **Name** 👥  | **Type** 🔑 | **Constraints** 🔒                            |
| ------------ | ------------| --------------------------------------------- |
| `id`         | *Integer*   | Primary Key, Auto Increment, Not Null, Unique |
| `name`       | *Integer*   | Not Null                                      |

### 👇 **Reviews table schema** 📝
| **Name** 👥     | **Type** 🔑 | **Constraints** 🔒                            |
| --------------- | ------------| --------------------------------------------- |
| `id`            | *Integer*   | Primary Key, Auto Increment, Not Null, Unique |
| `content`       | *Text*      | Not Null                                      |
| `course_id`     | *Integer*   | Not Null, Foreign Key (Courses.id)            |
| `ratings`       | *Integer*   | Not Null                                      |
| `created_at`    | *Timestamp* | Not Null, DEFAULT `current_timestamp()`       |
| `user_id`       | *Integer*   | Not Null, Foreign Key (Users.id)              |
| `is_flagged`    | *Boolean*   | Not Null, DEFAULT `false`                     |

### 👇 **Review Tag Map table schema** 📝🔖
| **Name** 👥    | **Type** 🔑 | **Constraints** 🔒                            |
| -------------- | ----------- | --------------------------------------------- |
| `id`           | *Integer*   | Primary Key, Auto Increment, Not Null, Unique |
| `review_id`    | *Integer*   | Not Null, Foreign Key (Reviews.id)            |
| `tag`_id       | *Integer*   | Not Null, Foreign Key (Tags.id)               |

### 👇 **Students table schema** 👤📖
| **Name** 👥           | **Type** 🔑 | **Constraints** 🔒                            |
| --------------------- | ----------- | --------------------------------------------- |
| `id`                  | *Integer*   | Primary Key, Auto Increment, Not Null, Unique |
| `category`            | *Text*      | Not Null,                                     |
| `dob`                 | *Timestamp* | Not Null,                                     |
| `gender`              | *Text*      | Not Null,                                     |
| `name`                | *Text*      | Not Null,                                     |
| `profile_picture_url` | *Text*      | Not Null,                                     |
| `pwd`                 | *Integer*   | Not Null,                                     |
| `roll_no`             | *Text*      | Not Null,                                     |
| `student_email`       | *Text*      | Not Null,                                     |
| `user_id`             | *Integer*   | Not Null, Foreign Key (Users.id)              |

### 👇 **Student About Me table schema** 👤📖
| **Name** 👥  | **Type** 🔑 | **Constraints** 🔒                            |
| ------------ | ----------- | --------------------------------------------- |
| `id`         | *Integer*   | Primary Key, Auto Increment, Not Null, Unique |
| `address`    | *Text*      | Not Null,                                     |
| `contact_no` | *Text*      | Not Null,                                     |
| `is_alumni`  | *Boolean*   | Not Null, Foreign Key (Levels.id)             |
| `level`      | *Integer*   | Not Null,                                     |
| `user_id`    | *Integer*   | Not Null, Foreign Key (Users.id)              |
| `term`       | *Text*      | Not Null,                                     |

### 👇 **Student Course Map table schema** 👤📖
| **Name** 👥 | **Type** 🔑 | **Constraints** 🔒                            |
| ----------- | ----------- | --------------------------------------------- |
| `id`        | *Integer*   | Primary Key, Auto Increment, Not Null, Unique |
| `course_id` | *Integer*   | Not Null, Foreign Key (Courses.id)            |
| `user_id`   | *Integer*   | Not Null, Foreign Key (Users.id)              |
"""