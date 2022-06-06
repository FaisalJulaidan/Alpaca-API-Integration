from typing import Union
from fastapi import APIRouter
from crud import assets
from schemas.asset import Asset, AssetClass
from schemas.http import HttpResponse

router = APIRouter()


@router.get('/assets', response_model=HttpResponse[list[Asset]])
def get_all_assets(asset_class: AssetClass) -> HttpResponse[list[Asset]]:
    return assets.get_all_assets(asset_class)
