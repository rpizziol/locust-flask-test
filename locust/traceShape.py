import csv
from locust import LoadTestShape
import pandas as pd


class TraceShape(LoadTestShape):
    lastStage = None
    mod = None
    shift = None
    duration = None
    traceFile = None
    data = None

    def __init__(self, mod=400, shift=10, duration=600, traceFile="./workloads/trace.csv"):
        super().__init__()
        self.mod = mod
        self.shift = shift
        self.duration = duration
        self.traceFile = traceFile
        self.data = pd.read_csv(self.traceFile).to_numpy().T[0]
        self.maxIndex = len(self.data)
        # rescale the trace
        mx = max(self.data)
        mn = min(self.data)
        self.data = [(v - mn) / (mx - mn) * self.mod + self.shift for v in self.data]

    def tick(self):
        run_time = self.get_run_time()
        if run_time <= self.duration:
            if int(run_time) % 20 == 0:  # Update number of users every 20 secs
                self.users = (self.f(int(run_time)), 1)
                self.save_users(self.users)
            return self.users
        return None

    def f(self, x):
        return self.data[int(x) % self.maxIndex]

    def save_users(self, users):
        with open("./workload.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([users])
            print(f"Saved users: {users}")
