from datetime import date
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

from app.models.genre import Genre


class Show(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str | None = None
    synopsis: str | None = None
    seasons_num: int | None = None
    release_date: date | None = None
    genre_id: int | None = Field(default=None, foreign_key="genre.id")
    poster_url: str | None = None
    rating: int | None = None
    created_at: date | None = None
    updated_at: date | None = None
    is_published: bool | None = None

    genre: Optional[Genre] = Relationship(back_populates="shows")