from flask import Flask, request, jsonify
from .inference import Model_loader

app = Flask("subscription")
loader = Model_loader()

@app.route("/predict", methods=["POST"])
def predict(): 
    client = request.get_json()
    prob = loader.forward(client)
    prob = {
        "subscription_prob": float(prob)
    }

    return jsonify(prob)

if __name__ == "__main__": 
    app.run(debug=True, host="0.0.0.0", port=9696)
