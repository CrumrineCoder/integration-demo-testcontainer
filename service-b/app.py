from flask import Flask

app = Flask(__name__)

@app.route("/respond")
def respond():
    return "Hello from B", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)