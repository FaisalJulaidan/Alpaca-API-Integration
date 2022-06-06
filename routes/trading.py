from fastapi import APIRouter
from crud import trading
from schemas.order import Order, OrderCreate
from schemas.position import Position
from schemas.portfolio import Portfolio
from schemas.http import HttpResponse

router = APIRouter()


@router.get('/trading/accounts/{account_id}/orders', response_model=HttpResponse[list[Order]])
def get_account_orders(account_id: str) -> HttpResponse[list[Order]]:
    return trading.get_account_orders(account_id)


@router.post('/trading/accounts/{account_id}/orders', response_model=HttpResponse[Order])
def create_account_order(account_id: str, order: OrderCreate) -> HttpResponse[Order]:
    return trading.create_account_order(account_id, order)


@router.get('/trading/accounts/{account_id}/positions', response_model=HttpResponse[list[Position]])
def get_account_orders(account_id: str) -> HttpResponse[list[Position]]:
    return trading.get_account_positions(account_id)


@router.get('/trading/accounts/{account_id}/account/portfolio/history', response_model=HttpResponse[Portfolio])
def get_account_portfolio(account_id: str) -> HttpResponse[Portfolio]:
    return trading.get_account_portfolio(account_id)
