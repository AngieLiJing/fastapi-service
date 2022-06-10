from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

class TestMain:
    def teardown_class(self):
        try:
            exit(0)
        except SystemExit:
            pass
    def test_hello(self):
        res = client.get('/hello')
        assert res.status_code == 200
