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