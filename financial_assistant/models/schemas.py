from pydantic import BaseModel

class ETFRequest(BaseModel):
    budget: float
    risk: str
    horizon: int