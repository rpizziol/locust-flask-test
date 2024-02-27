from flask import Flask, jsonify
import requests
from py_zipkin.zipkin import zipkin_span
import psutil as pu
import numpy as np


def get_current_time_in_ms():
    return pu.cpu_times().user + pu.cpu_times().system * 1000


def busy_wait(lock_time):
    start = get_current_time_in_ms()  # Start user time
    now = get_current_time_in_ms()  # Current user time

    while now - start < lock_time:
        now = get_current_time_in_ms()  # Update current user time

    return now - start  # Return elapsed time


app = Flask(__name__)


def http_transport(encoded_span):
    """
    The transport function to send spans to Zipkin server.
    """
    zipkin_url = "http://zipkin-service:9411/api/v2/spans"
    # zipkin_url = "http://localhost:9411/api/v2/spans"
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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
