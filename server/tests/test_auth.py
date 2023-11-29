from fastapi.testclient import TestClient

from server.main import app
from server.utils.crypto import decode_token
from server.utils.random import random_string

client = TestClient(app)


# Test: New user registration (success)
def test_register_user_success():
  user_data = {
      "email": random_string() + "@pickmycourse.online",
      "username": random_string(),
      "password": random_string(),
  }

  response = client.post("api/auth/register", json = user_data)

  assert response.status_code == 200
  assert response.json()["email"] == user_data["email"]
  assert response.json()["username"] == user_data["username"]

# Test: New user registration [existing email or username] (failure)
def test_register_user_existing_username_email_failure():
  user_data = {
    "email": "test@pickmycourse.online",
    "username": "testuser",
    "password": "test-password"
  }
  response = client.post("api/auth/register", json = user_data)

  assert response.status_code == 400
  assert "Email or Username already in use" in response.text


# Test: Logging in a user (success)
def test_login_user_success():
  user_data = {
    "username": "testuser",
    "password": "test-password"
  }
  response = client.post("api/auth/login", data = user_data)

  assert response.status_code == 200
  assert "access_token" in response.json() and "token_type" in response.json()