#!/bin/bash

# Kill all the Kubernetes cluster
echo +++ DELETING THE CLUSTERS +++
python3 gcloud_script.py del

# Play a sound to notify end
echo +++ TASK FINISHED +++
aplay /usr/share/sounds/sound-icons/piano-3.wav &> /dev/null