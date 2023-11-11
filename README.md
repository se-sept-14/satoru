## 🚧 **Software Engineering Project (Group 14)**

### **To deploy the api using Docker**
- `cd server`
- `sh deploy.sh` [Make sure Docker is installed on the system](https://docs.docker.com/engine/install)

### **Endpoints to make**
- [x] [~~Kashif~~*Tejas*]() ~~A get endpoint to fetch student's profile~~
- [x] [Kashif]() ~~A get endpoint to fetch all courses~~
- [x] [Kashif]() ~~A get endpoint to fetch course by given id~~
- [~~Kashif~~*Tejas*]() A post endpoint to update student's profile (takes in user id)
- [Ananya]() A post endpoint to create a review (takes in course id and user id)
- [Ananya]() A get endpoint to fetch all reviews
- [Ananya]() A delete endpoint to delete a review (takes in review id)
- [Potential endpoint]() A put endpoint to edit the review
- A get endpoint to generate recommendations (query params take in user id)
- [Ananya]() A post endpoint to search for courses (key word)
- A post endpoint to search for reviews
  - Reviews of a particular course
  - Reviews in a particular timeframe [**created_at field is required in the reviews table**]
- **ADMIN endpoints**
- [x] [~~Aarya~~ *Kashif*]() ~~A post endpoint to add a course~~
- [x] [~~Kashif~~*Aarya*]() A put endpoint to edit a course (takes in course id)
- [x] [~~Kashif~~*Aarya*]() A delete endpoint to delete a course (takes in course id)
- A put endpoint to update an existing student details (takes in user id)
  - This can mark the student as alumni or not
- A post endpoint to map a review to it's correct tag (takes in review id and tag id)
- A delete endpoint to delete a flagged review (takes in review id) [**make a db column called "flagged"**]
