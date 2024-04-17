import statistics

from flask import Flask, jsonify
from google.cloud import monitoring_v3
import numpy as np
import psutil as pu

import time

app = Flask(__name__)

request_count = 0
first_start = True
initial_time = 0
service_times = []


def get_current_time_in_ms():
    return pu.cpu_times().user + pu.cpu_times().system * 1000


def busy_wait(lock_time):
    start = get_current_time_in_ms()  # Start user time
    now = get_current_time_in_ms()  # Current user time
    while now - start < lock_time:
        now = get_current_time_in_ms()  # Update current user time
    return now - start  # Return elapsed time


@app.before_request
def before_request():
    global request_count
    request_count += 1


def write_custom_metric(metric_name, metric_value):
    project_id = 'my-microservice-test-project'
    client = monitoring_v3.MetricServiceClient()
    project_name = f"projects/{project_id}"

    series = monitoring_v3.TimeSeries()
    series.metric.type = f"custom.googleapis.com/{metric_name}"
    series.resource.type = "global"

    now = time.time()
    seconds = int(now)
    nanos = int((now - seconds) * 10 ** 9)
    interval = monitoring_v3.TimeInterval(
        {"end_time": {"seconds": seconds, "nanos": nanos}}
    )
    point = monitoring_v3.Point({"interval": interval, "value": {"double_value": metric_value}})
    series.points = [point]
    client.create_time_series(name=project_name, time_series=[series])


@app.route('/')
def homepage():
    global first_start
    global request_count
    global initial_time
    global service_times

    lock_time = np.random.exponential(100)  # in ms
    elapsed_time = busy_wait(lock_time)
    response = {'request_count': request_count, 'elapsed_time2': elapsed_time}
    service_times.append(elapsed_time)

    if first_start:
        print("First start")
        initial_time = time.time()
        first_start = False
    else:
        time_lapse = time.time() - initial_time
        print(f"Time lapse: {time_lapse}")
        if time_lapse > 5:
            # Calculate rps
            rps = request_count / time_lapse
            print(f"rps = {rps}")
            initial_time = time.time()
            request_count = 0
            write_custom_metric("rps_gauge", rps)

            # Calculate average_time
            average_time = statistics.mean(service_times)
            print(f"average time: {average_time}")
            write_custom_metric("service_time", average_time)
            service_times = []

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
