# Locust-Flask Test

A Toy application to learn how to use **Locust**, **Flask**, **Google Cloud** and **Kubernetes**.

## Project Structure

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

### Execution

1. Set up a GCloud cluster with the `my-prime-checker-app` webapp running
   ```
   ./gcloud/start.sh
   ```
  This should output also the host url.

2. Edit `locust/locustfile.py` to change the host url (check on Google Cloud. E.g., `host = "http://34.118.161.222:5001"` ) and then run the script `run_locust.sh`:

   ```
   ./run_locust <SwarmRate> <MaxUsers>
   ```
  
3. Kill the kubernetes cluster with (don't forget to press Enter to continue):

   ```
   python ./gcloud/gcloud_script.py del
   ```
  
### To Do
* Edit the locust file with the assigned host url in step 1

## Authors

* [Roberto Pizziol](https://github.com/rpizziol)
