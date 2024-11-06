# test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_transactions():
    response = client.get("/transactions")
    assert response.status_code == 200

def test_get_transaction():
    response = client.get("/transactions/1")
    assert response.status_code == 200

def test_fraudulent_transactions():
    response = client.get("/fraudulent-transactions")
    assert response.status_code == 200
