import time

from kubernetes import client, config
from kubernetes.client import ApiException

interval = 15  # Seconds to wait for each VPA update

config.load_kube_config()
v1_api = client.CoreV1Api()
vpa_api = client.CustomObjectsApi()


def scale_pod(pod_name, container_name, cpu_request, cpu_limit):
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
        v1_api.patch_namespaced_pod(name=pod_name, namespace="default", body=patch_body)
    except ApiException as e:
        if e.status == 403:
            print(f"Insufficient permissions to access pod '{pod_name}'.")
        elif e.status == 404:
            print(f"Pod '{pod_name}' not found in namespace 'default'.")
        else:
            print(f"Failed to scale pod: {e}")


def get_pods_by_deployment(deployment_name):
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


def get_cpu_by_vpa(vpa_name):
    try:
        api_response = vpa_api.list_namespaced_custom_object(group="autoscaling.k8s.io", version="v1",
                                                             namespace="default",
                                                             plural="verticalpodautoscalers")

        vpa_data = None
        for vpa in api_response["items"]:
            if vpa["metadata"]["name"] == vpa_name:
                vpa_data = vpa
                break
        if vpa_data:
            # Extract container recommendation (assuming only one container)
            container_recommendation = vpa_data['status']['recommendation']['containerRecommendations'][0]

            # Extract CPU values
            cpu_lower_bound = container_recommendation['lowerBound']['cpu']
            cpu_target = container_recommendation['target']['cpu']
            cpu_upper_bound = container_recommendation['upperBound']['cpu']

            # Print results
            print(f"VPA: {vpa_data['metadata']['name']}")
            print(f"  CPU Lower Bound: {cpu_lower_bound}")
            print(f"  CPU Target: {cpu_target}")
            print(f"  CPU Upper Bound: {cpu_upper_bound}")
            return cpu_lower_bound, cpu_upper_bound
        else:
            print(f"VPA named {vpa_name} not found in the provided data.")

    except client.ApiException as e:
        print(f"Error retrieving VPA details: {e}")


while True:
    for tier_number in range(1, 4):
        deployment_name = f"spring-test-app-tier{tier_number}"
        vpa_name = f"tier{tier_number}-vpa"

        pods = get_pods_by_deployment(deployment_name)

        for pod in pods:
            container_name = f"{deployment_name}-container"
            cpu_request, cpu_limit = get_cpu_by_vpa(vpa_name)
            scale_pod(pod, container_name, cpu_request, cpu_limit)
    time.sleep(interval)
