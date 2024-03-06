import uuid

from flask import Flask, jsonify
import requests
from py_zipkin.zipkin import zipkin_span
import numpy as np
import time

from threading import Thread, Lock

from utils import busy_wait

from google.cloud import monitoring_v3
from google.protobuf import timestamp_pb2

app = Flask(__name__)

# Global variable
request_count = 0
request_count_lock = Lock()


@app.before_request
def before_request():
    global request_count
    with request_count_lock:
        request_count += 1


def write_custom_metric(calculated_rps):
    project_id = 'my-microservice-test-project'
    client = monitoring_v3.MetricServiceClient()
    project_name = f"projects/{project_id}"

    series = monitoring_v3.TimeSeries()
    series.metric.type = "custom.googleapis.com/my_metric" + str(uuid.uuid4())
    series.resource.type = "gce_instance"
    series.resource.labels["instance_id"] = "1234567890123456789"
    series.resource.labels["zone"] = "us-central1-c"
    series.metric.labels["TestLabel"] = "My Label Data"
    now = time.time()
    seconds = int(now)
    nanos = int((now - seconds) * 10 ** 9)
    interval = monitoring_v3.TimeInterval(
        {"end_time": {"seconds": seconds, "nanos": nanos}}
    )
    point = monitoring_v3.Point({"interval": interval, "value": {"double_value": calculated_rps}})
    series.points = [point]
    client.create_time_series(name=project_name, time_series=[series])

    #
    # # Initialize the Monitoring client
    # client = monitoring_v3.MetricServiceClient()
    # project_name = f"projects/{project_id}"
    #
    # # Define the time series data
    # series = monitoring_v3.TimeSeries()
    # # series.metric.type = 'custom.googleapis.com/my_application/request_per_second'
    # # series.resource.type = 'global'  # Use 'global' for simplicity, or another resource type as appropriate
    # series.metric.type = 'custom.googleapis.com/my_metric/request_per_second'
    # series.resource.type = "gce_instance"
    # series.resource.labels["instance_id"] = "1234567890123456789"
    # series.resource.labels["zone"] = "us-central1-c"
    # series.metric.labels["TestLabel"] = "My Label Data"
    #
    # series.resource.labels['project_id'] = project_id
    #
    # now = time.time()
    # seconds = int(now)
    # nanos = int((now - seconds) * 10 ** 9)
    # interval = monitoring_v3.TimeInterval(
    #     {"end_time": {"seconds": seconds, "nanos": nanos}}
    # )
    #
    # #point = monitoring_v3.Point({"interval": interval, "value": {"double_value": calculated_rps}})
    # point = monitoring_v3.Point({"interval": interval, "value": {"double_value": 3.14}})
    #
    # series.points = [point]
    # client.create_time_series(name=project_name, time_series=[series])

    # # Create a new Point instance directly
    # point = monitoring_v3.Point()
    #
    #
    # # Properly initialize the interval and end_time
    # point.interval.end_time.FromSeconds(int(time.time()))  # This ensures end_time is initialized and sets the seconds
    #
    #
    # # Add a data point
    # #point = series.points.add()
    # point.value.double_value = calculated_rps
    # now = time.time()
    # point.interval.end_time.seconds = int(now)
    # point.interval.end_time.nanos = int((now - point.interval.end_time.seconds) * 10 ** 9)
    #
    # series.points.append(point)
    #
    # # Write the time series data
    # client.create_time_series(name=project_name, time_series=[series])


def calculate_and_report_rps():
    global request_count
    interval = 60
    while True:
        time.sleep(interval)
        with request_count_lock:
            rps = request_count / interval
            print(f"Request count = {request_count}")
            print(f"rps = {rps}")
            write_custom_metric()
            request_count = 0  # Reset request count


def http_transport(encoded_span):
    """
    The transport function to send spans to Zipkin server.
    """
    # zipkin_url = "http://zipkin-service:9411/api/v2/spans"
    zipkin_url = "http://localhost:9411/api/v2/spans"
    requests.post(
        zipkin_url,
        data=encoded_span,
        headers={'Content-Type': 'application/json'},
    )


@app.route('/')
# @zipkin_span(service_name='my_flask_service', span_name='home_page', port=5001)
def busy_lock_homepage():
    # Generate a lock time exponentially distributed with mean 100 ms
    lock_time = np.random.exponential(100)  # in ms
    with zipkin_span(
            service_name='my_flask_service',
            span_name='home_page',
            transport_handler=http_transport,
            port=5001,
            sample_rate=100,
    ):
        elapsed_time = busy_wait(lock_time)
    response = {'lock_time': lock_time, 'elapsed_time': elapsed_time}
    return jsonify(response)


rps_thread = Thread(target=calculate_and_report_rps)
rps_thread.start()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
