import time
from locust import HttpUser, task
import numpy as np


class MyUser(HttpUser):
    #host = "http://34.95.33.187:5001/"
    host = "http://127.0.0.1:5000/"

    @task
    def index_page(self):
        think_time = np.random.exponential(1000)  # in ms
        time.sleep(think_time / 1000)  # in s
        self.client.get("/")
