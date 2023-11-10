## 🚧 **Software Engineering Project (Group 14)**

### **To run the api server**
- `cd server`
- [OPTIONAL]() Create an environment
  - On Windows Powershell
    - `python -m venv .venv`
    - `.venv\Scripts\activate`
  - On Windows Git Bash or Linux or Mac
    - `python3 -m venv .venv`
    - `source .venv/bin/activate`
- Install dependencies `pip install -r requirements.txt`
- Run the api server
  - On Windows Powershell
    - `uvicorn main:app --port 5000 --reload`
  - On Windows Git Bash or Linux or Mac
    - `sh run.sh`
- You can use something like Insomnia, Postman or ThunderClient to test APIs
  - Or, just visit [http://localhost:5000/docs](http://127.0.0.1:5000/docs) to open Swagger and test the endpoints there

### **Endpoints to make**
- [Kashif]() A get endpoint to fetch student's profile
- [Kashif]() A post endpoint to update student's profile (takes in user id)
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
- A post endpoint to add a course
- A put endpoint to edit a course (takes in course id)
- A delete endpoint to delete a course (takes in course id)
- A put endpoint to update an existing student details (takes in user id)
  - This can mark the student as alumni or not
- A post endpoint to map a review to it's correct tag (takes in review id and tag id)
- A delete endpoint to delete a flagged review (takes in review id) [**make a db column called "flagged"**]
