import pandas as pd
import numpy as np

kubectl_rps = '/home/robb/PycharmProjects/locust-flask-test/results/20240516/scaling-kubectl/SpringTestApp_3Tier_-_RPS.csv'
api_rps = '/home/robb/PycharmProjects/locust-flask-test/results/20240516/scaling-api/SpringTestApp_3Tier_-_RPS.csv'
api2_rps = '/home/robb/PycharmProjects/locust-flask-test/results/20240516/scaling-api2/SpringTestApp_3Tier_-_RPS.csv'
api2a_rps = '/home/robb/PycharmProjects/locust-flask-test/results/20240516/scaling-api2a/SpringTestApp_3Tier_-_RPS.csv'

df_kubectl = pd.read_csv(kubectl_rps)
df_api = pd.read_csv(api_rps)
df_api2 = pd.read_csv(api2_rps)
df_api2a = pd.read_csv(api2a_rps)

mean_rps_kubectl = np.mean(df_kubectl['RPS'].to_numpy())
mean_rps_api = np.mean(df_api['RPS'].to_numpy())
mean_rps_api2 = np.mean(df_api2['RPS'].to_numpy())
mean_rps_api2a = np.mean(df_api2a['RPS'].to_numpy())

print(mean_rps_kubectl)
print(mean_rps_api)
print(mean_rps_api2)
print(mean_rps_api2a)