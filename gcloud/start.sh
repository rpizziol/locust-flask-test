#!/bin/bash

# Generate Kubernetes cluster
python gcloud_script.py new

# Deploy the application on the cluster
python gcloud_script.py kub

# Play a sound to notify end
paplay /usr/share/sounds/freedesktop/stereo/complete.oga 

