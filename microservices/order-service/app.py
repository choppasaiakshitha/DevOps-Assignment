from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/orders")
def orders():
    return jsonify({
        "data": ["Order-101", "Order-102", "Order-103"],
        "service": "Order Service"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
