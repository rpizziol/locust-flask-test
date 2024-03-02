import json
from google.cloud import monitoring_v3
from google.protobuf.json_format import MessageToJson

cluster_name = "cluster-1"
webapp_name = "busy-waiting-webapp"
zone_name = "northamerica-northeast1-a"

project_id = 'my-microservice-test-project'
project_name = f"projects/{project_id}"

# Initialize the client
client = monitoring_v3.MetricServiceClient()

# Define your MQL query
mql_query = f'''
fetch k8s_container
| metric 'kubernetes.io/container/cpu/core_usage_time'
| filter
    (resource.project_id == '{project_id}')
    && (metadata.system_labels.top_level_controller_name == '{webapp_name}'
    && metadata.system_labels.top_level_controller_type == 'Deployment')
    && (resource.cluster_name == '{cluster_name}'
    && resource.location == '{zone_name}'
    && resource.namespace_name == 'default')
| align rate(1m)
| every 1m
| group_by [], [value_core_usage_time_aggregate: aggregate(value.core_usage_time)]
'''

# Execute the MQL query
response = client.query_time_series(
    name=project_name,
    query=mql_query
)

# Convert the response to JSON
results = [MessageToJson(message) for message in response]

# Save the results as JSON
with open('query_results.json', 'w') as f:
    json.dump(results, f)

print("Query results saved to query_results.json")

# Parallelizza con subproccess (multiprocessing di python)
