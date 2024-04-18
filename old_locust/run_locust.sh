#!/bin/bash

# Set the spawn rate
swarm_rate=$1

# Set the maximum number of users
max_users=$2

# Run Locust in headless mode
locust -f locustfile.py -r "$swarm_rate" -u "$max_users" --headless


