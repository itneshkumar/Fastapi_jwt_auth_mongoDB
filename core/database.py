from pymongo.collection import Collection
from typing import Generator
from core.config import get_settings
from pymongo import MongoClient
settings = get_settings()

# MongoDB Connection Settings
MONGODB_URL = settings.MONGODB_URL
DATABASE_NAME = settings.DB_NAME

# MongoDB Client
client = MongoClient(MONGODB_URL)
database = client[DATABASE_NAME]
users_collection: Collection = database["users"]


def get_db() -> Generator:
    try:
        yield users_collection
    finally:
        # No need to close the MongoDB client, as it is managed by FastAPI
        pass
