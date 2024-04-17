# Kubernetes Clusters guide

## General commands

1. To check the **list of pods**:

    ```
    kubectl get pods
    ```
2. To get the **list of deployments**:

    ```
    kubectl get deployments
    ```

## Remote access to a pod

1. To access remotely to the pod (obtain `<pod-name>` from `kubectl get pods`):

    ```
    kubectl exec -it <pod-name> -- /bin/bash
    ```

2. Note that installed software is not permanent. Remember also to run `apt update` before installing anything. In order
   to install `ping`, run `apt install iputils-ping`.

## Horizontal scaling

1. To check current number of replicas of the `<deployment-name>` (in the example `spring-test-app-tier1`) deployment:

    ```
    kubectl get deployment spring-test-app-tier1 -o jsonpath='{.spec.replicas}'
    ```

2. To change number of replicas of the `spring-test-app-tier1` deployment (in the example, set it to `2`):

    ```
    kubectl scale deployment spring-test-app-tier1 --replicas=2
    ```
    Useful command to do it for the 3-tier example application.
    ```
    for i in {1..3}; do kubectl scale deployment "spring-test-app-tier$i" --replicas=2; done
    ```

### HPA

1. To enable the **Horizontal Pod Autoscaler**, run:

    ```
    kubectl autoscale deployment spring-test-app-tier1 --cpu-percent=50 --min=1 --max=100
    ```

2. To check if it worked properly:

    ```
    kubectl get hpa
    ```

3. To delete an HPA:
   
    ```
    kubectl delete hpa spring-test-app-tier1
    ```
   To delete all of them in the 3-tier example:
    ```
    for i in {1..3}; do kubectl delete hpa "spring-test-app-tier$i"; done
    ```
