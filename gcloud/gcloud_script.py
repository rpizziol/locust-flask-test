import subprocess
import sys


def create_cluster(cluster_name, zone, machine_type, num_nodes):
    command = ['gcloud', 'container', 'clusters', 'create', cluster_name]
    command.extend(['--zone', zone])
    command.extend(['--machine-type', machine_type])
    command.extend(['--num-nodes', str(num_nodes)])

    subprocess.run(command)


def delete_cluster(cluster_name, zone):
    command = ['gcloud', 'container', 'clusters', 'delete', cluster_name]
    command.extend(['--zone', zone])

    subprocess.run(command)


def kubectl_apply(filename):
    command = ['kubectl', 'apply']
    command.extend(['-f', filename])
    subprocess.run(command)


def run_kubectl():
    kubectl_apply('simpleapp/deployment.yaml')
    kubectl_apply('simpleapp/service.yaml')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: gcloud_script.py  [new/kub/del]")
        exit(1)

    action = sys.argv[1]

    # Default values
    zone = "northamerica-northeast1-a"
    machine_type = "c2-standard-8"
    cluster_name = "cluster-1"
    num_nodes = 1

    if action == "new":
        # Create the cluster
        create_cluster(cluster_name, zone, machine_type, num_nodes)
    elif action == "del":
        # Delete the cluster
        delete_cluster(cluster_name, zone)
    elif action == "kub":
        # Deploy the webapp and run the service
        run_kubectl()
    else:
        print("Invalid action:", action)
        print("Usage: gcloud_script.py  [new/kub/del]")
        exit(1)
