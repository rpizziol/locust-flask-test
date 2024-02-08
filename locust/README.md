The command used to create a Compute Engine Instance is:
```
gcloud compute instances create instance-1 \
    --project=my-microservice-test-project \
    --zone=northamerica-northeast1-a \
    --machine-type=e2-medium \
    --image=projects/ubuntu-os-cloud/global/images/ubuntu-2204-jammy-v20240207 \
    --boot-disk-size=10GB
```

And it should be already up and running.

Check if the machine is running:
```
gcloud compute instances list --project=my-microservice-test-project
```

To connect by SSH:
```
gcloud compute ssh instance-1 --project=my-microservice-test-project --zone=northamerica-northeast1-a
```


To stop the compute engine:
```
gcloud compute instances stop instance-1 --project=my-microservice-test-project --zone=northamerica-northeast1-a
```

To start it again:

```
gcloud compute instances start instance-1 --project=my-microservice-test-project --zone=northamerica-northeast1-a
```