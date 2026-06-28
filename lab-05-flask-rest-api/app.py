from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Witaj w systemie monitoringu transakcji!"

@app.route("/hello")                  # GET /hello?name=Anna
def hello():
    name = request.args.get("name", "nieznajomy")   # odczytaj parametr query
    return f"Cześć, {name}!"

@app.route("/transaction/<tx_id>")    # GET /transaction/TX0042
def get_transaction(tx_id):
    return jsonify({"tx_id": tx_id, "status": "znaleziono"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
