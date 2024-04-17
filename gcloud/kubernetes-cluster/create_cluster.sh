#!/bin/bash

source environment.sh

# Generate Kubernetes cluster
echo "[Creating the Google Cloud cluster \"$CLUSTER_NAME\" in zone \"$ZONE_NAME\", comprising $NUM_NODES \"$CLUSTER_MACHINE_TYPE\" nodes.]"
gcloud container clusters create "$CLUSTER_NAME" --zone="$ZONE_NAME" --machine-type="$CLUSTER_MACHINE_TYPE" --num-nodes="$NUM_NODES"

# Notify end of operation
echo "[Creation of cluster \"$CLUSTER_NAME\" completed.]"
aplay /usr/share/sounds/sound-icons/piano-3.wav &> /dev/null
