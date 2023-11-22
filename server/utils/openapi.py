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
| `corerequisite`      | *Text*      | Not Null                                      |
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
| `is_alumni`  | *Boolean*   | Not Null, DEFAULT `false`                     |
| `password`   | *Text*      | Not Null                                      |
| `email`      | *Text*      | Not Null, Unique                              |
| `username`   | *Text*      | Not Null, Unique                              |
| `created_at` | *Timestamp* | Not Null, DEFAULT `current_timestamp()`       |

### 👇 **User profile table schema** 👤📝
| **Name** 👥               | **Type** 🔑 | **Constraints** 🔒               |
| ------------------------- | ----------- | -------------------------------- |
| `career_goals`            | *Text*      |                                  |
| `completion_deadline`     | *Text*      |                                  |
| `courses_willing_to_take` | *Text*      |                                  |
| `hours_per_week`          | *Integer*   |                                  |
| `learning_preferences`    | *Text*      |                                  |
| `user`                    | *Integer*   | Not Null, Foreign Key (Users.id) |

### 👇 **Favorite Courses Order table schema** ⭐📖
| **Name** 👥    | **Type** 🔑 | **Constraints** 🔒                     |
| -------------- | ----------- | -------------------------------------- |
| `course`       | *Integer*   | Not Null, Foreign Key (Courses.id)     |
| `order_index`  | *Integer*   |                                        |
| `user_profile` | *Text*      | Not Null, Foreign Key (UserProfile.id) |

### 👇 **Reviews table schema** 📝
| **Name** 👥  | **Type** 🔑 | **Constraints** 🔒                            |
| ------------ | ------------| --------------------------------------------- |
| `id`         | *Integer*   | Primary Key, Auto Increment, Not Null, Unique |
| `content`    | *Text*      | Not Null                                      |
| `course`     | *Integer*   | Not Null, Foreign Key (Courses.id)            |
| `ratings`    | *Integer*   | Not Null                                      |
| `created_at` | *Timestamp* | Not Null, DEFAULT `current_timestamp()`       |
| `user`       | *Integer*   | Not Null, Foreign Key (Users.id)              |
| `is_flagged` | *Boolean*   | Not Null, DEFAULT `false`                     |

### 👇 **Review Tag Map table schema** 📝🔖
| **Name** 👥 | **Type** 🔑 | **Constraints** 🔒                            |
| ----------- | ----------- | --------------------------------------------- |
| `id`        | *Integer*   | Primary Key, Auto Increment, Not Null, Unique |
| `review`    | *Integer*   | Not Null, Foreign Key (Reviews.id)            |
| `tag`       | *Integer*   | Not Null, Foreign Key (Tags.id)               |

### 👇 **User Course Map table schema** 👤📖
| **Name** 👥 | **Type** 🔑 | **Constraints** 🔒                            |
| ----------- | ----------- | --------------------------------------------- |
| `id`        | *Integer*   | Primary Key, Auto Increment, Not Null, Unique |
| `course`    | *Integer*   | Not Null, Foreign Key (Courses.id)            |
| `user`      | *Integer*   | Not Null, Foreign Key (Users.id)              |
"""