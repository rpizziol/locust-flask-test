import subprocess
import sys


# gcloud container clusters create cluster-1 --zone=northamerica-northeast1-a --machine-type=c2-standard-8 --num-nodes=1
def create_cluster(cluster_name, zone, machine_type, num_nodes):
    command = ['gcloud', 'container', 'clusters', 'create', cluster_name]
    command.extend(['--zone', zone])
    command.extend(['--machine-type', machine_type])
    command.extend(['--num-nodes', str(num_nodes)])

    subprocess.run(command)


# gcloud container clusters delete cluster-1 --zone=northamerica-northeast1-a
def delete_cluster(cluster_name, zone):
    command = ['gcloud', 'container', 'clusters', 'delete', cluster_name]
    command.extend(['--zone', zone])
    command.extend(['--quiet']) # To avoid "Do you want to continue (Y/n)?"

    subprocess.run(command)


# kubectl apply -f filename.yaml
def kubectl_apply(filename):
    command = ['kubectl', 'apply']
    command.extend(['-f', filename])
    subprocess.run(command)


def run_kubectl():
    # kubectl apply -f deployment.yaml
    kubectl_apply('deployment.yaml')
    # kubectl apply -f service.yaml
    kubectl_apply('service.yaml')

def deploy_zipkin():
    # kubectl apply -f deployment.yaml
    kubectl_apply('../zipkin/zipkin-deployment.yaml')
    # kubectl apply -f service.yaml
    kubectl_apply('../zipkin/zipkin-service.yaml')


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
        # Deploy the webapp, run the service
        run_kubectl()
        deploy_zipkin()
    else:
        print("Invalid action:", action)
        print("Usage: gcloud_script.py  [new/kub/del]")
        exit(1)
