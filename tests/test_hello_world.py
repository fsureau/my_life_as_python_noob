import unittest
from app import app


class HelloWorldTest(unittest.TestCase):

    def test_request_example(self):
        client = app.test_client()
        response = client.get("/")
        self.assertNotEqual(b"Hello World!", response.data)
