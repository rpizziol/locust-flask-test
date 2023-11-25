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

* Edit `locust/locustfile.py` to change the swarm parameters and then run it with:

   ```
   locust -f ./locust/locustfile.py --headless
   ```
  

## Authors

* [Roberto Pizziol](https://github.com/rpizziol)
