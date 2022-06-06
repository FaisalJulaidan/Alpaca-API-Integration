from pydantic import BaseModel
from enum import Enum
from .asset import AssetClass, Exchange


class PositionSide(str, Enum):
    LONG = 'long'
    # SHORT = 'short'  # Not supported yet by Alpaca


class Position(BaseModel):
    asset_id: str
    symbol: str
    exchange: Exchange
    asset_class: AssetClass
    avg_entry_price: float
    qty: float
    side: PositionSide
    market_value: float
    cost_basis: float
    unrealized_pl: float
    unrealized_plpc: float
    unrealized_intraday_pl: float
    unrealized_intraday_plpc: float
    current_price: float
    lastday_price: float
    change_today: float