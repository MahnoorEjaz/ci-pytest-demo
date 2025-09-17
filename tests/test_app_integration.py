import pytest
from src.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_ping(client):
    res = client.get("/ping")
    assert res.status_code == 200
    assert res.get_json() == {"pong": True}
