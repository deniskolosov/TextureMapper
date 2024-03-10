from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.text == "pong"


def test_render_unsupported_file_type():
    response = client.post(
        "/render", files={"texture": ("test.txt", "dummy-content", "text/plain")}
    )
    assert response.status_code == 400
    assert response.text == "Unsupported file type"


def test_render_missing_file():
    response = client.post("/render")
    assert response.status_code == 422


def test_render_success():
    with open("test.png", "rb") as image:
        response = client.post(
            "/render", files={"texture": ("test.png", image, "image/png")}
        )
    assert response.status_code == 200
    assert response.headers["content-type"] == "model/gltf-binary"
    assert response.content is not None
