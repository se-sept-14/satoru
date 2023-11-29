from fastapi.testclient import TestClient

from server.main import app
from server.utils.crypto import create_access_token

client = TestClient(app)


# Test: Fetch a course by ID (success)
def test_fetch_course_by_id():
  user = { "id": 2, "is_admin": 0 }
  token = create_access_token(user)
  course_id = 1
  response = client.get(f"api/course/id/{course_id}", headers = { "Authorization": f"Bearer {token}" })
  
  assert response.status_code == 200
  assert "data" in response.json()