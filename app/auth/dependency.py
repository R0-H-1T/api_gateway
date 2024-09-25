import httpx
from typing import Annotated

async def get_async_client():
    async with httpx.AsyncClient() as client:
        yield client