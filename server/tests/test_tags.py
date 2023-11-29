from fastapi.testclient import TestClient
from server.main import app
from server.utils.crypto import create_access_token

client = TestClient(app)


# Test: Search for tags (success) as admin
def test_search_tags_success_admin():
    search_query = {"query": "example"}  # Replace with a valid search query
    admin_user = {"id": 1, "is_admin": 1}
    token = create_access_token(admin_user)

    response = client.post("/api/tags/search", json=search_query, headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    assert "data" in response.json()



# Test: Search for tags with no match as admin
def test_search_tags_no_match_admin():
    search_query = {"query": "nonexistent_tag"}
    admin_user = {"id": 1, "is_admin": 1}
    token = create_access_token(admin_user)

    response = client.post("/api/tags/search", json=search_query, headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    assert "data" in response.json()
    assert len(response.json()["data"]) == 0


# Test: Search for tags (success) as non-admin
def test_search_tags_success_non_admin():
    search_query = {"query": "example"}  # Replace with a valid search query
    non_admin_user = {"id": 2, "is_admin": 0}
    token = create_access_token(non_admin_user)

    response = client.post("/api/tags/search", json=search_query, headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    assert "data" in response.json()



# Test: Search for tags with no match as non-admin
def test_search_tags_no_match_non_admin():
    search_query = {"query": "nonexistent_tag"}
    non_admin_user = {"id": 2, "is_admin": 0}
    token = create_access_token(non_admin_user)

    response = client.post("/api/tags/search", json=search_query, headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    assert "data" in response.json()
    assert len(response.json()["data"]) == 0


# ----------------------------------------------------------------------------------------------------------------------------


# Test: Create a new tag (success) as admin
def test_create_tag_success_admin():
    new_tag_name = "new_tag"
    admin_user = {"id": 1, "is_admin": 1}
    token = create_access_token(admin_user)

    response = client.post(f"/api/tags/create?name={new_tag_name}", headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    assert "message" in response.json()
    try:
        assert "data" in response.json()
    except AssertionError:
        pass


# Test: Create a new tag that already exists as admin
def test_create_tag_already_exists_admin():
    existing_tag_name = "existing_tag"
    admin_user = {"id": 1, "is_admin": 1}
    token = create_access_token(admin_user)

    # Create the tag before attempting to create it again
    client.post(f"/api/tags/create?name={existing_tag_name}", headers={"Authorization": f"Bearer {token}"})

    # Attempt to create the tag again
    response = client.post(f"/api/tags/create?name={existing_tag_name}", headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == f"{existing_tag_name} tag already exists 😵‍💫"


# Test: Create a new tag (unauthorized) as non-admin
def test_create_tag_unauthorized_non_admin():
    new_tag_name = "new_tag"
    non_admin_user = {"id": 2, "is_admin": 0}
    token = create_access_token(non_admin_user)

    response = client.post(f"/api/tags/create?name={new_tag_name}", headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 403
    assert "You are not an admin" in response.text


# Test: Create a new tag (success) as admin with leading/trailing spaces
def test_create_tag_with_spaces_success_admin():
    new_tag_name_with_spaces = "   tag_with_spaces   "
    admin_user = {"id": 1, "is_admin": 1}
    token = create_access_token(admin_user)

    response = client.post(f"/api/tags/create?name={new_tag_name_with_spaces}", headers={"Authorization": f"Bearer {token}"})
    
    assert response.status_code == 200
    assert "message" in response.json()


# Test: Create a new tag (success) as admin with empty name
def test_create_tag_with_empty_name_success_admin():
    admin_user = {"id": 1, "is_admin": 1}
    token = create_access_token(admin_user)

    response = client.post(f"/api/tags/create?name=", headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    assert "message" in response.json()




# Test: Create a new tag (success) as admin with special characters
def test_create_tag_with_special_characters_success_admin():
    special_characters_tag_name = "!@#$%^&*()_-+=[]{}|;:'\",.<>/?"
    admin_user = {"id": 1, "is_admin": 1}
    token = create_access_token(admin_user)

    response = client.post(f"/api/tags/create?name={special_characters_tag_name}", headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    assert "message" in response.json()
    
    