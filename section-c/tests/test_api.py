"""api layer tests"""
from fastapi.testclient import TestClient

from eyesbeen.api import app

client = TestClient(app)


def test_read_isbn_validation():
    response = client.get("/isbn/031606652X")
    assert response.status_code == 200
    assert response.json() == {"result": "Invalid"}
