import time
from utils import run_subprocess, export_traces_to_csv

# Global parameters
ssh_username = "roberto_pizziol"
instance_name = "instance-1"
ssh_instance = f"{ssh_username}@{instance_name}"
zone_name = "northamerica-northeast1-a"

# Experiment parameters
max_time = 15  # minutes
n_replicas = 1
n_users = 8

#for n_replicas in range(2, 4):
#for n_users in range(18, 25):
# Experiment
# Update number of replicas of the webapp
# Get current number of replicas
print("Possibly updating number of replicas...")
res = run_subprocess("kubectl get deployment busy-waiting-webapp -o jsonpath='{.spec.replicas}'".split())
current_replicas = int(res.stdout.strip("'"))
if current_replicas != n_replicas:
    print("Number of replicas updated")
    run_subprocess(f"kubectl scale deployment busy-waiting-webapp --replicas={n_replicas}".split())
else:
    print("Number of replicas unchanged.")

# Restart zipkin
print("Restarting Zipkin...")
run_subprocess("kubectl delete pod -l app=zipkin".split())
time.sleep(20)  # Workaround - for the future: make sure zipkin is up and running
print("Zipkin should have been restarted by now.")

# Start locust swarm
print("Starting locust swarm...")
locust_command = f"~/.local/bin/locust -f ~/locust/locustfile.py -r 1 -u {n_users} --run-time {max_time}m --headless"
ssh_command = [
    "gcloud", "compute", "ssh", f"{ssh_username}@{instance_name}",
    "--zone", zone_name, "--command", locust_command
]
run_subprocess(ssh_command)

# Download data
print("Downloading zipkin traces...")
exp_id = f"r{n_replicas}-u{n_users}"
out_file = f"./traces/zipkin-traces_{exp_id}.csv"
zipkin_ip = "http://34.47.9.117"  # http://34.152.37.184
export_traces_to_csv(zipkin_ip, 300000, out_file)

# Download CPU usage from GCP
print("Your turn to download the CPU usage from GCP!")
