import os
from app.utils.statistics import calculate_statistics
import aiohttp
import asyncio

POKEAPI_BASE_URL = os.getenv("POKE_URL")


async def get_berry_statistics():
    # make the main request for berries
    async with aiohttp.ClientSession() as session:
        async with session.get(POKEAPI_BASE_URL) as response:
            response.raise_for_status()
            berries = await response.json()

        berry_data = {"names": [], "growth_times": []}

        # create asynchronous tasks to get the details of each berry
        tasks = []
        for berry in berries["results"]:
            tasks.append(fetch_berry_details(session, berry["url"], berry_data))

        # wait for all tasks to be completed
        await asyncio.gather(*tasks)

    return calculate_statistics(berry_data)


async def fetch_berry_details(session, url, berry_data):
    async with session.get(url) as response:
        response.raise_for_status()
        details = await response.json()
        berry_data['names'].append(details["name"])
        berry_data['growth_times'].append(details["growth_time"])
