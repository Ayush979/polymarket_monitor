from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.settings import settings
from app.database.health import check_database
from app.database.session import get_db
from app.api.polymarket import router as polymarket_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.include_router(polymarket_router)

@app.get("/")
async def root():
    return {
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
    }


@app.get("/health")
async def health(
    db: AsyncSession = Depends(get_db),
):
    database_ok = await check_database(db)

    return {
        "api": "ok",
        "database": database_ok,
    }