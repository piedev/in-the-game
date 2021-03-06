def test_ping(test_app):
    response = test_app.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
