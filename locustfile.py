import random
from locust import HttpUser, task


class MyUser(HttpUser):
    base_url = "http://192.168.1.100:5000"  # URL of the web application

    @task
    def index_page(self):
        self.client.get("/")

    @task
    def product_page(self):
        self.client.get("/product")

    @task
    def checkout_page(self):
        self.client.get("/checkout")


wait_time = random.randint(100, 500)  # Simulate random wait time between requests
