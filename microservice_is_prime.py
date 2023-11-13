from flask import Flask, jsonify
import random


def is_prime_recursive(number, divisor):
    if divisor * divisor > number:
        return True
    if number % divisor == 0:
        return False
    return is_prime_recursive(number, divisor + 2)


def is_prime(number):
    # Check simple cases first
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    # Check if the number is prime using the definition
    return is_prime_recursive(number, 5)


app = Flask(__name__)


@app.route('/random-is-prime')
def random_is_prime():
    random_number = random.randint(1, 1000000)
    is_prime_result = is_prime(random_number)
    response = {'random_number': random_number, 'is_prime': is_prime_result}
    return jsonify(response)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
