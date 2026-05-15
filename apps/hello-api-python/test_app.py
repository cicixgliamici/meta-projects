"""
UNIT TESTS (Pytest)
-------------------------------------------------------------------------------
These tests are executed automatically by our CI/CD pipelines (GitHub Actions
and GitLab CI) to ensure code quality before deployment.

Educational Note:
Automated testing is the backbone of CI/CD. Without tests, Continuous Deployment
is just "Continuous Danger". Pytest is a popular testing framework in Python 
because it makes writing small, readable tests easy while scaling to support
complex functional testing.
"""

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
    """
    Test Client Fixture.
    This sets up the Flask application in "TESTING" mode, which propagates
    exceptions rather than handling them via the app's error handlers,
    making it easier to find bugs.
    """
    app.config["TESTING"] = True
    with app.test_client() as client:
        # 'yield' makes this a generator. The test uses the client,
        # and once the test finishes, any teardown code after 'yield'
        # would run (though we don't have any here).
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

    # 1. Assert the HTTP status code
    assert response.status_code == 200

    # 2. Assert the exact JSON payload returned by the API
    assert response.json == {
        "message": "Hello from Software Delivery Lab!",
        "status": "ok",
    }


def test_health(client):
    """
    Test the health check endpoint (/health).
    Ensures DevOps monitoring tools will receive the correct status.
    """
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {
        "service": "hello-api-python",
        "status": "healthy",
    }
