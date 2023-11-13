from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route("/")
def index():
    return make_response(render_template("index.html"), 200)

@app.route("/product")
def product_page():
    return make_response(render_template("product_page.html"), 200)

@app.route("/checkout")
def checkout():
    return make_response(render_template("checkout.html"), 200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

