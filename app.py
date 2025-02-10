from flask import Flask, jsonify
from datetime import datetime, timezone
from flask_cors import CORS

import config

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def get_info():

    email = config.EMAIL
    github_url = config.GITHUB_URL

    utc_now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    return jsonify({
        "email": email,
        "current_datetime": utc_now,
        "github_url": github_url
    }), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)