from .alpaca_client import AlpacaClient
from schemas.transfer import Transfer, TransferCreate
from schemas.http import HttpResponse


def get_account_transfers(account_id: str) -> HttpResponse[list[Transfer]]:
    client = AlpacaClient()
    res = client.get('/accounts/' + account_id + '/transfers')
    return res


def create_account_transfer(account_id: str, transfer: TransferCreate) -> HttpResponse[Transfer]:
    client = AlpacaClient()
    res = client.post('/accounts/' + account_id + '/transfers', data=transfer.json())
    return res
