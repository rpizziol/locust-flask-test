import random
from locust import HttpUser, task, events, constant


class MyUser(HttpUser):

    host = "http://34.118.150.25:5001"

    # wait_time = random.randint(100, 500)  # Simulate random wait time between requests

    @task
    def index_page(self):
        self.client.get("/")
