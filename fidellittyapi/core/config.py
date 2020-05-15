import os

from dynaconf import settings
from starlette.datastructures import CommaSeparatedStrings, Secret
from databases import DatabaseURL

API_V1_STR = "/api"

JWT_TOKEN_PREFIX = "Token"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # one week

MAX_CONNECTIONS_COUNT = int(settings.MAX_CONNECTIONS_COUNT, 10)
MIN_CONNECTIONS_COUNT = int(settings.MIN_CONNECTIONS_COUNT, 10)
SECRET_KEY = Secret(settings.SECRET_KEY, "secret key for project")

PROJECT_NAME = settings.PROJECT_NAME, "FastAPI example application"
ALLOWED_HOSTS = CommaSeparatedStrings(settings.ALLOWED_HOSTS, "")

MONGODB_URL = settings.MONGODB_URL, ""  # deploying without docker-compose
if not MONGODB_URL:
    MONGO_HOST = settings.MONGO_HOST, "localhost"
    MONGO_PORT = int(settings.MONGO_PORT, 27017)
    MONGO_USER = settings.MONGO_USER, "admin"
    MONGO_PASS = settings.MONGO_PASSWORD, "markqiu"
    MONGO_DB = settings.MONGO_DB, "fastapi"

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
