from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, validator, Extra
from typing import Union
from enum import Enum
from .asset import AssetClass


class OrderClass(str, Enum):
    SIMPLE = 'simple'
    BRACKET = 'bracket'
    OCO = 'oco'
    OTO = 'oto'


class OrderType(str, Enum):
    MARKET = 'market'
    LIMIT = 'limit'
    STOP = 'stop'
    STOP_LIMIT = 'stop_limit'
    TRAILING_STOP = 'trailing_stop'


# https://alpaca.markets/docs/api-references/broker-api/trading/orders/#order-status
class OrderSatus(str, Enum):
    NEW = 'new'
    PARTIALLY_FILLED = 'partially_filled'
    FILLED = 'filled'
    DONE_FOR_DAY = 'done_for_day'
    CANCELED = 'canceled'
    EXPIRED = 'expired'
    REPLACED = 'replaced'
    PENDING_CANCEL = 'pending_cancel'
    PENDING_REPLACE = 'pending_replace'
    ACCEPTED = 'accepted'
    PENDING_NEW = 'pending_new'
    ACCEPTED_FOR_BIDDING = 'accepted_for_bidding'
    STOPPED = 'stopped'
    REJECTED = 'rejected'
    SUSPENDED = 'suspended'
    CALCULATED = 'calculated'


class FillSide(str, Enum):
    BUY = 'buy'
    SELL = 'sell'


# https://alpaca.markets/docs/trading/orders/#time-in-force
class OrderTimeInForce(str, Enum):
    DAY = 'day'
    GTC = 'gtc'
    OPG = 'opg'
    CLS = 'cls'
    IOC = 'ioc'
    FOK = 'fok'


class TakeProfit(BaseModel):
    limit_price: float


class StopLoss(BaseModel):
    stop_price: float
    limit_price: Union[float, None]


class Order(BaseModel):
    id: str
    client_order_id: str
    created_at: datetime
    submitted_at: datetime
    filled_at: Union[datetime, None]
    expired_at: Union[datetime, None]
    canceled_at: Union[datetime, None]
    failed_at: Union[datetime, None]
    replaced_at: Union[datetime, None]
    replaced_by: Union[datetime, None]
    replaces: Union[datetime, None]
    asset_id: str
    symbol: str
    asset_class: AssetClass
    notional: Union[float, None]
    qty: Union[float, None]
    filled_qty: float
    filled_avg_price: Union[float, None]
    order_class: Union[OrderClass, str, None]
    type: OrderType
    side: FillSide
    time_in_force: OrderTimeInForce
    limit_price: Union[float, None]
    stop_price: Union[float, None]
    status: OrderSatus
    extended_hours: Union[bool, None]
    legs: Union[list[Order], None]
    trail_percent: Union[float, None]
    trail_price: Union[float, None]
    hwm: Union[float, None]
    commission: Union[float, None]


# To understand orders visit:
# https://alpaca.markets/docs/trading/orders/
class OrderCreate(BaseModel):
    symbol: str
    qty: Union[float, None]
    notional: Union[float, None]
    type: OrderType
    side: FillSide
    time_in_force: OrderTimeInForce
    limit_price: Union[float, None]
    stop_price: Union[float, None]
    trail_percent: Union[float, None]
    trail_price: Union[float, None]
    extended_hours: Union[bool, None]
    client_order_id: Union[str, None]
    order_class: Union[OrderClass, None]
    take_profit: Union[TakeProfit, None]
    stop_loss: Union[StopLoss, None]
    commission: Union[float, None]  # commission to be collected from user if any.

    @validator('notional', always=True)
    def check_consistency(cls, value, values):
        if value is not None and values['qty'] is not None:
            raise ValueError('only one of qty or notional is accepted')
        if value is None and values.get('qty') is None:
            raise ValueError('must provide qty or notional')
        return value

    @validator('limit_price', 'stop_price', always=True)
    def check_limit_order(cls, value, values):
        if value is None and values['type'] in [OrderType.LIMIT, OrderType.STOP_LIMIT]:
            raise ValueError('must provide limit/stop price if order type is "limit" or "stop_limit"')
        return value

    @validator('trail_price', 'trail_percent', always=True)
    def check_trailing_order(cls, value, values):
        if value is None and values['type'] in [OrderType.TRAILING_STOP]:
            raise ValueError('must provide trail price/percent order type is "trailing_stop"')
        return value

    class Config:
        extra = Extra.forbid
