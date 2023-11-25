import locust


class MyLocust(locust.HttpUser):
    # Specify the host directly in the locustfile.py
    host = "http://<your_target_ip_address>"  # Replace with your target IP address

    task_set = locust.TaskSet()

    # Set the number of users (-u)
    task_set.users = 2500

    # Set the spawn rate (-r)
    task_set.spawn_rate = 10

    # Set the weight (--weight)
    # task_set.weight = 2

    @task_set.task
    def swarm(self):
        # Simulate a user visiting the target IP address
        self.client.get("/")
