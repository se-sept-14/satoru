from fastapi.testclient import TestClient

from server.main import app

client = TestClient(app)


# Test: New user registration (success)
def test_register_user_success():
  user_data = {
    "email": "test@pickmycourse.online",
    "username": "testuser",
    "password": "test-password"
  }

  response = client.post("api/auth/register", json = user_data)

  assert response.status_code == 200
  assert response.json()["email"] == user_data["email"]
  assert response.json()["username"] == user_data["username"]