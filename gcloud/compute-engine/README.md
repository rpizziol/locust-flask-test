# Compute Engine guide

## Starting, stopping and checking status

1. To check if the machine is running, visualize the **list of instances** of the
   project `my-microservice-test-project`:

    ```
    gcloud compute instances list --project=my-microservice-test-project
    ```

2. To **stop the compute engine** `instance-1`:

    ```
    gcloud compute instances stop instance-1 --project=my-microservice-test-project --zone=northamerica-northeast1-a
    ```

3. To **start the compute engine** `instance-1` (remember, when creating a Compute Engine, it should already be up and
   running):

    ```
    gcloud compute instances start instance-1 --project=my-microservice-test-project --zone=northamerica-northeast1-a
    ```

## SSH Connection and file upload or download

1. To **connect by SSH** to `instance-1`:

    ```
    gcloud compute ssh roberto_pizziol@instance-1 --project=my-microservice-test-project --zone=northamerica-northeast1-a
    ```

2. To **upload the files** to a compute engine `instance-1`:

   ```
   gcloud compute scp --recurse <local-source-path> roberto_pizziol@instance-1:/home/roberto_pizziol/<remote-destination-path>
   ```

3. Conversely, **to download files** from a compute engine `instance-1`:

   ```
   gcloud compute scp --recurse roberto_pizziol@instance-1:/home/roberto_pizziol/<remote-source-path> <local-destination-path>
   ```

4. To enable kubectl on the compute engine you may need to run this:

   ```
   gcloud container clusters get-credentials cluster-1 --region=northamerica-northeast1-a
   ```


