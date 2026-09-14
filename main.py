from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import httpx

app = FastAPI(title="Agro Clima API")

@app.get("/")
def home():
    return {"mensagem": "API de previsão do tempo para o agro"}

@app.get("/previsao")
async def previsao(lat: float, lon: float):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        "&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"
        "&timezone=auto"
    )
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        return resp.json()