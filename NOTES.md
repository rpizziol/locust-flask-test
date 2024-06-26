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



# Random notes
```
gcloud compute addresses create rpizziol-microservice-ip --project=my-microservice-test-project --network-tier=STANDARD --region=northamerica-northeast1 && gcloud compute instances add-access-config gke-cluster-1-default-pool-0a736462-qvxq --project=my-microservice-test-project --zone=northamerica-northeast1-a --address=IP_OF_THE_NEWLY_CREATED_STATIC_ADDRESS --network-tier=STANDARD
```