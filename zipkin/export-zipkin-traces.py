import requests
import csv
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


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


def plot_histogram(data):
    plt.figure(figsize=(10, 6))

    # Plot histogram of data
    plt.hist(data, bins='auto', density=True, label='Measured latency')  # alpha=0.7, color='blue',

    # Plot expected PDF of the exponential distribution
    lambda_hat = 1 / np.mean(data)
    x = np.linspace(0, max(data), 100)
    pdf = lambda_hat * np.exp(-lambda_hat * x)
    plt.plot(x, pdf, 'r-', lw=2, label='Exponential PDF')

    plt.legend()
    plt.title('Histogram vs. Exponential PDF')
    plt.show()


# Kolmogorov-Smirnov test
def kolmogorov_smirnov(data):
    ks_stat, ks_p_value = stats.kstest(data, 'expon', args=(0, np.mean(data)))
    print(f"KS test statistic: {ks_stat}, p-value: {ks_p_value}")


# Export traces to CSV file
out_file = "./traces/zipkin_traces.csv"
zipkin_ip = "http://localhost"  # http://34.152.37.184
export_traces_to_csv(zipkin_ip, 10000, out_file)

# Calculate average latency
df = pd.read_csv(out_file)
latency = df['duration']
avg_latency = np.mean(latency)  # in microseconds
print(f"The average experimental processing time is: {avg_latency/1000} ms")

# Check if it's exponential
latency_array = latency.to_numpy()
plot_histogram(latency_array)
kolmogorov_smirnov(latency_array)



#
# # Q-Q plot
# plt.figure(figsize=(10, 6))
# stats.probplot(data, dist="expon", plot=plt)
# plt.title('Q-Q Plot')
# plt.show()
#
#
# # Anderson-Darling test
# ad_stat, ad_critical_values, ad_significance_level = stats.anderson(data, dist='expon')
# print(
#     f"AD test statistic: {ad_stat}, critical values: {ad_critical_values}, significance levels: {ad_significance_level}")
