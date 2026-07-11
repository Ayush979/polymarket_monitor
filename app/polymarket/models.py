from pydantic import BaseModel


class Market(BaseModel):
    id: str
    slug: str
    question: str

    volume: float | None = 0
    liquidity: float | None = 0

    active: bool = True

    sports: str | None = None
    league: str | None = None
    category: str | None = None