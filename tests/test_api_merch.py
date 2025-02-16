from conftests import *


def test_buy_merch(client, db):
    """Тест API покупки товара"""
    client.post("/api/auth", json={"username": "buyer", "password": "123456"})
    token = client.post("/api/auth", json={"username": "buyer",
                                           "password": "123456"}).json()[
        "token"]

    response = client.get(
        "/api/buy/t-shirt",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert "Вы купили t-shirt" in response.json()["message"]
