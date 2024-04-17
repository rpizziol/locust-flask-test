#!/bin/bash

source environment.sh

# Create Compute Engine instance to run locust
echo "[Creating the Compute Engine \"$INSTANCE_NAME\" in zone \"$ZONE_NAME\" of \"$INSTANCE_MACHINE_TYPE\" machine type with image \"$IMAGE\" and $DISK_SIZE boot disk size.]"

gcloud compute instances create "$INSTANCE_NAME" --project="$PROJECT_NAME" --zone="$ZONE_NAME" \
       --machine-type="$INSTANCE_MACHINE_TYPE" --image="$IMAGE" --boot-disk-size="$DISK_SIZE"
# The Compute Engine instance should already be up and running

echo "[Compute Engine \"$INSTANCE_NAME\" created.]"