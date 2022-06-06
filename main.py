from fastapi import FastAPI
from routes import accounts, assets, banks, transfers, trading

app = FastAPI()
app.include_router(accounts.router)
app.include_router(assets.router)
app.include_router(banks.router)
app.include_router(transfers.router)
app.include_router(trading.router)
