#!/bin/bash

kubectl apply -f tier2-deployment.yaml
kubectl apply -f tier2-service.yaml
kubectl apply -f tier1-deployment.yaml
kubectl apply -f tier1-service.yaml