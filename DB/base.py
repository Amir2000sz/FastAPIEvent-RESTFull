from motor.motor_asyncio import AsyncIOMotorClient
from core.config import MONGO_URL, MONGO_DB_NAME

class MongoDB:
    client: AsyncIOMotorClient | None = None
    db = None

mongodb = MongoDB()

async def connect_to_mongo():
    mongodb.client = AsyncIOMotorClient(MONGO_URL)
    mongodb.db = mongodb.client[MONGO_DB_NAME]

async def close_mongo_connection():
    mongodb.client.close()

def get_db():
    return mongodb.db