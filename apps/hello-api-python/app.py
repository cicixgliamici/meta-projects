# -----------------------------------------------------------------------------
# FLASK WEB APPLICATION
# -----------------------------------------------------------------------------
# This is a minimal Python web API using the Flask framework.
# It serves as a mock application for our CI/CD and Docker laboratories.

from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)

# -----------------------------------------------------------------------------
# ROUTES
# -----------------------------------------------------------------------------

@app.get("/")
def home():
    """
    Root endpoint.
    Returns a simple JSON greeting to verify the API is serving traffic.
    """
    return jsonify({"message": "Hello from Software Delivery Lab!", "status": "ok"})

@app.get("/health")
def health():
    """
    Health Check endpoint.
    Crucial for DevOps (Kubernetes Liveness Probes, Load Balancers, CI/CD).
    Returns a 200 OK status to indicate the container is healthy and ready.
    """
    return jsonify({"service": "hello-api-python", "status": "healthy"})

# -----------------------------------------------------------------------------
# ENTRY POINT
# -----------------------------------------------------------------------------
# Only run this block if the script is executed directly (not imported).
if __name__ == "__main__":
    # host="0.0.0.0" makes the server externally visible (required for Docker)
    app.run(host="0.0.0.0", port=5000)
