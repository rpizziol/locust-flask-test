#!/bin/bash

# Deploy HPA on each tier
echo "[Deploying HPA for all tiers...]"
for i in {1..3}; do
  kubectl autoscale deployment "spring-test-app-tier$i" --cpu-percent=50 --min=1 --max=100
done

echo "[Deployment of HPA for all 3 tiers completed.]"
aplay /usr/share/sounds/sound-icons/piano-3.wav &> /dev/null