from flask import Flask, jsonify
from google.cloud import monitoring_v3
import numpy as np
import psutil as pu
# from threading import Thread

import time

app = Flask(__name__)

request_count = 0
first_start = True
initial_time = 0


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


def write_custom_metric(double_gauge):
    project_id = 'my-microservice-test-project'
    client = monitoring_v3.MetricServiceClient()
    project_name = f"projects/{project_id}"

    series = monitoring_v3.TimeSeries()
    series.metric.type = "custom.googleapis.com/rps_gauge"
    series.resource.type = "global"

    now = time.time()
    seconds = int(now)
    nanos = int((now - seconds) * 10 ** 9)
    interval = monitoring_v3.TimeInterval(
        {"end_time": {"seconds": seconds, "nanos": nanos}}
    )
    point = monitoring_v3.Point({"interval": interval, "value": {"double_value": double_gauge}})
    series.points = [point]
    client.create_time_series(name=project_name, time_series=[series])


# def calculate_and_report_rps():
#     global request_count
#     interval = 60
#     while True:
#         time.sleep(interval)
#         rps = request_count / interval
#         # print(f"Request count = {request_count}")
#         # print(f"rps = {rps}")
#         write_custom_metric(rps)
#         request_count = 0  # Reset request count


@app.route('/')
def homepage():
    global first_start
    global request_count
    global initial_time

    lock_time = np.random.exponential(100)  # in ms
    elapsed_time = busy_wait(lock_time)
    response = {'request_count': request_count, 'elapsed_time2': elapsed_time}

    if first_start:
        print("First start")
        initial_time = time.time()
        first_start = False
    else:
        time_lapse = time.time() - initial_time
        print(f"Time lapse: {time_lapse}")
        if time_lapse > 6:
            rps = request_count / time_lapse
            print(f"rps = {rps}")
            initial_time = time.time()
            write_custom_metric(rps)
            request_count = 0
    return jsonify(response)


# rps_thread = Thread(target=calculate_and_report_rps)
# rps_thread.daemon = True
# rps_thread.start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
