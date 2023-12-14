# import time
from locust import HttpUser, task, between  # events, constant,


class MyUser(HttpUser):
    host = "http://34.118.158.112:5001"

    wait_time = between(1, 5)  # Simulate random wait time between requests

    @task
    def index_page(self):
        # time.sleep(2) # think time
        self.client.get("/")
