from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/status')
def status():
    return jsonify({
        "status": "online",
        "node": "Throne",
        "mode": "Stateless",
        "epoch": os.environ.get("EPOCH_ID", "1")
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
