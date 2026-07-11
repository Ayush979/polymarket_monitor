from __future__ import annotations

import httpx
from tenacity import retry
from tenacity import stop_after_attempt
from tenacity import wait_exponential

from app.config.settings import settings

from . import endpoints
from .exceptions import PolymarketAPIError
from .models import Market


class PolymarketClient:

    def __init__(self):

        self.client = httpx.AsyncClient(
            base_url=settings.POLYMARKET_GAMMA_URL,
            timeout=30,
        )

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1),
        reraise=True,
    )
    async def list_markets(self) -> list[Market]:

        response = await self.client.get(
            endpoints.MARKETS
        )

        if response.status_code != 200:
            raise PolymarketAPIError(response.text)

        data = response.json()

        return [Market.model_validate(x) for x in data]

    async def close(self):
        await self.client.aclose()