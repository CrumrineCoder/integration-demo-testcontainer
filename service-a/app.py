import os
import requests 
from flask import Flask

app = Flask(__name__)
SERVICE_B_URL = os.environ.get("SERVICE_B_URL", "http://service-b:5001")

@app.route("/trigger")
def trigger():
    r = requests.get(f"{SERVICE_B_URL}/respond")
    return f"Service B Said: {r.text}", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)