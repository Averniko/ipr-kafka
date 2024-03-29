from logging.config import dictConfig

from fastapi import FastAPI

from core.config import LOGGER_CONFIG
from routers import router

dictConfig(LOGGER_CONFIG)

app = FastAPI(
    title="MC1"
)

app.include_router(router)
