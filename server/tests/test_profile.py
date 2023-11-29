from fastapi.testclient import TestClient

from server.main import app
from server.utils.crypto import create_access_token

client = TestClient(app)


# Test: Fetch the profile of a student (failure)
def test_fetch_profile_failure():
  user = { "id": 5, "is_admin": 0 }
  token = create_access_token(user)
  
  response = client.get(f"api/profile/", headers = { "Authorization": f"Bearer {token}" })

  assert response.status_code == 404
  assert "User profile not found" in response.text

# Test: Fetch the profile of a student (success)
def test_fetch_profile_success():
  user = { "id": 2, "is_admin": 0 }
  token = create_access_token(user)

  response = client.get(f"api/profile/", headers = { "Authorization": f"Bearer {token}" })

  assert response.status_code == 200
  assert "data" in response.json()

# Test: Fetch the profile of a student by ID (success)
def test_fetch_profile_by_id_success():
  admin_user = { "id": 1, "is_admin": 1 }
  token = create_access_token(admin_user)
  student_id = 2

  response = client.get(f"api/profile/{student_id}", headers = { "Authorization": f"Bearer {token}" })

  assert response.status_code == 200
  assert "data" in response.json()

# Test: Fetch the profile of a student by ID [non-admin user] (success)
def test_fetch_profile_by_id_nonadmin_user_failure():
  nonadmin_user = { "id": 2, "is_admin": 0 }
  token = create_access_token(nonadmin_user)
  student_id = 2

  response = client.get(f"api/profile/{student_id}", headers = { "Authorization": f"Bearer {token}" })

  assert response.status_code == 401
  assert "You are not an admin" in response.text

# Test data
student_update_data = {
  "category": "Science",
  "dob": "2000-01-01",
  "gender": "Male",
  "name": "John Doe",
  "profile_picture_url": "http://example.com/pic.jpg",
  "pwd": 1234,
  "roll_no": "CS101"
}

student_profile_update_data = {
  "career_goals": "Become a software engineer",
  "completion_deadline": "2024-01-01",
  "courses_willing_to_take": "Computer Science",
  "hours_per_week": 10,
  "learning_preferences": "Visual",
}

student_about_me_update_data = {
  "address": "123 Main St",
  "contact_no": "555-1234",
  "level": 1,
  "term": "Spring 2023",
}

# Test: Create/Edit profile
def test_create_profile():
  user = { "id": 3, "is_admin": 0 }
  token = create_access_token(user)

  response = client.post("api/profile", json = {
    "student_update": student_update_data,
    "student_profile_update": student_profile_update_data,
    "student_about_me_update": student_about_me_update_data
  }, headers = { "Authorization": f"Bearer {token}" })

  # Assert the response status code is 200 OK
  assert response.status_code == 200

  # Assert the response contains the expected data structure
  assert "data" in response.json()
  assert "student" in response.json()["data"]
  assert "profile" in response.json()["data"]
  assert "about_me" in response.json()["data"]

# Test: Create/Edit profile but Level ID is out of bounds
def test_create_profile_incorrect_level():
  user = { "id": 3, "is_admin": 0 }
  token = create_access_token(user)

  student_about_me_update_data["level"] = 5
  response = client.post("api/profile", json = {
    "student_update": student_update_data,
    "student_profile_update": student_profile_update_data,
    "student_about_me_update": student_about_me_update_data
  }, headers = { "Authorization": f"Bearer {token}" })

  assert response.status_code == 404
  assert "detail" in response.json()
  assert "No level with id" in response.json()["detail"]
