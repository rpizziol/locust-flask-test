#!/bin/bash

source environment.sh

echo "[Stopping compute engine \"$INSTANCE_NAME\"...]"
gcloud compute instances stop "$INSTANCE_NAME" --project="$PROJECT_NAME" --zone="$ZONE_NAME"
echo "[Compute engine stopped.]"