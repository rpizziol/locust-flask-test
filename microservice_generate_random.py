from flask import Flask, jsonify
import random

app = Flask(__name__)


@app.route('/')
def generate_random_number():
    random_number = random.randint(1, 100)
    response = {'random_number': random_number}
    return jsonify(response)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)