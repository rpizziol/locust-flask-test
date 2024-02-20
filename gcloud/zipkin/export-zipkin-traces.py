import requests
import csv

# https://zipkin.io/zipkin-api/#/

# Change the ip accordingly after having deployed Zipkin
zipkin_ip = "http://34.152.1.37"

# Replace this URL with your Zipkin's API endpoint
zipkin_url = zipkin_ip + ":9411/api/v2/traces?limit=100"  # Change limit as required

# Make a request to the Zipkin API to fetch traces
response = requests.get(zipkin_url)
traces = response.json()

# The CSV file where the traces will be saved
csv_file = "./traces/zipkin_traces.csv"

# Define the headers for the CSV file
# headers = ['traceId', 'id', 'parentId', 'name', 'service', 'timestamp', 'duration' 'spanKind']

headers = ['traceId', 'name', 'service', 'duration']

# Open the CSV file and write the headers and trace data
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()

    # Loop through each trace
    for trace in traces:
        # Loop through each span in a trace
        for span in trace:
            # Extract and transform the data you need
            csv_row = {
                'traceId': span.get('traceId'),
                # 'id': span.get('id'),
                # 'parentId': span.get('parentId', ''),
                'name': span.get('name'),
                # 'timestamp': span.get('timestamp', ''),
                'service': span.get('localEndpoint', {}).get('serviceName', ''),
                'duration': span.get('duration', '')
                # 'spanKind': span.get('kind', '')
            }
            # Write the row to the CSV file
            writer.writerow(csv_row)

print(f"Saved traces to {csv_file}")
