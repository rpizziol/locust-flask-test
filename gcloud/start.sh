#!/bin/bash

# Generate Kubernetes cluster
echo +++ CREATING THE CLUSTER +++
python3 gcloud_script.py new

# Deploy the application on the cluster
echo +++ DEPLOYING THE APPLICATION TO THE CLUSTER +++
python3 gcloud_script.py dep

# Play a sound to notify end
echo +++ TASK FINISHED +++
aplay /usr/share/sounds/sound-icons/at &> /dev/null
