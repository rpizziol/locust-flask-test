import sys
from time import sleep

import pandas as pd
import redis

# # Read from csv rps and service time
date = sys.argv[1]
exp_name = sys.argv[2]
# exp_name = 'hpa-sin_p400-30min'
# date = '20240429'

window = 2  # Number of seconds and entries to average
print(f"Monitoring Experiment \"{exp_name}\"...")
sleep(2)
while True:
    sleep(window)
    exp_path = f"./results/{date}/{exp_name}/{exp_name}_stats_history.csv"
    locust_data = pd.read_csv(exp_path)

    # Estimate number of users
    last_rows = locust_data.tail(window)
    # print(last_row)
    estimated_users = (last_rows['Total Average Response Time'] / 1000 + 1) * last_rows['Requests/s']
    user_value = max(int(estimated_users.mean()), 10)
    actual_users = int(last_rows['User Count'].iloc[-1])
    users_used = actual_users # max(user_value, actual_users)
    print(f"Estimated Users = {user_value}, Actual Users = {actual_users}") # -> Users Used = {users_used}")

    # Write on redis database the estimated result
    rCon = redis.Redis(host='localhost', port=6379, decode_responses=True)
    rCon.set('test1_wrk', str(users_used))
    rCon.set('test1_rps', str(last_rows['Requests/s'].mean()))
