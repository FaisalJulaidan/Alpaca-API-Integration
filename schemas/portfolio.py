from pydantic import BaseModel


class Portfolio(BaseModel):
    timestamp: list[int]
    equity: list[float]
    profit_loss: list[float]
    profit_loss_pct: list[float]
    base_value: float
    timeframe: str
