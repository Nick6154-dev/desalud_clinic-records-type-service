from motor.motor_asyncio import AsyncIOMotorClient
import os


async def initialize_mongo_instance():
    mongo_database_url = os.getenv('MONGO_DATABASE_URL', 'mongodb://localhost:27017/')
    mongo_database_name = os.getenv('MONGO_DATABASE_NAME', 'deSalud')
    client = AsyncIOMotorClient(mongo_database_url)
    db = client[mongo_database_name]
    return db
