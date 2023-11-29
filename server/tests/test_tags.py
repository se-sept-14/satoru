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


# Test: Search for tags (empty query) as admin
def test_search_tags_empty_query_admin():
    search_query = {"query": ""}
    admin_user = {"id": 1, "is_admin": 1}
    token = create_access_token(admin_user)

    response = client.post("/api/tags/search", json=search_query, headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 400
    assert "Search query empty" in response.text


# Test: Search for tags (server error) as admin
def test_search_tags_server_error_admin():
    search_query = {"query": "example"}  # Replace with a valid search query
    admin_user = {"id": 1, "is_admin": 1}
    token = create_access_token(admin_user)

    app.dependency_overrides[decode_token] = lambda: admin_user
    response = client.post("/api/tags/search", json=search_query, headers={"Authorization": f"Bearer {token}"})
    app.dependency_overrides.pop(decode_token)

    assert response.status_code == 500


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


# Test: Search for tags (empty query) as non-admin
def test_search_tags_empty_query_non_admin():
    search_query = {"query": ""}
    non_admin_user = {"id": 2, "is_admin": 0}
    token = create_access_token(non_admin_user)

    response = client.post("/api/tags/search", json=search_query, headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 400
    assert "Search query empty" in response.text


# Test: Search for tags (server error) as non-admin
def test_search_tags_server_error_non_admin():
    search_query = {"query": "example"}  # Replace with a valid search query
    non_admin_user = {"id": 2, "is_admin": 0}
    token = create_access_token(non_admin_user)

    app.dependency_overrides[decode_token] = lambda: non_admin_user
    response = client.post("/api/tags/search", json=search_query, headers={"Authorization": f"Bearer {token}"})
    app.dependency_overrides.pop(decode_token)

    assert response.status_code == 500


# Test: Search for tags with no match as non-admin
def test_search_tags_no_match_non_admin():
    search_query = {"query": "nonexistent_tag"}
    non_admin_user = {"id": 2, "is_admin": 0}
    token = create_access_token(non_admin_user)

    response = client.post("/api/tags/search", json=search_query, headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    assert "data" in response.json()
    assert len(response.json()["data"]) == 0
