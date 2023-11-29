from playhouse.shortcuts import model_to_dict
from fastapi import APIRouter, Depends, HTTPException

from models.db import Tags
from models.api import SearchQuery
from utils.crypto import decode_token

tags_router = APIRouter(tags = ["Tags 🔖"])

@tags_router.post("/search", summary = "Search for tags 🔎")
async def search_tags(search_query: SearchQuery, current_user: dict = Depends(decode_token)):
  if not search_query.query:
    raise HTTPException(status_code = 400, detail = "Search query empty 🗅")

  results = []
  try:
    query = search_query.query.strip()
    tags = Tags.select().where(Tags.name ** f"%{query}%")
    for tag in tags:
      results.append(model_to_dict(tag))
  except Exception as e:
    raise HTTPException(status_code = 500, detail = f"{str(e)}")
  
  return { "data": results }


@tags_router.post("/create", summary = "Create a new tag 📑")
async def create_tag(name: str, current_user: dict = Depends(decode_token)):
  is_admin = current_user["is_admin"]
  if not is_admin:
    raise HTTPException(status_code = 403, detail = "You are not an admin ❌")
  
  try:
    new_tag, created = Tags.get_or_create(name = name.strip())
    if created:
      return { "message": f"{new_tag.name} tag created successfully ✅", "data": model_to_dict(new_tag) }
    else:
      return { "message": f"{name.strip()} tag already exists 😵‍💫" }
  except Exception as e:
    raise HTTPException(status_code = 500, detail = str(e))


# ----------------------------------------------------------------------------------------------------------------------------


# Test: Create a new tag (success) as admin
def test_create_tag_success_admin():
    new_tag_name = "new_tag"
    admin_user = {"id": 1, "is_admin": 1}
    token = create_access_token(admin_user)

    response = client.post("/api/tags/create", json={"name": new_tag_name}, headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    assert "message" in response.json()
    assert "data" in response.json()
    assert response.json()["message"] == f"{new_tag_name} tag created successfully ✅"


# Test: Create a new tag that already exists as admin
def test_create_tag_already_exists_admin():
    existing_tag_name = "existing_tag"
    admin_user = {"id": 1, "is_admin": 1}
    token = create_access_token(admin_user)

    # Create the tag before attempting to create it again
    client.post("/api/tags/create", json={"name": existing_tag_name}, headers={"Authorization": f"Bearer {token}"})

    # Attempt to create the tag again
    response = client.post("/api/tags/create", json={"name": existing_tag_name}, headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == f"{existing_tag_name} tag already exists 😵‍💫"


# Test: Create a new tag (unauthorized) as non-admin
def test_create_tag_unauthorized_non_admin():
    new_tag_name = "new_tag"
    non_admin_user = {"id": 2, "is_admin": 0}
    token = create_access_token(non_admin_user)

    response = client.post("/api/tags/create", json={"name": new_tag_name}, headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 403
    assert "You are not an admin" in response.text


# Test: Create a new tag (server error)
def test_create_tag_server_error():
    # Simulate a server error by providing an invalid parameter type
    invalid_tag_name = 123
    admin_user = {"id": 1, "is_admin": 1}
    token = create_access_token(admin_user)

    response = client.post("/api/tags/create", json={"name": invalid_tag_name}, headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 500
    assert "valueError" in response.text  # Adjust this check based on the actual error message

# Test: Create a new tag (success) as admin with leading/trailing spaces
def test_create_tag_with_spaces_success_admin():
    new_tag_name_with_spaces = "   tag_with_spaces   "
    admin_user = {"id": 1, "is_admin": 1}
    token = create_access_token(admin_user)

    response = client.post("/api/tags/create", json={"name": new_tag_name_with_spaces}, headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    assert "message" in response.json()
    assert "data" in response.json()
    assert response.json()["message"] == f"{new_tag_name_with_spaces.strip()} tag created successfully ✅"


# Test: Create a new tag (success) as admin with empty name
def test_create_tag_with_empty_name_success_admin():
    admin_user = {"id": 1, "is_admin": 1}
    token = create_access_token(admin_user)

    response = client.post("/api/tags/create", json={"name": ""}, headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    assert "message" in response.json()
    assert "data" in response.json()
    assert response.json()["message"] == " tag created successfully ✅"


# Test: Create a new tag (success) as admin with very long name
def test_create_tag_with_long_name_success_admin():
    long_tag_name = "a" * 1000  # Replace with a very long tag name
    admin_user = {"id": 1, "is_admin": 1}
    token = create_access_token(admin_user)

    response = client.post("/api/tags/create", json={"name": long_tag_name}, headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    assert "message" in response.json()
    assert "data" in response.json()
    assert response.json()["message"] == f"{long_tag_name} tag created successfully ✅"


# Test: Create a new tag (success) as admin with special characters
def test_create_tag_with_special_characters_success_admin():
    special_characters_tag_name = "!@#$%^&*()_-+=[]{}|;:'\",.<>/?"
    admin_user = {"id": 1, "is_admin": 1}
    token = create_access_token(admin_user)

    response = client.post("/api/tags/create", json={"name": special_characters_tag_name}, headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    assert "message" in response.json()
    assert "data" in response.json()
    assert response.json()["message"] == f"{special_characters_tag_name} tag created successfully ✅"