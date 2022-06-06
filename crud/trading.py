from .alpaca_client import AlpacaClient
from schemas.order import Order, OrderCreate
from schemas.position import Position
from schemas.portfolio import Portfolio
from schemas.http import HttpResponse


def get_account_orders(account_id: str) -> HttpResponse[list[Order]]:
    client = AlpacaClient()
    res = client.get('/trading/accounts/' + account_id + '/orders', params={'status': 'all'})
    return res


def create_account_order(account_id: str, order: OrderCreate) -> HttpResponse[Order]:
    client = AlpacaClient()
    res = client.post('/trading/accounts/' + account_id + '/orders', data=order.json())
    return res


def get_account_positions(account_id: str) -> HttpResponse[list[Position]]:
    client = AlpacaClient()
    res = client.get('/trading/accounts/' + account_id + '/positions')
    return res


def get_account_portfolio(account_id: str) -> HttpResponse[Portfolio]:
    client = AlpacaClient()
    res = client.get('/trading/accounts/' + account_id + '/account/portfolio/history')
    return res
