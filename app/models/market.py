from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base


class Market(Base):
    __tablename__ = "markets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    market_id: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    event_id: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    slug: Mapped[str] = mapped_column(
        String(300),
        nullable=False,
        index=True,
    )

    question: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    sport: Mapped[str | None] = mapped_column(String(100))

    league: Mapped[str | None] = mapped_column(String(100))

    category: Mapped[str | None] = mapped_column(String(100))

    volume: Mapped[float] = mapped_column(
        Float,
        default=0,
    )

    liquidity: Mapped[float] = mapped_column(
        Float,
        default=0,
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )