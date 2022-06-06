from datetime import datetime
from pydantic import BaseModel
from typing import Union
from enum import Enum


class TransferDirection(str, Enum):
    INCOMING = 'INCOMING'
    OUTGOING = 'OUTGOING'


class FeePaymentMethod(str, Enum):
    USER = 'user'
    INVOICE = 'invoice'


class TransferStatus(str, Enum):
    QUEUED = 'QUEUED'
    APPROVAL_PENDING = 'APPROVAL_PENDING'
    PENDING = 'PENDING'
    SENT_TO_CLEARING = 'SENT_TO_CLEARING'
    REJECTED = 'REJECTED'
    CANCELED = 'CANCELED'
    APPROVED = 'APPROVED'
    COMPLETE = 'COMPLETE'
    RETURNED = 'RETURNED'


class TransferType(str, Enum):
    ACH = 'ach'  # Transfer via ACH (US Only)
    WIRE = 'wire'  # Transfer via wire (international)


class Transfer(BaseModel):
    id: str
    relationship_id: str
    account_id: str
    type: TransferType
    reason: Union[str, None]
    amount: float
    direction: TransferDirection
    status: TransferStatus
    created_at: datetime
    updated_at: datetime
    expires_at: datetime
    requested_amount: float
    fee: float
    fee_payment_method: FeePaymentMethod


class TransferCreate(BaseModel):
    relationship_id: str
    transfer_type: TransferType
    amount: float
    direction: TransferDirection
