from .alpaca_client import AlpacaClient
from schemas.bank import Bank, BankBase
from schemas.http import HttpResponse


def get_account_banks(account_id: str) -> HttpResponse[list[Bank]]:
    client = AlpacaClient()
    res = client.get('/accounts/' + account_id + '/recipient_banks')
    return res


def create_account_bank(account_id: str, bank: BankBase) -> HttpResponse[Bank]:
    client = AlpacaClient()
    res = client.post('/accounts/' + account_id + '/recipient_banks', data=bank.json())
    return res
