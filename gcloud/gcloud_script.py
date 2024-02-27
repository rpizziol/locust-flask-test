import subprocess
import sys

webapp_location = '../webapps/busy-waiting-webapp/'
zipkin_location = '../zipkin/'


# kubectl apply -f filename.yaml
def kubectl_apply(filename):
    command = ['kubectl', 'apply']
    command.extend(['-f', filename])
    subprocess.run(command)


def deploy_app(folder_location):
    # kubectl apply -f deployment.yaml
    kubectl_apply(folder_location + 'deployment.yaml')
    # kubectl apply -f service.yaml
    kubectl_apply(folder_location + 'service.yaml')


def usage_message():
    print("Usage: gcloud_script.py  [new/dep/del]")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        usage_message()
        exit(1)

    action = sys.argv[1]

    # Default values
    zone = "northamerica-northeast1-a"
    machine_type = "c2-standard-8"
    cluster_name = "cluster-1"
    num_nodes = 1

    if action == "new":  # Create the cluster
        # gcloud container clusters create cluster-1 --zone=northamerica-northeast1-a
        # --machine-type=c2-standard-8 --num-nodes=1
        command = ['gcloud', 'container', 'clusters', 'create', cluster_name]
        command.extend(['--zone', zone])
        command.extend(['--machine-type', machine_type])
        command.extend(['--num-nodes', str(num_nodes)])
        subprocess.run(command)
    elif action == "dep":
        # Deploy the webapp, run the service
        deploy_app(webapp_location)
        deploy_app(zipkin_location)
    elif action == "del":  # Delete the cluster
        # gcloud container clusters delete cluster-1 --zone=northamerica-northeast1-a
        command = ['gcloud', 'container', 'clusters', 'delete', cluster_name]
        command.extend(['--zone', zone])
        command.extend(['--quiet'])  # To avoid "Do you want to continue (Y/n)?"
        subprocess.run(command)
    else:
        print("Invalid action:", action)
        usage_message()
        exit(1)
