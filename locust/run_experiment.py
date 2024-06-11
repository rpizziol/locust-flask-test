import os
import datetime
import time
import argparse
import redis
from kubernetes import client, config
from kubernetes.client import ApiException


def get_cli():
    """
    Get input arguments from CLI.
    :return:    ArgumentParser object.
    """
    parser = argparse.ArgumentParser(description="Run Experiment - Command Line Interface")

    parser.add_argument("-n", "--name", type=str,
                        help='The experiment name (e.g., sin200-1h-vpa)', required=True)
    parser.add_argument("-a", "--address", type=str,
                        help='The ip target of the Locust swarm', required=True)
    return parser.parse_args()


def reset_redis():
    redis_client = redis.Redis(host="localhost", port=6379)
    redis_client.set("test1_wrk", 0)


def reset_deployment_replicas(deployment_name):
    try:
        # Configure client
        config.load_kube_config()
        v1_api = client.AppsV1Api()

        # Get deployment object
        try:
            deployment = v1_api.read_namespaced_deployment(deployment_name, 'default')
        except client.ApiException as e:
            print(f"Error getting deployment: {e}")
            return

        # Update deployment spec
        deployment.spec.replicas = 1

        # Prepare and patch deployment update
        deployment_update = client.AppsV1beta1Deployment(
            api_version="apps/v1",
            kind="Deployment",
            metadata=deployment.metadata,
            spec=deployment.spec,
        )
        v1_api.patch_namespaced_deployment(deployment_name, 'default', deployment_update)

        print(f"Deployment '{deployment_name}' replicas updated to 1.")
    except client.ApiException as e:
        print(f"Error updating deployment: {e}")


def get_pod_names_by_deployment(deployment_name):
    v1_api = client.CoreV1Api()
    pods = []
    try:
        all_pods = v1_api.list_namespaced_pod(namespace='default')
        for pod in all_pods.items:
            pod_name = pod.metadata.name
            if deployment_name in pod_name:
                pods.append(pod_name)
        return pods
    except client.ApiException as e:
        print(f"Exception when calling CoreV1Api->list_namespaced_pod: {e}\n")


def scale_pod(pod_name, container_name, cpu_request, cpu_limit):
    """
    Vertically scale a pod.

    :param pod_name:        The name of the pod.
    :param container_name:  The name of the container.
    :param cpu_request:     The CPU requests to be set for the pod.
    :param cpu_limit:       The CPU limit to be set for the pod.
    :return:
    """
    v1_api = client.CoreV1Api()
    patch_body = {
        "spec": {
            "containers": [
                {
                    "name": container_name,
                    "resources": {
                        "requests": {
                            "cpu": cpu_request
                        },
                        "limits": {
                            "cpu": cpu_limit
                        }
                    }
                }
            ]
        }
    }
    try:
        # logger.info(f"Updating pod {pod_name} to CPU request {cpu_request} and CPU limit {cpu_limit}")
        v1_api.patch_namespaced_pod(name=pod_name, namespace="default", body=patch_body)
    except ApiException as e:
        if e.status == 403:
            print(f"Insufficient permissions to access pod '{pod_name}'.")
        elif e.status == 404:
            print(f"Pod '{pod_name}' not found in namespace 'default'.")
        else:
            print(f"Failed to scale pod: {e}")


def reset_conditions():
    # Reset Redis value
    reset_redis()

    # Reset replicas and requests
    for i in range(1, 4):
        deployment_name = f"spring-test-app-tier{i}"
        reset_deployment_replicas(deployment_name)
        # Reset requests for each pod
        for pod in get_pod_names_by_deployment(deployment_name):
            scale_pod(pod, f"{deployment_name}-container", 1, 16)


def create_experiment_folder(folder_name):
    os.makedirs(folder_name, exist_ok=True)

    # Remove all files inside the experiment folder (if it exists)
    for filename in os.listdir(folder_name):
        file_path = os.path.join(folder_name, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)


args = get_cli()

host_url = args.address  # "http://34.47.0.52"
exp_name = args.name
current_date = datetime.datetime.now().strftime("%Y%m%d")
exp_folder = f"./results/{current_date}/{exp_name}"
time_file = f"{exp_folder}/{exp_name}-time.txt"

# reset_conditions()

time.sleep(60)  # Wait a minute to settle

# Create the experiment folder (if it doesn't exist)
create_experiment_folder(exp_folder)

print(f"[Launching experiment {exp_name} with Locust. Results will be stored in the {exp_folder} folder.]")

# Save starting time
with open(time_file, "w") as f:
    f.write(datetime.datetime.utcnow().isoformat(sep="T", timespec="milliseconds") + "Z\n")

# Run locust
locust_command = f"locust -f locustfile.py,traceShape.py --headless --csv=\"{exp_folder}/{exp_name}\" --host=\"{host_url}\""
os.system(locust_command)

print("[Experiment completed!]")

# Save closing time
with open(time_file, "a") as f:
    f.write(datetime.datetime.utcnow().isoformat(sep="T", timespec="microseconds") + "Z\n")

with open(time_file, "a") as f:
    f.write(datetime.datetime.utcnow().isoformat(sep="T", timespec="microseconds") + "Z\n")

# reset_conditions()
