from app import app


def test_home_endpoint_returns_ok_message():
    """The home endpoint should return a JSON response with status ok."""
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_health_endpoint_returns_healthy_status():
    """The health endpoint should expose a basic service health check."""
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["service"] == "hello-api-python"
    assert response.get_json()["status"] == "healthy"
