# Locust-Flask Test

A Toy application to learn how to use **Locust**, **Flask**, **Google Cloud** and **Kubernetes**.

## Getting Started

The structure of this project is the following:

* `gcloud`: a series of scripts and `.yaml` files used to automatically initialize the Kubernetes cluster, deploy a web application and delete the cluster.

* `locust`: the `locustfile.py` used to swarm the webapp with users.

* `webapps`: some example *Flask* webapps (the default one used for this project is `microservice_is_prime.py`) and a `Dockerfile`.

### Dependencies

All the required dependencies are in the `requirements.txt` file.

You can install them with `pip` as follows:

```
pip install -r requirements.txt
```

### Executing program

* Set up a GCloud cluster with the `my-prime-checker-app` webapp running
   ```
   ./gcloud/start.sh
   ```

* Run the Locust script to generate workload.

   ```
   cd locust; locust
   ```
  
   From the locust GUI (go to http://0.0.0.0:8089 ) select *Number of users*, *Spawn rate* and the *Host* (e.g., http://34.118.161.222:5001/, see Google Cloud for the assigned exposed url).

## Authors

* [Roberto Pizziol](https://github.com/rpizziol)
