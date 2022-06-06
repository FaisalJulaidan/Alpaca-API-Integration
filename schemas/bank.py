from datetime import datetime
from pydantic import BaseModel, Field
from enum import Enum


class BankStatus(str, Enum):
    QUEUED = 'QUEUED'
    SENT_TO_CLEARING = 'SENT_TO_CLEARING'
    APPROVED = 'APPROVED'
    CANCELED = 'CANCELED'


class BankCodeType(str, Enum):
    ABA = 'ABA'  # US
    BIC = 'BIC'  # International transfer


class BankBase(BaseModel):
    name: str
    bank_code: str = Field(description='SWIFT Code e.g. INMASARI')
    bank_code_type: BankCodeType
    account_number: str
    country: str = Field(description='ISO-alpha-3 country code format e.g. SAU')
    state_province: str
    postal_code: str
    city: str
    street_address: str


class Bank(BankBase):
    id: str
    account_id: str
    status: BankStatus
    created_at: datetime
    updated_at: datetime
