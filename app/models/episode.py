from datetime import date
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

from app.models.show import Show


class Episode(SQLModel, table=True):
    __tablename__ = "episodes"

    id: int | None=Field(default=None, primary_key=True)
    title: str | None
    synopsis: str | None
    season_num: int | None
    episode_num: int | None
    length: int | None
    release_date: date | None
    show_id: int | None = Field(default=None, foreign_key="shows.id")

    show: Optional[Show] = Relationship(back_populates="episodes")