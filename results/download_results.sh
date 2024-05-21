#!/bin/bash

date="20240520"

echo ["Downloading $date results from \"instance-1\"..."]
mkdir -p "./$date"
gcloud compute scp --recurse "roberto_pizziol@instance-1:/home/roberto_pizziol/results/$date/*" "./$date"
echo ["Results updated."]
