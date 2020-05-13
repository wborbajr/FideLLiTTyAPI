# FideLLiTTyAPI
FideLLiTTy RESTful API

### MariaDB
```
docker run -p 3306:3306 --rm -d --name api-db -eMARIADB_ROOT_PASSWORD=123mudar mariadb/server:10.4
docker ps -l
docker kill api-db
```

### PostgreSQL
```
docker run -p 5432:5432 --rm -d --name api-db -e POSTGRES_PASSWORD=123mudar postgres
docker ps -l
docker kill api-db
```

### Mongo
```
docker run -p 27017:27017 --rm -d --name api-db mongo
docker ps -l
docker kill api-db
```

Then run the following commands to bootstrap your environment with poetry:
```
git clone https://github.com/wborbajr/FideLLiTTyAPI.git
cd FideLLiTTyAPI
poetry install
poetry shell
```

Then create .env file (or rename and modify .env.example) in project root and set environment variables for application:
```
touch .env
echo "PROJECT_NAME=FastAPI RealWorld Application Example" >> .env
echo DATABASE_URL=mongo://$MONGO_USER:$MONGO_PASSWORD@$MONGO_HOST:$MONGO_PORT/$MONGO_DB >> .env
echo SECRET_KEY=$(openssl rand -hex 32) >> .env
echo ALLOWED_HOSTS='"127.0.0.1", "localhost"' >> .env
```

### To run the web application in debug use:
```
uvicorn app.main:app --reload
```

##Project structure

Files related to application are in the app directory. alembic is directory with sql migrations. Application parts are:
```
models  - pydantic models that used in crud or handlers
crud    - CRUD for types from models (create new user/article/comment, check if user is followed by another, etc)
db      - db specific utils
core    - some general components (jwt, security, configuration)
api     - handlers for routes
main.py - FastAPI application instance, CORS configuration and api router including
```

# TO-DO
1. 