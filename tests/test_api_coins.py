from conftests import *


def test_send_coins(client, db):
    """Тест API перевода монет"""
    client.post("/api/auth", json={"username": "alice", "password": "123456"})
    client.post("/api/auth", json={"username": "bob", "password": "123456"})

    token = client.post("/api/auth", json={"username": "alice",
                                           "password": "123456"}).json()[
        "token"]

    response = client.post(
        "/api/sendCoin",
        json={"toUser": "bob", "amount": 50},
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Перевод выполнен успешно"
