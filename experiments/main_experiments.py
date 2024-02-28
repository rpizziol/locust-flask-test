import time

from utils import run_subprocess, export_traces_to_csv

# Global parameters
ssh_username = "roberto_pizziol"
instance_name = "instance-1"
ssh_instance = f"{ssh_username}@{instance_name}"
zone_name = "northamerica-northeast1-a"

# Experiment parameters
max_time = 15  # minutes
n_users = 1
n_replicas = 1

# Experiment
# Update number of replicas of the webapp
# Get current number of replicas
res = run_subprocess("kubectl get deployment busy-waiting-webapp -o jsonpath='{.spec.replicas}'".split())
current_replicas = int(res.stdout.strip("'"))
if current_replicas != n_replicas:
    run_subprocess(f"kubectl scale deployment busy-waiting-webapp --replicas={n_replicas}".split())

# Restart zipkin
run_subprocess("kubectl delete pod -l app=zipkin".split())

time.sleep(20)
# TODO assicurarsi che zipkin sia up and running

# Start locust swarm
locust_command = f"~/.local/bin/locust -f ~/locust/locustfile.py -r 1 -u {n_users} --run-time {max_time}m --headless"
ssh_command = [
    "gcloud", "compute", "ssh", f"{ssh_username}@{instance_name}",
    "--zone", zone_name, "--command", locust_command
]
run_subprocess(ssh_command)

# Download data
exp_id = f"r{n_replicas}-u{n_users}"
out_file = f"./traces/zipkin-traces_{exp_id}.csv"
zipkin_ip = "http://34.152.37.184"  # http://34.152.37.184
export_traces_to_csv(zipkin_ip, 10000, out_file)

# Download CPU usage from GCP

# Parallelizza con subproccess (multiprocessing di python)