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