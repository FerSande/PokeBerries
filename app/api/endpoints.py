from fastapi_cache.decorator import cache
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from app.services.berries_service import get_berry_statistics
from app.utils.histogram import generate_histogram_html
from app.models.berry_stats import BerryStats

router = APIRouter()

CACHE_EXPIRE_TIME = 60 * 5


@router.get("/allBerryStats", response_model=BerryStats, response_description="Poke-berries Statistics", status_code=200)
@cache(expire=CACHE_EXPIRE_TIME)
async def all_berry_stats():
    berry_stats = await get_berry_statistics()
    return berry_stats


@router.get("/berryHistogram", response_class=HTMLResponse, response_description="Histogram of Growth Time Frequencies")
@cache(expire=CACHE_EXPIRE_TIME)
async def berry_histogram():
    berry_stats = await get_berry_statistics()
    return generate_histogram_html(berry_stats["frequency_growth_time"])
