from typing import Union
from .alpaca_client import AlpacaClient
from schemas.account import Account, AccountBase, AccountCreate, AccountActivity, AccountNonTradeActivity
from schemas.http import HttpResponse


def get_all_accounts() -> HttpResponse[list[AccountBase]]:
    client = AlpacaClient()
    res = client.get('/accounts')
    return res


def get_account(account_id: str) -> HttpResponse[Account]:
    client = AlpacaClient()
    res = client.get('/accounts/' + account_id)
    return res


def create_account(data: AccountCreate) -> HttpResponse[Account]:
    client = AlpacaClient()
    res = client.post('/accounts', data=data.json())
    return res


def get_account_activities(account_id: str) -> HttpResponse[list[Union[AccountActivity, AccountNonTradeActivity]]]:
    client = AlpacaClient()
    res = client.get('/accounts/activities', params={'account_id': account_id})
    return res
