import numpy as np
import time


outputs = []
for _ in range(10000000):
    think_time = np.random.exponential(1000)
    # time.sleep(think_time / 1000)
    outputs.append(think_time)


mean_value = np.mean(outputs)
print(f"Average thinking time: {mean_value} ms")
