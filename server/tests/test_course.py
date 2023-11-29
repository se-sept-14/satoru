from fastapi.testclient import TestClient

from server.main import app
from server.utils.crypto import create_access_token

client = TestClient(app)


# Test: Fetch a course by ID (success)
def test_fetch_course_by_id_success():
  user = { "id": 2, "is_admin": 0 }
  token = create_access_token(user)
  course_id = 1
  response = client.get(f"api/course/id/{course_id}", headers = { "Authorization": f"Bearer {token}" })

  assert response.status_code == 200
  assert "data" in response.json()

# Test: Fetch a course by ID (failure)
def test_fetch_course_by_id_failure():
  user = { "id": 2, "is_admin": 0 }
  token = create_access_token(user)
  course_id = 1000000 # Course ID one million
  response = client.get(f"api/course/id/{course_id}", headers = { "Authorization": f"Bearer {token}" })

  assert response.status_code == 404
  assert f"No course with id {course_id}" in response.text

# Test: Fetch all courses (success)
def test_fetch_course_by_id():
  user = { "id": 2, "is_admin": 0 }
  token = create_access_token(user)
  response = client.get(f"api/course/all", headers = { "Authorization": f"Bearer {token}" })

  assert response.status_code == 200
  assert "data" in response.json() and len(response.json()["data"]) >= 0

# Test: Add a new course (success)
def test_create_course_success():
  admin_user = { "id": 1, "is_admin": 1 }
  token = create_access_token(admin_user)

  # Test valid data
  valid_data = {
    "name": "Test Course",
    "code": "TC101",
    "price": 4000,
    "credits": 3,
    "description": "Test course description",
    "corequisite": "None",
    "prerequisites": "None",
    "hours_per_week": "15",
    "instructor_name": "John Doe",
    "instructor_picture": "http://example.com/johndoe.jpg",
    "tags": ["tag1", "tag2"]
  }

  response = client.post("api/course/", json = valid_data, headers = { "Authorization": f"Bearer {token}" })

  assert response.status_code == 200
  assert "message" in response.json() and "data" in response.json()

# Test: Add a new course [non-admin user] (failure)
def test_create_course_nonadmin_user_failure():
  nonadmin_user = { "id": 2, "is_admin": 0 }
  token = create_access_token(nonadmin_user)

  # Test valid data
  valid_data = {
    "name": "Test Course",
    "code": "TC101",
    "price": 4000,
    "credits": 3,
    "description": "Test course description",
    "corequisite": "None",
    "prerequisites": "None",
    "hours_per_week": "15",
    "instructor_name": "John Doe",
    "instructor_picture": "http://example.com/johndoe.jpg",
    "tags": ["tag1", "tag2"]
  }

  response = client.post("api/course/", json = valid_data, headers = { "Authorization": f"Bearer {token}" })

  assert response.status_code == 403
  assert "You are not an admin" in response.text

# # Test: Delete a course (success)
# def test_delete_course_success():
#   admin_user = { "id": 1, "is_admin": 1 }
#   token = create_access_token(admin_user)
#   course_to_delete = 6
#
#   response = client.delete(f"api/course/{course_to_delete}", headers = { "Authorization": f"Bearer {token}" })
#
#   assert response.status_code == 200
#   assert "message" in response.json() and "data" in response.json() and f"Course with ID {course_to_delete} deleted successfully" in response.json()["message"]def test_delete_course_success():

# Test: Delete a non-existent course (failure)
def test_delete_nonexistent_course_failure():
  admin_user = { "id": 1, "is_admin": 1 }
  token = create_access_token(admin_user)
  course_to_delete = 1000000

  response = client.delete(f"api/course/{course_to_delete}", headers = { "Authorization": f"Bearer {token}" })

  assert response.status_code == 404
  assert f"Course with ID {course_to_delete} not found" in response.text

# Test: Delete a course (failure)
def test_delete_course_nonadmin_user_failure():
  nonadmin_user = { "id": 2, "is_admin": 0 }
  token = create_access_token(nonadmin_user)
  course_to_delete = 6

  response = client.delete(f"api/course/{course_to_delete}", headers = { "Authorization": f"Bearer {token}" })

  assert response.status_code == 403
  assert "You are not an admin" in response.text

# Test: Edit an existing course [admin user] (success)
def test_edit_course_admin_user_success():
  admin_user = { "id": 1, "is_admin": 1 }
  token = create_access_token(admin_user)
  course_to_edit = 6

  # Test valid data
  valid_data = {
    "name": "Test Course - Edit",
    "code": "TC101",
    "price": 4000,
    "credits": 3,
    "description": "Test course description",
    "corequisite": "None",
    "prerequisites": "None",
    "hours_per_week": "15",
    "instructor_name": "John Doe",
    "instructor_picture": "http://example.com/johndoe.jpg",
    "tags": ["tag1", "tag2"]
  }

  response = client.put(f"api/course/{course_to_edit}", json = valid_data, headers = { "Authorization": f"Bearer {token}" })

  assert response.status_code == 200
  assert "data" in response.json() and "message" in response.json() and f"Course with ID {course_to_edit} updated successfully" in response.json()["message"]

# Test: Edit a non-existent course [admin user] (failure)
def test_edit_nonexistent_course_admin_user_failure():
  admin_user = { "id": 1, "is_admin": 1 }
  token = create_access_token(admin_user)
  course_to_edit = 1000000

  # Test valid data
  valid_data = {
    "name": "Test Course - Edit",
    "code": "TC101",
    "price": 4000,
    "credits": 3,
    "description": "Test course description",
    "corequisite": "None",
    "prerequisites": "None",
    "hours_per_week": "15",
    "instructor_name": "John Doe",
    "instructor_picture": "http://example.com/johndoe.jpg",
    "tags": ["tag1", "tag2"]
  }

  response = client.put(f"api/course/{course_to_edit}", json = valid_data, headers = { "Authorization": f"Bearer {token}" })

  assert response.status_code == 404
  assert f"Course with ID {course_to_edit} not found" in response.text

# Test: Edit an existing course [non-admin user] (failure)
def test_edit_course_nonadmin_user_failure():
  nonadmin_user = { "id": 2, "is_admin": 0 }
  token = create_access_token(nonadmin_user)
  course_to_edit = 6

  # Test valid data
  valid_data = {
    "name": "Test Course - Edit",
    "code": "TC101",
    "price": 4000,
    "credits": 3,
    "description": "Test course description",
    "corequisite": "None",
    "prerequisites": "None",
    "hours_per_week": "15",
    "instructor_name": "John Doe",
    "instructor_picture": "http://example.com/johndoe.jpg",
    "tags": ["tag1", "tag2"]
  }

  response = client.put(f"api/course/{course_to_edit}", json = valid_data, headers = { "Authorization": f"Bearer {token}" })

  assert response.status_code == 403
  assert "You are not an admin" in response.text

# Test: Search for courses
def test_search_courses():
  nonadmin_user = { "id": 2, "is_admin": 0 }
  token = create_access_token(nonadmin_user)
  search_term = { "query": "deep learning" }

  response = client.post(f"api/course/search", json = search_term, headers = { "Authorization": f"Bearer {token}" })

  assert response.status_code == 200
  assert "data" in response.json() and len(response.json()["data"]) >= 0

# Test: Get recommended courses
def test_get_recommended_courses():
  user = { "id": 2, "is_admin": 0 }
  token = create_access_token(user)

  # Test valid request
  response = client.get("api/course/recommend/3", headers = { "Authorization": f"Bearer {token}" })
  assert response.status_code == 200
  assert "data" in response.json()

  recommended_courses = response.json()["data"]
  assert len(recommended_courses) == 3