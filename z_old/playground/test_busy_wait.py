import psutil as pu
import numpy as np


def get_current_time_in_ms():
    return pu.cpu_times().user + pu.cpu_times().system * 1000


def busy_wait(lock_time):
    start = get_current_time_in_ms()  # Start user time
    now = get_current_time_in_ms()  # Current user time

    while now - start < lock_time:
        now = get_current_time_in_ms()  # Update current user time

    return now - start  # Return elapsed time


mean_values = []
desired_lock_times = []

for i in range(100):
    desired_lock_times.append(np.random.exponential(100))  # ms

    bw_outputs = []
    for _ in range(100):
        output = busy_wait(desired_lock_times[i])
        bw_outputs.append(output)

    mean_values.append(np.mean(bw_outputs))

    print(f"Mean waiting time {i}: {mean_values[i]} ms")
    print(f"Desired waiting time {i}: {desired_lock_times[i]} ms")

print(f"Total mean waiting time: {np.mean(mean_values)}")
print(f"Total mean desired waiting time: {np.mean(desired_lock_times)}")

print(f"Ratio = {np.mean(mean_values) / np.mean(desired_lock_times) * 100} %")
