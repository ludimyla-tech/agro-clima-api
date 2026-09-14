# Agro Clima API

API simples em Python (FastAPI) que consulta a previsão do tempo (Open-Meteo)
para apoiar decisões no campo, como irrigação e pulverização.

## Como rodar localmente
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Endpoint
`GET /previsao?lat=-15.6&lon=-56.1`