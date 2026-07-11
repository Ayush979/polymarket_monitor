from fastapi import APIRouter

from app.polymarket import PolymarketClient

router = APIRouter(prefix="/polymarket", tags=["Polymarket"])


@router.get("/markets")
async def markets():

    client = PolymarketClient()

    try:

        data = await client.list_markets()

        return {
            "count": len(data),
            "markets": data[:5],
        }

    finally:
        await client.close()