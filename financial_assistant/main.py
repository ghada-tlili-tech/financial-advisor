from fastapi import FastAPI
from models.schemas import ETFRequest
from core.etf_engine import generate_portfolio

app = FastAPI()

@app.post("/recommend")
def recommend(req: ETFRequest):
    return generate_portfolio(req)