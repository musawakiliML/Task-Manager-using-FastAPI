import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from app.server.config.config import Settings

# Importing enviroment Variables
settings = Settings()

# Database Configuration

client = AsyncIOMotorClient(settings.MONGODB_URL, serverSelectionTimeoutMS=5000)
client.get_io_loop = asyncio.get_event_loop
