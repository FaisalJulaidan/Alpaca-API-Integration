from pydantic import BaseModel, Field
from enum import Enum


class AssetClass(str, Enum):
    US_EQUITY = 'us_equity'
    CRYPTO = 'crypto'


class AssetStatus(str, Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'


class Exchange(str, Enum):
    AMEX = 'AMEX'
    ARCA = 'ARCA'
    BATS = 'BATS'
    NYSE = 'NYSE'
    NASDAQ = 'NASDAQ'
    NYSEARCA = 'NYSEARCA'
    OTC = 'OTC',
    FTXU = 'FTXU'  # for crypto


class Asset(BaseModel):
    id: str
    asset_class: AssetClass = Field(alias='class')
    exchange: Exchange
    symbol: str
    name: str
    status: AssetStatus
    tradable: bool
    marginable: bool
    shortable: bool
    easy_to_borrow: bool
    fractionable: bool
