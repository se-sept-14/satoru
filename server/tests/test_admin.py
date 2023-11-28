from fastapi.testclient import TestClient

from server.main import app
from server.utils.crypto import create_access_token

client = TestClient(app)


# Test: Fetch all students (success)
def test_get_all_students_success():
  admin_user = { "id": 1, "is_admin": 1 }
  token = create_access_token(admin_user) # Create a valid access token for the admin user
  
  # Make a request to endpoint with valid token
  response = client.get("/api/admin/all-students", headers = { "Authorization": f"Bearer {token}" })

  # Check that the response is 200 OK
  assert response.status_code == 200

  # Check that the response contains the "data" key
  assert "data" in response.json()

# Test: Fetch all students (failure)
def test_get_all_students_unauthorized():
  nonadmin_user = {"id": 2, "is_admin": 0 }
  token = create_access_token(nonadmin_user) # Create a valid access token for the non-admin user

  # Make a request to endpoint with non-admin user's token
  response = client.get("api/admin/all-students", headers = { "Authorization": f"Bearer {token}" })

  # Check that the response code is 403 (Forbidden)
  assert response.status_code == 403

  # Check that the response contains the expected error message
  assert "You are not an admin" in response.text


# Test: Make a student alumni (success)
def test_make_alumni_success():
  user_to_make_alumni = 2
  admin_user = { "id": 1, "is_admin": 1 }
  token = create_access_token(admin_user)

  response = client.get(f"api/admin/alumni/{user_to_make_alumni}", headers = { "Authorization": f"Bearer {token}" })

  assert response.status_code == 200
  assert "data" in response.json() and "id" in response.json()["data"]

# Test: Make a non-existent student alumni (failure)
def test_make_alumni_nonexistent_student_failure():
  user_to_make_alumni = 1000000 # User ID 1 million
  admin_user = { "id": 1, "is_admin": 1 }
  token = create_access_token(admin_user)

  response = client.get(f"api/admin/alumni/{user_to_make_alumni}", headers = { "Authorization": f"Bearer {token}" })

  assert response.status_code == 404
  assert f"User with ID {user_to_make_alumni} does not exist" in response.text

# Test: Make a student alumni (failure)
def test_make_alumni_unauthorized():
  user_to_make_alumni = 2
  nonadmin_user = { "id": 2, "is_admin": 0 }
  token = create_access_token(nonadmin_user)

  response = client.get(f"api/admin/alumni/{user_to_make_alumni}", headers = { "Authorization": f"Bearer {token}" })

  assert response.status_code == 403
  assert "You are not an admin" in response.text
