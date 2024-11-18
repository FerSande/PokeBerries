import os
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis.asyncio import Redis
from contextlib import asynccontextmanager
from app.api.endpoints import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis_host = os.getenv("REDIS_HOST")
    redis_port = int(os.getenv("REDIS_PORT"))
    redis = Redis(host=redis_host, port=redis_port)
    FastAPICache.init(RedisBackend(redis), prefix="poke_berries_cache")

    yield

    await redis.aclose()

app = FastAPI(lifespan=lifespan)

app.include_router(router)


@app.get("/")
def root():
    return {"message": "Welcome to the Poke-berries Statistics API"}
