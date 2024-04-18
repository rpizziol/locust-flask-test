#!/bin/bash

echo ["Downloading results from \"instance-1\"..."]
gcloud compute scp --recurse roberto_pizziol@instance-1:/home/roberto_pizziol/results/* .
echo ["Results updated."]
