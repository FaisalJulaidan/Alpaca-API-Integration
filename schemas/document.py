from pydantic import BaseModel, UUID4
from datetime import datetime
from enum import Enum


class DocumentTypes(str, Enum):
    identity_verification = 'identity_verification'
    address_verification = 'address_verification'
    date_of_birth_verification = 'date_of_birth_verification'
    tax_id_verification = 'tax_id_verification'
    account_approval_letter = 'account_approval_letter'
    w8ben = 'w8ben'


class DocumentSubTypes(str, Enum):
    Account_Application = 'Account Application'
    Form_WBEN = 'Form W-8BEN'
    passport = 'passport'


class DocumentBase(BaseModel):
    document_type: DocumentTypes
    document_sub_type: DocumentSubTypes
    content: str  # Base64


class Document(DocumentBase):
    id: UUID4
    created_at: datetime


class DocumentCreate(DocumentBase):
    mime_type: str
