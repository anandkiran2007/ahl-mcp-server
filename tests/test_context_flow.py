from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_context_bundle_generation():
    response = client.get("/context/test-patient")
    assert response.status_code == 200
    body = response.json()
    assert "conditions" in body
    assert "nlp" in body
