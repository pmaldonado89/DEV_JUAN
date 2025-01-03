from fastapi import FastAPI
from app.config  import lifespan
from app.adapters.api import api_router

app = FastAPI(lifespan=lifespan)

app.include_router(api_router, prefix="/api/v1")