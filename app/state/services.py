import databases
import aioredis
import asyncio

from app.state import config

loop: asyncio.AbstractEventLoop

database = databases.Database(str(config.MYSQL_DSN))
redis = aioredis.from_url(str(config.REDIS_DSN))
