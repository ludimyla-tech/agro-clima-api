from unittest.mock import AsyncMock, patch
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_home_mensagem():
    response = client.get("/")
    data = response.json()
    assert "mensagem" in data


def test_previsao_parametros_ausentes():
    response = client.get("/previsao")
    assert response.status_code == 422


def test_previsao_lat_invalida():
    response = client.get("/previsao", params={"lat": "abc", "lon": -55.0})
    assert response.status_code == 422


def test_previsao_sucesso_mockado():
    resposta_mock = {
        "daily": {
            "temperature_2m_max": [30.0],
            "temperature_2m_min": [18.0],
            "precipitation_sum": [0.0],
        }
    }

    class FakeResponse:
        def raise_for_status(self):
            return None

        def json(self):
            return resposta_mock

    with patch("main.httpx.AsyncClient.get", new=AsyncMock(return_value=FakeResponse())):
        response = client.get("/previsao", params={"lat": -14.235, "lon": -51.925})

    assert response.status_code == 200
    assert response.json() == resposta_mock


def test_docs_disponivel():
    response = client.get("/docs")
    assert response.status_code == 200