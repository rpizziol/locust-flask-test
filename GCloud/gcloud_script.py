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

# TODO Deployment and service currently work only on conteiner-1
def run_kubectl_file(file_name):
    command = ['kubectl', 'apply']
    command.extend(['-f', file_name])
   
    subprocess.run(command)
    

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: gcloud_script.py  [new/del/kub] <cluster_name/file_name>")
        exit(1)

    action = sys.argv[1]
    name = sys.argv[2]
    
    # Default values
    zone = "northamerica-northeast1-a"
    machine_type = "c2-standard-8"
    num_nodes = 1

    if action == "new":
        # Create the cluster
        create_cluster(name, zone, machine_type, num_nodes)
    elif action == "del":
        # Delete the cluster
        delete_cluster(name, zone)
    elif action == "kub":
        run_kubectl_file(name)
    else:
        print("Invalid action:", action)
        exit(1)

