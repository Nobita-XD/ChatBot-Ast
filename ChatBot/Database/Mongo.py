from ChatBot.main import MONGO_URL
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

mongo_client = MongoClient(MONGO_URL)
db = mongo_client.db
