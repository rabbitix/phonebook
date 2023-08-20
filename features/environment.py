from fastapi.testclient import TestClient
from phonebook.main import app


def before_all(context):
    client = TestClient(app, base_url="http://127.0.0.1:8000")

    context.client = client
