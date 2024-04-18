#!/bin/bash

source locustenv/bin/activate

current_date=$(date +%Y%m%d)
host_url="http://35.203.10.69:80"
exp_folder="./results/$current_date/$1"
time_file="$exp_folder/$1-time.txt"

# Check if an argument is provided
if [ "$1" ]; then
  mkdir -p "$exp_folder"
  echo "[Launching experiment $1 with Locust in 1 minute. Results will be stored in the $exp_folder folder.]"
  date -u +"%Y-%m-%dT%H:%M:%S.%3NZ" > "$time_file" # Save start time
  sleep 1m
  locust -f locustfile.py,traceShape.py --headless --csv="$exp_folder/$1" --host="$host_url"
  # locust -f locustfile.py -r 100 -u 20 --run-time 10m --headless --csv="$exp_folder/$1" --host="$host_url"
  echo "[Experiment completed!]"
  sleep 1m
  # Save end time
  date -u +"%Y-%m-%dT%H:%M:%S.%3NZ" >> "$time_file" # Save end time
else
    echo "[Please provide the name of the experiment (e.g. ./run_experiment.sh 80users20min).]"
fi
