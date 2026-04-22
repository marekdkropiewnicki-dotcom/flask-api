def test_create_app(app):
    """Creating the app with TESTING=True succeeds."""
    assert app is not None
    assert app.config["TESTING"] is True


def test_root(client):
    """GET / returns 200 with expected response shape."""
    response = client.get("/")
    assert response.status_code == 200
    body = response.get_json()
    assert body["status"] == 200
    assert body["message"] == "Root endpoint"
    assert "app" in body["data"]
    assert "environment" in body["data"]


def test_health(client):
    """GET /health returns 200 with healthy=True."""
    response = client.get("/health")
    assert response.status_code == 200
    body = response.get_json()
    assert body["status"] == 200
    assert body["message"] == "Health check OK"
    assert body["data"]["healthy"] is True


def test_status(client):
    """GET /status returns 200 with uptime_seconds and environment."""
    response = client.get("/status")
    assert response.status_code == 200
    body = response.get_json()
    assert body["status"] == 200
    assert body["message"] == "Service status"
    assert "uptime_seconds" in body["data"]
    assert "environment" in body["data"]
