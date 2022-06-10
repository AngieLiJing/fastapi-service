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

        print('hello')
        assert 1==1
