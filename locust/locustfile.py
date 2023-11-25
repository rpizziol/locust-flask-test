import random
from locust import HttpUser, task, events, constant


class MyUser(HttpUser):
    
    # base_url = "http://34.118.179.47:5001/"

    # wait_time = random.randint(100, 500)  # Simulate random wait time between requests

    @task
    def index_page(self):
        self.client.get("/")
    #
    # @task(weight=2)
    # def product_page(self):
    #     self.client.get("/product")
    #
    # @task(weight=1)
    # def checkout_page(self):
    #     self.client.get("/checkout")


# # Maximum number of users
# max_users = 100
#
# # Rate at which new users are created (per second)
# spawn_rate = 10
#
# # Total run time of the test in seconds
# run_time = 300
#
#
# # Configure the load test to start with 10 users and gradually increase to the maximum number of users
# def on_start(environment):
#     environment.user_count += 1
#     if environment.user_count < max_users:
#         events.locust_user_spawned.fire(environment, None, 1)
#     else:
#         timer = events.timer.Timer(spawn_rate, environment.user_count)
#         timer.add_listener(on_timer_fire)
#         timer.start()
#
#
# def on_timer_fire(timer):
#     if timer.remaining_time <= 0:
#         timer.stop()
#         return
#     if timer._current_count < max_users:
#         events.locust_user_spawned.fire(timer.environment, None, 1)
#         timer._current_count += 1
#     timer.reschedule()
