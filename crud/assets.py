import json
from .alpaca_client import AlpacaClient
from schemas.asset import Asset, AssetStatus, AssetClass
from schemas.http import HttpResponse


def get_all_assets(asset_class: AssetClass) -> HttpResponse[list[Asset]]:
    client = AlpacaClient()
    res = client.get('/assets', params={'status': AssetStatus.ACTIVE, 'asset_class': asset_class})
    return res
