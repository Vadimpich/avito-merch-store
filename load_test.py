from locust import HttpUser, task, between

class LoadTestUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        response = self.client.post("/api/auth", json={"username": "loadtest", "password": "123456"})

        self.client.post("/api/auth", json={"username": "receiver", "password": "123456"})
        self.token = response.json()["token"]

    @task
    def get_info(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        self.client.get("/api/info", headers=headers)

    @task
    def send_coins(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        self.client.post("/api/sendCoin", json={"toUser": "receiver", "amount": 1}, headers=headers)

    @task
    def buy_merch(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        self.client.get("/api/buy/pen", headers=headers)
