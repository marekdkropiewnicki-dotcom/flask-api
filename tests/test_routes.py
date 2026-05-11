def test_root(client):
    resp = client.get("/")
    assert resp.status_code == 200
    body = resp.get_json()
    assert body is not None
    assert "data" in body
    assert "app" in body["data"]
    assert "environment" in body["data"]


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    body = resp.get_json()
    assert body is not None
    assert "data" in body
    assert body["data"]["healthy"] is True


def test_status(client):
    resp = client.get("/status")
    assert resp.status_code == 200
    body = resp.get_json()
    assert body is not None
    assert "data" in body
    assert "uptime_seconds" in body["data"]
    assert "environment" in body["data"]
