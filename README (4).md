from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    """Return a simple welcome message."""
    return jsonify(
        {
            "message": "Hello from Software Delivery Lab!",
            "status": "ok",
        }
    )


@app.get("/health")
def health():
    """Return a basic health check response."""
    return jsonify(
        {
            "service": "hello-api-python",
            "status": "healthy",
        }
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
