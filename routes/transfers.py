from fastapi import APIRouter
from crud import transfers
from schemas.transfer import Transfer, TransferCreate
from schemas.http import HttpResponse

router = APIRouter()


@router.get('/accounts/{account_id}/transfers', response_model=HttpResponse[list[Transfer]])
def get_account_transfers(account_id: str) -> HttpResponse[list[Transfer]]:
    return transfers.get_account_transfers(account_id)


@router.post('/accounts/{account_id}/transfers', response_model=HttpResponse[Transfer])
def create_account_transfer(account_id: str, transfer: TransferCreate) -> HttpResponse[Transfer]:
    return transfers.create_account_transfer(account_id, transfer)
