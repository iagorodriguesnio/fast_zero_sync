from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Assert (orgaização)

    response = client.get('/')  # Action (ação)

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Hello World.'}
