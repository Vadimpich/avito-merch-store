from conftests import *


def test_auth_register_and_login(db, client):
    """Тест API регистрации и логина"""
    response = client.post("/api/auth",
                           json={"username": "testuser", "password": "123456"})
    assert response.status_code == 200
    assert "token" in response.json()
