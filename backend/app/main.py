from fastaapi import FastAPI
from backend.api.router import router

app = FastAPI()

app.include_router(router, prefix="/api/v1")