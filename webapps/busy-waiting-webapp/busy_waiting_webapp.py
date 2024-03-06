from flask import Flask, jsonify
import numpy as np
import time
import psutil as pu

from threading import Thread, Lock
from google.cloud import monitoring_v3

app = Flask(__name__)

thread_started = False


def get_current_time_in_ms():
    return pu.cpu_times().user + pu.cpu_times().system * 1000


def busy_wait(lock_time):
    start = get_current_time_in_ms()  # Start user time
    now = get_current_time_in_ms()  # Current user time
    while now - start < lock_time:
        now = get_current_time_in_ms()  # Update current user time
    return now - start  # Return elapsed time


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
    series.metric.type = "custom.googleapis.com/rps"
    series.resource.type = "global"

    now = time.time()
    seconds = int(now)
    nanos = int((now - seconds) * 10 ** 9)
    interval = monitoring_v3.TimeInterval(
        {"end_time": {"seconds": seconds, "nanos": nanos}}
    )
    point = monitoring_v3.Point({"interval": interval, "value": {"double_value": calculated_rps}})
    series.points = [point]
    client.create_time_series(name=project_name, time_series=[series])


def calculate_and_report_rps():
    global request_count
    interval = 300
    while True:
        time.sleep(interval)
        with request_count_lock:
            rps = request_count / interval
            print(f"Request count = {request_count}")
            print(f"rps = {rps}")
            write_custom_metric(rps)
            request_count = 0  # Reset request count


def start_rps_thread():
    global thread_started
    if not thread_started:
        rps_thread = Thread(target=calculate_and_report_rps)
        rps_thread.start()
        thread_started = True

start_rps_thread()


@app.route('/')
def busy_lock_homepage():
    # Generate a lock time exponentially distributed with mean 100 ms
    lock_time = np.random.exponential(100)  # in ms
    elapsed_time = busy_wait(lock_time)
    response = {'lock_time': lock_time, 'elapsed_time': elapsed_time}
    return jsonify(response)


# To avoid double requests every time
@app.route('/favicon.ico')
def favicon():
    return '', 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
