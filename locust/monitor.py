from kubernetes import client, config
from datetime import datetime
import time
import csv
import sys
import os

interval = 5  # Seconds


def get_replicas(deployment_name, v1_api):
    deployment = v1_api.read_namespaced_deployment(name=deployment_name, namespace='default')
    replica_count = deployment.spec.replicas
    return replica_count


def write_data(filepath, timestamp, value, mode):
    with open(filepath, mode, newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([timestamp, value])


# Configure Kubernetes API access
config.load_kube_config()
v1_api = client.AppsV1Api()

date = sys.argv[1]
exp_name = sys.argv[2]

replicas_folder_path = f"./results/{date}/{exp_name}/Replicas"

os.makedirs(replicas_folder_path, exist_ok=True)

# Write headers and create the files
for i in range(1, 4):
    out_path = f"{replicas_folder_path}/Replicas_{i}.csv"
    write_data(out_path, 'TimeSeries ID', 'Replicas', 'w')

while True:
    # Get current timestamp
    current_time = datetime.now().strftime("%a %b %d %Y %H:%M:%S GMT+0200 (Central European Summer Time)")

    for i in range(1, 4):
        out_path = f"{replicas_folder_path}/Replicas_{i}.csv"
        current_replicas = get_replicas(f"spring-test-app-tier{i}", v1_api)

        print(f"{i}: [{current_time}, {current_replicas}]")
        # Write data to CSV
        write_data(out_path, current_time, current_replicas, 'a')

    # Wait for the interval before next loop
    time.sleep(interval)

# # print("Data collection stopped.")
