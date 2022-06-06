from typing import Union

from fastapi import APIRouter
from crud import accounts
from schemas.account import Account, AccountBase, AccountCreate, AccountActivity, AccountNonTradeActivity
from schemas.http import HttpResponse

router = APIRouter()


@router.get('/accounts', response_model=HttpResponse[list[AccountBase]])
def get_all_accounts() -> HttpResponse[list[AccountBase]]:
    return accounts.get_all_accounts()


@router.get('/accounts/{account_id}', response_model=HttpResponse[Account])
def get_account(account_id: str) -> HttpResponse[Account]:
    return accounts.get_account(account_id)


@router.post('/accounts', response_model=HttpResponse[Account])
def create_account(account_data: AccountCreate) -> HttpResponse[Account]:
    return accounts.create_account(account_data)


@router.get('/accounts/{account_id}/activities',
            response_model=HttpResponse[list[Union[AccountActivity, AccountNonTradeActivity]]])
def get_account_activities(account_id: str) -> HttpResponse[list[Union[AccountActivity, AccountNonTradeActivity]]]:
    return accounts.get_account_activities(account_id)
