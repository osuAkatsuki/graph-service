import asyncio
from fastapi import FastAPI

import app.state
import app.logger
from app.api import endpoints

asgi_app = FastAPI()

asgi_app.include_router(endpoints.v2.router)


@asgi_app.route("/")
async def index():
    return f"Running graph-service v{app.state.config.VERSION}".encode()


@asgi_app.on_event("startup")
async def on_startup() -> None:
    app.state.loop = asyncio.get_running_loop()

    await app.state.services.database.connect()
    await app.state.services.redis.initialize()

    # TODO: Add tasks.initialize() here.

    app.logger.info("Startup process complete.")
    app.logger.info(f"Listening @ {app.state.config.SOCKET_FILE}")


@asgi_app.on_event("shutdown")
async def on_shutdown() -> None:
    # Shutdown services.
    await app.state.services.database.disconnect()
    await app.state.services.redis.close()

    # TODO: Add tasks.close() here.
