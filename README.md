# Locust-Flask Test

A Toy application to learn how to use **Google Cloud**,  **Kubernetes**, and **Locust**.

## Project Structure

The structure of this project is the following:

* `experiments`: scripts to run experiments and experimental data (`data`).

* `gcloud`: a series of scripts to automatically initialize the Kubernetes cluster, deploy a web application and delete the cluster.

* `locust`: the `locustfile.py` used to swarm the webapp with users.

* `playground`: a folder with scripts to test features and methods. Will be deleted in the final version of the project.

* `webapps`: some example *Flask* webapps and a `Dockerfile` that can be used for this project. The current version of the project uses [custom-metrics-app](https://hub.docker.com/r/rpizziol/custom-metrics-app).

* `zipkin`: `.yaml` files to deploy a Zipkin server and a script to export the traces from the exposed Zipkin web application. To be deleted.

### Dependencies

All the required dependencies are in the `requirements.txt` file.

You can install them with `pip` as follows:

```
pip install -r requirements.txt
```

### Execution

1. Set up a GCloud cluster with the chosen webapp running
   ```
   ./gcloud/start.sh
   ```
   This should output also the host url. If not, run manually:
   ```
   kubectl get service <app-service-name>
   ```
   
2. Check the endpoint assigned by GoogleCloud (the `LoadBalancer Ingress:` of the following command):

   ```
   kubectl describe services <app-service-name>
   ```

3. Edit `locust/locustfile.py` to change the host url obtained in step 2 (E.g., `host = "http://34.118.161.222:5001"` ) and run the script `run_locust.sh`:

   ```
   ./locust/run_locust.sh <SwarmRate> <MaxUsers>
   ```
  
4. Kill the kubernetes cluster with the script:

   ```
   ./gcloud/close.sh
   ```
  

## HPA
To enable the Horizontal Pod Autoscaler, run:

```
kubectl autoscale deployment busy-waiting-webapp --cpu-percent=50 --min=1 --max=100
```

To check if it worked properly:

```
kubectl get hpa
```

## Authors

* [Roberto Pizziol](https://github.com/rpizziol)
