from datetime import date, datetime
from enum import Enum
from typing import Union
from .document import Document, DocumentCreate
from .asset import AssetClass
from .order import FillSide
from pydantic import BaseModel, Extra, EmailStr, Field, IPvAnyAddress


class EmploymentStatus(str, Enum):
    UNEMPLOYED = 'unemployed'
    EMPLOYED = 'employed'
    STUDENT = 'student'
    RETIRED = 'retired'


class AccountStatus(str, Enum):
    INACTIVE = 'INACTIVE'
    ONBOARDING = 'ONBOARDING'
    SUBMITTED = 'SUBMITTED'
    ACTION_REQUIRED = 'ACTION_REQUIRED'
    EDITED = 'EDITED'
    APPROVAL_PENDING = 'APPROVAL_PENDING'
    APPROVED = 'APPROVED'
    REJECTED = 'REJECTED'
    ACTIVE = 'ACTIVE'
    SUBMISSION_FAILED = 'SUBMISSION_FAILED'
    DISABLED = 'DISABLED'
    ACCOUNT_CLOSED = 'ACCOUNT_CLOSED'


class CryptoStatus(str, Enum):
    INACTIVE = 'INACTIVE'
    ONBOARDING = 'ONBOARDING'
    SUBMITTED = 'SUBMITTED'
    ACTION_REQUIRED = 'ACTION_REQUIRED'
    EDITED = 'EDITED'
    APPROVAL_PENDING = 'APPROVAL_PENDING'
    APPROVED = 'APPROVED'
    REJECTED = 'REJECTED'
    ACTIVE = 'ACTIVE'
    SUBMISSION_FAILED = 'SUBMISSION_FAILED'
    DISABLED = 'DISABLED'
    ACCOUNT_CLOSED = 'ACCOUNT_CLOSED'


class Contact(BaseModel):
    email_address: str
    phone_number: str = Field(description="Phone number should include the country code, format: “+15555555555”")
    street_address: list[str]
    unit: Union[str, None]
    city: str
    state: Union[str, None]
    postal_code: Union[str, None]


class TrustedContact(BaseModel):
    given_name: str
    family_name: str
    email_address: str
    city: Union[str, None]
    state: Union[str, None]


class Identity(BaseModel):
    class TaxIdType(str, Enum):
        NOT_SPECIFIED = 'NOT_SPECIFIED'
        USA_SSN = 'USA_SSN'

    class FoundingSource(str, Enum):
        EMPLOYMENT_INCOME = 'employment_income'
        INVESTMENTS = 'investments'
        INHERITANCE = 'inheritance'
        BUSINESS_INCOME = 'business_income'
        SAVINGS = 'savings'
        FAMILY = 'family'

    given_name: str
    middle_name: Union[str, None]
    family_name: str
    date_of_birth: date
    tax_id: Union[str, None]
    tax_id_type: Union[TaxIdType, None]
    country_of_citizenship: Union[str, None] = Field(description='ISO-alpha-3 country code format e.g. SAU')
    country_of_birth: Union[str, None] = Field(description='ISO-alpha-3 country code format e.g. SAU')
    country_of_tax_residence: str = Field(description='ISO-alpha-3 country code format e.g. SAU')
    funding_source: list[FoundingSource]
    visa_type: Union[str, None]  # Only for USA
    visa_expiration_date: Union[date, None]
    date_of_departure_from_usa: Union[date, None]
    permanent_resident: Union[str, None] = Field(description='ISO-alpha-3 country code format e.g. SAU')


class Agreement(BaseModel):
    class AgreementTypes(str, Enum):
        MARGIN_AGREEMENT = 'margin_agreement'
        ACCOUNT_AGREEMENT = 'account_agreement'
        CUSTOMER_AGREEMENT = 'customer_agreement'
        CRYPTO_AGREEMENT = 'crypto_agreement'

    agreement: AgreementTypes
    signed_at: datetime
    ip_address: IPvAnyAddress
    revision: Union[str, None]


class Disclosures(BaseModel):
    is_control_person: bool
    is_affiliated_exchange_or_finra: bool
    is_politically_exposed: bool
    immediate_family_exposed: bool
    is_discretionary: Union[bool, None]
    employment_status: Union[EmploymentStatus, None]
    employer_name: Union[str, None]
    employer_address: Union[str, None]
    employment_position: Union[str, None]
    context: Union[list[dict], None]  # If you utilize Alpaca for KYCaaS


class AccountBase(BaseModel):
    id: str
    account_number: str
    status: AccountStatus
    crypto_status: CryptoStatus
    currency: str  # Always USD
    last_equity: Union[str, float]
    created_at: datetime
    account_type: str


class AccountDetails(BaseModel):
    contact: Contact
    identity: Identity
    disclosures: Disclosures
    agreements: Union[list[Agreement]]
    trusted_contact: Union[TrustedContact, None]


class Account(AccountBase, AccountDetails):
    documents: Union[list[Document], None]


class AccountCreate(AccountDetails):
    documents: Union[list[DocumentCreate], None]
    enabled_assets: Union[list[AssetClass], None]

    class Config:
        extra = Extra.forbid


class AccountActivityBase(BaseModel):
    class ActivityType(str, Enum):
        FILL = 'FILL'  # Order Fills (Partial/Full)
        ACATC = 'ACATC'  # ACATS IN/OUT (Cash)
        ACATS = 'ACATS'  # ACATS IN/OUT (Securities)
        CIL = 'CIL'  # Cash in Lieu of Stock
        CSD = 'CSD'  # Cash Disbursement (+)
        CSW = 'CSW'  # Cash Withdrawable
        DIV = 'DIV'  # Dividend
        INT = 'INT'  # Interest (Credit/Margin)
        JNLC = 'JNLC'  # Journal Entry (Cash)
        JNLS = 'JNLS'  # Journal Entry (Stock)
        SPIN = 'SPIN'  # Stock Spinoff
        SPLIT = 'SPLIT'  # Stock Split

    id: str
    account_id: str
    activity_type: ActivityType


class AccountActivity(AccountActivityBase):
    class FillType(str, Enum):
        FILL = 'fill'
        PARTIAL_FILL = 'partial_fill'

    transaction_time: datetime
    type: FillType
    price: float
    qty: float
    side: FillSide
    symbol: str
    leaves_qty: float
    order_id: str
    cum_qty: float
    order_status: str


class AccountNonTradeActivity(BaseModel):
    class ActivityStatus(str, Enum):
        EXECUTED = 'executed'
        CORRECT = 'correct'
        CANCELED = 'canceled'

    date: date
    net_amount: float
    description: str
    status: ActivityStatus
