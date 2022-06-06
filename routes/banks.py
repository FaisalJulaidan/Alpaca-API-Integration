from fastapi import APIRouter, Body
from crud import banks
from schemas.bank import Bank, BankBase
from schemas.http import HttpResponse

router = APIRouter()


@router.get('/accounts/{account_id}/recipient_banks', response_model=HttpResponse[list[Bank]])
def get_account_banks(account_id: str) -> HttpResponse[list[Bank]]:
    return banks.get_account_banks(account_id)


@router.post('/accounts/{account_id}/recipient_banks', response_model=HttpResponse[Bank])
def create_account_bank(account_id: str, bank: BankBase = Body()) -> HttpResponse[Bank]:
    print(bank)
    return banks.create_account_bank(account_id, bank)
