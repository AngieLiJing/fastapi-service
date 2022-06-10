from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)
def test_hello():
   res = client.get('/hello')
   assert res.status_code == 200