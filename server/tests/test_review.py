from fastapi.testclient import TestClient

from server.main import app
from server.utils.crypto import create_access_token

client = TestClient(app)

def test_create_review_success():
    global created_review_id

    user = {"id": 2, "is_admin": 0}
    valid_token = create_access_token(user)
    print(valid_token)

    # Test case where review content is missing
    response = client.post(
        "/api/review/",
        json={
            "course_id": 1,
            "ratings": 4,
        },
        headers={"Authorization": f"Bearer {valid_token}"},
    )
    assert response.status_code == 422

    # Test case where course is not found
    response = client.post(
        "/api/review/",
        json={
            "course_id": 999,
            "content": "Great course!",
            "ratings": 4,
        },
        headers={"Authorization": f"Bearer {valid_token}"},
    )
    assert response.status_code == 404
    assert "No such course with id 999" in response.text


    # Test case where review creation is successful with authentication
    response = client.post(
        "/api/review/",
        json={
            "course_id": 2,
            "content": "Great course!",
            "ratings": 4,
        },
        headers={"Authorization": f"Bearer {valid_token}"},
    )

    assert response.status_code == 200

    assert "message" in response.json()

    assert "data" in response.json()

    assert "id" in response.json()["data"]
    created_review_id = response.json()["data"]["id"]

    assert "profanity_check" in response.json()["data"]
    assert "Review created successfully ✔️" in response.json()["message"]

def test_get_all_reviews_success():
    user = {"id": 2, "is_admin": 0}
    valid_token = create_access_token(user)

    response = client.get("/api/review/all",
                          headers={"Authorization": f"Bearer {valid_token}"})
    assert response.status_code == 200
    assert "reviews" in response.json()

def test_get_review_by_course_id():
    user = {"id": 2, "is_admin": 0}
    valid_token = create_access_token(user)

    response = client.get("/api/review/course-id/2",
                          headers={"Authorization": f"Bearer {valid_token}"})
    assert response.status_code == 200
    assert "data" in response.json()

def test_flag_review():
    global created_review_id
    user = {"id": 2, "is_admin": 0}
    valid_token = create_access_token(user)

    response = client.post(f"/api/review/flag/{created_review_id}",
                          headers={"Authorization": f"Bearer {valid_token}"})
    assert response.status_code == 200
    assert "message" in response.json()
    assert "Review flag toggled successfully" in response.json()["message"]

def test_get_all_reviews_unauthorized():
    response = client.get("/api/review/all")
    assert response.status_code == 401
    assert "detail" in response.json()
    assert "Not authenticated" in response.json()["detail"]

def test_edit_review():
    global created_review_id

    user = {"id": 2, "is_admin": 0}
    valid_token = create_access_token(user)

    response = client.put(f"/api/review/{created_review_id}",
                          json={
                              "content": "Great course!",
                              "ratings": 4,
                              "course_id": 2  
                          },
                          headers={"Authorization": f"Bearer {valid_token}"})
    assert response.status_code == 200
    assert "message" in response.json()
    assert "Review updated successfully" in response.json()["message"]

# def test_delete_review():
#     global created_review_id
#     user = {"id": 2, "is_admin": 0}
#     valid_token = create_access_token(user)

#     response = client.delete(f"/api/review/{created_review_id}",
#                           headers={"Authorization": f"Bearer {valid_token}"})
#     assert response.status_code == 200
#     assert "message" in response.json()
#     assert "Review deleted successfully" in response.json()["message"]
def test_tag_review():
    global created_review_id
    admin = {"id": 1, "is_admin": 1}
    valid_token = create_access_token(admin)
    print('haaaaaaaaaaaaaaaa')
    print(created_review_id)
    response = client.post("/api/review/tag",
                          json={
                              "review_id": created_review_id,
                              "tag_id": 1
                          },
                          headers={"Authorization": f"Bearer {valid_token}"})
    assert response.status_code == 200
    assert "message" in response.json()
    assert "Review tagged successfully" in response.json()["message"]

def test_delete_flagged_review():
    global created_review_id
    admin = {"id": 1, "is_admin": 1}
    valid_token = create_access_token(admin)
    print(created_review_id)
    response = client.delete(f"/api/review/flagged/{created_review_id}",
                          headers={"Authorization": f"Bearer {valid_token}"})
    assert response.status_code == 200
    assert "message" in response.json()
    assert "Flagged review deleted successfully" in response.json()["message"]
