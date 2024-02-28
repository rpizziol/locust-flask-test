import subprocess
from csv_exporter import export_traces_to_csv

# Global parameters
ssh_username = "roberto_pizziol"
instance_name = "instance-1"
ssh_instance = f"{ssh_username}@{instance_name}"
zone_name = "northamerica-northeast1-a"

# Experiment parameters
max_time = 15  # minutes
n_users = 2
n_replicas = 1

exp_id = f"r{n_replicas}-u{n_users}"


# Experiment
# Restart zipkin
# subprocess.run("kubectl delete pod -l app=zipkin")

# Update number of replicas of the webapp
# subprocess.run(f"kubectl scale deployment busy-waiting-webapp --replicas={n_replicas}")

# Start locust swarm
# instance_command = f"'locust -f ./locust/locustfile.py -r 1 -u {n_users} --run-time {max_time}m --headless'"
# locust_command = ['gcloud', 'compute', 'ssh', ssh_instance, '--zone', zone_name, '--command', instance_command]
# subprocess.run(locust_command)
#
# # Download data
out_file = f"./traces/zipkin-traces_{exp_id}.csv"
zipkin_ip = "http://34.152.37.184"  # http://34.152.37.184
export_traces_to_csv(zipkin_ip, 10000, out_file)

# Download CPU usage from GCP