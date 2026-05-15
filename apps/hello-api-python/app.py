"""
FLASK WEB APPLICATION
-------------------------------------------------------------------------------
This is a minimal Python web API using the Flask framework.
It serves as a mock application for our CI/CD and Docker laboratories.

Educational Note:
In a real-world microservice architecture, this application would typically
handle specific business logic (e.g., User Authentication, Payment Processing).
Here, we use it to demonstrate how to package, test, and deploy a Python app.
"""

from flask import Flask, jsonify

# Initialize the Flask application
# __name__ tells Flask where to look for resources like templates and static files.
app = Flask(__name__)


# -----------------------------------------------------------------------------
# ROUTES (API Endpoints)
# -----------------------------------------------------------------------------


@app.get("/")
def home():
    """
    Root endpoint (HTTP GET /).
    Returns a simple JSON greeting to verify the API is serving traffic.

    In production, you might return API version info or documentation links here.
    """
    return jsonify(
        {
            "message": "Hello from Software Delivery Lab!",
            "status": "ok",
        }
    )


@app.get("/health")
def health():
    """
    Health Check endpoint (HTTP GET /health).

    CRITICAL FOR DEVOPS:
    - Kubernetes uses this for 'Liveness' and 'Readiness' probes to know if
      the Pod should receive traffic or if it needs to be restarted.
    - Load Balancers (like AWS ALB or NGINX) use this to route traffic only
      to healthy backend instances.
    """
    return jsonify(
        {
            "service": "hello-api-python",
            "status": "healthy",
        }
    )


# -----------------------------------------------------------------------------
# ENTRY POINT
# -----------------------------------------------------------------------------
# Only run this block if the script is executed directly (not imported elsewhere).
if __name__ == "__main__":
    # host="0.0.0.0" makes the server externally visible.
    # This is ABSOLUTELY REQUIRED when running inside a Docker container,
    # otherwise the app will only bind to localhost inside the container
    # and won't be accessible from the host machine or network.
    app.run(host="0.0.0.0", port=5000)
