#!/bin/bash

source environment.sh

echo "[Starting compute engine \"$INSTANCE_NAME\"...]"
gcloud compute instances start "$INSTANCE_NAME" --project="$PROJECT_NAME" --zone="$ZONE_NAME"
echo "[Compute engine started.]"