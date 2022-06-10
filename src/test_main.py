import requests
from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

class TestMain:
    def teardown_class(self):
        try:
            print('dddd')
            # client.close()
            exit(0)

        except SystemExit:
            pass

    def test_hello(self):
        # client.get('/hello')
        res = client.request(method='get', url='/hello')
        print('res=',res.status_code, 'result=', res.json())
        # requests.get('http://localhost:8000/hello')
        print('hello')
        assert 1==1
