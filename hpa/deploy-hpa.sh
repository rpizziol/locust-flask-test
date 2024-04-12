#!/bin/bash

# Deploy HPA on each tier
for i in {1..3}; do kubectl autoscale deployment "spring-test-app-tier$i" --cpu-percent=50 --min=1 --max=100; done

# Check if HPA was correctly deployed
kubectl get hpa

