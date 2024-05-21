#!/bin/bash

source environment.sh

echo "[Deleting possible instances of HPA already active...]"
for i in {1..3}; do
  kubectl delete hpa "spring-test-app-tier$i"
done

echo "[Resetting the amount of replicas to 1...]"
for i in {1..3}; do
  kubectl scale deployment "spring-test-app-tier$i" --replicas=1
done

echo "[Deploying VPA...]" #
gcloud container clusters update $CLUSTER_NAME --enable-vertical-pod-autoscaling

echo "[Deployment of VPA completed.]"
aplay /usr/share/sounds/sound-icons/piano-3.wav &> /dev/null