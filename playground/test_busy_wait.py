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


desired_lock_time = 100  # ms

bw_outputs = []
for _ in range(100):
    output = busy_wait(desired_lock_time)
    bw_outputs.append(output)

mean_value = np.mean(bw_outputs)

print(f"Mean waiting time: {mean_value} ms")
print(f"Min waiting time: {desired_lock_time} ms")
