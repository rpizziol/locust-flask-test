# Docker
## Build and deploy
To build and deploy the Docker Image, navigate to the `webapps` folder and run:

   ```
   docker build -t rpizziol/busy-waiting-webapp .
   docker push rpizziol/busy-waiting-webapp
   ```

### Authentication error

Remember to be logged-in in the Docker Hub registry:
```
docker login https://index.docker.io/v1/ -u <username> -p <password>
```


## Superuser rights
To avoid having to use `sudo` for every `docker` command, add your user to the `docker` group.
1. Check if docker group exists:
   ``` 
   grep docker /etc/group
   ```
2. If not, create it:
   ``` 
   sudo groupadd docker
   ```
3. Add your user to the `docker` group:
   ```
   sudo usermod -aG docker $USER
   ```
4. Restart your system and test:
   ```
   docker run hello-world
   ```
 

# Google Cloud
## Remote access to a pod
1. Check the pod name:
```
kubectl get pods
```
2. Access remotely to the pod:
```
kubectl exec -it <pod-name> -- /bin/bash
```
Note that installed software is not permanent. Remember also to run `apt update` before installing anything.
In order to install `ping`, run:
```
apt install iputils-ping
```

## Horizontal scaling
Get the list of deployments:
```
kubectl get deployments
```

Check current number of replicas of the `<deployment-name>` (in the example `spring-test-app-tier1`) deployment:

```
kubectl get deployment spring-test-app-tier1 -o jsonpath='{.spec.replicas}'
```

Change number of replicas of the `spring-test-app-tier1` deployment:
```
kubectl scale deployment spring-test-app-tier1 --replicas=2
```

```
for i in {1..3}; do kubectl scale deployment "spring-test-app-tier$i" --replicas=10; done
```


### HPA
To enable the Horizontal Pod Autoscaler, run:

```
kubectl autoscale deployment spring-test-app-tier1 --cpu-percent=50 --min=1 --max=100
```

To check if it worked properly:

```
kubectl get hpa
```

To delete all the HPA:

```
for i in {1..3}; do kubectl delete hpa "spring-test-app-tier$i"; done
```

## Compute Engine
To download the files from a compute engine `instance-1`:

```
gcloud compute scp --recurse roberto_pizziol@instance-1:/home/roberto_pizziol/source/folder/path /destination/folder/path
```

To access via terminal the compute engine `instance-1`:

```
gcloud compute ssh --zone "northamerica-northeast1-a" "roberto_pizziol@instance-1" --project "my-microservice-test-project"
```



# Random notes
```
gcloud compute addresses create rpizziol-microservice-ip --project=my-microservice-test-project --network-tier=STANDARD --region=northamerica-northeast1 && gcloud compute instances add-access-config gke-cluster-1-default-pool-0a736462-qvxq --project=my-microservice-test-project --zone=northamerica-northeast1-a --address=IP_OF_THE_NEWLY_CREATED_STATIC_ADDRESS --network-tier=STANDARD
```
