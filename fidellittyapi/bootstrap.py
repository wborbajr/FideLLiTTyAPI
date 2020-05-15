# from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from fidellittyapi.api.api_v1.api import router as api_router
from fidellittyapi.core.config import ALLOWED_HOSTS, API_V1_STR, PROJECT_NAME
from fidellittyapi.core.errors import (http_422_error_handler,
                                       http_error_handler)
from fidellittyapi.db.mongodb_utils import close_mongo_connection

app = FastAPI(title=PROJECT_NAME)

if not ALLOWED_HOSTS:
    ALLOWED_HOSTS = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.add_event_handler("startup", connect_to_mongo)
# app.add_event_handler("shutdown", close_mongo_connection)

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(
    HTTP_422_UNPROCESSABLE_ENTITY, http_422_error_handler
)

app.include_router(api_router, prefix=API_V1_STR)
