#!/bin/bash

# Deploy tiers and expose services
for i in {3..1}; do
  echo "[Deploying tier$i...]"
  kubectl apply -f "./deployments/tier$i-deployment.yaml"
  sleep 1
  kubectl apply -f "./deployments/tier$i-service.yaml"
  sleep 1
done

echo "[Deployment of 3-tier webapp completed.]"
aplay /usr/share/sounds/sound-icons/piano-3.wav &> /dev/null