# -----------------------------------------------------------------------------
# UNIT TESTS (Pytest)
# -----------------------------------------------------------------------------
# These tests are executed automatically by our CI/CD pipelines (GitHub Actions
# and GitLab CI) to ensure code quality before deployment.

import pytest
from app import app

# -----------------------------------------------------------------------------
# FIXTURES
# -----------------------------------------------------------------------------
# A fixture provides a fixed baseline so tests execute reliably and consistently.
# Here we create a "test client" that allows us to simulate HTTP requests
# to the Flask app without actually starting a live server on a port.

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

# -----------------------------------------------------------------------------
# TESTS
# -----------------------------------------------------------------------------

def test_home(client):
    """
    Test the root endpoint (/).
    Verifies that the status code is 200 OK and the JSON payload matches expectations.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json == {"message": "Hello from Software Delivery Lab!", "status": "ok"}

def test_health(client):
    """
    Test the health check endpoint (/health).
    Ensures DevOps monitoring tools will receive the correct status.
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"service": "hello-api-python", "status": "healthy"}
