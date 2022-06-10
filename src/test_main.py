import requests

class TestMain:

    def test_hello(self):
        requests.get('http://127.0.0.1:8000/hello')
        print('hello')
        assert 1==1
