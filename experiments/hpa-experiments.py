# Global parameters
import time

from experiments.utils import run_subprocess, export_traces_to_csv

ssh_username = "roberto_pizziol"
instance_name = "instance-1"
ssh_instance = f"{ssh_username}@{instance_name}"
zone_name = "northamerica-northeast1-a"

# Experiment parameters
max_time = 5  # minutes
n_users = 10

# Restart zipkin
# print("Restarting Zipkin...")
# run_subprocess("kubectl delete pod -l app=zipkin".split())
# time.sleep(20)  # Workaround - for the future: make sure zipkin is up and running
# print("Zipkin should have been restarted by now.")


# Start locust swarm
print("Starting locust swarm...")
locust_command = f"~/.local/bin/locust -f ~/locust/locustfile.py -r 100 -u {n_users} --run-time {max_time}m --headless --csv=locust_stats"
ssh_command = [
    "gcloud", "compute", "ssh", f"{ssh_username}@{instance_name}",
    "--zone", zone_name, "--command", locust_command
]
run_subprocess(ssh_command)

# # Download data
# print("Downloading zipkin traces...")
# exp_id = f"hpa-u{n_users}_{max_time}m"
# out_file = f"./traces/zipkin-traces_{exp_id}.csv"
# zipkin_ip = "http://34.118.174.240"  # http://34.152.37.184
# export_traces_to_csv(zipkin_ip, 300000, out_file)
