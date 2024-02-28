import csv
import requests


def export_traces_to_csv(zipkin_ip, limit, csv_file):
    zipkin_url = zipkin_ip + ":9411/api/v2/traces?limit=" + str(limit)

    # Make a request to the Zipkin API to fetch traces
    traces = requests.get(zipkin_url).json()

    # Headers of the CSV file
    # headers = ['traceId', 'id', 'parentId', 'name', 'service', 'timestamp', 'duration' 'spanKind']
    headers = ['traceId', 'name', 'service', 'timestamp', 'duration']

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
                    'service': span.get('localEndpoint', {}).get('serviceName', ''),
                    'timestamp': span.get('timestamp', ''),
                    'duration': span.get('duration', '')
                    # 'spanKind': span.get('kind', '')
                }
                # Write the row to the CSV file
                writer.writerow(csv_row)

    print(f"Saved traces to {csv_file}")