import os

from dynaconf import settings
from databases import DatabaseURL

API_V1_STR = "/api"

JWT_TOKEN_PREFIX = "Token"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # one week

MAX_CONNECTIONS_COUNT = settings.MAX_CONNECTIONS_COUNT
MIN_CONNECTIONS_COUNT = settings.MIN_CONNECTIONS_COUNT
SECRET_KEY = settings.SECRET_KEY

PROJECT_NAME = settings.PROJECT_NAME, "FastAPI example application"
ALLOWED_HOSTS = settings.ALLOWED_HOSTS

MONGODB_URL = settings.MONGODB_URL  # deploying without docker-compose

if not MONGODB_URL:
    MONGO_HOST = settings.MONGO_HOST
    MONGO_PORT = settings.MONGO_PORT
    MONGO_USER = settings.MONGO_USER
    MONGO_PASS = settings.MONGO_PASSWORD
    MONGO_DB = settings.MONGO_DB

    MONGODB_URL = DatabaseURL(
        f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
    )
else:
    MONGODB_URL = DatabaseURL(MONGODB_URL)

database_name = MONGO_DB
article_collection_name = "articles"
favorites_collection_name = "favorites"
tags_collection_name = "tags"
users_collection_name = "users"
comments_collection_name = "commentaries"
followers_collection_name = "followers"
