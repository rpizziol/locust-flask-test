#!/bin/bash

source environment.sh

# Delete Kubernetes cluster
echo "[Deleting the Google Cloud cluster \"$CLUSTER_NAME\" in zone \"$ZONE_NAME\".]"
gcloud container clusters delete "$CLUSTER_NAME" --zone="$ZONE_NAME" --quiet
# option "--quiet" to avoid "Do you want to continue (Y/n)?"

# Notify end of operation
echo "[Deletion of cluster \"$CLUSTER_NAME\" completed.]"
aplay /usr/share/sounds/sound-icons/piano-3.wav &> /dev/null