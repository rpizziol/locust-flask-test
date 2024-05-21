#!/bin/bash

echo "[Deleting possible instances of HPA already active...]"
for i in {1..3}; do
  kubectl delete hpa "spring-test-app-tier$i"
done

echo "[Resetting the amount of replicas to 1...]"
for i in {1..3}; do
  kubectl scale deployment "spring-test-app-tier$i" --replicas=1
done

echo "[Deploying HPA for all tiers...]" #
for i in {1..3}; do
#  kubectl apply -f "./deployments/hpa/hpa-deployment-$i.yaml"
  kubectl autoscale deployment "spring-test-app-tier$i" --cpu-percent=50 --min=1 --max=100
done

echo "[Deployment of HPA for all 3 tiers completed.]"
aplay /usr/share/sounds/sound-icons/piano-3.wav &> /dev/null