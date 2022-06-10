from fastapi.testclient import TestClient


from main import app

client = TestClient(app)
class TestMain:

    def test_hello(self):
        client.get('/world')
        print('hello')
        assert 1==1
