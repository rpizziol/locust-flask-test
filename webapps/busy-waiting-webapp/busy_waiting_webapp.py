from flask import Flask, jsonify
import requests
from py_zipkin.zipkin import zipkin_span
import psutil as pu
import numpy as np


def busy_wait(lock_time):
    start = pu.cpu_times().user * 1000  # Start user time in milliseconds
    now = pu.cpu_times().user * 1000  # Current user time in milliseconds

    while now - start < lock_time:
        now = pu.cpu_times().user * 1000  # Update current user time

    return now - start # Return elapsed time
    # print(str(lock_time) + " ms passed")


app = Flask(__name__)


def http_transport(encoded_span):
    """
    The transport function to send spans to Zipkin server.
    """
    zipkin_url = "http://zipkin-service:9411/api/v2/spans"
    #zipkin_url = "http://localhost:9411/api/v2/spans"
    requests.post(
        zipkin_url,
        data=encoded_span,
        headers={'Content-Type': 'application/json'},
    )


@app.route('/')
@zipkin_span(service_name='my_flask_service', span_name='home_page', port=5001)
def random_is_prime():
    with zipkin_span(
            service_name='my_flask_service',
            span_name='home_page',
            transport_handler=http_transport,
            port=5001,
            sample_rate=100,
    ):
        # Generate a lock time exponentially distributed with mean 100 ms
        lock_time = np.random.exponential(100) # in ms
        elapsed_time = busy_wait(lock_time)
        response = {'lock_time': lock_time, 'elapsed_time': elapsed_time}
        return jsonify(response)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
