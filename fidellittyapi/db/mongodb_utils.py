import logging

from motor.motor_asyncio import AsyncIOMotorClient

from ..core.config import (
    MAX_CONNECTIONS_COUNT,
    MIN_CONNECTIONS_COUNT,
    MONGODB_URL,
)
from .mongodb import db


async def connect_to_mongo():
    logging.info("Connect to the database...")
    db.client = AsyncIOMotorClient(
        str(MONGODB_URL),
        maxPoolSize=MAX_CONNECTIONS_COUNT,
        minPoolSize=MIN_CONNECTIONS_COUNT,
    )
    logging.info("Successfully connected to the database！")


async def close_mongo_connection():
    logging.info("Close the database connection...")
    db.client.close()
    logging.info("Database connection closed！")
