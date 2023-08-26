from fastapi.testclient import TestClient

from phonebook.main import app

client = TestClient(app)


def test_get_contact_list():
    response = client.get("/contacts/", )
    assert response.status_code == 200


def test_get_non_exists_contact():
    response = client.get("/contacts/2222/")
    assert response.status_code == 404
