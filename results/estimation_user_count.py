import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# path = '/home/robb/PycharmProjects/locust-flask-test/results/20240423/HPA-15m/HPA-15m_stats_history.csv'
path = '/home/robb/PycharmProjects/locust-flask-test/results/20240425/hpa-sin-1h/hpa-sin-1h_stats_history.csv'
# path = '/home/robb/PycharmProjects/locust-flask-test/results/20240425/muopt-sin-1h/muopt-sin-1h_stats_history.csv'

df = pd.read_csv(path)

df = df[["User Count", "Requests/s", "Total Average Response Time"]]

df["Estimated Users"] = (df["Total Average Response Time"]/1000 + 1) * df["Requests/s"]

column1 = df["User Count"]
column2 = df["Estimated Users"]
plt.step(np.linspace(1, column1.size, column1.size), column1, linestyle='-', label="User Count")
plt.step(np.linspace(1, column2.size, column2.size), column2, linestyle='-', label="Estimated Users")
plt.legend()
plt.savefig('./Users_Estimated_Users.pdf')
plt.show()

print(df)
